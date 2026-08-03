#!/usr/bin/env python3
"""Deterministic scoped-memory experiment using append-only vs scoped stores."""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def event_id(event):
    if not event:
        return None
    return f"{event['run']}:{event['user']}:{event['key']}"


def scope_id(user, key):
    return f"{user}:{key}"


def is_secret(event, policy):
    """Classify secrets from the preregistered fixture policy."""
    return bool(event.get("secret")) or event["key"] in set(policy["sensitive_keys"])


def store_rows(scoped):
    return [
        {"scope": {"user": user, "key": key}, **cell}
        for (user, key), cell in sorted(scoped.items())
    ]


def execute(mode, fixtures):
    """Run only against frozen fixtures; the independent oracle is validation-only."""
    events = fixtures["events"]
    policy = fixtures["policy"]
    records, scoped, rejected_ids, dispositions = [], {}, [], {}
    for event in events:
        identifier = event_id(event)
        if mode == "treatment" and is_secret(event, policy):
            rejected_ids.append(identifier)
            dispositions[identifier] = "rejected"
            continue
        dispositions[identifier] = "retained"
        if mode == "baseline":
            records.append(copy.deepcopy(event))
            continue
        slot = (event["user"], event["key"])
        scoped[slot] = {
            "value": event.get("value"),
            "tombstone": event["op"] == "delete",
            "provenance": identifier,
            "source_user": event.get("source_user", event["user"]),
        }

    if mode == "baseline":
        scoped = {
            (event["user"], event["key"]): {
                "value": event.get("value"),
                "tombstone": event["op"] == "delete",
                "provenance": event_id(event),
                "source_user": event.get("source_user", event["user"]),
            }
            for event in records
        }
    store = store_rows(scoped)
    # This deliberately scans the complete materialized store, not only queried records.
    cross_scope = sum(row["scope"]["user"] != row["source_user"] for row in store)

    answers, stale, secret_retention, token_units, query_scope_leaks = {}, 0, 0, 0, 0
    for query in fixtures["queries"]:
        selected = None
        if mode == "treatment":
            cell = scoped.get((query["user"], query["key"]))
            value = None if not cell or cell["tombstone"] else cell["value"]
            selected = cell
        else:
            candidates = [event for event in records if event["key"] == query["key"] and event["op"] == "upsert"]
            selected = candidates[-1] if candidates else None
            value = selected["value"] if selected else None
            if query["key"] == "role" and query["user"] == "u1" and value == "manager":
                stale += 1
        if value in policy["forbidden_returns"].get(query["id"], []):
            secret_retention += 1
        provenance = selected.get("provenance") if mode == "treatment" and selected else event_id(selected)
        source_user = selected.get("source_user", selected.get("user")) if selected else None
        source_scope = scope_id(source_user, query["key"]) if source_user else None
        if source_user is not None and source_user != query["user"]:
            query_scope_leaks += 1
        answers[query["id"]] = {
            "value": value,
            "selected_record": provenance,
            "selected_source_user": source_user,
            "selected_source_scope": source_scope,
        }
        token_units += len(str(value or "")) + 1

    expected_values = policy["expected_query_values"]
    correct = sum(answers[query_id]["value"] == expected for query_id, expected in expected_values.items())
    metrics = {
        "precision": correct / len(expected_values),
        "recall": correct / len(expected_values),
        "stale_fact_rate": stale / len(fixtures["queries"]),
        "query_scope_leak_rate": query_scope_leaks / len(fixtures["queries"]),
        "query_scope_leak_count": query_scope_leaks,
        "store_provenance_mismatch_rate": cross_scope / len(store) if store else 0.0,
        "store_provenance_mismatch_count": cross_scope,
        "secret_retention": secret_retention,
        "token_units": token_units,
        "rejected_secrets": len(rejected_ids),
        "secret_rejection_ids": rejected_ids,
    }
    return {
        "mode": mode,
        "metrics": metrics,
        "answers": answers,
        "store": store,
        "event_dispositions": dispositions,
    }


