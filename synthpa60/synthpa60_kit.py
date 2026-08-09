#!/usr/bin/env python3
"""
SynthPA-60 construction kit.

The design principle that makes this benchmark defensible: you are NOT the
oracle. Gold labels are a deterministic function of a criteria vector, and the
criteria come from published payer policy text. A reviewer can audit
derive_label() in thirty seconds and check it against the policy PDF. That is
the difference between a benchmark and a pile of cases you labelled by hand.

The generation direction matters too. You pick the criteria vector FIRST, then
have a model write a clinical note that realises it. Never write a note and
then label it -- that reintroduces you as the oracle and the labels inherit
your errors.

Workflow:
    1. Source 12 policies -> policies.jsonl        (manual, see POLICY_SOURCING.md)
    2. python synthpa60_kit.py plan                 -> cases_plan.jsonl (60 criteria vectors)
    3. python synthpa60_kit.py prompts              -> prompts/*.txt for the generator model
    4. paste generated notes back into cases.jsonl  (manual validation pass)
    5. python synthpa60_kit.py validate             -> hard fails on any inconsistency

CONTAMINATION RULE: generate notes with GPT-4o or Gemini. Never with
llama-3.1-8b-instant, which is the system under test.
"""

import argparse
import json
import os
import random
from collections import Counter, defaultdict

# --------------------------------------------------------------------------
# SCHEMA
# --------------------------------------------------------------------------

# policies.jsonl -- one object per line:
POLICY_SCHEMA = {
    "policy_id": "P01",
    "title": "Lumbar spine MRI without contrast",
    "code": "72148",
    "code_system": "CPT",
    "source_name": "CMS LCD L34807",          # real, citable
    "source_url": "https://...",              # the page you actually read
    "retrieved_on": "2026-08-09",
    "required": {                              # ALL must be true to approve
        "R1": "Low back pain documented for at least 6 weeks",
        "R2": "Failed conservative therapy including at least 4 weeks of PT",
    },
    "any_of": {                                # at least ONE must be true
        "A1": "Neurological deficit on exam",
        "A2": "Red flag symptoms present",
    },
    "exclusions": {                            # ANY true forces denial
        "X1": "Imaging of the same region within the prior 6 months without interval change",
    },
}

# cases.jsonl -- one object per line:
CASE_SCHEMA = {
    "case_id": "C001",
    "policy_id": "P01",
    "stratum": "clear_approve",
    "criteria": {"R1": True, "R2": True, "A1": True, "A2": False, "X1": False},
    "gold_decision": "APPROVED",               # MUST equal derive_label(...)
    "gold_policy_id": "P01",                   # for retrieval recall@k
    "distractor_policy_id": None,              # set for retrieval_distractor stratum
    "clinical_note": "...",                    # generated, then human-validated
    "note_contains_phi": True,                 # exercises the redaction node
    "validated_by": "FQ",
    "validated_on": "2026-08-__",
}

DECISIONS = ["APPROVED", "DENIED", "MORE_INFO"]
UNDOC = "undocumented"


# --------------------------------------------------------------------------
# LABEL DERIVATION -- the auditable core
# --------------------------------------------------------------------------

def derive_label(policy: dict, criteria: dict) -> str:
    """Deterministic gold label from a criteria vector.

    Criterion values are True, False, or "undocumented".

    Order of precedence:
      1. Any exclusion affirmatively met      -> DENIED
      2. Any required criterion affirmatively unmet -> DENIED
      3. Anything load-bearing undocumented   -> MORE_INFO
      4. any_of group with nothing true       -> DENIED
      5. Otherwise                            -> APPROVED

    MORE_INFO is deliberately separate from DENIED. A case you cannot decide
    is not a case you decided against, and conflating them is exactly the
    failure mode the escalation rule exists to prevent.
    """
    for cid in policy.get("exclusions", {}):
        if criteria.get(cid) is True:
            return "DENIED"

    required = policy.get("required", {})
    for cid in required:
        if criteria.get(cid) is False:
            return "DENIED"
    for cid in required:
        if criteria.get(cid) == UNDOC:
            return "MORE_INFO"

    any_of = policy.get("any_of", {})
    if any_of:
        vals = [criteria.get(cid) for cid in any_of]
        if not any(v is True for v in vals):
            return "MORE_INFO" if any(v == UNDOC for v in vals) else "DENIED"

    for cid in policy.get("exclusions", {}):
        if criteria.get(cid) == UNDOC:
            return "MORE_INFO"

    return "APPROVED"


# --------------------------------------------------------------------------
# STRATIFIED PLAN -- 60 cases over 12 policies, 5 each
# --------------------------------------------------------------------------

