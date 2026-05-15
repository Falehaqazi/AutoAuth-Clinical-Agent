# backend/main.py
# FastAPI backend — now wired to the LangGraph agent instead of a single LLM call.

import os
import json
import uuid
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from backend.agent import graph

load_dotenv()

app = FastAPI(title="Auto-Auth Production API v2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOG_DIR = "data"
LOG_FILE = f"{LOG_DIR}/audit_log.json"
os.makedirs(LOG_DIR, exist_ok=True)

class AnalysisRequest(BaseModel):
    fhir_bundle: dict
    policy: str

def save_to_audit_log(entry: dict):
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

@app.get("/")
async def root():
    return {"status": "online", "version": "2.0-langgraph"}

@app.post("/analyze")
async def analyze_claim(request: AnalysisRequest):
    try:
        clinical_input = json.dumps(request.fhir_bundle)
        
        result = graph.invoke({
            "clinical_input": clinical_input,
            "redacted_input": "",
            "retrieved_policy": "",
            "messages": [],
            "draft_decision": "",
            "critique_verdict": "",
            "final_decision": "",
            "final_reasoning": "",
            "revision_count": 0,
        })

        entry = {
            "case_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "input_snapshot": request.fhir_bundle,
            "decision": result["final_decision"],
            "reasoning": result["final_reasoning"],
            "confidence": 0.95,
            "schema_version": "v2.0-langgraph",
            "status": "COMPLETED"
        }

        save_to_audit_log(entry)
        return entry

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pipeline Failure: {str(e)}")

@app.get("/audit")
async def get_audit_trail():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)