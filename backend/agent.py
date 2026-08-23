# backend/agent.py
# LangGraph agent: 6 nodes wired into a state machine.
# redact -> retrieve -> reason (ReAct loop with tools) -> critique -> finalize

import os
import re
from typing import TypedDict, Annotated, Literal, Optional

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

from backend.tools import lookup_cpt_code, lookup_icd10_code
from backend.policy_store import retrieve_relevant_policy, retrieve_with_scores

load_dotenv()

CONFIDENCE_THRESHOLD = 0.80
MAX_REVISIONS = 1

# --- 1. STATE ---
# `messages` uses the add_messages reducer so node updates APPEND to the
# conversation instead of replacing it. Without this, ToolNode's return value
# overwrites the whole history and the ReAct loop breaks.
class AgentState(TypedDict):
    clinical_input: str
    redacted_input: str
    retrieved_policy: str
    retrieved_chunk_ids: list
    retrieved_policy_ids: list
    retrieval_scores: list
    messages: Annotated[list, add_messages]
    draft_decision: str
    critique_verdict: str
    critique_feedback: str
    revision_count: int
    final_decision: str
    final_reasoning: str
    confidence: float
    escalation_reason: Optional[str]


# --- 2. LLM ---
_api_key = os.getenv("GROQ_API_KEY")
if not _api_key:
    raise RuntimeError(
        "GROQ_API_KEY is not set. Create a .env file with GROQ_API_KEY=your_key"
    )

TOOLS = [lookup_cpt_code, lookup_icd10_code]
llm = ChatGroq(model="openai/gpt-oss-20b", api_key=_api_key, temperature=float(os.getenv("AUTOAUTH_TEMP", "0.1")))
llm_with_tools = llm.bind_tools(TOOLS)


# --- 3. NODES ---

# Each pattern requires an explicit label and colon, so ordinary clinical prose
# such as "the patient reports low back pain" is left intact.
_REDACTION_PATTERNS = [
    (r"(?i)\bpatient(?:\s+name)?\s*:\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*", "Patient: [REDACTED]"),
    (r"(?i)\b(?:mrn|medical\s+record\s+(?:no|number))\s*:?\s*[A-Za-z0-9-]+", "MRN: [REDACTED]"),
    (r"(?i)\bid\s*:\s*\d+", "ID: [REDACTED]"),
    (r"\b\d{3}-\d{2}-\d{4}\b", "[SSN-REDACTED]"),
    (r"(?i)\bdob\s*:?\s*\d{1,4}[/-]\d{1,2}[/-]\d{1,4}", "DOB: [REDACTED]"),
    (r"\b[\w.+-]+@[\w-]+\.[\w.]+\b", "[EMAIL-REDACTED]"),
    (r"\b(?:\+\d{1,3}[\s-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b", "[PHONE-REDACTED]"),
]


def redact_node(state: AgentState) -> dict:
    """Strip direct identifiers before anything else touches the data."""
    text = state["clinical_input"]
    for pattern, replacement in _REDACTION_PATTERNS:
        text = re.sub(pattern, replacement, text)
    return {"redacted_input": text}


def retrieve_node(state: AgentState) -> dict:
    """Pull only the policy chunks relevant to this case."""
    text, cids, pids, scores = retrieve_with_scores(state["redacted_input"], k=3)
    return {"retrieved_policy": text, "retrieved_chunk_ids": cids,
            "retrieved_policy_ids": pids, "retrieval_scores": scores}


SYSTEM_PROMPT = """You are a Prior Authorization clinical reviewer using the ReAct pattern.

For each case:
- Thought: reason about what you need to verify
- Action: if you need to verify a CPT or ICD-10 code, call the appropriate tool
- Observation: review the tool's response
- Repeat until you have enough information

When you have enough, output your final decision in exactly this format:
DECISION: [APPROVED | DENIED]
CONFIDENCE: [0.0-1.0]
REASON: [Clinical justification citing the policy]"""


