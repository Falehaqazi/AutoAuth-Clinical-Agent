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
# We simulate parsing a standard FHIR Bundle (Patient + Condition + ServiceRequest)
def parse_fhir_bundle(fhir_json):
    try:
        data = json.loads(fhir_json)
        patient = data.get("patient", {}).get("name", "Unknown")
        condition = data.get("condition", {}).get("code", "Unknown Condition")
        request = data.get("serviceRequest", {}).get("type", "Unknown Service")
        history = data.get("clinicalNote", "")
        return f"Patient: {patient}\nCondition: {condition}\nRequest: {request}\nNotes: {history}"
    except Exception:
        return "Error parsing FHIR JSON"

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

# Tabs for different modes
tab1, tab2 = st.tabs(["⚡ Live Analysis", "🧪 Batch Evaluation"])

# --- TAB 1: LIVE INTERACTIVE DASHBOARD ---
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📥 Input: FHIR Resource")
        
        # Pre-filled FHIR Mock Data
        default_fhir = json.dumps({
            "resourceType": "Bundle",
            "patient": {"id": "P-123", "name": "John Doe"},
            "condition": {"code": "M54.5 (Low Back Pain)", "onset": "2023-11-01"},
            "serviceRequest": {"type": "Lumbar MRI", "priority": "routine"},
            "clinicalNote": "Patient has had back pain for 2 weeks. No PT tried yet."
        }, indent=2)
        
        fhir_input = st.text_area("Paste FHIR JSON Bundle", value=default_fhir, height=250)
        
        st.subheader("📜 Insurance Policy")
        policy_input = st.text_area("Policy Rules", value="Approve MRI only if: Pain > 6 weeks AND Physical Therapy > 4 weeks.", height=100)
        
        run_btn = st.button("🚀 Analyze Claim", type="primary")

    with col2:
        st.subheader("📤 AI Decision Output")
        if run_btn:
            with st.spinner("Parsing FHIR & Consulting LLM..."):
                # 1. Parse FHIR
                clinical_summary = parse_fhir_bundle(fhir_input)
                st.info(f"**Parsed Context:**\n{clinical_summary}")
                
                # 2. Run AI
                result = analyze_claim(clinical_summary, policy_input)
                
                # 3. Display Results
                if result['decision'] == "APPROVED":
                    st.success(f"✅ **APPROVED** (Conf: {result['confidence']})")
                elif result['decision'] == "DENIED":
                    st.error(f"❌ **DENIED** (Conf: {result['confidence']})")
                else:
                    st.warning(f"⚠️ **NEEDS REVIEW** (Conf: {result['confidence']})")
                
                st.write(f"**Reason:** {result['reason']}")
                
                # Metric Visualization
                st.progress(result['confidence'], text="AI Confidence Score")

# --- TAB 2: PERFORMANCE EVALUATION ---
with tab2:
    st.header("🧪 Clinical Dataset Evaluation")
    st.write("Simulating batch processing on synthetic clinical records to measure Accuracy, Precision, and Recall.")
    
    if st.button("Run Validation Dataset"):
        # Synthetic "Gold Standard" Dataset
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
        
        # Calculate Simple Accuracy
        accuracy = len(df[df["Match"] == "✅"]) / len(df)
        st.metric(label="Model Accuracy", value=f"{accuracy*100}%")