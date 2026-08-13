#!/usr/bin/env python3
"""Dispatch frozen generation tasks to a JSON stdin/stdout adapter.

The adapter receives one generation-request/v1 object on stdin and must return one
generation-response/v1 object on stdout. This keeps provider credentials and SDKs
outside the benchmark while preserving exact requests, outputs, attempts, usage,
cost, and resumability as content-addressed evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from artifact_store import ArtifactStore
from common import ROOT, ValidationError, hash_without, read_json, read_jsonl, sha256_value


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _store_restricted_log(directory: Path | None, run_id: str, task_id: str, attempt: int, data: bytes | str | None) -> str | None:
    if data is None:
        return None
    payload = data.encode() if isinstance(data, str) else data
    digest = hashlib.sha256(payload).hexdigest()
    if directory is not None:
        target = directory / run_id / task_id / f"{attempt:04d}-{digest}.stderr"
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            descriptor = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        except FileExistsError:
            if target.read_bytes() != payload:
                raise ValidationError("restricted stderr log digest collision")
        else:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(payload); stream.flush(); os.fsync(stream.fileno())
    return digest


def validate_snapshots(value: dict[str, Any], plan: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if set(value) != {"schema_version", "skills"} or value["schema_version"] != "skill-snapshots/v1":
        raise ValidationError("skill snapshot bundle contract invalid")
    expected = {(task["skill_id"], task["skill_revision"]) for task in plan["tasks"]}
    indexed = {}
    for item in value["skills"]:
        if set(item) != {"skill_id", "revision", "source_uri", "skill_text", "skill_sha256"}:
            raise ValidationError("skill snapshot keys invalid")
        if hashlib.sha256(item["skill_text"].encode()).hexdigest() != item["skill_sha256"]:
            raise ValidationError(f"skill snapshot hash mismatch: {item['skill_id']}")
        key = (item["skill_id"], item["revision"])
        if key in indexed:
            raise ValidationError(f"duplicate skill snapshot: {key}")
        indexed[key] = item
    if set(indexed) != expected:
        raise ValidationError("skill snapshots do not exactly cover planned revisions")
    return indexed


def build_requests(plan: dict[str, Any], cases: list[dict[str, Any]], snapshots: dict[str, Any]) -> list[dict[str, Any]]:
    if plan.get("schema_version") not in {None, "generation-plan/v1"}:
        raise ValidationError("generation plan version invalid")
    if "plan_sha256" in plan and hash_without(plan, "plan_sha256") != plan["plan_sha256"]:
        raise ValidationError("generation plan hash invalid")
    if sha256_value(plan.get("generator_contract")) != plan.get("generator_contract_sha256"):
        raise ValidationError("generator contract hash invalid")
    indexed_cases = {case["case_id"]: case for case in cases}
    if len(indexed_cases) != len(cases):
        raise ValidationError("duplicate cases in dispatch input")
    indexed_skills = validate_snapshots(snapshots, plan)
    requests = []
    for task in plan["tasks"]:
        task_body = {key: value for key, value in task.items() if key not in {"task_id", "task_sha256"}}
        if sha256_value(task_body) != task.get("task_id") or sha256_value({**task_body, "task_id": task.get("task_id")}) != task.get("task_sha256"):
            raise ValidationError("generation task hashes invalid")
        case = indexed_cases.get(task["case_id"])
        if (case is None or hash_without(case, "case_sha256") != case.get("case_sha256")
                or case["case_sha256"] != task["case_sha256"]
                or sha256_value(case["prompt"]) != task["prompt_sha256"]
                or task["generator_contract_sha256"] != plan["generator_contract_sha256"]):
            raise ValidationError(f"planned case missing or changed: {task['case_id']}")
        skill = indexed_skills[(task["skill_id"], task["skill_revision"])]
        request = {
            "schema_version": "generation-request/v1",
            "task": task,
            "case": case,
            "skill_snapshot": skill,
            "generator_contract": plan["generator_contract"],
        }
        request["request_sha256"] = sha256_value(request)
        requests.append(request)
    return requests


def _validate_response(response: Any, request: dict[str, Any]) -> None:
    required = {"schema_version", "task_id", "text", "provider_request_id", "model_provider", "model_family", "model_revision", "usage", "cost"}
    if not isinstance(response, dict) or set(response) != required or response["schema_version"] != "generation-response/v1":
        raise ValidationError("generation response contract invalid")
    if (response["task_id"] != request["task"]["task_id"] or not isinstance(response["text"], str)
            or not response["text"].strip() or not isinstance(response["provider_request_id"], str)
            or not response["provider_request_id"].strip()):
        raise ValidationError("generation response task/text invalid")
    contract = request["generator_contract"]
    expected = (contract["model_provider"], contract["model_family"], contract["model_revision"])
    actual = (response["model_provider"], response["model_family"], response["model_revision"])
    if actual != expected:
        raise ValidationError("generation response model identity differs from frozen contract")
    usage = response["usage"]
    if usage is not None:
        if set(usage) != {"input_tokens", "output_tokens", "total_tokens"} or any(not isinstance(usage[key], int) or usage[key] < 0 for key in usage):
            raise ValidationError("usage must be null or nonnegative integer token counts")
        if usage["input_tokens"] + usage["output_tokens"] != usage["total_tokens"]:
            raise ValidationError("usage token total mismatch")
    cost = response["cost"]
    if cost is not None and (set(cost) != {"currency", "amount"} or not isinstance(cost["currency"], str) or not isinstance(cost["amount"], (int, float)) or cost["amount"] < 0):
        raise ValidationError("cost must be null or a nonnegative amount with currency")


def _output(request: dict[str, Any], response: dict[str, Any]) -> dict[str, str]:
    task = request["task"]
    text = response["text"]
    keys = ("task_id", "task_sha256", "case_id", "case_sha256", "prompt_sha256", "skill_id", "skill_revision", "generator_contract_sha256")
    return {**{key: task[key] for key in keys}, "text": text, "output_sha256": hashlib.sha256(text.encode()).hexdigest()}


def dispatch(plan: dict[str, Any], cases: list[dict[str, Any]], snapshots: dict[str, Any], store: ArtifactStore,
             run_id: str, adapter: list[str] | None, timeout_seconds: int = 300, max_tasks: int | None = None,
             restricted_log_dir: Path | None = None) -> dict[str, Any]:
    if (not isinstance(run_id, str) or run_id in {".", ".."} or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", run_id) is None
            or not isinstance(timeout_seconds, int) or timeout_seconds < 1):
        raise ValidationError("run id or timeout invalid")
    requests = build_requests(plan, cases, snapshots)
    command_sha = sha256_value(adapter) if adapter else None
    completed = failed = prepared = executed = 0
    for request in requests:
        task_id = request["task"]["task_id"]
        success_path = Path("runs") / run_id / "success" / f"{task_id}.json"
        existing = store.read_ref(success_path)
        if existing is not None:
            receipt = store.get_json(existing)
            if receipt["task_sha256"] != request["task"]["task_sha256"] or receipt["status"] != "success":
                raise ValidationError(f"resume receipt does not match task: {task_id}")
            completed += 1
            continue
        request_ref = store.put_json("request", request)
        store.put_ref_once(Path("runs") / run_id / "requests" / f"{task_id}.json", request_ref)
        prepared += 1
        if adapter is None or (max_tasks is not None and executed >= max_tasks):
            continue
        executed += 1
        attempt_dir = store.root / "runs" / run_id / "attempts" / task_id
        attempt_dir.mkdir(parents=True, exist_ok=True)
        attempt = len(list(attempt_dir.glob("*.json"))) + 1
        started = _now(); monotonic = time.monotonic()
        status = "failed"; error = None; response_ref = output_ref = None; usage = cost = None
        stderr_digest = None
        try:
            process = subprocess.run(adapter, input=json.dumps(request, ensure_ascii=False), text=True,
                                     capture_output=True, timeout=timeout_seconds, check=False)
            if process.returncode != 0:
                stderr_digest = _store_restricted_log(restricted_log_dir, run_id, task_id, attempt, process.stderr)
                error = {"category": "adapter_exit", "exit_code": process.returncode, "stderr_sha256": stderr_digest}
                raise RuntimeError("adapter_exit")
            try:
                response = json.loads(process.stdout)
            except json.JSONDecodeError as exc:
                raise ValidationError(f"adapter stdout is not one JSON object: {exc}") from exc
            _validate_response(response, request)
            response_ref = store.put_json("response", response)
            output = _output(request, response)
            output_ref = store.put_json("output", output)
            usage, cost, status = response["usage"], response["cost"], "success"
        except subprocess.TimeoutExpired as exc:
            stderr_digest = _store_restricted_log(restricted_log_dir, run_id, task_id, attempt, exc.stderr)
            error = {"category": "timeout", "exit_code": None, "stderr_sha256": stderr_digest}
        except OSError:
            error = {"category": "adapter_os_error", "exit_code": None, "stderr_sha256": None}
        except ValidationError:
            error = {"category": "invalid_response", "exit_code": 0, "stderr_sha256": stderr_digest}
        except RuntimeError as exc:
            if str(exc) != "adapter_exit":
                raise
        receipt = {
            "schema_version": "generation-receipt/v1", "run_id": run_id, "task_id": task_id,
            "task_sha256": request["task"]["task_sha256"], "attempt": attempt, "status": status,
            "started_at": started, "finished_at": _now(), "duration_ms": round((time.monotonic()-monotonic)*1000),
            "adapter_command_sha256": command_sha, "request": request_ref, "response": response_ref,
            "output": output_ref, "usage": usage, "cost": cost, "error": error,
        }
        receipt_ref = store.put_json("receipt", receipt)
        store.put_ref_once(Path("runs") / run_id / "attempts" / task_id / f"{attempt:04d}.json", receipt_ref)
        if status == "success":
            store.put_ref_once(success_path, receipt_ref); completed += 1
        else:
            failed += 1
    return {"run_id": run_id, "planned": len(requests), "prepared": prepared, "completed": completed,
            "failed": failed, "pending": len(requests)-completed, "cost_status": "not_executed" if adapter is None else "recorded_per_receipt"}


def export_outputs(plan: dict[str, Any], store: ArtifactStore, run_id: str) -> list[dict[str, Any]]:
    rows = []
    for task in plan["tasks"]:
        ref = store.read_ref(Path("runs") / run_id / "success" / f"{task['task_id']}.json")
        if ref is None:
            raise ValidationError(f"cannot export incomplete run; missing {task['task_id']}")
        receipt = store.get_json(ref)
        rows.append(store.get_json(receipt["output"]))
    return rows


def accounting(plan: dict[str, Any], store: ArtifactStore, run_id: str) -> dict[str, Any]:
    totals = {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
    currencies: dict[str, float] = {}
    completed = usage_unknown = cost_unknown = 0
    for task in plan["tasks"]:
        ref = store.read_ref(Path("runs") / run_id / "success" / f"{task['task_id']}.json")
        if ref is None:
            continue
        receipt = store.get_json(ref); completed += 1
        if receipt["usage"] is None:
            usage_unknown += 1
        else:
            for key in totals:
                totals[key] += receipt["usage"][key]
        if receipt["cost"] is None:
            cost_unknown += 1
        else:
            currency = receipt["cost"]["currency"]
            currencies[currency] = currencies.get(currency, 0) + receipt["cost"]["amount"]
    return {"completed": completed, "usage_totals": totals, "usage_unknown_receipts": usage_unknown,
            "cost_totals": currencies, "cost_unknown_receipts": cost_unknown}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, required=True); parser.add_argument("--cases", type=Path, required=True)
    parser.add_argument("--snapshots", type=Path, required=True); parser.add_argument("--store", type=Path, required=True)
    parser.add_argument("--run-id", required=True); parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--max-tasks", type=int); parser.add_argument("--export-output", type=Path)
    parser.add_argument("--restricted-log-dir", type=Path)
    parser.add_argument("--adapter", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    summary = dispatch(read_json(args.plan), read_jsonl([args.cases]), read_json(args.snapshots), ArtifactStore(args.store),
                       args.run_id, args.adapter or None, args.timeout, args.max_tasks, args.restricted_log_dir)
    summary["accounting"] = accounting(read_json(args.plan), ArtifactStore(args.store), args.run_id)
    if args.export_output is not None:
        rows = export_outputs(read_json(args.plan), ArtifactStore(args.store), args.run_id)
        payload = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n" for row in rows)
        args.export_output.parent.mkdir(parents=True, exist_ok=True)
        if args.export_output.exists() and args.export_output.read_text() != payload:
            raise ValidationError(f"refusing to overwrite immutable export: {args.export_output}")
        args.export_output.write_text(payload)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if summary["failed"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
