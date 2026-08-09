#!/usr/bin/env python3
"""
AutoAuth / SynthPA-60 evaluation harness.

Two halves:
  PART 1 (run_case)  -- you wire ~10 lines to your LangGraph entry point.
  PART 2 (metrics)   -- repo-agnostic; computes every number the preprint needs.

Usage:
    # 1. run the agent, write predictions
    python eval_autoauth.py run --config full   --seed 0 --out preds/full_s0.jsonl
    python eval_autoauth.py run --config nogate --seed 0 --out preds/nogate_s0.jsonl

    # 2. score everything
    python eval_autoauth.py score preds/*.jsonl --outdir results/

Outputs results/metrics.json (paste-ready numbers), results/risk_coverage.png,
results/reliability.png, and results/summary.md.

Guards built in against the three errors flagged in the earlier sepsis paper:
  - AUROC is only computed on a real score (confidence), never on hard labels.
  - Each config is scored independently; identical metric rows across configs
    raise a warning instead of silently shipping copy-pasted numbers.
  - No resampling/rebalancing happens anywhere near metric computation.
"""

import argparse
import glob
import json
import os
import random
import sys
import time
from collections import defaultdict

import numpy as np

# --------------------------------------------------------------------------
# PART 1 -- RUNNER.  Wire this to your graph.
# --------------------------------------------------------------------------

CONFIGS = {
    # name        tau   critique  retrieval  description
    "full":      dict(tau=0.80, critique=True,  retrieval=True),
    "nogate":    dict(tau=0.00, critique=True,  retrieval=True),   # gate ablation
    "nocritique":dict(tau=0.80, critique=False, retrieval=True),   # critique ablation
    "norag":     dict(tau=0.80, critique=True,  retrieval=False),  # RAG ablation
    "zeroshot":  dict(tau=0.00, critique=False, retrieval=False),  # bare LLM baseline
}


def load_benchmark(path="synthpa60/cases.jsonl"):
    """Each line: {case_id, request_text, gold_decision, gold_policy_id, ...}"""
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def run_case(case, cfg, seed):
    """
    >>> WIRE THIS <<<
    Invoke your six-node graph once and return a flat record.

    Something like:

        from autoauth.graph import build_graph
        graph = build_graph(tau=cfg["tau"],
                            use_critique=cfg["critique"],
                            use_retrieval=cfg["retrieval"],
                            temperature=0.0, seed=seed)
        state = graph.invoke({"request_text": case["request_text"]})

    Then map state -> the fields below.  `deferred` must be True whenever the
    gate fired OR the no-autonomous-denial rule routed to a human.
    """
    raise NotImplementedError("wire run_case to your graph")

    # return {
    #     "case_id": case["case_id"],
    #     "seed": seed,
    #     "config": cfg["_name"],
    #     "gold": case["gold_decision"],           # approve | deny | more_info
    #     "pred": state["decision"],
    #     "confidence": float(state["confidence"]),
    #     "deferred": bool(state["routed_to_human"]),
    #     "gold_policy_id": case["gold_policy_id"],
    #     "retrieved_policy_ids": state["retrieved_ids"],   # ranked, len>=5
    #     "latency_s": state["latency_s"],
    #     "n_llm_calls": state["n_llm_calls"],
    #     "rationale": state["rationale"],          # keep for qualitative appendix
    # }


