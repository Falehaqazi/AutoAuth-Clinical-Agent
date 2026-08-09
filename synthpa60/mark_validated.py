#!/usr/bin/env python3
"""Stamp validated_by once you have worked through the worksheet."""
import json, sys, datetime
if len(sys.argv) < 2:
    raise SystemExit("usage: python mark_validated.py <initials>  e.g. FQ")
who = sys.argv[1]
cases = [json.loads(l) for l in open("synthpa60/cases.jsonl")]
today = datetime.date.today().isoformat()
for c in cases:
    c["validated_by"] = who
    c["validated_on"] = today
with open("synthpa60/cases.jsonl", "w") as f:
    for c in cases:
        f.write(json.dumps(c) + "\n")
print(f"stamped {len(cases)} cases: validated_by={who} validated_on={today}")
