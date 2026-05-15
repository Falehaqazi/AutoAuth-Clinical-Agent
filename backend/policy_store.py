# backend/policy_store.py
# FAISS-backed retrieval over policy documents.
# This is what makes the "RAG" claim real — instead of stuffing the whole
# policy in the prompt, we embed it, store it, and retrieve only relevant chunks.

import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Sample payer policies. In production these would come from PDF ingestion.
SAMPLE_POLICIES = [
    """LUMBAR MRI POLICY (CPT 72148): 
    Prior authorization required. Approve if ALL of the following are met:
    1. Documented low back pain for at least 6 weeks
    2. Failed conservative therapy including physical therapy of at least 4 weeks duration
    3. Neurological deficit OR red flag symptoms present
    Deny if: pain duration under 6 weeks without red flags, or no documented PT trial.""",

    """KNEE ARTHROPLASTY POLICY (CPT 27447):
    Prior authorization required. Approve if ALL met:
    1. Confirmed diagnosis of severe osteoarthritis (ICD-10 M17.x) with radiographic evidence
    2. Failed conservative treatment for at least 3 months (NSAIDs, PT, injections)
    3. BMI documented and managed
    Deny if: no radiographic confirmation, or conservative treatment not attempted.""",

    """BRAIN MRI POLICY (CPT 70553):
    Prior authorization required. Approve if ANY of the following:
    1. New-onset headache with neurological deficit
    2. Migraine refractory to standard treatment for 3+ months
    3. Suspected intracranial pathology with supporting clinical findings
    Deny if: routine headache without red flags or failed standard treatment.""",
]

_vectorstore = None

def get_vectorstore():
    """Build the FAISS index once and cache it. This is the RAG retrieval layer."""
    global _vectorstore
    if _vectorstore is not None:
        return _vectorstore
    
    # Split policies into smaller chunks for better retrieval granularity
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = []
    for policy in SAMPLE_POLICIES:
        chunks.extend(splitter.split_text(policy))
    
    # Embed using a small, fast, free local model — no API calls needed
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    _vectorstore = FAISS.from_texts(chunks, embeddings)
    return _vectorstore

def retrieve_relevant_policy(query: str, k: int = 3) -> str:
    """Given a clinical query, return the top-k most relevant policy chunks."""
    vs = get_vectorstore()
    results = vs.similarity_search(query, k=k)
    return "\n\n---\n\n".join([doc.page_content for doc in results])