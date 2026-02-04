# Auto-Auth: Clinical Decision Support Agent 🏥

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI Model](https://img.shields.io/badge/Model-Llama3_70b-orange)
![Compliance](https://img.shields.io/badge/HIPAA-Compliant-green)

## ⚡ Overview
**Auto-Auth** is a Neuro-Symbolic AI agent designed to automate the insurance prior authorization process. Unlike standard "chatbots," this system uses a deterministic pipeline to validate unstructured clinical notes against structured policy guidelines, ensuring both efficiency and patient safety.

This project was engineered to solve the "Black Box" problem in Health AI by implementing **Confidence-Based Routing**—automatically escalating low-certainty claims to human reviewers.

## 🔑 Key Features
* **🛡️ Privacy First:** Implements local PII (Personally Identifiable Information) redaction *before* data leaves the secure environment.
* **🧠 Neuro-Symbolic Logic:** Combines LLM reasoning with strict policy rules (e.g., "Must have 6 weeks of conservative therapy").
* **⚠️ Human-in-the-Loop:** Automatically flags ambiguous cases (confidence < 85%) for manual review, preventing AI hallucinations from denying care.
* **🚀 Batch Processing:** Capable of processing multiple patient claims in a single stream.

## 🛠️ Architecture
1.  **Input:** Clinical Note (Unstructured) + Insurance Policy (Structured).
2.  **Sanitization:** Python-based PII redaction layer.
3.  **Inference:** Llama-3-70b (via Groq) extracts clinical entities and validates against policy criteria.
4.  **Decision Engine:** JSON-structured output with `APPROVED`, `DENIED`, or `HUMAN_REVIEW` status.

## 💻 Tech Stack
* **Language:** Python
* **Model:** Llama-3.3-70b-Versatile (via Groq API)
* **Libraries:** `pydantic` (Data Validation), `python-dotenv` (Security), `openai` (Client SDK)

## 🚀 How to Run
```bash
# 1. Clone the repo
git clone [https://github.com/Falehaqazi/AutoAuth-Clinical-Agent.git](https://github.com/Falehaqazi/AutoAuth-Clinical-Agent.git)

# 2. Install dependencies
pip install openai pydantic python-dotenv

# 3. Set up API Key
# Create a .env file and add: OPENAI_API_KEY=gsk_...

# 4. Run the agent
python main.py