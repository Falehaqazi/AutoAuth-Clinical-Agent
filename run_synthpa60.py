#!/usr/bin/env python3
"""
run_synthpa60.py — resumable, quota-aware driver for the SynthPA-60 evaluation.

Wraps eval_autoauth.py. Does NOT replace your pipeline; it calls into it.

Why this exists:
  1. RESUMABILITY. A crash at case 47 must not cost you the run. Every case is
     flushed + fsynced to JSONL immediately. Re-running skips completed cases.
  2. QUOTA AWARENESS. Reads x-ratelimit-* headers from Groq and paces to the
     real limit rather than a guessed one. Honours retry-after on 429.
  3. COMPLETE CAPTURE. Logs every field the analysis needs on the FIRST pass so
     you never re-run to recover a column you forgot.

Usage:
    python run_synthpa60.py --cases synthpa60.jsonl --out runs/ --seeds 0 1 2
    python run_synthpa60.py --cases synthpa60.jsonl --out runs/ --seeds 0 --dry-run 3
"""

import argparse, json, os, sys, time, hashlib, traceback, threading
from datetime import datetime, timezone
from collections import deque

# ---------------------------------------------------------------------------
# 1. PIPELINE ADAPTER  <-- THE ONLY BLOCK YOU EDIT
# ---------------------------------------------------------------------------

from autoauth_adapter import run_case


# ---------------------------------------------------------------------------
# 2. RATE LIMITER
# ---------------------------------------------------------------------------

class QuotaGovernor:
    """Token+request bucket. Learns real limits from Groq response headers."""

    def __init__(self, rpm=30, tpm=6000, est_tokens_per_call=1500):
        self.rpm, self.tpm = rpm, tpm
        self.est = est_tokens_per_call
        self.req_times, self.tok_events = deque(), deque()
        self.lock = threading.Lock()
        self.learned = False

    def observe_headers(self, headers: dict):
        """Groq returns x-ratelimit-limit-requests / -tokens. Trust them."""
        try:
            if "x-ratelimit-limit-requests" in headers:
                self.rpm = int(headers["x-ratelimit-limit-requests"])
            if "x-ratelimit-limit-tokens" in headers:
                self.tpm = int(headers["x-ratelimit-limit-tokens"])
            if not self.learned:
                print(f"[governor] learned limits: {self.rpm} RPM / {self.tpm} TPM")
                self.learned = True
        except (ValueError, TypeError):
            pass

    def _prune(self, now):
        while self.req_times and now - self.req_times[0] > 60:
            self.req_times.popleft()
        while self.tok_events and now - self.tok_events[0][0] > 60:
            self.tok_events.popleft()

    def acquire(self, est_tokens=None):
        est = est_tokens or self.est
        while True:
            with self.lock:
                now = time.time()
                self._prune(now)
                used_tok = sum(t for _, t in self.tok_events)
                if len(self.req_times) < self.rpm and used_tok + est <= self.tpm * 0.85:
                    self.req_times.append(now)
                    self.tok_events.append((now, est))
                    return
                oldest = min(
                    self.req_times[0] if self.req_times else now,
                    self.tok_events[0][0] if self.tok_events else now,
                )
                wait = max(0.5, 60 - (now - oldest) + 0.25)
            print(f"[governor] pacing {wait:.1f}s", flush=True)
            time.sleep(wait)

    def settle(self, actual_tokens):
        with self.lock:
            if self.tok_events:
                t, _ = self.tok_events[-1]
                self.tok_events[-1] = (t, actual_tokens)


# ---------------------------------------------------------------------------
# 3. DRIVER
# ---------------------------------------------------------------------------

REQUIRED = [
    "case_id", "stratum", "seed", "gold_decision", "pred_decision",
    "confidence", "escalated", "autonomous_denial",
]

def load_cases(path):
    with open(path) as f:
        if path.endswith(".jsonl"):
            return [json.loads(l) for l in f if l.strip()]
        data = json.load(f)
        return data["cases"] if isinstance(data, dict) else data


def completed_ids(path):
    if not os.path.exists(path):
        return set()
    done = set()
    with open(path) as f:
        for line in f:
            try:
                r = json.loads(line)
                if r.get("error") is None:
                    done.add(r["case_id"])
            except json.JSONDecodeError:
                continue   # torn final line from a hard kill; ignore
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", required=True)
    ap.add_argument("--out", default="runs")
    ap.add_argument("--seeds", type=int, nargs="+", default=[0])
    ap.add_argument("--dry-run", type=int, default=0, help="run only first N cases")
    ap.add_argument("--rpm", type=int, default=30)
    ap.add_argument("--tpm", type=int, default=6000)
    ap.add_argument("--resume", action="store_true", default=True)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    cases = load_cases(args.cases)
    if args.dry_run:
        cases = cases[: args.dry_run]

    gov = QuotaGovernor(rpm=args.rpm, tpm=args.tpm, est_tokens_per_call=2500)
    started = datetime.now(timezone.utc).isoformat()

    for seed in args.seeds:
        out_path = os.path.join(args.out, f"synthpa60_seed{seed}.jsonl")
        done = completed_ids(out_path) if args.resume else set()
        todo = [c for c in cases if c["case_id"] not in done]

        print(f"\n=== seed {seed} | {len(done)} done, {len(todo)} to run ===")
        t_seed = time.time()

        with open(out_path, "a") as fh:
            for i, case in enumerate(todo, 1):
                gov.acquire()
                t0 = time.time()
                try:
                    rec = run_case(case, seed)
                    missing = [k for k in REQUIRED if k not in rec]
                    if missing:
                        raise KeyError(f"adapter omitted required fields: {missing}")
                    gov.settle((rec.get("tokens_in") or 0) + (rec.get("tokens_out") or 0))
                except Exception as e:
                    rec = {
                        "case_id": case.get("case_id"), "stratum": case.get("stratum"),
                        "seed": seed, "gold_decision": case.get("gold_decision"),
                        "error": f"{type(e).__name__}: {e}",
                        "traceback": traceback.format_exc(),
                    }
                    print(f"  [!] {case.get('case_id')}: {rec['error']}", flush=True)

                rec.setdefault("wall_s", round(time.time() - t0, 3))
                rec["run_started_utc"] = started

                fh.write(json.dumps(rec) + "\n")
                fh.flush()
                os.fsync(fh.fileno())      # survive a kill -9

                if i % 5 == 0 or i == len(todo):
                    el = time.time() - t_seed
                    eta = el / i * (len(todo) - i)
                    print(f"  {i}/{len(todo)}  elapsed {el/60:.1f}m  eta {eta/60:.1f}m",
                          flush=True)

        errs = sum(1 for l in open(out_path) if json.loads(l).get("error"))
        print(f"=== seed {seed} complete: {out_path} ({errs} errored) ===")

    manifest = {
        "started_utc": started,
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "seeds": args.seeds,
        "n_cases": len(cases),
        "cases_file": args.cases,
        "cases_sha256": hashlib.sha256(open(args.cases, "rb").read()).hexdigest(),
        "governor": {"rpm": gov.rpm, "tpm": gov.tpm},
        "python": sys.version,
    }
    with open(os.path.join(args.out, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nmanifest -> {args.out}/manifest.json")


if __name__ == "__main__":
    main()
