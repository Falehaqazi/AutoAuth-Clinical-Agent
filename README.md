# 🏥 Auto-Auth: Production-Grade Prior-Auth Pipeline

An AI-driven clinical decision support system designed for high-integrity healthcare environments. This system automates the review of FHIR-formatted medical requests against insurance policies with full auditability.



## 🏗️ System Architecture
- **Backend**: FastAPI microservice handling LLM orchestration and logic.
- **Frontend**: Streamlit Operations Console for clinical reviewers.
- **Data Layer**: Persistent JSON-based Audit Trail for HIPAA compliance and traceability.

## 🛡️ Key Engineering Features
1. **Traceability**: Every decision is assigned a unique UUID and logged with a timestamp, raw reasoning, and confidence score.
2. **PII Protection**: Integrated redaction layer to ensure data privacy before LLM transmission.
3. **Safety Thresholds**: Logic-based fallbacks for low-confidence AI outputs.
4. **Interoperability**: Native support for FHIR (Fast Healthcare Interoperability Resources) data structures.

## 🚦 How to Run

### 1. Start the Backend (API)
```bash
cd backend
uvicorn main:app --reload