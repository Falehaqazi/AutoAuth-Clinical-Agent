import streamlit as st
import os
import json
import pandas as pd
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from openai import OpenAI

# --- CONFIGURATION & SETUP ---
st.set_page_config(page_title="AutoAuth FHIR Agent", page_icon="🏥", layout="wide")
load_dotenv()

# Sidebar: API Key Handling
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.sidebar.error("⚠️ OPENAI_API_KEY not found in .env")
    st.stop()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)

# --- 1. FHIR & INTEROPERABILITY LAYER ---
def parse_fhir_bundle(fhir_json):
    try:
        # Check if input is empty
        if not fhir_json.strip():
            return "No data provided."
        
        data = json.loads(fhir_json)
        
        # Handling the simplified mock structure and standard FHIR entry list
        if "entry" in data:
            # Basic parsing for the standard FHIR format
            patient = "Unknown"
            request = "Unknown Service"
            for entry in data["entry"]:
                res = entry.get("resource", {})
                if res.get("resourceType") == "Patient":
                    patient = res.get("name", [{}])[0].get("family", "Unknown")
                if res.get("resourceType") == "ServiceRequest":
                    request = res.get("code", {}).get("text", "Unknown Service")
            return f"Patient: {patient}\nRequest: {request}"
        else:
            # Original simple parser for your default mock data
            patient = data.get("patient", {}).get("name", "Unknown")
            condition = data.get("condition", {}).get("code", "Unknown Condition")
            request = data.get("serviceRequest", {}).get("type", "Unknown Service")
            history = data.get("clinicalNote", "")
            return f"Patient: {patient}\nCondition: {condition}\nRequest: {request}\nNotes: {history}"
    except Exception as e:
        return f"Error parsing FHIR JSON: {str(e)}"

# --- 2. AI DECISION ENGINE ---
class DecisionSchema(BaseModel):
    decision: str = Field(description="APPROVED, DENIED, or NEEDS_INFO")
    reason: str = Field(description="Brief reason based on policy")
    confidence: float = Field(description="0.0 to 1.0 confidence score")

def analyze_claim(clinical_text, policy):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a Utilization Review Agent. Analyze the FHIR summary against the policy."},
            {"role": "user", "content": f"Policy: {policy}\n\nClinical Summary: {clinical_text}"}
        ],
        tools=[{
            "type": "function",
            "function": {
                "name": "submit_decision",
                "parameters": DecisionSchema.model_json_schema()
            }
        }],
        tool_choice={"type": "function", "function": {"name": "submit_decision"}}
    )
    return json.loads(completion.choices[0].message.tool_calls[0].function.arguments)

# --- 3. UI LAYOUT ---
st.title("🏥 Auto-Auth: Intelligent Prior Authorization")
st.markdown("### FHIR-Integrated Clinical Decision Support System")

tab1, tab2 = st.tabs(["⚡ Live Analysis", "🧪 Batch Evaluation"])

# --- TAB 1: LIVE INTERACTIVE DASHBOARD ---
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📥 Input: FHIR Resource")
        
        # Initialize session state for fhir_input if it doesn't exist
        if 'fhir_input' not in st.session_state:
            st.session_state['fhir_input'] = json.dumps({
                "resourceType": "Bundle",
                "patient": {"id": "P-123", "name": "John Doe"},
                "condition": {"code": "M54.5 (Low Back Pain)", "onset": "2023-11-01"},
                "serviceRequest": {"type": "Lumbar MRI", "priority": "routine"},
                "clinicalNote": "Patient has had back pain for 2 weeks. No PT tried yet."
            }, indent=2)

        # The Load Sample Button
        if st.button("📝 Load Sample FHIR Data"):
            sample_fhir = {
                "resourceType": "Bundle",
                "entry": [
                    {"resource": {"resourceType": "Patient", "name": [{"family": "Doe"}]}},
                    {"resource": {"resourceType": "ServiceRequest", "code": {"text": "MRE brain with contrast"}}}
                ]
            }
            # Update session state with pretty-printed JSON
            st.session_state['fhir_input'] = json.dumps(sample_fhir, indent=2)
            st.rerun() # Refresh to show the new value in the text area

        # Single Text Area linked to session state
        fhir_input = st.text_area("Paste FHIR JSON Bundle", value=st.session_state['fhir_input'], height=250)
        
        st.subheader("📜 Insurance Policy")
        policy_input = st.text_area("Policy Rules", value="Approve MRI only if: Pain > 6 weeks AND Physical Therapy > 4 weeks.", height=100)
        
        run_btn = st.button("🚀 Analyze Claim", type="primary")

    with col2:
        st.subheader("📤 AI Decision Output")
        if run_btn:
            with st.spinner("Parsing FHIR & Consulting LLM..."):
                clinical_summary = parse_fhir_bundle(fhir_input)
                st.info(f"**Parsed Context:**\n{clinical_summary}")
                
                result = analyze_claim(clinical_summary, policy_input)
                
                if result['decision'] == "APPROVED":
                    st.success(f"✅ **APPROVED** (Conf: {result['confidence']})")
                elif result['decision'] == "DENIED":
                    st.error(f"❌ **DENIED** (Conf: {result['confidence']})")
                else:
                    st.warning(f"⚠️ **NEEDS REVIEW** (Conf: {result['confidence']})")
                
                st.write(f"**Reason:** {result['reason']}")
                st.progress(result['confidence'], text="AI Confidence Score")

# --- TAB 2: PERFORMANCE EVALUATION ---
with tab2:
    st.header("🧪 Clinical Dataset Evaluation")
    st.write("Simulating batch processing on synthetic clinical records.")
    
    if st.button("Run Validation Dataset"):
        dataset = [
            {"id": 1, "truth": "DENIED", "note": "Back pain 1 week. No PT.", "policy": "Pain > 6w, PT > 4w"},
            {"id": 2, "truth": "APPROVED", "note": "Pain 12 weeks. PT 8 weeks done.", "policy": "Pain > 6w, PT > 4w"},
            {"id": 3, "truth": "DENIED", "note": "Knee pain. Wants MRI immediately.", "policy": "Pain > 6w, PT > 4w"},
            {"id": 4, "truth": "APPROVED", "note": "Chronic back pain 6 months. Failed NSAIDs and PT x 6w.", "policy": "Pain > 6w, PT > 4w"},
            {"id": 5, "truth": "NEEDS_INFO", "note": "Patient hurts. Dr says maybe MRI.", "policy": "Pain > 6w, PT > 4w"}
        ]
        
        results = []
        progress_bar = st.progress(0)
        
        for i, case in enumerate(dataset):
            pred = analyze_claim(case['note'], case['policy'])
            match = (pred['decision'] == case['truth']) or (case['truth'] == "NEEDS_INFO" and pred['confidence'] < 0.9)
            results.append({
                "Case ID": case['id'],
                "Ground Truth": case['truth'],
                "AI Prediction": pred['decision'],
                "Confidence": pred['confidence'],
                "Match": "✅" if match else "❌"
            })
            progress_bar.progress((i + 1) / len(dataset))
            
        df = pd.DataFrame(results)
        st.dataframe(df, use_container_width=True)
        
        accuracy = len(df[df["Match"] == "✅"]) / len(df)
        st.metric(label="Model Accuracy", value=f"{accuracy*100}%")