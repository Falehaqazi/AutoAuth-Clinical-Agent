#!/usr/bin/env python3
"""Build a validation worksheet.

Turns "read 60 notes and somehow check them" into 60 short, specific yes/no
questions. For each case it prints the note next to the exact claim each
criterion makes, so you are confirming a fact rather than forming a judgement.

    python make_worksheet.py           -> validation_worksheet.md
    python mark_validated.py FQ        -> stamps validated_by once you're done
"""
import json

cases = [json.loads(l) for l in open("synthpa60/cases.jsonl")]
pols = {p["policy_id"]: p for p in
        (json.loads(l) for l in open("synthpa60/policies.jsonl"))}

WORD = {True: "TRUE", False: "FALSE", "undocumented": "ABSENT"}
ASK = {
    True:  "note must state this is met",
    False: "note must state this is NOT met",
    "undocumented": "note must NOT establish this either way",
}

# criteria the automated audit flagged for a closer look
FLAGGED = {"C006", "C014", "C026", "C027", "C031", "C032", "C038", "C052", "C055"}

out = ["# SynthPA-60 validation worksheet", "",
       "For each case: read the note, confirm each line, tick the box.",
       "A case passes only if every criterion line is correct **and** the note",
       "never states or implies a decision.", "",
       f"{len(cases)} cases. Nine are marked FLAGGED — the automated audit found",
       "the note discusses a criterion marked ABSENT. In most of these the note",
       "says the information *could not be established*, which is arguably the",
       "right way to render a documentation gap in realistic prose. You are the",
       "one who decides whether that reads as absent or as a negative finding.",
       "", "---", ""]

for c in cases:
    p = pols[c["policy_id"]]
    labels = {**p.get("required", {}), **p.get("any_of", {}), **p.get("exclusions", {})}
    flag = "  **FLAGGED**" if c["case_id"] in FLAGGED else ""
    out += [f"## {c['case_id']} — {p['title']} ({p['code_system']} {p['code']}){flag}", "",
            f"stratum `{c['stratum']}` · gold **{c['gold_decision']}**", "",
            "> " + c["clinical_note"].replace("\n", " "), "", "Confirm:", ""]
    for cid, val in c["criteria"].items():
        out.append(f"- [ ] **{WORD[val]}** — {labels.get(cid, cid)}  \n"
                   f"      *{ASK[val]}*")
    out += ["- [ ] note states no decision and no recommendation",
            "- [ ] note contains a fictional name, MRN and DOB", ""]
    if c["distractor_policy_id"]:
        out += [f"- [ ] mentions a second unrelated procedure "
                f"({pols[c['distractor_policy_id']]['title']}) that does not affect the criteria", ""]
    out += ["---", ""]

open("validation_worksheet.md", "w").write("\n".join(out))
print(f"wrote validation_worksheet.md — {len(cases)} cases, {len(FLAGGED)} flagged")
print("Work through it, then run: python mark_validated.py <your initials>")