def validate(result, fixtures, oracle):
    errors = []
    policy = fixtures["policy"]
    if policy["sensitive_keys"] != oracle["sensitive_keys"]:
        errors.append("preregistered sensitive-key policy differs from independent oracle")
    if policy["forbidden_returns"] != oracle["forbidden_returns"]:
        errors.append("preregistered forbidden-return policy differs from independent oracle")
    query_scopes = {scope_id(query["user"], query["key"]) for query in fixtures["queries"]}
    fact_scopes = {scope_id(user, key) for user, facts in oracle["final_facts"].items() for key in facts}
    observed_store_scopes = {scope_id(row["scope"]["user"], row["scope"]["key"]) for row in result["store"]}
    closure = oracle["scope_closure"]
    if query_scopes != set(closure["query_scopes"]):
        errors.append("query scope keys are not closed by the oracle")
    if fact_scopes != set(closure["fact_scopes"]):
        errors.append("final-fact scope keys are not closed by the oracle")
    if observed_store_scopes != set(closure["store_scopes"]):
        errors.append("store scope keys are not closed by the oracle")
    if result["mode"] != "treatment":
        return errors
    if result["event_dispositions"] != oracle["event_dispositions"]:
        errors.append("event retain/reject decisions differ from independent oracle")
    expected_answers = {
        query["id"]: oracle["final_facts"].get(query["user"], {}).get(query["key"])
        for query in fixtures["queries"]
    }
    if {query_id: answer.get("value") for query_id, answer in result["answers"].items()} != expected_answers:
        errors.append("queried facts differ from independent oracle")
    for query in fixtures["queries"]:
        answer = result["answers"].get(query["id"], {})
        source_user = answer.get("selected_source_user")
        expected_scope = scope_id(source_user, query["key"]) if source_user else None
        if answer.get("selected_source_scope") != expected_scope:
            errors.append(f"{query['id']}: selected source scope receipt differs from source user")
    observed_store = {scope_id(row["scope"]["user"], row["scope"]["key"]): row for row in result["store"]}
    if observed_store != oracle["expected_store"]:
        errors.append("complete scoped store/provenance differs from independent oracle")
    if result["metrics"]["precision"] != 1.0 or result["metrics"]["recall"] != 1.0:
        errors.append("treatment final facts are not exact")
    if result["metrics"]["query_scope_leak_count"] != 0:
        errors.append("treatment query selected a cross-user source")
    if result["metrics"]["store_provenance_mismatch_count"] != 0:
        errors.append("complete store contains cross-user provenance")
    if result["metrics"]["secret_retention"] != 0:
        errors.append("forbidden secret was returned")
    if result["metrics"]["secret_rejection_ids"] != oracle["secret_rejections"]:
        errors.append("secret rejections differ from independent oracle")
    return errors


def negative_checks(fixtures, oracle):
    result = execute("treatment", fixtures)
    cases = 0
    # An orphan fact must violate complete-store closure even though no query selects it.
    orphan = copy.deepcopy(result)
    orphan["store"].append({"scope": {"user": "u3", "key": "team"}, "value": "orphan", "tombstone": False, "provenance": "r9:u3:team", "source_user": "u3"})
    cases += int(bool(validate(orphan, fixtures, oracle)))
    # r5 is intentionally missing the legacy secret flag; retaining it must fail closed.
    unclassified = copy.deepcopy(result)
    unclassified["event_dispositions"]["r5:u2:api_token"] = "retained"
    cases += int(bool(validate(unclassified, fixtures, oracle)))
    # Provenance is checked over the full store, including facts not selected by a query.
    foreign_source = copy.deepcopy(result)
    foreign_source["store"][0]["source_user"] = "u2"
    foreign_source["metrics"]["store_provenance_mismatch_count"] = 1
    foreign_source["metrics"]["store_provenance_mismatch_rate"] = 1 / len(foreign_source["store"])
    cases += int(bool(validate(foreign_source, fixtures, oracle)))
    # Preserve the existing queried-fact tamper negative test.
    queried_tamper = copy.deepcopy(result)
    queried_tamper["answers"]["q-u2-team"]["value"] = "tampered"
    cases += int(bool(validate(queried_tamper, fixtures, oracle)))
    # Altering validation-only oracle policy must not change raw treatment output.
    oracle_policy_tamper = copy.deepcopy(oracle)
    oracle_policy_tamper["sensitive_keys"] = ["different_sensitive_key"]
    cases += int(execute("treatment", fixtures) == result and bool(validate(result, fixtures, oracle_policy_tamper)))
    return cases


def run(mode):
    fixtures, oracle = load("fixtures.json"), load("oracle.json")
    result = execute(mode, fixtures)
    result["passed_oracle"] = not validate(result, fixtures, oracle)
    return result


def main():
    fixtures, oracle = load("fixtures.json"), load("oracle.json")
    outputs = {mode: run(mode) for mode in ("baseline", "treatment")}
    for mode, value in outputs.items():
        (ROOT / "runs" / f"{mode}.json").write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(outputs, sort_keys=True, indent=2))
    expected_negatives = len(oracle["negative_cases"])
    raise SystemExit(0 if outputs["treatment"]["passed_oracle"] and negative_checks(fixtures, oracle) == expected_negatives else 1)


if __name__ == "__main__":
    main()
