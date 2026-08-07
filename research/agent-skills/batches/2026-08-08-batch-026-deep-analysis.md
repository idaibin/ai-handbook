# GitHub Skills Catalog deep analysis — Batch 026

Observed: `2026-08-08`

Status: `structure-reviewed`

Runtime validation: `not_executed`

## Scope and completion rule

This batch continued from the persisted GitHub Skills / Agent Skills indexed queue and content-reviewed **10 repository entries**. A repository was counted only after its GitHub identity and exact point-in-time star count were verified and actual repository content was inspected. Metadata-only candidates were not treated as completed skills repositories.

The review surface included README or the actual root commit when no README exists, `SKILL.md` or equivalent definitions, supporting scripts/references/eval material when available, and content-level duplicate/reference detection. Third-party installers, models, external APIs, file movers, builds, tests, eval runners, and other repository code were **not executed**.

## Batch result

| Repository | Repo id | Stars observed | Content-level classification | Local skill reports | Result |
|---|---:|---:|---|---:|---|
| `sampath1310/AgentSkills` | 1194503996 | 0 | `single_prompt_not_agent_skill_package` | 0 | content-rejected / held |
| `ctvida/agentskills` | 1194741834 | 0 | `skill_collection_workflow_and_design` | 3 | structure-reviewed |
| `wujixialan/agentskills` | 1194302478 | 0 | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| `ILyes-SS/agentskills` | 1194703771 | 0 | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| `Jahid11978/agentskills` | 1194380358 | 1 | `official_agent_skills_spec_mirror_snapshot` | 0 | reference / dedupe |
| `zurbrick/ooda-skill` | 1194834757 | 0 | `single_skill_decision_methodology` | 1 | structure-reviewed |
| `nijaru/agentskills` | 1193497345 | 1 | `agent_skills_go_reference_tooling` | 0 | tooling / reference |
| `dev-juha/agentskills` | 1193730251 | 0 | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| `luizotavioautomacao/agentskills` | 1194009493 | 0 | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| `netover/agentskills` | 1193622038 | 0 | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| **Total** | — | — | — | **4** | **10 queue entries content-reviewed** |

Star values were verified through owner/repository-scoped GitHub repository searches using exact `stars:N` predicates during this review. They are point-in-time observations and may change.

## Repository analyses

### 1. `sampath1310/AgentSkills`

**Verified**

- Public repository id `1194503996`, default branch `main`; exact star observation: `0`.
- The repository has a single commit, `6612c3be0fa0c48de38131002fcafde0226465d2`.
- The commit contains one file: `DataEngineer/DataEngineerInterviewer.md`. `README.md` is absent.
- The file is a standalone principal/senior data-engineering interview prompt covering PySpark internals, Delta Lake/lakehouse architecture, software-engineering practices, ETL/system design, drill-down questions, code challenges, scenario questions, and an end-of-interview evaluation.
- No `SKILL.md`, scripts, references, evals, or Agent Skills package structure exists in the inspected tree.

**Content-level correction**

- The index-stage `skill_collection` label is not supported by the actual repository. It is held as `single_prompt_not_agent_skill_package` and contributes **0** skill reports.

### 2. `ctvida/agentskills`

**Verified**

- Public repository id `1194741834`, default branch `main`; exact star observation: `0`.
- Root `README.md` is absent, but commit history and current files show three independent local skills: `drive-organizer`, `export-session`, and `uxpsych-design`.
- `drive-organizer/SKILL.md` defines a staged audit → propose → optional content analysis → human review → commit workflow for local directories or Google Drive. The current skill explicitly requires a target path, writes deterministic intermediate artifacts, and separates proposal from mutation.
- `drive-organizer/README.md` documents local and Google Drive modes and an opt-out approval model. `committer.py` was directly inspected: it blocks a local filesystem root as the base, moves only rows whose `approved` field is `TRUE`, skips no-op paths, and removes only empty source directories after successful moves. The Google Drive path uses authenticated API mutation. No move was executed.
- `export-session/SKILL.md` defines conversation export to Markdown with semantic summary/tags and a conditional resume-point gate. The implementation in `scripts/session-exporter.py` reads Claude JSONL transcripts, filters harness/meta-command turns, samples long transcripts for summarization, supports several model backends, writes YAML-frontmatter Markdown, and fails on empty/too-short transcript content. Source was read only.
- `export-session/evals/evals.json` defines three scenario-style expected outputs. The eval file is evidence of an intended evaluation surface only; no eval was run.
- `uxpsych-design/SKILL.md` is a UI/UX conversion-psychology checklist with explicit build/review rules and guardrails against fabricated reviews, urgency, numbers, or losses. `references/playbook.md` provides the expanded rationale/examples and was inspected through the latest skill update.

