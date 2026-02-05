import requests
import pandas as pd

API_URL = "http://localhost:8000/analyze"

# Ground Truth: What the AI SHOULD decide
TEST_CASES = [
    {
        "name": "Valid Case (Jane)",
        "payload": {
            "fhir_bundle": {"clinicalNote": "12 weeks pain, 8 weeks PT"},
            "policy": "Pain > 6w, PT > 4w"
        },
        "expected": "APPROVED"
    },
    {
        "name": "Invalid Case (John)",
        "payload": {
            "fhir_bundle": {"clinicalNote": "2 weeks pain, no PT"},
            "policy": "Pain > 6w, PT > 4w"
        },
        "expected": "DENIED"
    }
]

def run_test():
    results = []
    for case in TEST_CASES:
        res = requests.post(API_URL, json=case["payload"]).json()
        results.append({
            "Case": case["name"],
            "Expected": case["expected"],
            "Actual": res["decision"],
            "Pass": "✅" if res["decision"] == case["expected"] else "❌"
        })
    print(pd.DataFrame(results))

if __name__ == "__main__":
    run_test()