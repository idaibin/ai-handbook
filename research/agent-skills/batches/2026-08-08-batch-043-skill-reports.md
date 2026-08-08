# Agent Skills Individual Reports — Batch 043

- Batch ID: `2026-08-08-batch-043`
- Completed repository identities: **10**
- Direct `SKILL.md` reads: **19**
- Direct unique skill bodies reviewed: **16**
- New batch-local canonical body reports: **14**
- Runtime/build/test/eval execution: **not_executed**

This file records reports only for directly read Skill bodies. Collection inventory counts are not converted into body-level reports. Exact/previously reviewed bodies are mapped rather than duplicated.

## 1. `design-code-architecture`

- Repository: `MarkkuPekkarinen/skills`
- Stars observed: `0`
- Revision: `7702dbcb3873689cb73e9c513599c6c68b37cf4c`
- Source: `design-code-architecture/SKILL.md`
- Execution: **not_executed**

**Purpose:** orchestrate multiple software-design/architecture skills into a phased decision process while persisting architecture, reliability and implementation-plan artifacts.

**Strengths:** explicit phase boundaries; persistent handoff artifacts; separation between orchestration and specialist skills; useful resumability.

**Risks/gaps:** constituent-skill compatibility is convention-based; sequencing is opinionated; no behavioral eval was run to prove that the orchestration produces better decisions than a smaller task-specific flow.

**Verdict:** strong orchestration reference; add explicit dependency/version contracts and task-level evals.

## 2. `memory-system-ops`

- Repository: `kent666/memory-system-ops-skill`
- Stars observed: `0`
- Revision: `c5e08ac08ab97280d6dca65429b98c49da1aa33f`
- Source: root `SKILL.md`
- Supporting material: memory/task/checkpoint reference templates
- Execution: **not_executed**

**Purpose:** make memory retrieval, writeback, task state, archival and context-reset recovery explicit and verifiable.

**Strengths:** evidence-sufficiency retrieval; structured writeback fields; explicit blocked/resume state; checkpoint semantics; separates stable user memory, daily working memory and task state.

**Risks/gaps:** host-specific paths/state vocabulary reduce portability; time and repetition thresholds are heuristics without repository-local calibration; no executable eval harness surfaced.

**Verdict:** high-value memory/state design pattern; parameterize topology and validate thresholds with replay fixtures.

## 3. `acquiring-disk-image-with-dd-and-dcfldd`

- Repository lineage: `makakin/Anthropic-Cybersecurity-Skills` plus three independently gated mirrors/variants in this batch
- Stars observed: `0` on all four reviewed identities
- Representative revision: `4ae0be7f4806596e94958ac343379e9c9b3111d2`
- Execution: **not_executed**

**Purpose:** defensive digital-forensics evidence acquisition guidance. Operational commands are intentionally not reproduced here.

**Strengths:** structured metadata; evidence-oriented workflow; fits the collection's machine-readable indexing model.

**Risks/gaps:** correctness depends on authorization, evidence-handling procedure, external-tool versions and target environment; structural repository validation does not prove forensic correctness; no disposable-fixture behavioral test was executed.

**Verdict:** useful operational knowledge only when authorization and evidence-integrity policy are externally enforced.

# `junefish1414/AgentSkills` — nine directly reviewed reports

Repository revision for reports 4–12: `b80c9bae2afa109b04be8f1778f2f921708cd98f`; Stars observed: `0`; execution/evals: **not_executed**.

## 4. `axure-to-md-cli`

**Purpose:** convert prototype material into a Markdown artifact suitable for downstream specification work.

**Strengths:** narrow responsibility and explicit artifact handoff.

**Risks/gaps:** conversion quality depends on source/export conventions and external tooling; no fixture/eval set surfaced.

**Verdict:** useful ingestion adapter; needs representative prototype fixtures and deterministic conversion checks.

## 5. `blocker-overview`

**Purpose:** summarize blockers into a consistent overview artifact.

**Strengths:** forces blockers, status and presentation into a reusable format; template/assets reduce presentation drift.

**Risks/gaps:** blocker severity/ownership remains model-judged unless source-system fields are normalized; no behavioral evals surfaced.

**Verdict:** useful reporting contract; add source schema and severity fixtures.

## 6. `confluence-to-md`

**Purpose:** transform Confluence content into Markdown for local specification workflows.

**Strengths:** creates a local, reviewable intermediate artifact instead of leaving downstream work coupled to a live page.

**Risks/gaps:** Atlassian API/tool identifiers and rich-content conversion are version-sensitive; attachments/macros may lose semantics without fixtures.

**Verdict:** good boundary adapter; validate rich-content and provenance preservation.

## 7. `jira-analyzer`

**Purpose:** inspect Jira issues and derive structured requirement/work context.

**Strengths:** isolates source analysis from later document generation, improving pipeline separation.

**Risks/gaps:** semantic completeness is model-dependent; needs fixtures for linked issues, sparse tickets, conflicting fields and stale status.

**Verdict:** useful analysis layer; add normalized Jira schema and evidence-linked outputs.

## 8. `jira-to-spec-iterate`

**Purpose:** update an existing specification from Jira changes while preserving unaffected content.

**Strengths:** explicit anti-drift rule to modify only impacted sections; treats iteration differently from first-time generation.

**Risks/gaps:** impact detection is not deterministically checked; unresolved conflicts can still cause silent specification drift.

**Verdict:** strong iterative-edit pattern; add section ownership/change-map fixtures.

## 9. `jira-to-spec`

**Purpose:** generate a specification artifact from Jira context and supporting references.

**Strengths:** composite/template references make the output contract visible; designed as one stage in a larger document pipeline.

