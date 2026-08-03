#!/usr/bin/env python3
"""Apply one validated mark only inside a fail-closed isolated workspace."""
from __future__ import annotations

import difflib
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

CASE = Path(__file__).resolve().parent
HANDBOOK_ROOT = CASE.parents[3]
KNOWLEDGE_DISTILLATION_ROOT = Path(os.environ.get("KNOWLEDGE_DISTILLATION_ROOT", HANDBOOK_ROOT.parent / "knowledge-distillation")).expanduser()
SOURCE_RELATIVE = Path("examples/engineering/agent-runtime-orchestration/knowledge.yaml")
VALIDATOR_RELATIVE = Path("scripts/validate_ir.py")
SOURCE = KNOWLEDGE_DISTILLATION_ROOT / SOURCE_RELATIVE
VALIDATOR = KNOWLEDGE_DISTILLATION_ROOT / VALIDATOR_RELATIVE
SOURCE_LABEL = "https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/agent-runtime-orchestration/knowledge.yaml"
VALIDATOR_LABEL = "https://github.com/idaibin/knowledge-distillation/blob/main/scripts/validate_ir.py"
WORKSPACE = CASE / "workspace"
TARGET = WORKSPACE / "input/knowledge.yaml"
WORKSPACE_RELATIVE = Path("workspace")
TARGET_RELATIVE = Path("workspace/input/knowledge.yaml")
MARK = "# APPLICATION-MARK: isolated-knowledge-patch-v1"
RAW_EVIDENCE = {"target_file_mark_added", "validator_passed", "scoped_unified_diff", "forbidden_paths_unchanged", "target_workspace_match"}
RAW_FORBIDDEN_PATHS = [SOURCE_LABEL, VALIDATOR_LABEL]
ORACLE_SHA256 = "8877993b7bf18785a3f73585ecc66e67126f7928407facf8c6231bf02cf26634"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def metrics(expected: set[str], predicted: set[str]) -> dict[str, float | int]:
    tp, fp, fn = len(expected & predicted), len(predicted - expected), len(expected - predicted)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"TP": tp, "FP": fp, "FN": fn, "precision": precision, "recall": recall, "F1": f1}


def contained(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def fail_closed_paths(oracle: dict[str, object]) -> tuple[bool, str]:
    """Validate all mutable locations before any mkdir/rmtree/copy/write."""
    case = CASE.resolve()
    workspace = WORKSPACE.resolve(strict=False)
    target = TARGET.resolve(strict=False)
    if CASE.is_symlink() or WORKSPACE.is_symlink():
        return False, "case/workspace must not be symlinks"
    if TARGET.exists() and TARGET.is_symlink():
        return False, "target must not be a symlink"
    if not contained(workspace, case) or workspace != (case / WORKSPACE_RELATIVE).resolve(strict=False):
        return False, "workspace escapes CASE or does not match workspace-relative target"
    if not contained(target, workspace) or not contained(target, case):
        return False, "target escapes workspace/CASE"
    if target != (case / TARGET_RELATIVE).resolve(strict=False) or target.relative_to(case) != TARGET_RELATIVE:
        return False, "target does not match fixed CASE-relative target"
    oracle_workspace = oracle.get("workspace_relative")
    oracle_target = oracle.get("target_relative")
    if oracle_workspace != WORKSPACE_RELATIVE.as_posix() or oracle_target != TARGET_RELATIVE.as_posix():
        return False, "oracle workspace/target relative paths do not match fixed target"
    if target.relative_to(case).as_posix() != str(oracle_target):
        return False, "oracle target does not match TARGET.relative_to(CASE)"
    return True, ""


def load_oracle() -> tuple[dict[str, object] | None, str, str | None]:
    data = CASE.joinpath("oracle.json").read_bytes()
    before = hashlib.sha256(data).hexdigest()
    if before != ORACLE_SHA256:
        return None, before, "frozen oracle SHA-256 mismatch"
    try:
        oracle = json.loads(data)
    except json.JSONDecodeError as error:
        return None, before, f"invalid frozen oracle: {error}"
    return (oracle if isinstance(oracle, dict) else None), before, None if isinstance(oracle, dict) else "frozen oracle must be an object"


def run_validator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["python3", str(VALIDATOR), str(path)], text=True, capture_output=True)