**Inference**

- The collection is heterogeneous but has stronger-than-average operational boundary documentation: mutation is explicit in `drive-organizer`, session export distinguishes finished vs unfinished work, and `uxpsych-design` explicitly constrains persuasion techniques.
- The most material source-level risk is `drive-organizer`'s opt-out approval default (`TRUE`), because the final commit phase can move files or mutate Drive state. The human review step reduces risk but does not make the default conservative.

**Not verified**

- Google Drive OAuth/API behavior, Gemini/model calls, filesystem moves, session export execution, install scripts, evals, or any runtime behavior.

### 3. `wujixialan/agentskills`

**Verified**

- Public repository id `1194302478`, default branch `main`; exact star observation: `0`.
- Latest repository commit is `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4`.
- The same commit SHA exists in `agentskills/agentskills`; therefore the entire Git tree at that snapshot is content-identical to the official Agent Skills repository at that commit.
- Actual `README.md` states that the repository contains the specification, documentation, and reference SDK and points to external example skills rather than presenting a local domain-skill catalog.

**Content-level correction**

- Treat as an official specification/reference snapshot, not as an independent skill collection. No duplicate local skill reports are emitted.

### 4. `ILyes-SS/agentskills`

**Verified**

- Public repository id `1194703771`, default branch `main`; exact star observation: `0`.
- Latest repository commit is the same `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4` official Agent Skills commit.
- `README.md` has the same blob SHA (`98534c18d286e0a651f74028666b1ae97db687ed`) and describes specification/documentation/reference-SDK content.

**Content-level correction**

- Exact official snapshot; no independent skill reports.

### 5. `Jahid11978/agentskills`

**Verified**

- Public repository id `1194380358`, default branch `main`; exact star observation: `1`.
- Latest commit is `217be548739f21d6008915c29aefe320ea1a90af`, which is also the exact current commit in `agentskills/agentskills` inspected in this review. The commit updates `docs/specification.mdx` to clarify `metadata` as string-key/string-value mapping.
- Current `README.md` defines the Agent Skills open format, progressive disclosure model, skill directory structure, and links to external example skills.
- `skills-ref/README.md` was directly read. It describes a demonstration/reference Python library and CLI for validation, property reading, and generating the available-skills prompt; it explicitly says it is not intended for production.

**Content-level correction**

- This is a specification/reference mirror snapshot, not a distinct domain-skill catalog. No duplicate skill reports are emitted.

### 6. `zurbrick/ooda-skill`

**Verified**

- Public repository id `1194834757`, default branch `main`; exact star observation: `0`.
- Single commit `7010b0a7d38494a659549c8de6340ab6356dbfb5` contains exactly three content files: `SKILL.md`, `references/decision-types.md`, and `references/loop-template.md`. No README, scripts, or evals are present.
- `SKILL.md` defines a compact Observe → Orient → Decide → Act → re-loop decision workflow for uncertainty, explicitly excluding trivial, execution-heavy, under-researched, and high-blast-radius cases.
- `decision-types.md` separates reversible, costly-but-reversible, and irreversible/high-blast-radius decisions and requires escalation rather than relying on fast-loop OODA alone for the last category.
- `loop-template.md` provides a reusable output contract including verified facts, unknowns, constraints, reversibility, trade-offs, owner, timing, feedback signal, and reassessment trigger.