def cmd_run(args):
    cases = load_benchmark(args.bench)
    cfg = dict(CONFIGS[args.config], _name=args.config)
    random.seed(args.seed)
    np.random.seed(args.seed)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    done = set()
    if os.path.exists(args.out):  # resume after a rate-limit crash
        with open(args.out) as f:
            done = {json.loads(l)["case_id"] for l in f if l.strip()}
        print(f"resuming, {len(done)} cases already done")

    with open(args.out, "a") as f:
        for i, case in enumerate(cases):
            if case["case_id"] in done:
                continue
            for attempt in range(5):
                try:
                    rec = run_case(case, cfg, args.seed)
                    break
                except NotImplementedError:
                    raise
                except Exception as e:  # Groq 429s etc.
                    wait = 2 ** attempt * 5
                    print(f"  {case['case_id']} failed ({e}); retry in {wait}s")
                    time.sleep(wait)
            else:
                print(f"  {case['case_id']} PERMANENTLY FAILED -- logging null")
                rec = {"case_id": case["case_id"], "seed": args.seed,
                       "config": args.config, "gold": case["gold_decision"],
                       "pred": None, "confidence": 0.0, "deferred": True,
                       "gold_policy_id": case["gold_policy_id"],
                       "retrieved_policy_ids": [], "error": True}
            f.write(json.dumps(rec) + "\n")
            f.flush()
            time.sleep(args.sleep)
            print(f"[{i+1}/{len(cases)}] {case['case_id']}")


# --------------------------------------------------------------------------
# PART 2 -- METRICS.  Repo-agnostic.
# --------------------------------------------------------------------------

CLASSES = ["approve", "deny", "more_info"]


def _acc(recs):
    return float(np.mean([r["pred"] == r["gold"] for r in recs])) if recs else float("nan")


def per_class_prf(recs):
    out = {}
    for c in CLASSES:
        tp = sum(1 for r in recs if r["pred"] == c and r["gold"] == c)
        fp = sum(1 for r in recs if r["pred"] == c and r["gold"] != c)
        fn = sum(1 for r in recs if r["pred"] != c and r["gold"] == c)
        p = tp / (tp + fp) if tp + fp else 0.0
        rc = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * p * rc / (p + rc) if p + rc else 0.0
        out[c] = dict(precision=p, recall=rc, f1=f1, support=tp + fn)
    out["macro_f1"] = float(np.mean([out[c]["f1"] for c in CLASSES]))
    return out


def confusion(recs):
    m = {g: {p: 0 for p in CLASSES + [None]} for g in CLASSES}
    for r in recs:
        m[r["gold"]][r["pred"] if r["pred"] in CLASSES else None] += 1
    return m


def gate_metrics(recs, tau):
    """Selective-prediction view. `deferred` is whatever the system actually did."""
    auto = [r for r in recs if not r["deferred"]]
    n = len(recs)
    return dict(
        coverage=len(auto) / n if n else float("nan"),
        deferral_rate=1 - len(auto) / n if n else float("nan"),
        selective_accuracy=_acc(auto),
        selective_risk=1 - _acc(auto) if auto else float("nan"),
        forced_accuracy=_acc(recs),          # accuracy if the gate were removed
        n_auto=len(auto),
        n_deferred=n - len(auto),
        tau=tau,
    )


def safety_metrics(recs):
    """The paper's central safety claim. Both must be 0."""
    auto_denials = [r["case_id"] for r in recs
                    if r["pred"] == "deny" and not r["deferred"]]
    missed_denials = [r["case_id"] for r in recs
                      if r["gold"] == "deny" and not r["deferred"]
                      and r["pred"] != "deny"]
    return dict(
        autonomous_denials=len(auto_denials),
        autonomous_denial_ids=auto_denials,
        deny_cases_auto_decided=len([r for r in recs
                                     if r["gold"] == "deny" and not r["deferred"]]),
        false_approvals_on_deny_cases=len(missed_denials),
        false_approval_ids=missed_denials,
    )


def risk_coverage(recs, n_points=50):
    """Sweep tau. This is the figure for a paper called 'Confidence-Gated'."""
    rs = sorted(recs, key=lambda r: -r["confidence"])
    cov, risk, taus = [], [], []
    for k in range(1, len(rs) + 1):
        head = rs[:k]
        cov.append(k / len(rs))
        risk.append(1 - _acc(head))
        taus.append(head[-1]["confidence"])
    aurc = float(np.trapezoid(risk, cov)) if len(cov) > 1 else float("nan")
    return dict(coverage=cov, risk=risk, tau=taus, aurc=aurc)


