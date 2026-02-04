import os
import json
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from openai import OpenAI

# 1. Load Credentials
load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

# --- THE DATASET (3 Distinct Cases) ---
test_cases = [
    {
        "id": "CASE-001 (Clear Denial)",
        "note": """
        Patient: Alice Smith (DOB: 1990). 
        Back pain for 2 weeks. Wants MRI. 
        No conservative therapy tried.
        """,
        "policy": "MRI approved only if pain > 6 weeks AND therapy > 4 weeks."
    },
    {
        "id": "CASE-002 (Clear Approval)",
        "note": """
        Patient: Bob Jones. 
        Chronic back pain for 3 months (12 weeks). 
        Physical therapy completed for 6 weeks with no improvement. 
        Requesting Lumbar MRI.
        """,
        "policy": "MRI approved only if pain > 6 weeks AND therapy > 4 weeks."
    },
    {
        "id": "CASE-003 (Ambiguous / Human Review)",
        "note": """
        Patient: Charlie. 
        Patient reports 'long-term' discomfort. 
        Handwriting illegible regarding therapy duration. 
        Dr. notes 'maybe' need imaging.
        """,
        "policy": "MRI approved only if pain > 6 weeks AND therapy > 4 weeks."
    }
]

# --- HELPER FUNCTIONS ---
def redact_pii(text):
    # Simple redaction for demo
    for name in ["Alice Smith", "Bob Jones", "Charlie"]:
        text = text.replace(name, "[REDACTED]")
    return text

class DecisionSchema(BaseModel):
    decision: str = Field(description="APPROVED, DENIED, or NEEDS_INFO")
    reason: str = Field(description="Brief reason based on policy")
    confidence: float = Field(description="0.0 to 1.0 confidence score")

def analyze_claim(note, policy):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=[
            {"role": "system", "content": "You are an insurance auditor. Return JSON."},
            {"role": "user", "content": f"Policy: {policy}\nNote: {note}"}
        ],
        tools=[{
            "type": "function",
            "function": {
                "name": "submit_decision",
                "parameters": DecisionSchema.model_json_schema()
            }
        }],
        tool_choice={"type": "function", "function": {"name": "submit_decision"}}
    )
    return json.loads(completion.choices[0].message.tool_calls[0].function.arguments)

# --- THE BATCH RUNNER ---
print("🚀 STARTING BATCH PROCESSING AUTOMATION...\n")

for case in test_cases:
    print(f"--- Processing {case['id']} ---")
    
    # 1. Redact
    safe_note = redact_pii(case['note'])
    
    # 2. Analyze
    try:
        result = analyze_claim(safe_note, case['policy'])
        
        # 3. Decision Logic
        status_icon = "❓"
        if result['confidence'] < 0.85:
            status_icon = "⚠️ HUMAN REVIEW"
        elif result['decision'] == "APPROVED":
            status_icon = "✅ APPROVED"
        else:
            status_icon = "❌ DENIED"
            
        print(f"Status: {status_icon}")
        print(f"Reason: {result['reason']}")
        print(f"Confidence: {result['confidence']}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    print("-" * 30)

print("\n🏁 BATCH COMPLETE.")