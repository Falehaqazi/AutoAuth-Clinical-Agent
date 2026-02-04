# 🏥 AutoAuth: FHIR-Integrated Clinical Decision Support
**An AI-driven Prior Authorization engine designed for healthcare interoperability.**

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)
![FHIR](https://img.shields.io/badge/Standard-HL7%20FHIR-green)
![LLM](https://img.shields.io/badge/Model-Llama--3.3--70B-orange)

## 🚀 Overview
AutoAuth is a "Human-in-the-loop" AI agent that automates the medical prior authorization process. It takes structured **HL7 FHIR** data, compares it against complex insurance policies, and provides a transparent approval/denial decision with a confidence score.

This project solves the "Black Box" problem in healthcare AI by providing clear reasoning and a dedicated performance evaluation suite for clinical auditing.

## ✨ Key Features
* **🩺 FHIR Interoperability:** Automatically parses FHIR JSON bundles (Patient, Condition, and ServiceRequest resources).
* **🧠 Neuro-Symbolic Reasoning:** Combines LLM intelligence (Llama-3.3-70B) with hardcoded clinical policy logic.
* **📊 Clinical Dashboard:** A professional Web UI built with Streamlit for clinician review and real-time analysis.
* **🧪 Performance Evaluation:** Built-in validation module to measure AI accuracy, precision, and recall against synthetic clinical datasets.
* **🛡️ Confidence-Based Routing:** Decisions with low confidence (<0.85) are automatically flagged for manual human review.

## 🛠️ Technical Stack
* **Language:** Python 3.13
* **LLM API:** Groq / OpenAI (Llama-3.3-70B-Versatile)
* **Interface:** Streamlit
* **Data Standards:** HL7 FHIR (JSON)
* **Schema Validation:** Pydantic (Structured Outputs)

## 📸 Dashboard Preview
The dashboard consists of two main modules:
1.  **Live Analysis:** Ingests FHIR resources and outputs immediate decisions.
2.  **Batch Evaluation:** Runs the model against a "Gold Standard" dataset to calculate accuracy metrics.

## 🏁 Getting Started

### 1. Prerequisites
* Python 3.13+
* A Groq API Key (stored in a `.env` file)

### 2. Installation
```bash
git clone [https://github.com/Falehaqazi/AutoAuth-Clinical-Agent.git](https://github.com/Falehaqazi/AutoAuth-Clinical-Agent.git)
cd AutoAuth
pip install streamlit pandas python-dotenv openai pydantic