def calibration(recs, n_bins=10):
    """ECE + Brier + AUROC of confidence as an error detector.

    NOTE: AUROC here is confidence (a continuous score) predicting correctness
    (binary). It is *not* roc_auc_score on hard decision labels.
    """
    conf = np.array([r["confidence"] for r in recs], float)
    correct = np.array([r["pred"] == r["gold"] for r in recs], float)

    edges = np.linspace(0, 1, n_bins + 1)
    ece, bins = 0.0, []
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (conf > lo) & (conf <= hi) if lo > 0 else (conf >= lo) & (conf <= hi)
        if m.sum() == 0:
            bins.append(dict(lo=lo, hi=hi, n=0, acc=None, conf=None))
            continue
        acc_b, conf_b = correct[m].mean(), conf[m].mean()
        ece += m.sum() / len(conf) * abs(acc_b - conf_b)
        bins.append(dict(lo=float(lo), hi=float(hi), n=int(m.sum()),
                         acc=float(acc_b), conf=float(conf_b)))

    pos, neg = conf[correct == 1], conf[correct == 0]
    if len(pos) and len(neg):
        auroc = float(np.mean([(a > b) + 0.5 * (a == b)
                               for a in pos for b in neg]))
    else:
        auroc = float("nan")

    return dict(ece=float(ece), brier=float(np.mean((conf - correct) ** 2)),
                auroc_error_detection=auroc, bins=bins,
                mean_confidence=float(conf.mean()), accuracy=float(correct.mean()))


def retrieval_metrics(recs, ks=(1, 3, 5)):
    valid = [r for r in recs if r.get("gold_policy_id") and r.get("retrieved_policy_ids")]
    if not valid:
        return {}
    out = {}
    for k in ks:
        out[f"recall@{k}"] = float(np.mean(
            [r["gold_policy_id"] in r["retrieved_policy_ids"][:k] for r in valid]))
    mrr = []
    for r in valid:
        ids = r["retrieved_policy_ids"]
        mrr.append(1 / (ids.index(r["gold_policy_id"]) + 1)
                   if r["gold_policy_id"] in ids else 0.0)
    out["mrr"] = float(np.mean(mrr))
    out["n_scored"] = len(valid)
    return out


def bootstrap_ci(recs, fn, n_boot=2000, alpha=0.05, rng=None):
    """Cluster bootstrap over case_id (seeds of the same case resample together)."""
    rng = rng or np.random.default_rng(0)
    by_case = defaultdict(list)
    for r in recs:
        by_case[r["case_id"]].append(r)
    ids = list(by_case)
    vals = []
    for _ in range(n_boot):
        pick = rng.choice(len(ids), len(ids), replace=True)
        samp = [r for i in pick for r in by_case[ids[i]]]
        v = fn(samp)
        if v == v:
            vals.append(v)
    if not vals:
        return dict(point=fn(recs), lo=float("nan"), hi=float("nan"))
    return dict(point=float(fn(recs)),
                lo=float(np.percentile(vals, 100 * alpha / 2)),
                hi=float(np.percentile(vals, 100 * (1 - alpha / 2))))


def paired_delta(a_recs, b_recs, fn, n_boot=2000, rng=None):
    """Paired bootstrap for 'is full better than ablation'. Reports delta CI."""
    rng = rng or np.random.default_rng(1)
    a_by, b_by = defaultdict(list), defaultdict(list)
    for r in a_recs:
        a_by[r["case_id"]].append(r)
    for r in b_recs:
        b_by[r["case_id"]].append(r)
    ids = sorted(set(a_by) & set(b_by))
    deltas = []
    for _ in range(n_boot):
        pick = rng.choice(len(ids), len(ids), replace=True)
        av = fn([r for i in pick for r in a_by[ids[i]]])
        bv = fn([r for i in pick for r in b_by[ids[i]]])
        if av == av and bv == bv:
            deltas.append(av - bv)
    d = fn(a_recs) - fn(b_recs)
    lo, hi = np.percentile(deltas, [2.5, 97.5])
    return dict(delta=float(d), lo=float(lo), hi=float(hi),
                significant=bool(lo > 0 or hi < 0), n_paired=len(ids))