def main() -> int:
    oracle, oracle_before, oracle_error = load_oracle()
    if oracle_error:
        print(oracle_error)
        return 1
    assert oracle is not None
    safe, safety_error = fail_closed_paths(oracle)
    if not safe:
        print(f"fail-closed: {safety_error}")
        return 1
    if not SOURCE.is_file():
        print(f"KNOWLEDGE_DISTILLATION_ROOT source is missing: {SOURCE_LABEL}")
        return 1
    if not VALIDATOR.is_file():
        print(f"KNOWLEDGE_DISTILLATION_ROOT validator is missing: {VALIDATOR_LABEL}")
        return 1

    # No filesystem mutation occurs before the oracle and path-containment checks above.
    CASE.joinpath("runs").mkdir(exist_ok=True)
    source_before = digest(SOURCE)
    validator_before = digest(VALIDATOR)
    basis = {"source": SOURCE_LABEL, "validator": VALIDATOR_LABEL, "source_sha256_before": source_before, "validator_sha256_before": validator_before, "workspace_relative": WORKSPACE_RELATIVE.as_posix(), "target_relative": TARGET_RELATIVE.as_posix(), "workspace": WORKSPACE_RELATIVE.as_posix(), "target": TARGET_RELATIVE.as_posix(), "mutation": "append exactly one marked comment to isolated copy", "forbidden_paths": RAW_FORBIDDEN_PATHS, "oracle_sha256_before": oracle_before}
    CASE.joinpath("basis.json").write_text(json.dumps(basis, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    baseline = {"strategy": "wide-path/no-diff-evidence", "claimed_complete": True, "evidence": [], "out_of_bounds": True, "no_evidence_completion": True, "residual_permissions": ["wide workspace", "no revoke receipt"], "metrics": metrics(set(oracle.get("required_evidence", [])), set())}
    CASE.joinpath("runs/baseline.json").write_text(json.dumps(baseline, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if WORKSPACE.exists():
        shutil.rmtree(WORKSPACE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    before_target = digest(TARGET)
    original_bytes = TARGET.read_bytes()
    TARGET.write_bytes(original_bytes + (b"\n" if not original_bytes.endswith(b"\n") else b"") + (MARK + "\n").encode())
    after_target = digest(TARGET)
    diff_lines = list(difflib.unified_diff(SOURCE.read_text(encoding="utf-8").splitlines(), TARGET.read_text(encoding="utf-8").splitlines(), fromfile=SOURCE_LABEL, tofile=TARGET_RELATIVE.as_posix(), lineterm=""))
    diff_text = "\n".join(diff_lines) + ("\n" if diff_lines else "")
    validation = run_validator(TARGET)
    source_after = digest(SOURCE)
    forbidden_unchanged = source_before == source_after and validator_before == digest(VALIDATOR)
    added_lines = [line[1:] for line in diff_lines if line.startswith("+") and not line.startswith("+++")]
    scoped_diff = bool(diff_lines) and added_lines == [MARK] and all(MARK in line or line.startswith(("---", "+++", "@@", " ", "-")) for line in diff_lines)
    target_match = TARGET.relative_to(CASE).as_posix() == oracle["target_relative"] and WORKSPACE.relative_to(CASE).as_posix() == oracle["workspace_relative"]
    treatment_evidence = set()
    if added_lines == [MARK] and after_target != before_target:
        treatment_evidence.add("target_file_mark_added")
    if validation.returncode == 0:
        treatment_evidence.add("validator_passed")
    if scoped_diff:
        treatment_evidence.add("scoped_unified_diff")
    if forbidden_unchanged:
        treatment_evidence.add("forbidden_paths_unchanged")
    if target_match:
        treatment_evidence.add("target_workspace_match")
    treatment = {"strategy": "fail-closed-isolated-copy+scoped-diff+validator+receipt", "target": TARGET_RELATIVE.as_posix(), "target_relative": TARGET_RELATIVE.as_posix(), "workspace_relative": WORKSPACE_RELATIVE.as_posix(), "before_sha256": before_target, "after_sha256": after_target, "validator_command": ["python3", VALIDATOR_LABEL, TARGET_RELATIVE.as_posix()], "validator_exit": validation.returncode, "validator_stdout": validation.stdout.strip().replace(str(TARGET), TARGET_RELATIVE.as_posix()), "unified_diff": diff_text, "evidence": sorted(treatment_evidence), "out_of_bounds": False, "no_evidence_completion": False, "residual_permissions": [], "receipt": {"mutation": "append one application mark", "revoke": "workspace remains local and no external credential/session was opened"}, "metrics": metrics(set(oracle.get("required_evidence", [])), treatment_evidence)}
    CASE.joinpath("runs/treatment.json").write_text(json.dumps(treatment, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    oracle_after = digest(CASE / "oracle.json")
    passed = (oracle_after == oracle_before and treatment_evidence == set(oracle.get("required_evidence", [])) and added_lines == oracle.get("allowed_added_lines") and oracle.get("forbidden_paths") == RAW_FORBIDDEN_PATHS and target_match and validation.returncode == 0 and forbidden_unchanged)
    adjudication = {"oracle_pass": passed, "baseline_metrics": baseline["metrics"], "treatment_metrics": treatment["metrics"], "baseline_out_of_bounds": baseline["out_of_bounds"], "baseline_no_evidence_completion": baseline["no_evidence_completion"], "treatment_residual_permissions": treatment["residual_permissions"], "target_workspace_match": target_match, "source_unchanged": source_before == source_after, "oracle_sha256_before": oracle_before, "oracle_sha256_after": oracle_after, "oracle_hash_unchanged": oracle_before == oracle_after}
    CASE.joinpath("adjudication.json").write_text(json.dumps(adjudication, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    CASE.joinpath("summary.md").write_text("\n".join(["# Case 03 result", "", f"- Fixed containment target: `{TARGET_RELATIVE}` below workspace `{WORKSPACE_RELATIVE}`; all mutable operations ran only after fail-closed canonical containment checks.", f"- Source SHA-256 unchanged: `{source_before == source_after}` (`{source_before}`).", f"- Baseline reports complete without evidence; adjudicated out-of-bounds=`{baseline['out_of_bounds']}` and no-evidence=`{baseline['no_evidence_completion']}`.", f"- Treatment evidence: `{sorted(treatment_evidence)}`; validator exit `{validation.returncode}`; frozen-oracle pass=`{passed}`.", f"- Frozen oracle SHA-256 unchanged: `{oracle_before == oracle_after}` (`{oracle_before}`).", "- Not verified: external credentials, browser profile, MCP session, and production side effects.", ""]), encoding="utf-8")
    print(json.dumps(adjudication, ensure_ascii=False, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
