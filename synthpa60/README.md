# SynthPA-60

A 60-case benchmark for prior authorization decision support, over 12 payer
policies, with gold labels derived deterministically from criteria vectors.

Built 09 August 2026.

```
policies.jsonl   12 policies, criteria decomposed into required / any_of / exclusions
cases.jsonl      60 cases: criteria vector, gold label, clinical note
cases_plan.jsonl the criteria vectors before notes were attached (audit trail)
synthpa60_kit.py derive_label(), the stratified planner, and the validator
```

Freeze hashes at construction:

```
policies.jsonl  sha256 9f269eb10a7fed0c5c3a6f5bb3dec648cc86ced8f5f51737abb8254bcada4b40
cases.jsonl     sha256 37fa82b4256918495b1d6133561c8d12e74c319fb8f34c7e6eb6902205d2684d
```

## Composition

| Stratum | n | Gold label |
|---|---|---|
| clear_approve | 15 | APPROVED |
| clear_deny | 15 | DENIED |
| documentation_gap | 15 | MORE_INFO |
| borderline | 8 | APPROVED |
| retrieval_distractor | 7 | APPROVED |

Labels: 30 APPROVED, 15 DENIED, 15 MORE_INFO. Five cases per policy across all
12 policies. Notes run 140–183 words.

`borderline` cases sit exactly on a stated threshold — conservative therapy at
precisely three months, AHI of exactly 15.0, an ABI of 0.90 at the lower bound of
normal. These are where a confidence-gated system should hesitate, and they are
the reason the risk-coverage curve is informative rather than flat.

`retrieval_distractor` cases mention a second, unrelated procedure so that
retrieval faces a competing policy. The distractor never affects whether the
criteria are met.

## How gold labels were produced

Labels are **not** human judgements. For each case a criteria vector was fixed
first, then `derive_label()` computed the label from it by a published rule:

1. Any exclusion affirmatively met → DENIED
2. Any required criterion affirmatively unmet → DENIED
3. Any load-bearing criterion undocumented → MORE_INFO
4. `any_of` group with nothing true → DENIED
5. Otherwise → APPROVED

The note was then written to realise that vector. Generating in this direction —
vector first, prose second — means the label cannot inherit an annotator's
reading of an ambiguous note. Anyone can audit the twenty lines of
`derive_label()` against the criteria and check every label in the set.

MORE_INFO is deliberately distinct from DENIED. A case you cannot decide is not
a case you decided against, and collapsing the two is the exact failure the
escalation rule exists to prevent.

## Provenance and limitations

State all four of these in the paper. They are the questions a reviewer will
ask, and each is cheaper to declare than to be caught on.

**The policies are synthetic.** All twelve were authored for this benchmark,
modelled on the structure of commercial medical policy bulletins. They are not
transcribed from, and do not reproduce, any published payer policy. Every record
carries this in its `source_name` field. The clinical criteria are plausible but
carry no regulatory authority, and results here do not transfer to any real
payer's decisions. The upside is that the benchmark is releasable: transcribed
payer policy text is copyrighted and could not be redistributed as a dataset.

**Notes were model-generated.** Written by Claude Opus 5 from the criteria
vectors. Critically, this is *not* the system under test — the pipeline runs
llama-3.1-8b-instant — so there is no generator/evaluator contamination. Record
the generator model in the paper.

**Automated audit: complete.** All 280 criterion assignments were machine
checked (`audit.py`) for topic consistency — does the note discuss a criterion
marked TRUE or FALSE, and stay silent on one marked ABSENT. This caught a real
defect in C058, where the vector asserted a documented AHI in a case with no
sleep study; the vector was corrected and the label re-derived (unchanged,
DENIED). Nine cases are marked `automated_audit: flagged_for_review`; in these
the note renders a documentation gap as "could not be established" rather than
by silence, which is arguably more realistic but is a human call. The other 51
carry `automated_audit: passed`.

**Human validation: outstanding.** Every record still reads
`validated_by: "pending"`, and that is accurate. An automated topic check is not
a human confirming the note realises its vector, and the model that wrote the
notes cannot be the one that certifies them. `validation_worksheet.md` reduces
this to 60 sets of tick boxes — each criterion restated as a specific claim to
confirm, with the nine flagged cases marked. Budget around an hour. Then run
`python mark_validated.py FQ`.

**If you decide not to do the read, that is a legitimate option** — but then say
so. Report the benchmark as model-generated and automatically audited, not human
validated, and name it in the limitations. A weaker honest claim costs you far
less than a stronger one that does not hold. What is not available is leaving
`validated_by` filled in by anyone who did not read the notes.

**Patient identifiers are fictional.** Names, MRNs, and dates of birth are
invented, and exist so the pipeline's redaction node has something to remove. No
real patient data is present. State this and that IRB approval is therefore not
required, with that justification, as ML4H asks.

## The label-space mismatch, and what to do about it

`derive_label` emits three labels. Your agent's `finalize_node` emits APPROVED or
DENIED, which the escalation rules then map to PENDING_REVIEW. The spaces do not
match and the paper has to say how that is scored.

The defensible reading, and the one that matches the thesis: MORE_INFO and DENIED
are both cases where auto-approval is wrong, so correct behaviour for both is
escalation. Score **approve vs escalate** as the primary task and put the
three-way breakdown in an appendix. That makes the confidence gate the object of
study rather than a detail.

Decide this before running evaluations. It changes nothing in the data and
everything in the results section.

## Note on the safety claim

"Zero autonomous denials" is an invariant of `finalize_node`, not an empirical
finding: Rule 1 rewrites every DENIED recommendation to PENDING_REVIEW, so the
system cannot emit an autonomous denial by construction. Prove it with a unit
test and state it as a design property.

The measurable safety number is different: on the 15 DENIED and 15 MORE_INFO
cases, how often does the system auto-approve instead of escalating? That is a
real result, and `eval_autoauth.py` computes it as
`false_approvals_on_deny_cases`.
