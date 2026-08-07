# Agent Skills individual reports — Batch 018

- Observed at: 2026-08-07
- Batch: `2026-08-07-batch-018`
- Repository-scoped reports: **53**
- Validation state: `structure-reviewed`
- Runtime validation: `not_executed`
- Counting rule: only repository-scoped current skill identities are counted. Deprecated/migrated external repositories, README examples, and dependency-owned skills are not reassigned to the source repository.

Evidence labels:

- `direct-body-reviewed`: the current `SKILL.md` or equivalent body was directly read in this run.
- `inventory-verified`: identity and purpose were verified from a repository-maintained complete inventory; representative bodies and support surfaces were directly read.

## `wtsi-hgi/agentskills` — 27 reports

The maintained `docs/skills.md` inventory maps directly to `skills/` and defines a layered system: universal conduct, shared implementation/testing principles, workflow/orchestration skills, and stack-specific convention/implementor/reviewer triplets.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `agent-conduct` | direct-body-reviewed | Repository/workspace mutation boundaries, git safety, no fabricated blocker workarounds, and explicit honesty about unavailable capabilities. |
| `implementation-principles` | direct-body-reviewed | Smallest coherent change, semantic reuse before new abstractions, TDD, and explicit quality-gate reporting. |
| `testing-principles` | direct-body-reviewed | Behaviour-focused tests, anti-flakiness rules, and rejection of tests coupled only to implementation details. |
| `subagents` | direct-body-reviewed | Cross-harness orchestration contract, writable-worker requirement, bounded calls, explicit blocker propagation, and worker cleanup. |
| `bugfix` | inventory-verified | Orchestrates TDD bug fixing and review rather than embedding stack-specific implementation logic. |
| `frontend-design` | inventory-verified | Frontend interface design capability kept separate from implementation/review workflows. |
| `orchestrator` | direct-body-reviewed | Phase-plan execution delegates implementation/review, marks progress only after success, and requires fresh review loops. |
| `pr-reviewer` | inventory-verified | Branch-vs-base review workflow with implementor-assisted fixes. |
| `pr-resolver` | inventory-verified | PR comment triage and resolution workflow separating required changes from questions/suggestions. |
| `spec-writer` | inventory-verified | Orchestrates spec creation and review through specialized subskills. |
| `spec-author` | inventory-verified | Authors feature specs with user stories and acceptance tests. |
| `spec-reviewer` | inventory-verified | Checks spec completeness against the feature description and returns a bounded pass/fail result. |
| `spec-proofreader` | inventory-verified | Text-quality review isolated from feature-domain correctness. |
| `phase-creator` | inventory-verified | Converts specification implementation order into phase-plan artifacts. |
| `phase-reviewer` | inventory-verified | Reviews phase plans against the source spec and fixes plan text issues. |
| `go-conventions` | inventory-verified | Centralizes Go project/test conventions for implementor and reviewer skills. |
| `go-implementor` | inventory-verified | Go TDD implementation workflow layered over shared principles. |
| `go-reviewer` | inventory-verified | Go implementation review against acceptance tests and shared principles. |
| `nextflow-conventions` | inventory-verified | Centralizes Nextflow DSL2 project, test, container, and command conventions. |
| `nextflow-implementor` | inventory-verified | Nextflow TDD workflow layered over shared conventions. |
| `nextflow-reviewer` | inventory-verified | Nextflow implementation review against spec acceptance tests. |
| `nextjs-fastapi-conventions` | inventory-verified | Shared full-stack architecture/testing/styling conventions for Next.js + FastAPI. |
| `nextjs-fastapi-implementor` | inventory-verified | Full-stack TDD workflow reusing shared principles and stack conventions. |
| `nextjs-fastapi-reviewer` | inventory-verified | Full-stack implementation review against acceptance tests and shared principles. |
| `python-conventions` | inventory-verified | Modern Python project, typing, linting, testing, and command conventions. |
| `python-implementor` | inventory-verified | Python TDD workflow layered over shared principles and conventions. |
| `python-reviewer` | inventory-verified | Python implementation review against acceptance tests and shared principles. |

## `omaclaren/agent-skills-public` — 5 reports

| Skill | Evidence | Finding |
| --- | --- | --- |
| `guide-mode` | direct-body-reviewed | Explicit invocation only; keeps read-only exploration proactive while requiring sign-off for mutations and preserving user control over pacing. |
| `critique-skill` | direct-body-reviewed | Read-only writing/code critique with exact-source markers; explicitly treats analyzed content as data rather than instructions. |
| `annotated-reply-skill` | direct-body-reviewed | Small clipboard handoff workflow for user annotation; deliberately explicit-only and output-minimal. |
| `preview-browser-skill` | direct-body-reviewed | Renders prior assistant/file Markdown through local tools and temp files; includes fallback validation when transcript extraction is uncertain. |
| `iir-identifiability` | direct-body-reviewed | Evidence-conscious scientific workflow that distinguishes local null space from invariant null space, requires differentiability preflight, and avoids overstating reparameterisation claims. |

## `ok406lhq/skills-guardian` — 1 report

| Skill | Evidence | Finding |
| --- | --- | --- |
| `skills-guardian` | direct-body-reviewed | Static heuristic scanner with JSON/text reports. Its own documentation correctly states that results are signals, not a safety guarantee. The Python implementation uses lexical regex checks and additive scoring, so false positives/negatives remain an explicit limitation. |

## `timeplus-io/AgentSkills` — 6 reports