def score_config(recs, tau):
    per_seed = defaultdict(list)
    for r in recs:
        per_seed[r["seed"]].append(r)
    seed_acc = [gate_metrics(v, tau)["selective_accuracy"] for v in per_seed.values()]

    return dict(
        n_records=len(recs), n_cases=len({r["case_id"] for r in recs}),
        n_seeds=len(per_seed),
        gate=gate_metrics(recs, tau),
        safety=safety_metrics(recs),
        calibration=calibration(recs),
        retrieval=retrieval_metrics(recs),
        per_class=per_class_prf(recs),
        confusion=confusion(recs),
        risk_coverage={k: v for k, v in risk_coverage(recs).items()
                       if k == "aurc"},
        _rc_curve=risk_coverage(recs),
        seed_variance=dict(
            mean=float(np.mean(seed_acc)),
            sd=float(np.std(seed_acc, ddof=1)) if len(seed_acc) > 1 else 0.0,
            per_seed=dict(zip(map(str, per_seed), map(float, seed_acc)))),
        ci_selective_accuracy=bootstrap_ci(
            recs, lambda rs: gate_metrics(rs, tau)["selective_accuracy"]),
        ci_forced_accuracy=bootstrap_ci(recs, _acc),
        ci_macro_f1=bootstrap_ci(recs, lambda rs: per_class_prf(rs)["macro_f1"]),
    )


def make_figures(by_config, outdir):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib unavailable; skipping figures")
        return

    fig, ax = plt.subplots(figsize=(5, 3.6))
    for name, m in by_config.items():
        rc = m["_rc_curve"]
        ax.plot(rc["coverage"], rc["risk"], lw=1.6,
                label=f"{name} (AURC={rc['aurc']:.3f})")
    op = by_config.get("full", {}).get("gate")
    if op:
        ax.scatter([op["coverage"]], [op["selective_risk"]], s=45, zorder=5,
                   marker="D", color="k", label=f"operating point tau={op['tau']}")
    ax.set_xlabel("coverage (fraction auto-decided)")
    ax.set_ylabel("selective risk (error rate)")
    ax.legend(fontsize=7, frameon=False)
    ax.grid(alpha=.25, lw=.5)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "risk_coverage.png"), dpi=300)

    fig, ax = plt.subplots(figsize=(3.8, 3.6))
    cal = by_config.get("full", list(by_config.values())[0])["calibration"]
    xs = [b["conf"] for b in cal["bins"] if b["n"]]
    ys = [b["acc"] for b in cal["bins"] if b["n"]]
    ns = [b["n"] for b in cal["bins"] if b["n"]]
    ax.plot([0, 1], [0, 1], "--", color="gray", lw=1)
    ax.scatter(xs, ys, s=[12 + 4 * n for n in ns], alpha=.8)
    ax.set_xlabel("mean confidence")
    ax.set_ylabel("empirical accuracy")
    ax.set_title(f"ECE = {cal['ece']:.3f}", fontsize=9)
    ax.grid(alpha=.25, lw=.5)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "reliability.png"), dpi=300)
    print(f"wrote figures to {outdir}/")