STRATA = {
    "clear_approve":       15,   # every criterion comfortably met
    "clear_deny":          15,   # a required criterion affirmatively unmet
    "documentation_gap":   15,   # load-bearing criterion undocumented -> MORE_INFO
    "borderline":           8,   # criterion met exactly at the stated threshold
    "retrieval_distractor": 7,   # note also mentions a code from another policy
}


def _vector(policy, stratum, rng):
    req = list(policy.get("required", {}))
    anyof = list(policy.get("any_of", {}))
    excl = list(policy.get("exclusions", {}))
    v = {c: True for c in req}
    v.update({c: False for c in anyof})
    if anyof:
        v[rng.choice(anyof)] = True
    v.update({c: False for c in excl})

    if stratum == "clear_deny":
        if req and rng.random() < 0.7:
            v[rng.choice(req)] = False
        elif excl:
            v[rng.choice(excl)] = True
        elif anyof:
            for c in anyof:
                v[c] = False
        else:
            v[rng.choice(req)] = False
    elif stratum == "documentation_gap":
        pool = req or anyof or excl
        v[rng.choice(pool)] = UNDOC
    return v


def cmd_plan(args):
    policies = [json.loads(l) for l in open(args.policies) if l.strip()]
    if len(policies) < 2:
        raise SystemExit("need at least 2 policies; 12 is the target")
    rng = random.Random(args.seed)

    assignments = []
    for stratum, n in STRATA.items():
        assignments += [stratum] * n
    rng.shuffle(assignments)

    # spread evenly across policies
    order = []
    while len(order) < len(assignments):
        order += rng.sample(policies, len(policies))
    order = order[:len(assignments)]

    cases = []
    for i, (stratum, policy) in enumerate(zip(assignments, order), start=1):
        v = _vector(policy, stratum, rng)
        distractor = None
        if stratum == "retrieval_distractor":
            others = [p for p in policies if p["policy_id"] != policy["policy_id"]]
            distractor = rng.choice(others)["policy_id"]
        cases.append({
            "case_id": f"C{i:03d}",
            "policy_id": policy["policy_id"],
            "stratum": stratum,
            "criteria": v,
            "gold_decision": derive_label(policy, v),
            "gold_policy_id": policy["policy_id"],
            "distractor_policy_id": distractor,
            "clinical_note": "",
            "note_contains_phi": True,
            "validated_by": "",
            "validated_on": "",
        })

    with open(args.out, "w") as f:
        for c in cases:
            f.write(json.dumps(c) + "\n")
    dist = Counter(c["gold_decision"] for c in cases)
    print(f"wrote {len(cases)} case slots -> {args.out}")
    print("label distribution:", dict(dist))
    print("per policy:", dict(Counter(c["policy_id"] for c in cases)))


# --------------------------------------------------------------------------
# GENERATION PROMPTS
# --------------------------------------------------------------------------

GEN_TEMPLATE = """You are generating a synthetic prior authorization case for a
research benchmark. All content is fictional. No real patient data.

PAYER POLICY ({policy_id} -- {title}, {code_system} {code}):
{policy_text}

Write a clinical note for a prior authorization request for this procedure.

The note MUST make each of the following criteria unambiguously true, false, or
absent, exactly as specified. This is the whole point -- a reader with the
policy in hand must reach the same verdict on every line.

{criteria_block}

Requirements:
- 120 to 200 words, in the register of a real referral note.
- Include a patient name, an MRN, and a date of birth in labelled form
  (e.g. "Patient: ...", "MRN: ...", "DOB: ..."). These are fictional and exist
  so the pipeline's de-identification step has something to remove.
- State the requested {code_system} code {code} explicitly.
- Do NOT state a decision, a recommendation, or the word approve/deny.
- Do NOT hint at which criteria are met. Report clinical facts only.
- For any criterion marked ABSENT: say nothing about it at all. Do not write
  "no PT documented" -- simply omit it. Absence must look like a real
  documentation gap, not a negative finding.
{distractor_line}
Output only the note text.
"""

DISTRACTOR_LINE = ("- Also mention, in passing, an unrelated prior or planned "
                   "procedure so that a retrieval system faces a competing policy. "
                   "It must not affect whether the criteria above are met.\n")


