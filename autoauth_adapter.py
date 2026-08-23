import os, re, time, json
from backend import agent as A

_P = json.loads('{}')
try:
    _P = {p["policy_id"]: (p.get("text") or p.get("body") or "")
          for p in (json.loads(l) for l in open("synthpa60/policies.jsonl") if l.strip())}
except Exception as e:
    print("policy load failed:", e)

DEC = re.compile(r"DECISION\s*:\s*\[?\s*(APPROVED|DENIED)\s*\]?", re.I)
CONF = re.compile(r"CONFIDENCE\s*:\s*\[?\s*([01](?:\.\d+)?|\.\d+)", re.I)

def _msgs_text(state):
    out = []
    for m in state.get("messages") or []:
        c = getattr(m, "content", None)
        if isinstance(c, str) and c.strip():
            out.append(c)
    return out

def _tokens(state):
    i = o = 0
    for m in state.get("messages") or []:
        u = getattr(m, "usage_metadata", None) or {}
        i += u.get("input_tokens", 0); o += u.get("output_tokens", 0)
    return i, o

def run_case(case, seed):
    t0 = time.time()
    note = case["clinical_note"]
    state = A.graph.invoke({"clinical_input": note, "messages": [], "revision_count": 0})

    gold3 = case["gold_decision"]
    final = state.get("final_decision")
    gold_act = "auto_approve" if gold3 == "APPROVED" else "escalate"
    sys_act  = "auto_approve" if final == "APPROVED" else "escalate"

    texts = _msgs_text(state)
    blob = "\n".join(texts[-3:])
    draft_raw = state.get("draft_decision") or ""
    dm = DEC.search(str(draft_raw)) or DEC.search(blob)
    cm = CONF.search(str(draft_raw)) or CONF.search(blob)

    red = state.get("redacted_input") or ""
    nm = re.search(r"Patient:\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)", note)
    mrn = re.search(r"MRN[:.\s]+([0-9]{4,})", note)
    leaked = [t for t in [nm.group(1) if nm else None, mrn.group(1) if mrn else None]
              if t and t in red]

    pol = state.get("retrieved_policy") or ""
    def _in(pid):
        if not pid: return None
        if pid in pol: return True
        t = _P.get(pid, "")
        return bool(t) and t[:80].strip() in pol

    ti, to = _tokens(state)
    return {
        "case_id": case["case_id"], "stratum": case["stratum"], "seed": seed,
        "gold_decision": gold_act, "pred_decision": sys_act,
        "gold_decision_3class": gold3, "final_decision_raw": final,
        "false_approval": gold3 != "APPROVED" and final == "APPROVED",
        "false_escalation": gold3 == "APPROVED" and final != "APPROVED",
        "draft_decision": dm.group(1).upper() if dm else "UNPARSEABLE",
        "draft_correct": (dm.group(1).upper() == gold3) if (dm and gold3 in ("APPROVED","DENIED")) else None,
        "confidence": float(state.get("confidence") or (cm.group(1) if cm else 0.0)),
        "confidence_raw": cm.group(0) if cm else None,
        "escalated": final != "APPROVED",
        "escalation_reason": state.get("escalation_reason"),
        "autonomous_denial": final == "DENIED",
        "critique_verdict": state.get("critique_verdict"),
        "critique_flagged": state.get("critique_verdict") == "REVISE",
        "revision_count": state.get("revision_count", 0),
        "pre_critique_decision": None,
        "retrieval_scores": state.get("retrieval_scores") or [],
        "gold_policy_retrieved": case.get("gold_policy_id") in (state.get("retrieved_policy_ids") or []),
        "distractor_retrieved": case.get("distractor_policy_id") in (state.get("retrieved_policy_ids") or []),
        "retrieved_chunk_ids": state.get("retrieved_chunk_ids") or [],
        "retrieved_policy_ids": state.get("retrieved_policy_ids") or [],
        "gold_chunk_ids": [],
        "cited_policy_id": (state.get("retrieved_policy_ids") or [None])[0],
        "gold_policy_id": case.get("gold_policy_id"),
        "criteria_gold": case.get("criteria"),
        "phi_spans_gold": ["name", "mrn"] if case.get("note_contains_phi") else [],
        "phi_leaked_spans": leaked,
        "latency_total_s": round(time.time() - t0, 3), "latency_per_node": {},
        "tokens_in": ti, "tokens_out": to,
        "json_parse_failures": int(dm is None), "retries": 0, "http_429s": 0,
        "model": "openai/gpt-oss-20b",
        "temperature": float(os.getenv("AUTOAUTH_TEMP", "0.1")),
        "error": None,
        "final_reasoning": state.get("final_reasoning"),
        "raw_final_output": blob[-4000:],
    }
