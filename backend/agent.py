# backend/agent.py
# The LangGraph agent: 4 nodes wired into a state machine.
# redact -> retrieve -> reason (with tools, ReAct loop) -> critique
# This is the file that makes "agentic + multi-step + self-reflection + tool-calling" real.

import os
import re
from typing import TypedDict, Annotated, Literal
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

from backend.tools import lookup_cpt_code, lookup_icd10_code
from backend.policy_store import retrieve_relevant_policy

load_dotenv()

# --- 1. THE STATE ---
# This is what flows between nodes. Each node reads from and writes to this dict.
class AgentState(TypedDict):
    clinical_input: str      # raw clinical data from the user
    redacted_input: str      # after PII removal
    retrieved_policy: str    # FAISS-retrieved policy chunks
    messages: list           # ReAct conversation history (for tool-calling loop)
    draft_decision: str      # the reasoning node's initial verdict
    critique_verdict: str    # the critique node's APPROVE or REVISE
    final_decision: str      # APPROVED / DENIED / PENDING_REVIEW
    final_reasoning: str
    revision_count: int      # how many times we've looped back for revision

# --- 2. THE LLM (with tools bound) ---
TOOLS = [lookup_cpt_code, lookup_icd10_code]
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("OPENAI_API_KEY"),  # despite name, this is the Groq key
    temperature=0.1,
)
llm_with_tools = llm.bind_tools(TOOLS)

# --- 3. THE NODES ---

def redact_node(state: AgentState) -> dict:
    """Strip PII before anything else touches the data."""
    text = state["clinical_input"]
    text = re.sub(r"(?i)patient[:\s]+\w+\s*\w*", "Patient: [REDACTED]", text)
    text = re.sub(r"\bID[:\s]+\d+", "ID: [REDACTED]", text)
    text = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[SSN-REDACTED]", text)
    return {"redacted_input": text}

def retrieve_node(state: AgentState) -> dict:
    """Use FAISS to pull only the policy chunks relevant to this case."""
    policy_chunks = retrieve_relevant_policy(state["redacted_input"], k=3)
    return {"retrieved_policy": policy_chunks}

def reason_node(state: AgentState) -> dict:
    """The ReAct reasoning step. The LLM can call tools here.
    LangGraph will loop back to this node if the LLM requests a tool call."""
    
    # First entry into this node — set up the conversation
    if not state.get("messages"):
        system_prompt = """You are a Prior Authorization clinical reviewer using the ReAct pattern.

For each case, follow this loop:
- Thought: reason about what you need to verify
- Action: if you need to verify a CPT or ICD-10 code, call the appropriate tool
- Observation: review the tool's response
- Repeat until you have enough information

When you have enough, output your final decision in this format:
DECISION: [APPROVED | DENIED]
CONFIDENCE: [0.0-1.0]
REASON: [Clinical justification citing the policy]"""

        user_prompt = f"""POLICY (retrieved via RAG):
{state['retrieved_policy']}

CLINICAL CASE:
{state['redacted_input']}

Begin your ReAct reasoning. Use tools to verify any codes mentioned."""
        
        messages = [SystemMessage(content=system_prompt), HumanMessage(content=user_prompt)]
    else:
        messages = state["messages"]
    
    response = llm_with_tools.invoke(messages)
    messages.append(response)
    
    return {"messages": messages, "draft_decision": response.content or ""}

def critique_node(state: AgentState) -> dict:
    """Self-reflection: a second LLM call reviews the first one's decision."""
    
    critique_prompt = f"""You are a senior clinical reviewer auditing another reviewer's decision.

POLICY APPLIED:
{state['retrieved_policy']}

CASE:
{state['redacted_input']}

DRAFT DECISION FROM JUNIOR REVIEWER:
{state['draft_decision']}

Your job: check whether the decision is sound and the reasoning cites the policy correctly.
Reply with exactly one of:
- APPROVE: if the decision is well-reasoned and matches the policy
- REVISE: if there is a logical flaw or the policy was misapplied (briefly explain why)"""
    
    response = llm.invoke([SystemMessage(content=critique_prompt)])
    verdict_text = response.content.upper()
    verdict = "APPROVE" if verdict_text.startswith("APPROVE") else "REVISE"
    
    return {"critique_verdict": verdict}

def finalize_node(state: AgentState) -> dict:
    """Parse the draft decision into the final output structure."""
    draft = state["draft_decision"]
    
    if "DECISION: APPROVED" in draft.upper():
        decision = "APPROVED"
    elif "DECISION: DENIED" in draft.upper():
        decision = "DENIED"
    else:
        decision = "PENDING_REVIEW"
    
    conf_match = re.search(r"CONFIDENCE:\s*([\d\.]+)", draft)
    confidence = float(conf_match.group(1)) if conf_match else 0.5
    
    if confidence < 0.80:
        decision = "PENDING_REVIEW"
    
    return {"final_decision": decision, "final_reasoning": draft}

# --- 4. THE ROUTING LOGIC ---

def should_use_tools(state: AgentState) -> Literal["tools", "critique"]:
    """After reasoning: did the LLM request a tool call, or is it done?"""
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return "critique"

def after_critique(state: AgentState) -> Literal["reason", "finalize"]:
    """If critique says REVISE and we haven't looped too many times, go back."""
    if state["critique_verdict"] == "REVISE" and state.get("revision_count", 0) < 1:
        return "reason"
    return "finalize"

# --- 5. BUILD THE GRAPH ---

def build_graph():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("redact", redact_node)
    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("reason", reason_node)
    workflow.add_node("tools", ToolNode(TOOLS))
    workflow.add_node("critique", critique_node)
    workflow.add_node("finalize", finalize_node)
    
    workflow.set_entry_point("redact")
    workflow.add_edge("redact", "retrieve")
    workflow.add_edge("retrieve", "reason")
    workflow.add_conditional_edges("reason", should_use_tools)
    workflow.add_edge("tools", "reason")
    workflow.add_conditional_edges("critique", after_critique)
    workflow.add_edge("finalize", END)
    
    return workflow.compile()

# Singleton compiled graph
graph = build_graph()