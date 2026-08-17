# AutoAuth: Confidence-Gated Agentic RAG for Prior Authorization

An AI decision-support system for clinical prior authorization, built so that its
safety behaviour is enforced by the graph structure rather than by prompt wording.
Requests are reviewed against insurance policy text, and every decision carries a
confidence score, a reasoning trace, and an audit record.

**Stack:** Python, LangGraph, FAISS, Sentence-Transformers, Llama 3.1 8B via Groq, FastAPI, Streamlit

**Live demo:** https://falehaqazi-autoauth-clinical-agent-app-tx3rkx.streamlit.app/

## Architecture

A six-node LangGraph state machine:

```
redact -> retrieve -> reason -> tools -> critique -> finalize
                        ^         |
                        +---------+   (ReAct loop)
```

| Node | Responsibility |
|---|---|
| `redact` | Strips identifiers from the request before anything is sent to the model |
| `retrieve` | Top-3 semantic retrieval over policy documents via FAISS |
| `reason` | Drafts a recommendation against the retrieved policy, with tool access |
| `tools` | Structured lookups called from the reasoning step |
| `critique` | Reviews the draft and its reasoning trace |
| `finalize` | Applies the confidence gate and emits the audited decision |

Retrieval uses `all-MiniLM-L6-v2` embeddings. Generation runs
`llama-3.1-8b-instant` through the Groq API. The backend is a FastAPI service;
the operations console for human reviewers is a Streamlit app.

## Safety design

The three mechanisms below are the point of the project.

**1. Redaction before inference.** The `redact` node removes patient identifiers
from the request text before it reaches retrieval or the LLM, so raw identifiers
are never transmitted to a third-party model endpoint.

**2. Confidence gate at 0.80.** The model emits a calibrated confidence with each
draft. Anything below `0.80` is routed to human review rather than returned as a
decision.

**3. No autonomous denial.** The agent cannot issue an adverse recommendation on
its own authority. Denials are always escalated to a human reviewer, on the
principle that the cost of a wrong denial falls entirely on the patient and is
not symmetric with the cost of a wrong approval.

Every decision is written to a persistent audit trail with a UUID, timestamp,
raw reasoning, and confidence score, so any output can be reconstructed after
the fact.

## Repository layout

```
app.py                  Streamlit operations console
backend/
  main.py               FastAPI application and routes
  agent.py              LangGraph state machine and node definitions
  tools.py              Tools available at the reasoning step
  policy_store.py       Policy ingestion, chunking, FAISS index
  evaluate.py           Evaluation harness
  start.sh              Service entrypoint
requirements.txt
```

## Running locally

Requires a Groq API key.

```bash
git clone https://github.com/Falehaqazi/AutoAuth-Clinical-Agent.git
cd AutoAuth-Clinical-Agent
pip install -r requirements.txt
export GROQ_API_KEY=your_key_here
```

Start the backend:

```bash
cd backend
uvicorn main:app --reload
```

Then start the console in a second terminal:

```bash
streamlit run app.py
```

## Evaluation

`backend/evaluate.py` runs cases against the live API and compares the returned
decision to an expected label. The harness currently ships with a small set of
smoke-test cases covering an approval and a denial path.

A larger synthetic benchmark, SynthPA-60, is in preparation alongside a
technical write-up of the method and results.

## Limitations

Stated plainly, because a decision-support system that hides these is worse than
one that does not have them.

- **Redaction is pattern-based.** It matches common identifier formats and is a
  demonstration of where redaction belongs in the pipeline, not a validated
  de-identification pipeline. It has not been evaluated against a standard such
  as HIPAA Safe Harbor.
- **Confidence is self-reported.** The 0.80 threshold gates a value the model
  produces about its own output. It has not yet been calibrated against outcomes.
- **The evaluation set is small.** Current results are indicative, not
  statistically meaningful.
- **Single model, single policy corpus.** Behaviour across other models and
  broader policy sets is untested.
- **Not for clinical use.** Research prototype only.

## Author

Faleha Qazi — [falehaqazi.github.io](https://falehaqazi.github.io) · [LinkedIn](https://linkedin.com/in/falehaqazi)
