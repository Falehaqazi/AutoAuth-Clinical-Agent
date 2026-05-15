# backend/tools.py
# Tool functions the agent can CALL during reasoning.
# These are what make this "tool-calling" — the LLM decides when to invoke them.

from langchain_core.tools import tool

# Hardcoded reference data — in production this would be a database lookup.
CPT_CODES = {
    "72148": "MRI Lumbar Spine without contrast",
    "72141": "MRI Cervical Spine without contrast",
    "70553": "MRI Brain with and without contrast",
    "99213": "Office visit, established patient, low complexity",
    "99214": "Office visit, established patient, moderate complexity",
    "27447": "Total knee arthroplasty",
    "29827": "Arthroscopy, shoulder, surgical",
    "93000": "Electrocardiogram, routine",
}

ICD10_CODES = {
    "M54.5": "Low back pain",
    "M54.4": "Lumbago with sciatica",
    "G43.909": "Migraine, unspecified, not intractable",
    "M17.11": "Primary osteoarthritis, right knee",
    "M75.100": "Unspecified rotator cuff tear",
    "I10": "Essential hypertension",
    "E11.9": "Type 2 diabetes mellitus without complications",
    "J18.9": "Pneumonia, unspecified organism",
}

@tool
def lookup_cpt_code(code: str) -> str:
    """Look up the clinical description for a CPT procedure code.
    Use this when you need to verify what procedure is being requested."""
    code = code.strip()
    if code in CPT_CODES:
        return f"CPT {code}: {CPT_CODES[code]}"
    return f"CPT {code}: Code not found in reference database. Verify manually."

@tool
def lookup_icd10_code(code: str) -> str:
    """Look up the clinical description for an ICD-10 diagnosis code.
    Use this when you need to verify the patient's diagnosis."""
    code = code.strip()
    if code in ICD10_CODES:
        return f"ICD-10 {code}: {ICD10_CODES[code]}"
    return f"ICD-10 {code}: Code not found in reference database. Verify manually."