#!/usr/bin/env python3
"""Hash-locked source readers for the full writing benchmark corpus.

The readers expose source records; family assignment, language balancing and split
selection remain in ``build_full_corpus.py``.  No reference answer is returned.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import tarfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    record_id: str
    title: str
    text: str
    locator: str
    native_language: str | None = None
    criteria: tuple[str, ...] = ()
    metadata: tuple[tuple[str, str], ...] = ()

    @property
    def content_sha256(self) -> str:
        value = {
            "source_id": self.source_id,
            "record_id": self.record_id,
            "title": self.title,
            "text": self.text,
            "metadata": dict(self.metadata),
        }
        payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(payload.encode()).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_file(path: Path, expected: str) -> None:
    if not path.is_file():
        raise ValueError(f"missing locked source artifact: {path}")
    actual = sha256_file(path)
    if actual != expected:
        raise ValueError(f"source SHA-256 mismatch for {path.name}: expected {expected}, got {actual}")


def _decode(value: bytes) -> str:
    return value.decode("utf-8", errors="replace")


def _strip_frontmatter(value: str) -> str:
    if value.startswith("---\n"):
        end = value.find("\n---\n", 4)
        if end >= 0:
            return value[end + 5 :]
    return value


def _clean_markdown(value: str) -> str:
    """Remove front matter, fenced code and presentation markup.

    This deliberately does not claim to parse Markdown. Inline code and indented code
    can remain in the returned excerpt, so documentation records require a later
    source-specific prose/code license review before case materialization.
    """
    value = _strip_frontmatter(value)
    value = re.sub(r"```[\s\S]*?```", "\n", value)
    value = re.sub(r"<!--.*?-->", " ", value, flags=re.S)
    value = re.sub(r"{%[\s\S]*?%}|{{[\s\S]*?}}", " ", value)
    value = re.sub(r"!\[[^]]*]\([^)]*\)", " ", value)
    value = re.sub(r"\[([^]]+)]\([^)]*\)", r"\1", value)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"^#{1,6}\s+", "", value, flags=re.M)
    value = re.sub(r"^\s*[-*+]\s+", "", value, flags=re.M)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def bounded_excerpt(value: str, minimum: int = 900, maximum: int = 3600) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) < minimum:
        return ""
    if len(value) <= maximum:
        return value
    cut = value[:maximum]
    boundary = max(cut.rfind(". "), cut.rfind("。"), cut.rfind("! "), cut.rfind("? "))
    if boundary >= minimum:
        cut = cut[: boundary + 1]
    return cut.strip()


def load_writingbench(path: Path, lock: dict[str, Any]) -> list[SourceRecord]:
    verify_file(path, lock["content_sha256"])
    records: list[SourceRecord] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            criteria = tuple(
                str(item.get("criteria_description", "")).strip()
                for item in row.get("checklist", [])[:5]
                if str(item.get("criteria_description", "")).strip()
            )
            records.append(SourceRecord(
                "writingbench", str(row["index"]), str(row["domain2"]),
                str(row["query"]),
                f"https://github.com/X-PLUG/WritingBench/blob/{lock['revision']}/{lock['path']}#index-{row['index']}",
                str(row["lang"]), criteria,
                tuple(sorted({"domain1": str(row["domain1"]), "domain2": str(row["domain2"])}.items())),
            ))
    if len(records) != int(lock["expected_rows"]):
        raise ValueError(f"WritingBench row count mismatch: {len(records)}")
    return records


def load_govreport(path: Path, lock: dict[str, Any]) -> list[SourceRecord]:
    verify_file(path, lock["content_sha256"])
    document = json.loads(path.read_text(encoding="utf-8"))
    records: list[SourceRecord] = []
    for item in document["rows"]:
        row = item["row"]
        text = bounded_excerpt(str(row["report"]), 1200, 4800)
        if not text:
            continue
        index = str(item["row_idx"])
        records.append(SourceRecord(
            "govreport", index, f"GovReport test document {index}", text,
            f"hf://datasets/ccdv/govreport-summarization@{lock['revision']}/document/test#{index}",
            "en", (), (("split", "test"),),
        ))
    if len(records) < int(lock["materialized_rows"]):
        raise ValueError(f"GovReport materialized row count mismatch: {len(records)}")
    return records


def _iter_tar_text(path: Path, suffix: str) -> Iterable[tuple[str, str]]:
    with tarfile.open(path, "r:gz") as archive:
        for member in archive:
            if not member.isfile() or not member.name.endswith(suffix):
                continue
            handle = archive.extractfile(member)
            if handle is None:
                continue
            yield member.name, _decode(handle.read())


def load_github_docs(path: Path, lock: dict[str, Any]) -> list[SourceRecord]:
    verify_file(path, lock["content_sha256"])
    prefix = f"docs-{lock['revision']}/content/"
    records: list[SourceRecord] = []
    for name, raw in _iter_tar_text(path, ".md"):
        if not name.startswith(prefix):
            continue
        text = bounded_excerpt(_clean_markdown(raw))
        if not text:
            continue
        relative = name[len(f"docs-{lock['revision']}/"):]
        title = relative.rsplit("/", 2)[-2].replace("-", " ")
        records.append(SourceRecord(
            "github_docs", relative, title, text,
            f"https://github.com/github/docs/blob/{lock['revision']}/{relative}", "en",
        ))
    if len(records) < 1000:
        raise ValueError(f"GitHub Docs candidate pool unexpectedly small: {len(records)}")
    return records


def load_mdn(path: Path, lock: dict[str, Any]) -> list[SourceRecord]:
    verify_file(path, lock["content_sha256"])
    prefix = f"content-{lock['revision']}/files/en-us/"
    records: list[SourceRecord] = []
    for name, raw in _iter_tar_text(path, "index.md"):
        if not name.startswith(prefix):
            continue
        text = bounded_excerpt(_clean_markdown(raw))
        if not text:
            continue
        relative = name[len(f"content-{lock['revision']}/"):]
        title = relative.rsplit("/", 2)[-2].replace("_", " ")
        records.append(SourceRecord(
            "mdn_content", relative, title, text,
            f"https://github.com/mdn/content/blob/{lock['revision']}/{relative}", "en",
        ))
    if len(records) < 1000:
        raise ValueError(f"MDN candidate pool unexpectedly small: {len(records)}")
    return records


def load_dolly(path: Path, lock: dict[str, Any]) -> list[SourceRecord]:
    verify_file(path, lock["content_sha256"])
    records: list[SourceRecord] = []
    permitted = {"brainstorming", "information_extraction", "summarization", "closed_qa"}
    with path.open(encoding="utf-8") as handle:
        for index, line in enumerate(handle):
            row = json.loads(line)
            if row["category"] not in permitted:
                continue
            context = str(row.get("context", "")).strip()
            instruction = str(row["instruction"]).strip()
            combined = f"Instruction: {instruction}"
            if context:
                combined += f"\n\nContext: {bounded_excerpt(context, 0, 3000)}"
            if len(combined) < 120:
                continue
            records.append(SourceRecord(
                "dolly_15k", str(index), f"Dolly {row['category']} instruction", combined,
                f"hf://datasets/databricks/databricks-dolly-15k@{lock['revision']}/train#{index}",
                "en", (), (("category", str(row["category"])),),
            ))
    if len(records) < 1000:
        raise ValueError(f"Dolly candidate pool unexpectedly small: {len(records)}")
    return records


def _repair_mojibake(value: str) -> str:
    if "Ã" not in value and "Â" not in value:
        return value
    try:
        return value.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return value


def load_nhtsa(paths: list[Path], lock: dict[str, Any]) -> list[SourceRecord]:
    for path in paths:
        verify_file(path, lock["files"][path.name])
    latest: dict[str, dict[str, str]] = {}
    for path in paths:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                report_id = row.get("Report ID", "").strip()
                if not report_id or row.get("Narrative - CBI?", "").strip().upper() == "Y":
                    continue
                narrative = _repair_mojibake(row.get("Narrative", "").strip())
                if len(narrative) < 350 or "CONFIDENTIAL BUSINESS INFORMATION" in narrative.upper():
                    continue
                version = int(row.get("Report Version", "0") or 0)
                previous = latest.get(report_id)
                if previous is None or version > int(previous.get("Report Version", "0") or 0):
                    latest[report_id] = row | {"Narrative": narrative}
    records: list[SourceRecord] = []
    safe_fields = [
        "Report Month", "Report Year", "State", "Roadway Type", "Crash With",
        "Highest Injury Severity Alleged", "SV Pre-Crash Movement", "Any Air Bags Deployed?",
        "Was Any Vehicle Towed?", "Weather - Clear", "Weather - Rain", "Weather - Snow",
    ]
    for report_id, row in latest.items():
        facts = [f"{field}: {row[field].strip()}" for field in safe_fields if row.get(field, "").strip()]
        text = bounded_excerpt(row["Narrative"], 350, 3200)
        if not text:
            continue
        source = "Known report fields:\n" + "\n".join(facts) + "\n\nReported narrative:\n" + text
        records.append(SourceRecord(
            "nhtsa_incidents", report_id, f"NHTSA incident {report_id}", source,
            f"https://static.nhtsa.gov/odi/ffdd/sgo-2021-01/#report-{report_id}", "en",
            (), (("report_version", row.get("Report Version", "")),),
        ))
    if len(records) < int(lock.get("minimum_candidate_rows", 100)):
        raise ValueError(f"NHTSA incident candidate pool unexpectedly small: {len(records)}")
    return records


def select_by_hash(records: Iterable[SourceRecord], count: int, seed: str,
                   used: set[tuple[str, str]]) -> list[SourceRecord]:
    candidates = [record for record in records if (record.source_id, record.record_id) not in used]
    candidates.sort(key=lambda item: hashlib.sha256(
        f"{seed}\0{item.source_id}\0{item.record_id}".encode()
    ).hexdigest())
    if len(candidates) < count:
        raise ValueError(f"{seed}: requested {count} records, only {len(candidates)} available")
    selected = candidates[:count]
    used.update((item.source_id, item.record_id) for item in selected)
    return selected