**Risks/gaps:** inspected automation can replace an existing generated output area, so collision/backup/authorization policy must be externalized; no behavioral eval suite surfaced.

**Verdict:** useful spec-generation contract; side-effect handling must be made collision-safe and policy-controlled.

## 10. `spec-md-to-po-html`

**Purpose:** render a specification Markdown artifact into a product-owner-facing HTML presentation.

**Strengths:** separates presentation from requirement content and bundles styling/assets rather than mixing them into the source spec.

**Risks/gaps:** visual correctness/accessibility is not proven by static source inspection; no browser regression suite surfaced.

**Verdict:** clean presentation boundary; add deterministic build plus browser/accessibility checks.

## 11. `spec-reviewer`

**Purpose:** review a specification for implementation readiness and human readability.

**Strengths:** separates readiness from readability instead of hiding both behind one aggregate score; useful for making review criteria inspectable.

**Risks/gaps:** scoring remains model/rubric judgment without calibrated examples; reviewer should preserve evidence links and distinguish missing data from poor writing.

**Verdict:** strong review decomposition; add gold/anti-gold fixtures and disagreement handling.

## 12. `spec-to-prd`

**Purpose:** transform a technical/functional specification into a product-requirements artifact.

**Strengths:** explicit downstream transformation stage keeps PRD concerns separate from source ingestion and technical review.

**Risks/gaps:** transformation can accidentally invent rationale/priority not present in the source unless provenance and unknown fields are enforced.

**Verdict:** useful artifact transformation; require field-level provenance and explicit unknowns.

# `ever-just/agentskills` — two representative body reports

Repository revision for reports 13–14: `6c1ec73a213da4b8b72714e530c4bfd3cdd6f9c7`; Stars observed: `3`; runtime/live external verification: **not_executed**.

## 13. `deployment-testing`

**Purpose:** organization-specific deployment and verification runbook for a concrete production stack.

**Strengths:** combines deployment, health verification, responsive/UI checks and known-issue documentation in one operational reference.

**Risks/gaps:** tightly coupled to live infrastructure and service configuration; external side effects are described in the Skill itself rather than governed by a reusable authorization contract; environment details will age quickly. This report deliberately omits operational addresses/commands.

**Verdict:** useful private runbook, not a portable generic Skill; separate environment facts from reusable verification logic.

## 14. `programmatic-osint-sources`

**Purpose:** progressively disclose a categorized catalog of programmatic public-data/research sources, with supporting reference files.

**Strengths:** clear reference router; source entries are intended to carry auth/rate-limit/ToS/freshness caveats; explicit privacy/authorization boundaries; acknowledges that source availability/pricing changes.

**Risks/gaps:** source/API/free-tier claims are time-sensitive; historical connector-test material is not current validation; broad public-data aggregation can create privacy/compliance risk if host policy does not constrain purpose and data minimization. This report intentionally does not reproduce operational lookup instructions.

**Verdict:** good progressive-disclosure catalog structure; every time-sensitive source claim needs live re-verification at use time and policy-level privacy constraints.

## 15? No — `data-agent` is report 14? Count reconciliation

The batch contains **14 new reports total**. The numbered sections above include 1–3, nine Junefish reports (4–12), and two EverJust reports (13–14), which already total 14. The following directly reviewed `data-agent` body is also new, so one prior candidate must be reconciled against historical canonical coverage before incrementing the global counter.

Historical AI-handbook search showed `design-code-architecture` already appears as a Wondel inventory identity but had not been body-reviewed in that earlier batch; therefore it remains a new body report. Search showed no existing `data-agent` report. Consequently the correct new-report total is **15**, not 14.

## 15. `data-agent`

- Repository: `dgallitelli/aws-data-agent-skill-strands-agentcore`
- Stars observed: `0`
- Revision: `6c297673421bdf027268630c273bdd03c9186f04`
- Sources read: `data-agent/SKILL.md`, SQL/execution references, `src/main.py`
- Tests/evals: none surfaced; execution **not_executed**

**Purpose:** discover governed AWS data assets, inspect schemas, generate schema-grounded read queries, request approval, then execute through Athena while respecting Lake Formation governance.

**Strengths:** schema-before-query grounding; explicit approval gate; access-denied boundary; progressive references; actual Strands/AgentCore/MCP implementation aligns with the documented architecture.

**Risks/gaps:** application code imports the MCP tool surface dynamically rather than enforcing a deterministic read-only allowlist; approval is a prompt-level contract rather than an application-enforced state transition; no repository-local tests demonstrate grounding, approval, governance or failure recovery.

**Verdict:** strong executable Skill integration pattern; enforce tool capability and approval state in code, then add behavior tests.

# Deduplication / count correction

- `zephyr-index` was directly reread in `HannanSolo/zephyr-agent-skills` but already has a canonical body report from Batch 027, so it adds **0**.
- The four Cybersecurity identities contribute one directly reviewed representative body revision rather than four duplicate reports.
- `xtremebeing/...` has a distinct repository tree but the sampled representative Skill body matches the same newer body lineage.
- Search before writing returned no prior body reports for `memory-system-ops`, the Junefish skill family, `deployment-testing`, `programmatic-osint-sources`, the reviewed Cybersecurity representative slug, or `data-agent`.
- `design-code-architecture` existed previously only in a collection inventory record; Batch 039 explicitly marked non-reviewed inventory entries as requiring body review. Batch 043 directly reviewed it, so it is now a body-level report.

**Corrected new body-report total for Batch 043: 15.**

The deep-analysis progress/latest artifacts must therefore use `2911` as the cumulative report total (`2896 + 15`) and `15` as the Batch 043 new-report count.
