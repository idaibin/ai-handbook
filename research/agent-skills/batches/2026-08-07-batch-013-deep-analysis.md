# GitHub Agent Skills Deep Analysis — Batch 013

## Run result

- Batch: `2026-08-07-batch-013`
- Repository completions: **10**
- Individual skill reports: **266 repository-scoped identities**
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Before: **120 completed repositories / 1392 skill reports**
- After: **130 completed repositories / 1658 skill reports**
- Index snapshot: **2502 unique / 2088 eligible / 414 held**
- Eligible remaining estimate: **1958**
- Completion rule: no repository was completed from metadata alone. README plus actual skill/support content was inspected for every repository.
- Large collections: current repository-maintained catalogs enumerate all identities; representative `SKILL.md` bodies and available scripts/references/evals were directly read.
- Runtime validation: `not_executed`; third-party commands/tests/evals were inspected, not run.
- Stars are mutable rounded GitHub UI observations from this run.
- Individual records:
  - [`2026-08-07-batch-013-skill-reports-01.md`](2026-08-07-batch-013-skill-reports-01.md)
  - [`2026-08-07-batch-013-skill-reports-02.md`](2026-08-07-batch-013-skill-reports-02.md)
  - [`2026-08-07-batch-013-skill-reports-03.md`](2026-08-07-batch-013-skill-reports-03.md).

## Repository summary

| Repository | GitHub ID | Branch | Stars | Skill reports | Direct evidence |
|---|---:|---|---:|---:|---|
| `AvdLee/Swift-Concurrency-Agent-Skill` | `1129568168` | `main` | 1.6k | 1 | README + swift-concurrency/SKILL.md + references/actors.md + .github/scripts/sync-readme.js |
| `ast-grep/agent-skill` | `1097687797` | `main` | 829 | 2 | README + ast-grep/skills/{ast-grep,outline}/SKILL.md + rule_reference.md |
| `AvdLee/Xcode-Build-Optimization-Agent-Skill` | `1180781840` | `main` | 1.2k | 6 | README + xcode-build-orchestrator/SKILL.md + scripts/benchmark_builds.py |
| `Akxan/ppt-agent-skill` | `1187538031` | `main` | 121 | 1 | README + root SKILL.md + scripts/smoke_skill.py + persisted smoke report |
| `MicrosoftDocs/Agent-Skills` | `1142983380` | `main` | 686 | 194 | README + docs/CATALOG.md + representative skills/azure-functions/SKILL.md |
| `openclaw/agent-skills` | `1246722622` | `main` | 1.0k | 8 | README + skills/autoreview/SKILL.md + scripts/install-skills |
| `sunbigfly/ppt-agent-skills` | `1187464970` | `main` | 873 | 1 | README + root SKILL.md + scripts/smoke_skill.py + references/cli-cheatsheet.md |
| `dbt-labs/dbt-agent-skills` | `1130059064` | `main` | 651 | 12 | README + using-dbt-for-analytics-engineering/SKILL.md + evals/README.md |
| `elastic/agent-skills` | `1174313682` | `main` | 546 | 35 | README + elasticsearch-esql/SKILL.md + scripts/esql.js + esql-version-history.md |
| `Kotlin/kotlin-agent-skills` | `1180940534` | `main` | 987 | 6 | README + CATEGORIES + kotlin-backend-jpa-entity-mapping/SKILL.md + validate-skills workflow |

## Repository analyses

### 1. `AvdLee/Swift-Concurrency-Agent-Skill`

Single-domain Swift concurrency skill with a compact router in SKILL.md and deeper topic references. Strong guardrails distinguish isolation, Sendable, actor use, migration-sensitive project settings, and verification. README structure is synchronized by a repository helper; no dedicated model-behavior eval harness was observed in the inspected surfaces.

Direct support evidence: `references/actors.md` documents actor isolation and MainActor decisions; `.github/scripts/sync-readme.js` regenerates the README structure block from current reference files.

### 2. `ast-grep/agent-skill`

Two complementary skills: one translates structural-search intent into tested ast-grep rules; the other provides a low-cost codebase outline before full reads. The reference layer documents atomic, relational, and composite rules. No repo-local execution harness was observed; runtime use depends on the ast-grep CLI.

Both current skill bodies were directly read. `ast-grep` uses a test-before-search workflow; `ast-grep-outline` explicitly limits itself to syntax structure. `rule_reference.md` documents atomic, relational, and composite rule semantics.

### 3. `AvdLee/Xcode-Build-Optimization-Agent-Skill`

Six-skill orchestration package. The orchestrator separates recommend-only analysis from approved execution, makes wall-clock wait time the primary metric, requires baseline/re-benchmark evidence, and routes to specialist skills. The benchmark script implements repeatable clean/incremental/cached-clean measurements and timing-summary artifacts.

The orchestrator defines a recommend-only analysis phase, explicit approval gate, implementation handoff, then re-benchmark. `scripts/benchmark_builds.py` records repeated clean/incremental/cached-clean measurements, timing summaries and raw logs.

### 4. `Akxan/ppt-agent-skill`

Single presentation-generation skill with a six-step research/planning/design pipeline, structured artifacts, 26 style presets, chart/layout references, and HTML→SVG→PPTX tooling. The repository contains an end-to-end smoke harness and persisted smoke results; this batch inspected but did not execute them.