**Inference**

- The useful design pattern is the explicit escalation boundary: the skill is intentionally narrow rather than presenting OODA as a universal decision mechanism.

**Not verified**

- No runtime or outcome validation exists in the repository and none was performed.

### 7. `nijaru/agentskills`

**Verified**

- Public repository id `1193497345`, default branch `main`; exact star observation: `1`.
- The repository is a small Go implementation of the Agent Skills format, not a local catalog of production skills.
- `README.md` documents `Load`, `Registry`, `NormalizeName`, `ValidateName`, progressive disclosure, Unicode/NFKC handling, accepted frontmatter fields, and `go test ./...` / `go vet ./...` development commands.
- `skill.go` was directly inspected. It parses standard skill metadata/body, validates required fields and limits, preserves YAML metadata types, rejects unknown frontmatter fields, and exposes a one-line summary.
- `skill_test.go` contains synthetic skill fixtures covering loader behavior, scalar/list `allowed-tools`, internal metadata, registration/deregistration, name validation, Unicode/NFKC behavior, length boundaries, unknown fields, and malformed frontmatter.

**Content-level correction**

- Classify as Go SDK/reference tooling with **0** repository-scoped production skill reports.

**Not verified**

- Tests and vet were not executed; source/test presence is not recorded as a pass.

### 8. `dev-juha/agentskills`

**Verified**

- Public repository id `1193730251`, default branch `main`; exact star observation: `0`.
- Latest commit is `b5ce2a438123f9f9c9b167c5af297c048f15395b`, which is the exact official `agentskills/agentskills` commit that updates the quickstart random-number example.
- Actual `README.md` is the official specification/documentation/reference-SDK README snapshot.

**Content-level correction**

- Exact official reference snapshot; no independent skill reports.

### 9. `luizotavioautomacao/agentskills`

**Verified**

- Public repository id `1194009493`, default branch `main`; exact star observation: `0`.
- Latest commit is `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4`, the same official Agent Skills snapshot verified above.
- `README.md` has blob SHA `98534c18d286e0a651f74028666b1ae97db687ed` and describes specification/documentation/reference SDK rather than independent skills.

**Content-level correction**

- Exact official reference snapshot; no independent skill reports.

### 10. `netover/agentskills`

**Verified**

- Public repository id `1193622038`, default branch `main`; exact star observation: `0`.
- Latest commit is `b5ce2a438123f9f9c9b167c5af297c048f15395b`, identical to the official Agent Skills snapshot verified above.
- `README.md` has the same official blob SHA and describes specification/documentation/reference SDK content.

**Content-level correction**

- Exact official reference snapshot; no independent skill reports.

## Cross-batch findings

1. **Metadata naming remains a weak qualifier.** Six of the ten indexed `agentskills` identities in this batch are exact snapshots/mirrors of the official specification repository, not independent skill libraries.
2. **Git commit identity is a strong dedupe signal.** Matching a fork/mirror HEAD commit SHA to the official repository proves identical Git tree content for that snapshot and avoids generating duplicate skill reports.
3. **A repository named AgentSkills may contain no skill package at all.** `sampath1310/AgentSkills` contains one interview prompt and no Agent Skills structure.
4. **Tooling should not be counted as production skills.** `nijaru/agentskills` has meaningful loader/validator/test code but no repository-scoped production skill definition.
5. **Source-level safety boundaries vary materially.** `zurbrick/ooda-skill` explicitly escalates irreversible/high-impact decisions, while `ctvida/drive-organizer` uses an opt-out approval default before a mutation-capable commit phase; these are materially different operating contracts.

## Validation boundary

`structure-reviewed` means repository identity and exact star observation were checked, actual repository content was read, local skill/equivalent definitions were directly inspected when present, scripts/references/evals were inspected when surfaced and material, and duplicate/reference-only candidates were content-corrected instead of promoted from metadata.

It does **not** mean any third-party runtime, installer, API, model, filesystem mutation, Google Drive operation, build, test suite, or eval runner succeeded. Runtime validation remains `not_executed`.
