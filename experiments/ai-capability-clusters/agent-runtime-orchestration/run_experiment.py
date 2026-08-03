#!/usr/bin/env python3
"""Deterministic local simulation of interrupt/retry runtime semantics."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def simulate(case, treatment):
    events = ["guardrail_checked"]
    effects = []
    turns = 1
    if treatment and case["guardrail"] == "block":
        events.append("gate_blocked")
        return events, effects, "blocked", turns
    if not treatment and case["guardrail"] == "block":
        events.append("effect_applied")  # intentional guardrail leak in baseline
        effects.append(f"{case['effect']}:{case['idempotency_key']}:turn{turns}")
        return events, effects, "completed", turns

    events.append("effect_applied")
    effects.append(f"{case['effect']}:{case['idempotency_key']}")
    events.append("checkpoint_saved")
    if case["interrupt_after_effect"]:
        events.append("interrupt")
        if turns >= case["max_turns"]:
            events.append("turn_budget_exhausted")
            return events, effects, "blocked", turns
        turns += 1
        if treatment:
            events.append("effect_deduped")
        else:
            effects.append(f"{case['effect']}:{case['idempotency_key']}:retry")
            events.append("effect_applied")
        events.append("recovered")
    return events, effects, "recovered" if case["interrupt_after_effect"] else "completed", turns


def run(mode):
    fixtures, oracle = load("fixtures.json"), load("oracle.json")
    treatment = mode == "treatment"
    rows = {}
    duplicate_count = guardrail_leaks = budget_violations = 0
    max_turns = 0
    for case in fixtures["cases"]:
        events, effects, state, turns = simulate(case, treatment)
        rows[case["id"]] = {"events": events, "side_effects": effects, "final_state": state, "turns": turns}
        duplicate_count += max(0, len(effects) - len({e.split(":retry")[0] for e in effects}))
        if case["guardrail"] == "block" and effects:
            guardrail_leaks += 1
        if turns > case["max_turns"]:
            budget_violations += 1
        max_turns = max(max_turns, turns)
    expected = oracle["treatment"]
    recovery_ids = expected["recovery_cases"]
    final_state_matches = sum(
        rows[case_id]["final_state"] == expected["final_states"][case_id]
        for case_id in expected["final_states"]
    )
    metrics = {
        "recovery_state": sum(rows[case_id]["final_state"] == "recovered" for case_id in recovery_ids),
        "recovery_cases": len(recovery_ids),
        "final_state_accuracy": final_state_matches / len(expected["final_states"]),
        "duplicate_side_effects": duplicate_count,
        "guardrail_leaks": guardrail_leaks,
        "budget_violations": budget_violations,
        "max_turns": max_turns,
    }
    passed = True
    fixture_ids = {case["id"] for case in fixtures["cases"]}
    passed &= fixture_ids == set(expected["event_traces"]) == set(expected["side_effects"]) == set(expected["final_states"])
    for case_id, exp_events in expected["event_traces"].items():
        row = rows[case_id]
        # This is an ordered trace contract: set comparison would accept
        # duplicate, reversed, or checkpoint/interrupt/recovery-swapped events.
        passed &= row["events"] == exp_events
        passed &= row["side_effects"] == expected["side_effects"][case_id]
        passed &= row["final_state"] == expected["final_states"][case_id]
    passed &= metrics["duplicate_side_effects"] == 0 and metrics["guardrail_leaks"] == 0
    passed &= metrics["budget_violations"] == 0
    passed &= metrics["final_state_accuracy"] == 1.0
    return {"mode": mode, "metrics": metrics, "cases": rows, "passed_oracle": bool(passed)}


def main():
    outputs = {m: run(m) for m in ("baseline", "treatment")}
    for mode, value in outputs.items():
        (ROOT / "runs" / f"{mode}.json").write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(outputs, sort_keys=True, indent=2))
    raise SystemExit(0 if outputs["treatment"]["passed_oracle"] else 1)


if __name__ == "__main__":
    main()
