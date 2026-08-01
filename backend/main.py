# backend/main.py
# FastAPI backend wired to the LangGraph agent.

import os
import json
import uuid
import logging
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from backend.agent import graph

load_dotenv()
logger = logging.getLogger("autoauth")

app = FastAPI(title="Auto-Auth API v2.1")

# Restrict origins via ALLOWED_ORIGINS (comma separated). Note that
# allow_credentials=True with a "*" origin is rejected by browsers, so
# credentials are only enabled when explicit origins are configured.
_origins = [o for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins or ["*"],
    allow_credentials=bool(_origins),
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

LOG_DIR = os.getenv("AUDIT_DIR", "data")
LOG_FILE = os.path.join(LOG_DIR, "audit_log.jsonl")
os.makedirs(LOG_DIR, exist_ok=True)


class AnalysisRequest(BaseModel):
    fhir_bundle: dict
    policy: str | None = None


def save_to_audit_log(entry: dict) -> None:
    """Append one JSON object per line. Append-only suits an audit trail
    better than rewriting the whole file, which loses every prior record
    if the process dies mid-write."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


@app.get("/")
async def root():
    return {"status": "online", "version": "2.1-langgraph"}


@app.post("/analyze")
async def analyze_claim(request: AnalysisRequest):
    try:
        result = graph.invoke({
            "clinical_input": json.dumps(request.fhir_bundle),
            "redacted_input": "",
            "retrieved_policy": "",
            "messages": [],
            "draft_decision": "",
            "critique_verdict": "",
            "critique_feedback": "",
            "revision_count": 0,
            "final_decision": "",
            "final_reasoning": "",
            "confidence": 0.0,
            "escalation_reason": None,
        })
    except Exception as e:
        logger.exception("pipeline failure")
        raise HTTPException(status_code=500, detail="Pipeline failure") from e

    entry = {
        "case_id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        # The redacted input is stored, not the raw bundle, so the audit trail
        # does not itself become a store of identifiers.
        "input_snapshot": result.get("redacted_input"),
        "decision": result["final_decision"],
        "reasoning": result["final_reasoning"],
        # The real parsed confidence that drove the gate. This was previously
        # hardcoded to 0.95 for every case, which made the audit trail useless.
        "confidence": result.get("confidence"),
        "escalation_reason": result.get("escalation_reason"),
        "critique_verdict": result.get("critique_verdict"),
        "revision_count": result.get("revision_count", 0),
        "schema_version": "v2.1-langgraph",
        "status": "COMPLETED",
    }
    save_to_audit_log(entry)
    return entry


@app.get("/audit")
async def get_audit_trail():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]
