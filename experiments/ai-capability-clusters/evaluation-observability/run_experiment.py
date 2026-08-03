#!/usr/bin/env python3
"""Deterministic three-axis evaluation experiment using frozen local traces."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LABELS = ("pass", "fail", "unknown")


def load(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def predict(trace: dict, mode: str) -> str:
    if mode == "baseline":
        # Baseline trusts outcome; complete traces are the only intended pass contract,
        # but this deliberately demonstrates false passes when telemetry is absent.
        return "pass" if trace["outcome"] == "success" else "fail"
    # Security failure is a fail even when process/telemetry axes are unknown.
    if trace["security"] == "fail":
        return "fail"
    # Incomplete telemetry cannot establish a pass, even when all observed axes look normal.
    if trace.get("trace_complete") is not True:
        return "unknown"
    if "unknown" in (trace["outcome"], trace["process"], trace["security"]):
        return "unknown"
    if trace["outcome"] == "error" or trace["process"] == "incomplete":
        return "fail"
    return "pass"


def macro_f1(traces: list[dict], predictions: dict[str, str]) -> float:
    scores = []
    for label in LABELS:
        tp = sum(1 for trace in traces if trace["truth"] == label and predictions[trace["id"]] == label)
        fp = sum(1 for trace in traces if trace["truth"] != label and predictions[trace["id"]] == label)
        fn = sum(1 for trace in traces if trace["truth"] == label and predictions[trace["id"]] != label)
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        scores.append((2 * precision * recall / (precision + recall)) if precision + recall else 0.0)
    return round(sum(scores) / len(scores), 9)


def execute(fixtures: dict, mode: str) -> dict:
    traces = fixtures["traces"]
    predictions = {trace["id"]: predict(trace, mode) for trace in traces}
    false_pass = sum(1 for trace in traces if trace["truth"] != "pass" and predictions[trace["id"]] == "pass")
    unknown_total = sum(1 for trace in traces if trace["truth"] == "unknown")
    unknown_correct = sum(1 for trace in traces if trace["truth"] == "unknown" and predictions[trace["id"]] == "unknown")
    security_masking = sum(1 for trace in traces if trace["security"] == "fail" and predictions[trace["id"]] != "fail")
    return {
        "experiment_id": fixtures["experiment_id"],
        "mode": mode,
        "predictions": predictions,
        "axes": {trace["id"]: {"outcome": trace["outcome"], "process": trace["process"], "security": trace["security"], "trace_complete": trace.get("trace_complete")} for trace in traces},
        "metrics": {
            "macro_f1": macro_f1(traces, predictions),
            "false_pass": false_pass,
            "unknown_recall": round(unknown_correct / unknown_total, 9) if unknown_total else 0.0,
            "security_masking": security_masking,
        },
    }


def expected_axes(fixtures: dict) -> dict[str, dict]:
    """Construct the full, immutable axis contract from the frozen fixtures."""
    return {
        trace["id"]: {
            "outcome": trace["outcome"],
            "process": trace["process"],
            "security": trace["security"],
            "trace_complete": trace.get("trace_complete"),
        }
        for trace in fixtures["traces"]
    }


def metrics_from_fixtures(fixtures: dict, predictions: dict[str, str]) -> dict:
    """Recompute every reported metric from frozen truth, never result.axes."""
    traces = fixtures["traces"]
    false_pass = sum(1 for trace in traces if trace["truth"] != "pass" and predictions[trace["id"]] == "pass")
    unknown_total = sum(1 for trace in traces if trace["truth"] == "unknown")
    unknown_correct = sum(1 for trace in traces if trace["truth"] == "unknown" and predictions[trace["id"]] == "unknown")
    security_masking = sum(1 for trace in traces if trace["security"] == "fail" and predictions[trace["id"]] != "fail")
    return {
        "macro_f1": macro_f1(traces, predictions),
        "false_pass": false_pass,
        "unknown_recall": round(unknown_correct / unknown_total, 9) if unknown_total else 0.0,
        "security_masking": security_masking,
    }


def validate(result: dict, fixtures: dict, oracle: dict) -> list[str]:
    if result.get("mode") not in oracle["expected"]:
        return [f"unknown mode {result.get('mode')!r}"]
    expected = oracle["expected"][result["mode"]]
    errors = []
    if result.get("experiment_id") != fixtures["experiment_id"] or result.get("experiment_id") != oracle["experiment_id"]:
        errors.append("experiment_id differs from frozen contract")
    axes = expected_axes(fixtures)
    if set(result.get("axes", {})) != set(axes):
        errors.append("axis IDs differ from frozen fixtures")
    for trace_id, expected_axis in axes.items():
        if result.get("axes", {}).get(trace_id) != expected_axis:
            errors.append(f"{trace_id}: axes differ from frozen fixtures")
    if set(result.get("predictions", {})) != set(axes):
        errors.append("prediction IDs differ from frozen fixtures")
    if result.get("predictions") != expected["predictions"]:
        errors.append("predictions differ from independent oracle")
    if set(result.get("predictions", {})) == set(axes):
        recomputed = metrics_from_fixtures(fixtures, result["predictions"])
        if result.get("metrics") != recomputed:
            errors.append(f"metrics {result.get('metrics')!r} != recomputed {recomputed!r}")
        if recomputed != expected["metrics"]:
            errors.append(f"recomputed metrics {recomputed!r} != oracle {expected['metrics']!r}")
    if result["mode"] == "treatment":
        for trace_id, axis in axes.items():
            if axis["trace_complete"] is not True and axis["security"] != "fail" and result["predictions"].get(trace_id) != "unknown":
                errors.append(f"{trace_id}: incomplete telemetry must predict unknown")
        if result["predictions"].get("security-process-unknown") != "fail":
            errors.append("security failure must override incomplete telemetry")
    return errors


def negative_checks(fixtures: dict, oracle: dict) -> int:
    """Assert all axis fields and completeness fail closed when tampered."""
    result = execute(fixtures, "treatment")
    cases = 0
    incomplete = dict(result)
    incomplete["predictions"] = dict(result["predictions"])
    incomplete["predictions"]["trace-incomplete-normal"] = "pass"
    cases += int(bool(validate(incomplete, fixtures, oracle)))
    security = dict(result)
    security["predictions"] = dict(result["predictions"])
    security["predictions"]["security-process-unknown"] = "unknown"
    cases += int(bool(validate(security, fixtures, oracle)))
    for trace_id, axis in expected_axes(fixtures).items():
        for field, replacement in (("outcome", "tampered"), ("process", "tampered"), ("security", "tampered"), ("trace_complete", not axis["trace_complete"])):
            tampered = copy.deepcopy(result)
            tampered["axes"][trace_id][field] = replacement
            cases += int(bool(validate(tampered, fixtures, oracle)))
    return cases


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("baseline", "treatment", "all"), default="all")
    args = parser.parse_args()
    try:
        fixtures, oracle = load("fixtures.json"), load("oracle.json")
        modes = ("baseline", "treatment") if args.mode == "all" else (args.mode,)
        for mode in modes:
            result = execute(fixtures, mode)
            errors = validate(result, fixtures, oracle)
            if errors:
                raise ValueError(f"{mode}: " + "; ".join(errors))
            (ROOT / "runs" / f"{mode}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        expected_negative_checks = oracle["negative_check_count"]
        if args.mode in ("all", "treatment") and negative_checks(fixtures, oracle) != expected_negative_checks:
            raise ValueError("negative completeness checks did not fail closed")
        return 0
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"experiment failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
