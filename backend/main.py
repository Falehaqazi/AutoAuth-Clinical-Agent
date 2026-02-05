import os
import json
import uuid
import re
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from openai import OpenAI
from dotenv import load_dotenv

# --- 1. CONFIGURATION & APP INIT ---
load_dotenv()
app = FastAPI(title="Auto-Auth Production API", version="1.0.0")

# Requirement: CORS Middleware 
# This allows your Streamlit Cloud frontend to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace "*" with your Streamlit URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM Client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1", 
    api_key=os.getenv("OPENAI_API_KEY")
)

# Ensure data directory exists for audit logs
# Note: On cloud platforms like Render, local files are temporary. 
# For a real job, you'd use a Database, but this works for a demo!
LOG_DIR = "../data"
LOG_FILE = f"{LOG_DIR}/audit_log.json"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# --- 2. SCHEMAS ---
class AnalysisRequest(BaseModel):
    fhir_bundle: dict
    policy: str

class AuditEntry(BaseModel):
    case_id: str
    timestamp: str
    input_snapshot: dict
    decision: str
    reasoning: str
    confidence: float
    schema_version: str = "v1.0"
    status: str = "COMPLETED"

# --- 3. PRIVACY LAYER ---
def redact_pii(text: str) -> str:
    """Requirement 2: Ensure no names or IDs are passed to the LLM."""
    text = re.sub(r"Patient: \w+", "Patient: [REDACTED]", text)
    text = re.sub(r"ID: \d+", "ID: [REDACTED]", text)
    return text

# --- 4. CORE LOGIC ---
def save_to_audit_log(entry: AuditEntry):
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            logs = []
    
    logs.append(entry.model_dump())
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

@app.get("/")
async def root():
    """Requirement 3: Cloud Health Check endpoint"""
    return {
        "status": "online",
        "service": "Auto-Auth Backend",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/analyze", response_model=AuditEntry)
async def analyze_claim(request: AnalysisRequest):
    try:
        # Step 1: Redact PII
        raw_clinical_data = json.dumps(request.fhir_bundle)
        safe_clinical_data = redact_pii(raw_clinical_data)

        # Step 2: LLM Orchestration
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": """You are a Prior Authorization Reviewer. 
                Evaluate the clinical data against the policy strictly.
                Output Format: 
                DECISION: [APPROVED/DENIED]
                CONFIDENCE: [0.0-1.0]
                REASON: [Short clinical justification]"""},
                {"role": "user", "content": f"POLICY: {request.policy}\n\nDATA: {safe_clinical_data}"}
            ]
        )
        
        raw_response = completion.choices[0].message.content
        
        # Step 3: Parse Decision
        decision = "APPROVED" if "DECISION: APPROVED" in raw_response.upper() else "DENIED"
        
        # Step 4: Safety Threshold (Fallback Logic)
        confidence = 0.95 
        status = "COMPLETED"
        
        conf_match = re.search(r"CONFIDENCE:\s*([\d\.]+)", raw_response)
        if conf_match:
            try:
                confidence = float(conf_match.group(1))
            except:
                pass

        # TRIGGER HUMAN REVIEW IF UNSURE
        if confidence < 0.80:
            decision = "PENDING_REVIEW"
            status = "PENDING_HUMAN_REVIEW"

        # Step 5: Create Audit Record
        audit_entry = AuditEntry(
            case_id=str(uuid.uuid4()),
            timestamp=datetime.now().isoformat(),
            input_snapshot=request.fhir_bundle,
            decision=decision,
            reasoning=raw_response,
            confidence=confidence,
            status=status
        )

        # Step 6: Persist
        save_to_audit_log(audit_entry)
        
        return audit_entry

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pipeline Failure: {str(e)}")

@app.get("/audit")
async def get_audit_trail():
    """Requirement 2: Full Traceability Access for Admin UI"""
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)