The root skill defines a six-step research→planning→design pipeline. `scripts/smoke_skill.py` exercises prompt rendering, planning contracts, visual QA, resource loading and prompt harnesses. A persisted smoke report records 6 pass / 0 fail / 0 warning; it was not rerun here.

### 5. `MicrosoftDocs/Agent-Skills`

Large generated Azure skill catalog based on Microsoft Learn. Current catalog enumeration contains 194 distinct skill identities across 19 categories. Representative skill metadata records generator and generation date, combines local category indexes with network retrieval of Microsoft docs, and tells agents to refresh when generated content becomes stale.

`docs/CATALOG.md` enumerates **194 distinct skill identities across 19 categories**. The README says `193+`, which is compatible with the current count. `azure-functions/SKILL.md` records generator `docs2skills/1.0.0`, generated date `2026-07-26`, category routing, network documentation retrieval, and freshness guidance.

### 6. `openclaw/agent-skills`

Canonical shared-workflow collection for OpenClaw projects. Skills are package-local and reusable across agent runtimes. Autoreview defines evidence-preserving closeout review and scope control; the installer deterministically discovers SKILL.md packages and supports copy/symlink/dry-run modes. README documents validator/test surfaces.

`autoreview/SKILL.md` defines source-aware closeout review, evidence verification, scope control and explicit boundaries versus behavior validation. `scripts/install-skills` deterministically discovers `SKILL.md` packages and supports symlink/copy/dry-run/force; README lists validator/test commands.

### 7. `sunbigfly/ppt-agent-skills`

Single presentation skill implemented as a strict multi-stage state machine with explicit gates, subagent isolation, prompt harnesses, planning contracts, visual QA, and dual PPTX export. The CLI cheatsheet is a step-scoped command contract. Its smoke harness blob matches Akxan/ppt-agent-skill, proving shared implementation at that file without inferring repository ownership.

The root skill is a strict gate/state-machine orchestrator with subagent-only production boundaries, prompt harnesses, wait points and rollback rules. `references/cli-cheatsheet.md` centralizes stage commands. Its `scripts/smoke_skill.py` blob SHA matches Akxan's (`39645ccd7cd1f5e4dfdbaf2ffd8b6ce1eb9817a6`), proving shared file content only.

### 8. `dbt-labs/dbt-agent-skills`

Twelve dbt skills split between analytics-engineering and migration groups. The representative skill enforces model/version boundaries, existing YAML/context reads, dbt show validation, untrusted-data handling, and cost controls. The repository includes a real A/B skill-evaluation CLI with scenario isolation, tool constraints, transcript capture, grading, and comparison reporting.

The directly read analytics-engineering skill routes breaking changes to dbt Mesh, requires YAML/data inspection and `dbt show` validation, treats query/external content as untrusted, and includes cost controls. `evals/README.md` documents a real A/B evaluation CLI with isolated scenarios, tool restrictions, transcripts, grading and reports.

### 9. `elastic/agent-skills`

Official Elastic technical-preview collection with 35 current skills across Cloud, Elasticsearch, Kibana, Observability, and Security. The directly read ES|QL package couples a version-aware SKILL.md, executable client helper, schema discovery, and feature-availability reference. README explicitly warns that skills are still evolving and recommends tight privileges/non-production evaluation.

The current README catalog has **35** skills: 5 Cloud, 7 Elasticsearch, 8 Kibana, 11 Observability, 4 Security. The directly read ES|QL package couples version-aware instructions, `scripts/esql.js`, schema discovery and `esql-version-history.md`. README marks the collection Technical Preview and recommends least privilege/non-production evaluation.

### 10. `Kotlin/kotlin-agent-skills`

Six current Kotlin skills under backend/tooling categories. The directly read JPA skill gives Kotlin-specific ORM guardrails and correctness constraints. CI validates naming against CATEGORIES and runs an external skill validator for changed SKILL.md directories.

Current categories are `backend` and `tooling`; six skill identities were found. The directly read JPA skill contains Kotlin-specific entity/equality/fetch-plan guardrails. `.github/workflows/validate-skills.yml` enforces `kotlin-<category>-<functional-name>` against `CATEGORIES` and runs a skill validator.

## Cross-repository findings

1. `dbt-labs/dbt-agent-skills` has the strongest dedicated behavior-evaluation surface in this batch.
2. The Xcode package makes benchmark → approval → re-benchmark evidence part of the skill contract.
3. MicrosoftDocs demonstrates a reusable freshness contract for generated documentation skills: generator metadata + generated date + upstream retrieval path.
4. Kotlin, OpenClaw, and both PPT repositories have structural validation/smoke mechanisms, but those mechanisms are not equivalent to model-behavior proof.
5. The two PPT repositories share at least one identical helper blob; no repository lineage/ownership conclusion is inferred from that alone.

## Verification boundaries

- Verified: repository identity/default branch via GitHub; displayed stars from live GitHub UI observation; actual README/skill/support files through GitHub.
- Verified arithmetic: `1 + 2 + 6 + 1 + 194 + 8 + 1 + 12 + 35 + 6 = 266` repository-scoped reports.
- Not executed: package installs, external APIs, Xcode builds, dbt commands, Elasticsearch queries, PPT rendering, CI workflows, smoke/eval suites.
- Inventory-backed skill records are labeled as such in the companion report and are not represented as direct body reads.
- `ppt-agent` appears in two repositories; canonical identity is repository + skill, so both are counted.
