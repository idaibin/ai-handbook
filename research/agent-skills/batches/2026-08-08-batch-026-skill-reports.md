# Agent Skills individual reports — Batch 026

Observed: `2026-08-08`

Repository-scoped skill reports: **4**

Only actual local skill definitions are reported here. Exact official specification mirrors, SDK/tooling repositories, and the non-skill interview-prompt repository are intentionally not expanded into duplicate or synthetic skill reports.

## `ctvida/agentskills`

### `drive-organizer`

- **Definition:** `drive-organizer/SKILL.md`
- **Purpose:** Organize a confirmed local directory or Google Drive target through a staged audit/proposal/review/commit pipeline.
- **Structure:** `SKILL.md`, local README, Python workflow scripts, dependency/install material, and generated intermediate artifacts described by the protocol.
- **Workflow contract:** audit first; produce `audit.json`; generate `governed_actions.csv`; optionally analyze ambiguous file content; summarize proposals; wait for human review; then run a local or Drive commit path.
- **Implementation evidence:** `committer.py` executes only rows with `approved=TRUE`, skips normalized no-op paths, blocks using a local filesystem root as the base, and cleans only empty source folders after moves. Google Drive mode can create destination folders and update parent relationships through authenticated APIs.
- **Risk boundary:** final commit is mutation-capable. The repository's governance model defaults proposals to `TRUE`, so review is opt-out rather than conservative opt-in. This increases the importance of the explicit wait/review step.
- **References/evals:** no dedicated eval suite was surfaced in the inspected current skill material.
- **Runtime:** not executed. No files or Drive objects were moved.

### `export-session`

- **Definition:** `export-session/SKILL.md`
- **Purpose:** Export current or historical Claude conversation transcripts to searchable Markdown with summary, semantic tags, metadata, and an optional operator note.
- **Structure:** `SKILL.md`, `scripts/`, and `evals/evals.json`.
- **Workflow contract:** if work is unfinished, prepare a user-confirmed resume point before export; completed work must not receive an invented next-action marker. Export then resolves a session/project, reconstructs conversation text, summarizes/tags it, and writes an immutable Markdown record.
- **Implementation evidence:** `scripts/session-exporter.py` reads Claude Code JSONL transcript files, ignores sidechains, filters AI/harness meta-command turns, rejects effectively empty transcripts, samples head/middle/tail for long conversations, supports Claude/local/OpenRouter summarization backends, builds YAML frontmatter, and writes the final Markdown file.
- **Eval surface:** `evals/evals.json` defines three expected-output scenarios covering default export, export with note, and export of a specified historical session/project.
- **Risk/quality note:** model-generated summary/tags are derived artifacts while the full exported conversation is preserved. The current implementation falls back to a generic summary/tag if model inference fails rather than failing the entire export.
- **Runtime:** scripts and evals were not executed.

### `uxpsych-design`

- **Definition:** `uxpsych-design/SKILL.md`
- **Reference:** `uxpsych-design/references/playbook.md`
- **Purpose:** Apply a checkable UI/UX conversion and trust checklist during interface generation or review.
- **Design:** the compact skill body carries executable review/build rules while the larger playbook is progressively loaded for rationale and examples.
- **Notable contract elements:** hero hierarchy, friction reduction, trust near decision points, value-before-signup, mobile thumb-zone checks, empty-state requirements, typography/metric hierarchy, and explicit pre-output checks.
- **Guardrail:** the skill explicitly forbids fabricated reviews, numbers, urgency, or losses and frames persuasion rules as valid only when claims are true.
- **Quality note:** many rules are intentionally prescriptive. They are useful as review heuristics but should not be treated as universal empirical laws without product-specific testing.
- **Runtime/evals:** no UI build, browser check, A/B test, or eval runner was executed.

## `zurbrick/ooda-skill`

### `ooda`

- **Definition:** root `SKILL.md`
- **References:** `references/decision-types.md`, `references/loop-template.md`
- **Purpose:** Fast structured decision support under uncertainty using Observe → Orient → Decide → Act plus an explicit re-loop trigger.
- **Activation boundary:** intended for live uncertain decisions with incomplete signals; explicitly excluded for trivial tasks, execution-heavy work, fact-poor situations needing research first, and irreversible/high-blast-radius decisions that need fuller review.
- **Decision model:** orientation captures goal, constraints, incentives, risks, reversibility, hidden assumptions, and framing errors before a decision is made.
- **Reference design:** `decision-types.md` calibrates behavior by reversibility and requires escalation for irreversible/high-impact cases; `loop-template.md` standardizes verified facts, unknowns, trade-offs, owner, timing, feedback signal, and reassessment trigger.
- **Implementation:** methodology-only; no scripts or executable dependencies.
- **Evals/runtime:** no eval suite is present and no runtime/outcome validation was performed.

## Zero-report reviewed repositories

The following reviewed queue entries intentionally contribute **0** skill reports:

- `sampath1310/AgentSkills` — one standalone data-engineering interview prompt; no Agent Skills package.
- `wujixialan/agentskills` — exact official Agent Skills specification snapshot at `5e7f3e2c...`.
- `ILyes-SS/agentskills` — exact official Agent Skills specification snapshot at `5e7f3e2c...`.
- `Jahid11978/agentskills` — exact official Agent Skills specification/reference snapshot at `217be548...`.
- `nijaru/agentskills` — Go loader/validator/registry tooling with tests, not a production skill catalog.
- `dev-juha/agentskills` — exact official Agent Skills specification snapshot at `b5ce2a43...`.
- `luizotavioautomacao/agentskills` — exact official Agent Skills specification snapshot at `5e7f3e2c...`.
- `netover/agentskills` — exact official Agent Skills specification snapshot at `b5ce2a43...`.