def reason_node(state: AgentState) -> dict:
    """ReAct reasoning step. The LLM may call tools here."""
    if not state.get("messages"):
        user_prompt = f"""POLICY (retrieved via RAG):
{state['retrieved_policy']}

CLINICAL CASE:
{state['redacted_input']}

Begin your ReAct reasoning. Use tools to verify any codes mentioned."""
        outgoing = [SystemMessage(content=SYSTEM_PROMPT), HumanMessage(content=user_prompt)]
    else:
        outgoing = []

    response = llm_with_tools.invoke(list(state.get("messages", [])) + outgoing)

    # add_messages appends these; it does not replace the history.
    return {"messages": outgoing + [response], "draft_decision": response.content or ""}


def critique_node(state: AgentState) -> dict:
    """Self-reflection: a second call audits the first one's decision."""
    critique_prompt = f"""You are a senior clinical reviewer auditing another reviewer's decision.

POLICY APPLIED:
{state['retrieved_policy']}

CASE:
{state['redacted_input']}

DRAFT DECISION FROM JUNIOR REVIEWER:
{state['draft_decision']}

Check whether the decision is sound and the reasoning cites the policy correctly.
Begin your reply with exactly one word, APPROVE or REVISE, then explain briefly."""

    response = llm.invoke([SystemMessage(content=critique_prompt)])
    text = (response.content or "").strip()
    verdict = "APPROVE" if text.upper().startswith("APPROVE") else "REVISE"

    update = {
        "critique_verdict": verdict,
        "critique_feedback": text,
        # Incremented here so the revision guard in after_critique can actually
        # terminate. Previously this was never written and the graph could loop
        # until LangGraph's recursion limit raised GraphRecursionError.
        "revision_count": state.get("revision_count", 0) + (1 if verdict == "REVISE" else 0),
    }

    # Feed the critique back into the conversation, otherwise the reasoning node
    # re-runs with no new information and reproduces the same draft.
    if verdict == "REVISE":
        update["messages"] = [
            HumanMessage(
                content=(
                    "A senior reviewer rejected your draft for the following reason:\n\n"
                    f"{text}\n\n"
                    "Reconsider the case and output a corrected decision in the required format."
                )
            )
        ]
    return update


def finalize_node(state: AgentState) -> dict:
    """Parse the draft and apply the escalation rules."""
    draft = state.get("draft_decision") or ""
    upper = draft.upper()

    if "DECISION: APPROVED" in upper:
        recommendation = "APPROVED"
    elif "DECISION: DENIED" in upper:
        recommendation = "DENIED"
    else:
        recommendation = "UNPARSEABLE"

    match = re.search(r"CONFIDENCE:\s*([01](?:\.\d+)?)", draft)
    confidence = float(match.group(1)) if match else 0.0

    decision = recommendation
    escalation_reason = None

    # Rule 1: no autonomous denial. An adverse recommendation is never returned
    # as a final decision; it is surfaced to a human reviewer instead. The cost
    # of a wrong denial falls on the patient and is not symmetric with the cost
    # of a wrong approval.
    if recommendation == "DENIED":
        decision = "PENDING_REVIEW"
        escalation_reason = "no_autonomous_denial"

    # Rule 2: confidence gate.
    elif confidence < CONFIDENCE_THRESHOLD:
        decision = "PENDING_REVIEW"
        escalation_reason = "below_confidence_threshold"

    # Rule 3: unparseable output is never treated as an approval.
    elif recommendation == "UNPARSEABLE":
        decision = "PENDING_REVIEW"
        escalation_reason = "unparseable_model_output"

    # Rule 4: critique still objected after the revision budget was spent.
    if state.get("critique_verdict") == "REVISE" and decision != "PENDING_REVIEW":
        decision = "PENDING_REVIEW"
        escalation_reason = "unresolved_critique"

    return {
        "final_decision": decision,
        "final_reasoning": draft,
        "confidence": confidence,
        "escalation_reason": escalation_reason,
    }


# --- 4. ROUTING ---

def should_use_tools(state: AgentState) -> Literal["tools", "critique"]:
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "tools"
    return "critique"


def after_critique(state: AgentState) -> Literal["reason", "finalize"]:
    if state["critique_verdict"] == "REVISE" and state.get("revision_count", 0) <= MAX_REVISIONS:
        return "reason"
    return "finalize"


# --- 5. GRAPH ---

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


graph = build_graph()