The README declares six self-contained top-level skills using a conventional `SKILL.md` + optional `references/` / `scripts/` layout.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `timeplus-sql-guide` | direct-body-reviewed | Deep streaming-SQL guide with explicit environment-based credentials, streaming-vs-historical semantics, operational error cases, and progressive reference files. |
| `timeplus-app-builder` | inventory-verified | Timeplus application packaging/install workflow; kept as a separate product-building skill rather than mixed into the SQL guide. |
| `timeplus-design` | inventory-verified | UI/design capability isolated from data/query operations. |
| `pulsebot-app-builder` | inventory-verified | Real-time single-file app construction for Pulsebot/Proton use cases. |
| `searxng-web-search` | direct-body-reviewed | Self-hosted search integration with structured JSON output, timeout/error handling, environment configuration, and a concrete Python implementation. |
| `cisco-asa-syslog` | inventory-verified | Domain-specific log interpretation capability separated from general search/data skills. |

## `avoidthekitchen/agent-agnostic-skills` — 4 reports

| Skill | Evidence | Finding |
| --- | --- | --- |
| `bootstrap-checks-from-prs` | direct-body-reviewed | Mines merged-PR evidence into candidate review checks, writes auditable artifacts, uses collision-safe drafts, and recommends holdout calibration before adoption. Its candidate extractor combines frequency, risk, detectability, scope, and evidence links rather than treating raw comment frequency as truth. |
| `rpi-research` | direct-body-reviewed | Evidence-backed research workflow with parallel tracks, conflict reconciliation, file/line citations, explicit inference labels, and a durable research memo. |
| `rpi-plan` | direct-body-reviewed | Converts research/requirements into phased, file-level, implementation-ready checklists with measurable verification and explicit out-of-scope items. |
| `rpi-implement-plan` | direct-body-reviewed | Executes approved plans phase-by-phase, updates checkboxes only after work/verification, and surfaces plan-vs-code mismatches instead of mechanically following stale plans. |

## `yashasvigirdhar/skills` — 4 reports

The README declares four current skills, each with `SKILL.md`, `SETUP.md`, and optional references. `feature-inventory` was directly reviewed; the other identities are inventory-verified in this batch.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `feature-inventory` | direct-body-reviewed | Two-mode bootstrap/drift-sync workflow for a YAML feature inventory. Bootstrap has a single human confirmation gate and stops in non-interactive contexts; drift-sync compares declared product surfaces against code and logs each run. |
| `nightly-qa` | inventory-verified | Human-like browser E2E testing workflow with recurring-run intent; runtime behavior was not exercised here. |
| `competitor-backlink-audit` | inventory-verified | Browser-based competitive backlink research workflow; author usage claims were not independently runtime-verified. |
| `competitor-pricing-tracker` | inventory-verified | Structured competitor pricing tracking with staleness/update workflow; external-site behavior was not executed here. |

## `postnitro/postnitro-carousel-skill` — 1 report

| Skill | Evidence | Finding |
| --- | --- | --- |
| `postnitro-carousel` | direct-body-reviewed | External SaaS integration with a clear asynchronous initiate/status/output lifecycle, environment-held credentials, strict slide schema, examples, and a dedicated API reference. Correctness still depends on the live external service and account state, which were not tested. |

## `maxamillion/agentskill-rhoai-cve-analysis` — 1 report

| Skill | Evidence | Finding |
| --- | --- | --- |
| `rhoai-cve-analysis` | direct-body-reviewed | Defensive vulnerability-analysis pipeline separates source collection, deterministic pre-triage, deferred review, remediation generation, and reporting. A key limitation is that later fallback tiers intentionally trade precision for completion, so automatic classifications require validation before being treated as product-security truth. |

## `Digidai/website2markdown-skills` — 1 report

| Skill | Evidence | Finding |
| --- | --- | --- |
| `website2markdown` | direct-body-reviewed | External web-to-Markdown service wrapper with progressive references for batch/extraction/crawl features. The repository documents response/error modes and context-size controls, but service availability, access-policy compatibility, and platform adapter behavior were not runtime-verified here. |

## `zht043/AgentSkills` — 3 current reports

The repository README explicitly marks the monorepo **Deprecated** and says maintained suites have moved to independent repositories. Only the three README-listed not-yet-migrated local skills are counted here. The root `SKILL.md` is treated as repository-governance/meta guidance rather than an additional installable skill identity.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `markdown-mermaid-illustrator` | direct-body-reviewed | Canonical Mermaid illustration workflow with explicit chart-type routing, rendering limitations, theme/layout rules, and user confirmation for ambiguous visual choices. |
| `doc-illustrator` | direct-body-reviewed | Legacy Mermaid illustration workflow; README explicitly recommends the newer `markdown-mermaid-illustrator`, so this identity should not be treated as the preferred current implementation. |
| `export-history` | direct-body-reviewed | Local Claude Code history export capability that reads session files and produces a standalone HTML viewer; handling of potentially sensitive conversation data is a deployment/privacy consideration. |

## Count reconciliation

```text
wtsi-hgi/agentskills                    27
omaclaren/agent-skills-public            5
ok406lhq/skills-guardian                 1
timeplus-io/AgentSkills                  6
avoidthekitchen/agent-agnostic-skills    4
yashasvigirdhar/skills                   4
postnitro/postnitro-carousel-skill       1
maxamillion/agentskill-rhoai-cve-analysis 1
Digidai/website2markdown-skills          1
zht043/AgentSkills                       3
------------------------------------------
total                                   53
```

## Validation boundary

This file records source/content review, not runtime verification. No third-party installer, network service workflow, browser automation, application server, build, test suite, evaluation runner, cloud API, CVE-analysis pipeline, external search service, or repository script was executed. Direct body review means the source was read, not that its claimed behavior was reproduced.