def cmd_score(args):
    recs = []
    for pat in args.preds:
        for path in sorted(glob.glob(pat)):
            with open(path) as f:
                recs += [json.loads(l) for l in f if l.strip()]
    if not recs:
        sys.exit("no records found")

    by_config = {}
    for name in sorted({r["config"] for r in recs}):
        sub = [r for r in recs if r["config"] == name]
        tau = CONFIGS.get(name, {}).get("tau", 0.80)
        by_config[name] = score_config(sub, tau)

    # copy-paste guard
    sigs = {}
    for n, m in by_config.items():
        s = (round(m["gate"]["selective_accuracy"], 6),
             round(m["per_class"]["macro_f1"], 6))
        if s in sigs:
            print(f"!! WARNING: {n} and {sigs[s]} have identical metrics. "
                  f"Check you actually varied the config.", file=sys.stderr)
        sigs[s] = n

    deltas = {}
    if "full" in by_config:
        full = [r for r in recs if r["config"] == "full"]
        for name in by_config:
            if name == "full":
                continue
            tau_f = CONFIGS["full"]["tau"]
            deltas[f"full_vs_{name}"] = paired_delta(
                full, [r for r in recs if r["config"] == name],
                lambda rs: gate_metrics(rs, tau_f)["selective_accuracy"])

    os.makedirs(args.outdir, exist_ok=True)
    out = {"configs": by_config, "ablation_deltas": deltas,
           "total_records": len(recs)}
    clean = {"configs": {k: {kk: vv for kk, vv in v.items() if kk != "_rc_curve"}
                         for k, v in by_config.items()},
             "ablation_deltas": deltas, "total_records": len(recs)}
    with open(os.path.join(args.outdir, "metrics.json"), "w") as f:
        json.dump(clean, f, indent=2)

    make_figures(by_config, args.outdir)
    write_summary(by_config, deltas, args.outdir)
    print(f"\nwrote {args.outdir}/metrics.json  (paste numbers from here, not by hand)")


def write_summary(by_config, deltas, outdir):
    L = ["# AutoAuth on SynthPA-60 -- results", ""]
    L.append("| config | cov | sel-acc [95% CI] | macro-F1 | AURC | ECE | R@3 | auto-denials |")
    L.append("|---|---|---|---|---|---|---|---|")
    for n, m in by_config.items():
        g, c = m["gate"], m["calibration"]
        ci = m["ci_selective_accuracy"]
        r3 = m["retrieval"].get("recall@3")
        L.append(f"| {n} | {g['coverage']:.2f} | {g['selective_accuracy']:.3f} "
                 f"[{ci['lo']:.3f}, {ci['hi']:.3f}] | "
                 f"{m['per_class']['macro_f1']:.3f} | {m['_rc_curve']['aurc']:.3f} | "
                 f"{c['ece']:.3f} | {r3:.3f} | "
                 f"{m['safety']['autonomous_denials']} |" if r3 is not None else
                 f"| {n} | {g['coverage']:.2f} | {g['selective_accuracy']:.3f} "
                 f"[{ci['lo']:.3f}, {ci['hi']:.3f}] | "
                 f"{m['per_class']['macro_f1']:.3f} | {m['_rc_curve']['aurc']:.3f} | "
                 f"{c['ece']:.3f} | n/a | {m['safety']['autonomous_denials']} |")
    L += ["", "## Ablation deltas (paired bootstrap, selective accuracy)", ""]
    for k, d in deltas.items():
        star = "*" if d["significant"] else " (n.s.)"
        L.append(f"- {k}: {d['delta']:+.3f} [{d['lo']:+.3f}, {d['hi']:+.3f}]{star}")
    L += ["", "## Safety", ""]
    for n, m in by_config.items():
        s = m["safety"]
        L.append(f"- {n}: autonomous denials = {s['autonomous_denials']}, "
                 f"deny-cases auto-decided = {s['deny_cases_auto_decided']}")
    L += ["", "## Seed variance (selective accuracy)", ""]
    for n, m in by_config.items():
        v = m["seed_variance"]
        L.append(f"- {n}: {v['mean']:.3f} +/- {v['sd']:.3f} over {m['n_seeds']} seeds")
    with open(os.path.join(outdir, "summary.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run")
    r.add_argument("--config", choices=list(CONFIGS), default="full")
    r.add_argument("--seed", type=int, default=0)
    r.add_argument("--bench", default="synthpa60/cases.jsonl")
    r.add_argument("--out", required=True)
    r.add_argument("--sleep", type=float, default=2.0, help="Groq rate-limit pad")
    r.set_defaults(func=cmd_run)

    s = sub.add_parser("score")
    s.add_argument("preds", nargs="+")
    s.add_argument("--outdir", default="results")
    s.set_defaults(func=cmd_score)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
