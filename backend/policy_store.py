# backend/policy_store.py
# FAISS-backed retrieval over the SynthPA-60 payer policy corpus.

import json, os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

POLICY_PATH = os.getenv("SYNTHPA_POLICIES", "synthpa60/policies.jsonl")


def _render(p: dict) -> str:
    """Flatten one policy record into the prose a reviewer would actually read."""
    L = [f"POLICY {p['policy_id']}: {p['title']} ({p['code_system']} {p['code']})",
         "Prior authorization required."]
    if p.get("required"):
        L.append("ALL of the following are required:")
        L += [f"  {k}. {v}" for k, v in p["required"].items()]
    if p.get("any_of"):
        L.append("AND AT LEAST ONE of the following:")
        L += [f"  {k}. {v}" for k, v in p["any_of"].items()]
    if p.get("exclusions"):
        L.append("Deny or exclude if ANY of the following apply:")
        L += [f"  {k}. {v}" for k, v in p["exclusions"].items()]
    return "\n".join(L)


_vectorstore = None
_policies = None


def load_policies():
    global _policies
    if _policies is None:
        with open(POLICY_PATH) as f:
            _policies = [json.loads(l) for l in f if l.strip()]
    return _policies


def get_vectorstore():
    """Build the FAISS index once and cache it."""
    global _vectorstore
    if _vectorstore is not None:
        return _vectorstore

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    texts, metas = [], []
    for p in load_policies():
        body = _render(p)
        header = f"POLICY {p['policy_id']}: {p['title']} ({p['code_system']} {p['code']})"
        for i, chunk in enumerate(splitter.split_text(body)):
            # Re-attach the header so a mid-policy chunk stays attributable.
            texts.append(chunk if chunk.startswith("POLICY ") else f"{header}\n{chunk}")
            metas.append({"policy_id": p["policy_id"], "code": p["code"],
                          "title": p["title"], "chunk_id": f"{p['policy_id']}_{i}"})

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    _vectorstore = FAISS.from_texts(texts, embeddings, metadatas=metas)
    return _vectorstore


def retrieve_relevant_policy(query: str, k: int = 3) -> str:
    """Top-k policy chunks as a single prompt-ready string."""
    return "\n\n---\n\n".join(d.page_content for d in get_vectorstore().similarity_search(query, k=k))


def retrieve_with_scores(query: str, k: int = 3):
    """Same retrieval, but returns (text, chunk_ids, policy_ids, scores) for the eval harness."""
    hits = get_vectorstore().similarity_search_with_score(query, k=k)
    text = "\n\n---\n\n".join(d.page_content for d, _ in hits)
    return (text,
            [d.metadata["chunk_id"] for d, _ in hits],
            [d.metadata["policy_id"] for d, _ in hits],
            [float(s) for _, s in hits])