def cmd_prompts(args):
    policies = {p["policy_id"]: p for p in
                (json.loads(l) for l in open(args.policies) if l.strip())}
    cases = [json.loads(l) for l in open(args.plan) if l.strip()]
    os.makedirs(args.outdir, exist_ok=True)

    for c in cases:
        p = policies[c["policy_id"]]
        labels = {**p.get("required", {}), **p.get("any_of", {}),
                  **p.get("exclusions", {})}
        lines = []
        for cid, val in c["criteria"].items():
            word = {True: "TRUE", False: "FALSE", UNDOC: "ABSENT"}[val]
            lines.append(f"  [{word}] {labels.get(cid, cid)}")
        text = GEN_TEMPLATE.format(
            policy_id=p["policy_id"], title=p["title"],
            code_system=p.get("code_system", "CPT"), code=p.get("code", ""),
            policy_text=json.dumps({k: p[k] for k in
                                    ("required", "any_of", "exclusions") if k in p},
                                   indent=2),
            criteria_block="\n".join(lines),
            distractor_line=DISTRACTOR_LINE if c["distractor_policy_id"] else "")
        with open(os.path.join(args.outdir, f"{c['case_id']}.txt"), "w") as f:
            f.write(text)
    print(f"wrote {len(cases)} prompts -> {args.outdir}/")
    print("Generate with GPT-4o or Gemini. NOT llama-3.1-8b-instant.")


# --------------------------------------------------------------------------
# VALIDATOR
# --------------------------------------------------------------------------

def cmd_validate(args):
    policies = {p["policy_id"]: p for p in
                (json.loads(l) for l in open(args.policies) if l.strip())}
    cases = [json.loads(l) for l in open(args.cases) if l.strip()]
    errs, warns = [], []

    if len(policies) != 12:
        warns.append(f"{len(policies)} policies, target is 12")
    if len(cases) != 60:
        warns.append(f"{len(cases)} cases, target is 60")

    seen = set()
    for c in cases:
        cid = c["case_id"]
        if cid in seen:
            errs.append(f"{cid}: duplicate case_id")
        seen.add(cid)
        p = policies.get(c["policy_id"])
        if not p:
            errs.append(f"{cid}: unknown policy {c['policy_id']}")
            continue

        expected = derive_label(p, c["criteria"])
        if c["gold_decision"] != expected:
            errs.append(f"{cid}: gold={c['gold_decision']} but derive_label gives "
                        f"{expected} -- the label and the criteria disagree")

        known = set(p.get("required", {})) | set(p.get("any_of", {})) | set(p.get("exclusions", {}))
        for k in c["criteria"]:
            if k not in known:
                errs.append(f"{cid}: criterion {k} not defined in {p['policy_id']}")
        for k in known:
            if k not in c["criteria"]:
                errs.append(f"{cid}: criterion {k} missing from vector")

        note = (c.get("clinical_note") or "").strip()
        if not note:
            errs.append(f"{cid}: no clinical_note")
        else:
            low = note.lower()
            for banned in ("approve", "denied", "deny", "authorization granted"):
                if banned in low:
                    errs.append(f"{cid}: note leaks the decision (contains '{banned}')")
            if str(p.get("code", "")) and str(p["code"]) not in note:
                warns.append(f"{cid}: note does not state code {p['code']}")
            if len(note.split()) < 60:
                warns.append(f"{cid}: note is only {len(note.split())} words")
        if not c.get("validated_by"):
            warns.append(f"{cid}: not marked human-validated")

    dist = Counter(c["gold_decision"] for c in cases)
    for d in DECISIONS:
        if dist.get(d, 0) < 5:
            warns.append(f"only {dist.get(d,0)} {d} cases -- too few to estimate anything")

    per_pol = Counter(c["policy_id"] for c in cases)
    for pid in policies:
        if per_pol.get(pid, 0) == 0:
            warns.append(f"policy {pid} has no cases")

    print(f"cases: {len(cases)}  policies: {len(policies)}")
    print("labels:", dict(dist))
    print("strata:", dict(Counter(c.get("stratum") for c in cases)))
    for w in warns:
        print("WARN ", w)
    for e in errs:
        print("ERROR", e)
    if errs:
        raise SystemExit(f"\n{len(errs)} errors. Benchmark is not usable yet.")
    print("\nOK -- benchmark is internally consistent.")
    print("Now freeze it: git add, commit, and record the commit hash in the paper.")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("plan", help="generate 60 criteria vectors + gold labels")
    p1.add_argument("--policies", default="synthpa60/policies.jsonl")
    p1.add_argument("--out", default="synthpa60/cases_plan.jsonl")
    p1.add_argument("--seed", type=int, default=20260809)
    p1.set_defaults(func=cmd_plan)

    p2 = sub.add_parser("prompts", help="write generation prompts")
    p2.add_argument("--policies", default="synthpa60/policies.jsonl")
    p2.add_argument("--plan", default="synthpa60/cases_plan.jsonl")
    p2.add_argument("--outdir", default="synthpa60/prompts")
    p2.set_defaults(func=cmd_prompts)

    p3 = sub.add_parser("validate", help="hard-check the finished benchmark")
    p3.add_argument("--policies", default="synthpa60/policies.jsonl")
    p3.add_argument("--cases", default="synthpa60/cases.jsonl")
    p3.set_defaults(func=cmd_validate)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
