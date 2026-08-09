# Sourcing the 12 policies

This is the only part that can't be generated. It's mechanical, not hard.
Budget 20–30 minutes per policy. Do as many as you can tonight, finish the rest
in one sitting later.

## Where to get them

All of these are public, no login, no paywall:

- **Aetna Clinical Policy Bulletins** — start here. Criteria are written as
  numbered clinical conditions, which is exactly the shape this kit expects.
- **Cigna Medical Coverage Policies** and **UnitedHealthcare Medical Policies** —
  same structure, and useful when an Aetna bulletin is vague.

**Correction — do not start with CMS LCDs.** I originally recommended them and
that was wrong. Checked against the actual documents: for advanced imaging there
is often no NCD at all, coverage is split across seven regional MAC-level LCDs
that disagree, many published articles are superseded drafts, and what they
contain is a list of a thousand-plus covered ICD-10 codes plus documentation
boilerplate ("the record must be legible", "a physician's order is required").
That does not decompose into `required` / `any_of` / `exclusions` predicates.
Commercial payer policies do. Use CMS only for a procedure where you find an LCD
that genuinely states numbered clinical criteria, and check its revision status.

Pick whichever states its criteria most explicitly. You are not doing a payer
comparison; you need twelve policies whose criteria a reader can check.

## Which twelve

You already have three encoded in `policy_store.py`. Replace their invented text
with real sourced text, then add nine more. Prior authorization concentrates in
these areas — pick nine that have crisp, countable criteria:

| # | Area | Typical code |
|---|---|---|
| 1 | Lumbar spine MRI | CPT 72148 *(have)* |
| 2 | Total knee arthroplasty | CPT 27447 *(have)* |
| 3 | Brain MRI with contrast | CPT 70553 *(have)* |
| 4 | Lumbar spinal fusion | CPT 22612 |
| 5 | Bariatric surgery | CPT 43644 |
| 6 | Polysomnography / sleep study | CPT 95810 |
| 7 | CPAP device | HCPCS E0601 |
| 8 | Total hip arthroplasty | CPT 27130 |
| 9 | Cardiac CT angiography | CPT 75574 |
| 10 | Shoulder arthroscopy | CPT 29827 |
| 11 | Power wheelchair | HCPCS K0823 |
| 12 | Hyperbaric oxygen therapy | HCPCS G0277 |

Favour procedures with **duration or count thresholds** ("at least 6 weeks",
"at least 3 months", "two prior failed trials"). Those give you clean
`borderline` cases — a note documenting exactly 6 weeks sits precisely on the
line, which is where a confidence-gated system should hesitate.

## How to encode one

Read the policy, then decompose it into three buckets:

- **`required`** — every one of these must hold to approve. ALL semantics.
- **`any_of`** — at least one must hold. Leave `{}` if the policy has no such clause.
- **`exclusions`** — any one of these forces a denial.

Give each an id (`R1`, `A1`, `X1`) and a one-line restatement. Keep the restatement
close to the source wording; you're not interpreting, you're indexing.

```json
{"policy_id":"P04","title":"Lumbar spinal fusion","code":"22612","code_system":"CPT",
 "source_name":"CMS LCD L______","source_url":"https://...","retrieved_on":"2026-08-09",
 "required":{"R1":"...","R2":"..."},"any_of":{"A1":"..."},"exclusions":{"X1":"..."}}
```

One line per policy in `synthpa60/policies.jsonl`.

**Record `source_url` and `retrieved_on` for every one.** Payer policies get
revised. Without the retrieval date your benchmark becomes unauditable the first
time a policy changes, and that is the question a reviewer will ask.

## What the paper has to say about this

Three sentences you'll need in the methods section, so decide them now:

1. **Criteria are transcribed, not authored.** State that gold labels are a
   deterministic function of a criteria vector via a published rule
   (`derive_label`), not a human judgement call.
2. **Notes are model-generated, validated by one annotator.** One annotator is a
   real limitation — name it rather than letting a reviewer find it. If you can
   get any second reader for even 15 of the 60 and report agreement, do it.
3. **The generator is not the system under test.** GPT-4o or Gemini writes the
   notes; Llama-3.1-8b-instant is evaluated. Say so explicitly.

## One design decision to make before generating

`derive_label` emits three labels: `APPROVED`, `DENIED`, `MORE_INFO`.

Your agent currently emits only `APPROVED` or `DENIED` from `finalize_node`,
which then get mapped to `PENDING_REVIEW` by the escalation rules. So the gold
label space and the system's output space don't match, and you have to say how
you're scoring that.

The defensible reading, and the one that fits your thesis: `MORE_INFO` and
`DENIED` are both cases where auto-approval is wrong, so the correct system
behaviour for both is escalation. Score them as "should escalate" and report
approve-vs-escalate as the primary task, with the three-way breakdown in an
appendix. That makes the confidence gate the object of study rather than a
detail — which is what the paper is about.

Write this down before you generate cases. It changes nothing about the data and
everything about the results section.
