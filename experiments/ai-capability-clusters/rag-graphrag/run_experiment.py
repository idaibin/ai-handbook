#!/usr/bin/env python3
"""Deterministic lexical-vs-graph retrieval experiment; no network or model calls."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def terms(text):
    return set(re.findall(r"[a-z]+", text.lower()))


def lexical(question, docs, k):
    qt = terms(question["text"])
    scored = [(len(qt & terms(d["text"])), d["id"]) for d in docs]
    return [doc_id for score, doc_id in sorted(scored, key=lambda x: (-x[0], x[1]))[:k] if score > 0]


def infer_kind(text):
    """Infer routing from question text; fixture labels are deliberately untrusted."""
    return "multi-hop" if re.search(r"\bfounded by\b", text.lower()) else "direct"


def treatment_retrieve(question, docs):
    by_id = {d["id"]: d for d in docs}
    if infer_kind(question["text"]) == "direct":
        return lexical(question, docs, 1)
    # Classifier selects a founder document, then follows its frozen graph edge.
    first = lexical(question, docs, 1)
    if not first:
        return []
    path = [first[0]]
    path.extend(by_id[first[0]]["edges"][:1])
    return path


def answer_from_evidence(evidence, docs):
    text = " ".join(d["text"] for d in docs if d["id"] in evidence)
    for place in ("Paris", "Rome"):
        if place in text:
            return place
    return None


def run(mode):
    fixtures, oracle = load("fixtures.json"), load("oracle.json")
    docs = fixtures["documents"]
    rows = {}
    lexical_recall = evidence_precision = graph_path_recall = direct_ok = 0.0
    direct_cases = multi_hop_cases = 0
    label_negative_cases = 0
    expansion_budget = 0
    total_cost = 0
    for q in fixtures["questions"]:
        lexical_evidence = lexical(q, docs, fixtures["top_k"])
        evidence = lexical_evidence if mode == "baseline" else treatment_retrieve(q, docs)
        answer = answer_from_evidence(evidence, docs)
        expected = oracle["answers"][q["id"]]
        exp_evidence, exp_path = set(expected["evidence"]), expected["path"]
        inferred_kind = infer_kind(q["text"])
        if q.get("label_perturbed") and q.get("kind") != inferred_kind:
            label_negative_cases += 1
        lexical_recall += float(exp_evidence.issubset(set(lexical_evidence)))
        evidence_precision += (len(exp_evidence & set(evidence)) / len(evidence)) if evidence else 0.0
        if inferred_kind == "multi-hop":
            multi_hop_cases += 1
            graph_path_recall += float(evidence == exp_path)
            expansion_budget += max(0, len(evidence) - 1)
        else:
            direct_cases += 1
            direct_ok += float(answer == expected["answer"] and evidence == expected["evidence"])
        total_cost += len(evidence) + len(terms(q["text"]))
        rows[q["id"]] = {
            "answer": answer,
            "evidence": evidence,
            "path": evidence,
            "inferred_kind": inferred_kind,
            "label_kind": q.get("kind"),
            "lexical_evidence": lexical_evidence,
            "expansion_steps": max(0, len(evidence) - 1),
            "cost_units": len(evidence) + len(terms(q["text"])),
        }
    n = len(fixtures["questions"])
    metrics = {
        "lexical_recall_at_k": lexical_recall / n,
        "evidence_precision": evidence_precision / n,
        "graph_path_recall": graph_path_recall / multi_hop_cases if multi_hop_cases else 1.0,
        "graph_expansion_budget": expansion_budget,
        "direct_accuracy": direct_ok / direct_cases if direct_cases else 1.0,
        "direct_cases": direct_cases,
        "multi_hop_cases": multi_hop_cases,
        "kind_label_negative_cases": label_negative_cases,
        "cost_units": total_cost,
    }
    expected_budgets = oracle["graph_expansion_steps"]
    passed = True
    fixture_question_ids = {q["id"] for q in fixtures["questions"]}
    passed &= fixture_question_ids == set(oracle["answers"])
    passed &= fixture_question_ids == set(expected_budgets)
    passed &= {
        q["id"] for q in fixtures["questions"]
        if q.get("label_perturbed") and q.get("kind") != infer_kind(q["text"])
    } == set(oracle["label_negative_cases"])
    for q in fixtures["questions"]:
        qid = q["id"]
        expected = oracle["answers"][qid]
        row = rows[qid]
        passed &= row["inferred_kind"] == oracle["inferred_kinds"][qid]
        passed &= row["answer"] == expected["answer"]
        passed &= row["evidence"] == expected["evidence"]
        if mode == "treatment":
            passed &= row["path"] == expected["path"]
        passed &= row["lexical_evidence"] == oracle["lexical_evidence"][qid]
        # Per-question checking prevents one expansion overrun from being
        # cancelled out by another question using fewer steps.
        passed &= row["expansion_steps"] == expected_budgets[qid]
    passed &= metrics["evidence_precision"] == 1.0
    passed &= metrics["graph_path_recall"] == 1.0
    return {"mode": mode, "metrics": metrics, "questions": rows, "passed_oracle": passed}


def main():
    outputs = {m: run(m) for m in ("baseline", "treatment")}
    baseline_direct = outputs["baseline"]["metrics"]["direct_accuracy"]
    treatment_direct = outputs["treatment"]["metrics"]["direct_accuracy"]
    comparison = {
        "baseline_direct_accuracy": baseline_direct,
        "treatment_direct_accuracy": treatment_direct,
        "direct_question_regression": treatment_direct < baseline_direct,
    }
    for mode, value in outputs.items():
        value["comparison"] = comparison
        (ROOT / "runs" / f"{mode}.json").write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(outputs, sort_keys=True, indent=2))
    raise SystemExit(0 if outputs["treatment"]["passed_oracle"] else 1)


if __name__ == "__main__":
    main()
