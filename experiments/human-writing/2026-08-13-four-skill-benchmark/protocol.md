# Execution protocol

This file preserves the effective task contracts used for the final generation and judgment runs. Paths are expressed relative to the experiment or as materialized skill identities; ephemeral local paths are intentionally removed.

## Generator contract

Each of four fresh agents received one fixed skill and the same task:

> Formal independent generation. Read the assigned fixed `SKILL.md` in full and any references it routes for this task. Read only `generator-inputs.md`; do not read `cases.md`, experiment `outputs/`, `results/`, `README.md`, or other repository files. Process T01–T10 using each case's Instruction and Input. Write `outputs/<skill>.md` with headings T01–T10 and the finished artifact only, followed by Run metadata containing this task contract and the files actually read.

The assigned skill trees and commits are in `manifest.yaml`. `generator-inputs.md` contains neutral IDs and omits source paths, references, degradation/control labels, and expected decisions.

## Judge contract

Three fresh agents each received only its numbered packet and this task:

> Anonymous judge JN. Read only `results/blind-review-N.md`; do not read mappings, other packets, outputs, skills, cases, or reports. For every case, score candidates A–D from 1–5 on fidelity, instruction/structure, clarity, naturalness, and restraint. Record any factual omission/addition or modality/claim-strength change as `hard_issue`. Treat Reference as a style reference, not a unique valid answer. Provide a parseable Markdown table, `Ranking: ...` with `=` for ties, and concrete evidence. Write `results/judge-N.md`.

Each numbered packet contains the frozen definitions and 1/3/5 anchors for all five dimensions, the rule that a localized hard issue caps fidelity at 3, and a case-specific semantic criterion. The saved judge sheets are the fresh runs made after those anchors were added.

## Aggregation rules

- Six controlled-repair cases distinguish rewrite performance; four untouched cases test unnecessary editing.
- Every protected span must remain verbatim.
- A hard issue is reported separately from the five-dimension mean.
- Ties split first-place share evenly.
- `evaluate.py` builds a seeded, Latin-rotated packet for each judge.
- `aggregate.py` fails unless it parses exactly 120 score rows, 30 complete rankings, bijective mappings, A–D once per judge/case, valid 1–5 scores, and first-place shares totaling 18/30.
