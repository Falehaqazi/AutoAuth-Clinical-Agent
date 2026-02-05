import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="Auto-Auth Ops Console", page_icon="🏥", layout="wide")

# Custom CSS for a "Medical Dashboard" feel
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .status-box { padding: 20px; border-radius: 10px; border: 1px solid #e0e0e0; background-color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- API HELPERS ---
API_BASE_URL = "https://autoauth-clinical-agent.onrender.com"

def trigger_analysis(fhir_data, policy_text):
    try:
        payload = {
            "fhir_bundle": fhir_data,
            "policy": policy_text
        }
        response = requests.post(f"{API_BASE_URL}/analyze", json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def fetch_logs():
    try:
        response = requests.get(f"{API_BASE_URL}/audit")
        return response.json()
    except:
        return []

# --- SIDEBAR: OBSERVABILITY (Requirement 3) ---
st.sidebar.title("🛠️ System Health")
st.sidebar.info("Connected to FastAPI Backend: `v1.0.0` (Stable)")

logs = fetch_logs()
if logs:
    df_logs = pd.DataFrame(logs)
    st.sidebar.metric("Total Cases Processed", len(logs))
    approval_rate = (df_logs['decision'] == 'APPROVED').mean()
    st.sidebar.metric("Approval Rate", f"{int(approval_rate*100)}%")
    
    # Simple Latency/Confidence Simulation
    st.sidebar.subheader("AI Confidence Distribution")
    st.sidebar.bar_chart(df_logs['confidence'])

# --- MAIN UI ---
st.title("🏥 Auto-Auth: Intelligent Prior-Auth Pipeline")
st.markdown("---")

tab1, tab2 = st.tabs(["🚀 New Case Analysis", "📜 Audit & Traceability"])

with tab1:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📥 Input Clinical Data")
        
        # Scenario Selector for quick demo
        scenario = st.selectbox("Quick Load Scenario", ["Manual Entry", "Approved Case (Jane Smith)", "Denied Case (John Doe)"])
        
        default_json = {
            "resourceType": "Bundle",
            "patient": {"name": "John Doe"},
            "serviceRequest": {"type": "Lumbar MRI"},
            "clinicalNote": "2 weeks of back pain. No PT."
        }
        
        if scenario == "Approved Case (Jane Smith)":
            default_json = {
                "resourceType": "Bundle",
                "patient": {"name": "Jane Smith"},
                "serviceRequest": {"type": "Lumbar MRI"},
                "clinicalNote": "12 weeks of back pain. Completed 8 weeks of PT with no improvement."
            }

        fhir_input = st.text_area("FHIR JSON Bundle", value=json.dumps(default_json, indent=2), height=300)
        policy_input = st.text_area("Insurance Policy Criteria", value="Approve MRI only if: Pain > 6 weeks AND Physical Therapy > 4 weeks.")
        
        analyze_btn = st.button("🚀 Run AI Pipeline")

    with col2:
        st.subheader("📤 Real-time Decision")
        if analyze_btn:
            with st.spinner("Executing Backend Pipeline..."):
                try:
                    data = json.loads(fhir_input)
                    result = trigger_analysis(data, policy_input)
                    
                    if "error" in result:
                        st.error(f"Backend Error: {result['error']}")
                    else:
                        # Decision Display
                        if result['decision'] == "APPROVED":
                            st.success(f"### DECISION: {result['decision']}")
                        else:
                            st.error(f"### DECISION: {result['decision']}")
                        
                        # Traceability Metadata (Requirement 2)
                        with st.container():
                            st.markdown(f"""
                            <div class="status-box">
                                <b>Case UUID:</b> <code>{result['case_id']}</code><br>
                                <b>Timestamp:</b> {result['timestamp']}<br>
                                <b>Schema Version:</b> {result.get('schema_version', 'v1.0')}<br>
                                <b>AI Confidence:</b> {int(result['confidence']*100)}%
                            </div>
                            """, unsafe_allow_html=True)
                            
                        st.write("#### AI Reasoning")
                        st.info(result['reasoning'])
                except Exception as e:
                    st.error(f"Input Error: Please ensure JSON is valid. {e}")

with tab2:
    st.subheader("🕵️ Audit Trail (HIPAA Traceability)")
    st.write("All decisions are logged at the API layer for compliance review.")
    
    if logs:
        # Re-formatting for display
        display_df = pd.DataFrame(logs)[['case_id', 'timestamp', 'decision', 'confidence']]
        st.dataframe(display_df, use_container_width=True)
        
        st.download_button(
            label="📥 Export Audit Log (CSV)",
            data=display_df.to_csv().encode('utf-8'),
            file_name=f"audit_log_{datetime.now().strftime('%Y%m%d')}.csv",
            mime='text/csv',
        )
    else:
        st.write("No audit logs found. Run an analysis to generate data.")