#!/usr/bin/env bash
# Run from the repository root so that "from backend.agent import graph" resolves.
cd "$(dirname "$0")/.."
exec uvicorn backend.main:app --host 0.0.0.0 --port "${PORT:-8000}"
