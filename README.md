# 🏥 AutoAuth: FHIR-Integrated Clinical Decision Support
**An AI-driven Prior Authorization engine designed for healthcare interoperability.**

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)
![FHIR](https://img.shields.io/badge/Standard-HL7%20FHIR-green)
![LLM](https://img.shields.io/badge/Model-Llama--3.3--70B-orange)

## 🚀 Overview
AutoAuth is a "Human-in-the-loop" AI agent that automates the medical prior authorization process. It ingests structured **HL7 FHIR** data, evaluates it against clinical insurance policies, and provides a transparent decision with a confidence score.



## ✨ Key Features
* **🩺 FHIR Integration:** Specifically designed to parse FHIR-like resource structures (Patient, Condition, ServiceRequest) for seamless EHR integration.
* **🧠 Neuro-Symbolic Reasoning:** Combines LLM intelligence with hardcoded clinical policy logic to ensure decisions follow strict medical guidelines.
* **📊 Clinician Dashboard:** A Streamlit-based UI that allows medical reviewers to audit AI decisions in real-time.
* **🧪 Performance Evaluation:** A built-in validation suite that measures accuracy, precision, and recall against synthetic clinical benchmarks.

## 🏁 How to Run the UI
To run the dashboard locally for evaluation:

1. **Install Dependencies:**
   ```bash
   pip install streamlit pandas python-dotenv openai pydantic

## 🔗 Live Demo
Check out the live dashboard here: [AutoAuth Live App](https://falehaqazi-autoauth-clinical-agent-app-tx3rkx.streamlit.app/)