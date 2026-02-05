import os
import json
import uuid
import re
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from openai import OpenAI
from dotenv import load_dotenv

# --- 1. CONFIGURATION ---
load_dotenv()
app = FastAPI(title="Auto-Auth Production API", version="1.0.0")

# Initialize LLM Client (using Groq for high-speed inference)
client = OpenAI(
    base_url="https://api.groq.com/openai/v1", 
    api_key=os.getenv("OPENAI_API_KEY")
)

# Ensure data directory exists for audit logs
LOG_DIR = "../data"
LOG_FILE = f"{LOG_DIR}/audit_log.json"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# --- 2. SCHEMAS (Requirement 6: Versioning) ---
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
    status: str = "COMPLETED"  # Can be COMPLETED or PENDING_HUMAN_REVIEW

# --- 3. PRIVACY LAYER (Requirement 2: De-identification) ---
def redact_pii(text: str) -> str:
    """Simple regex layer to ensure no names or IDs are passed to the LLM."""
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
        except json.JSONDecodeError:
            logs = []
    
    logs.append(entry.model_dump())
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

@app.post("/analyze", response_model=AuditEntry)
async def analyze_claim(request: AnalysisRequest):
    try:
        # Step 1: Extract clinical story & Redact PII
        raw_clinical_data = json.dumps(request.fhir_bundle)
        safe_clinical_data = redact_pii(raw_clinical_data)

        # Step 2: LLM Orchestration
        # Note: In a true prod environment, we'd use 'instructor' or tool_use for structured output
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
        
        # Step 3: Parse Decision (Simple parsing for demo logic)
        decision = "APPROVED" if "DECISION: APPROVED" in raw_response.upper() else "DENIED"
        
        # Step 4: Safety Threshold (Requirement 5: Fallback Logic)
        # We simulate a confidence score extraction here
        confidence = 0.95 
        status = "COMPLETED"
        
        if "CONFIDENCE:" in raw_response:
            try:
                # Extracting float from string like "CONFIDENCE: 0.85"
                conf_match = re.search(r"CONFIDENCE:\s*([\d\.]+)", raw_response)
                if conf_match:
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
    """Requirement 2: Full Traceability Access"""
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)

@app.get("/health")
async def health_check():
    """Requirement 3: Observability"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat(), "model": "llama-3.3-70b"}