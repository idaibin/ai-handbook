# Agent Skills Individual Reports — Batch 043

- Batch ID: `2026-08-08-batch-043`
- Completed repository identities: **10**
- Direct `SKILL.md` reads: **19**
- Direct unique skill bodies reviewed: **16**
- New batch-local canonical body reports: **15**
- Runtime/build/test/eval execution: **not_executed**

This file records reports only for directly read Skill bodies. Large collection inventory counts are not converted into body-level reports. Exact/previously reviewed bodies are mapped rather than duplicated. `zephyr-index` is the one directly reread unique body that already had a canonical report, leaving 15 new reports from 16 unique bodies.

## 1. `design-code-architecture`

- Repository: `MarkkuPekkarinen/skills`
- Stars: `0`
- Revision: `7702dbcb3873689cb73e9c513599c6c68b37cf4c`
- Source: `design-code-architecture/SKILL.md`

**Purpose:** orchestrate multiple architecture/design skills into a phased process while persisting architecture, reliability and implementation-plan artifacts.

**Strengths:** explicit phase boundaries; persistent handoffs; separation of orchestration from specialist skills; resumable decision trail.

**Gaps:** constituent-skill compatibility is convention-based; sequencing is opinionated; no behavioral eval was executed.

**Verdict:** strong orchestration reference; add dependency/version contracts and task-level evals.

## 2. `memory-system-ops`

- Repository: `kent666/memory-system-ops-skill`
- Stars: `0`
- Revision: `c5e08ac08ab97280d6dca65429b98c49da1aa33f`
- Supporting material: memory/task/checkpoint references

**Purpose:** make retrieval, writeback, task state, archive/resume and context-reset recovery explicit.

**Strengths:** evidence-sufficiency retrieval; structured Decision/Why/Impact/Next/Verify writebacks; explicit blocked/resume state; checkpoint semantics.

**Gaps:** host-specific topology/state vocabulary; time/repetition thresholds are uncalibrated heuristics; no executable eval harness surfaced.

**Verdict:** high-value state/evidence pattern; parameterize topology and validate thresholds with replay fixtures.

## 3. `acquiring-disk-image-with-dd-and-dcfldd`

- Repository lineage: `makakin/Anthropic-Cybersecurity-Skills` plus three independently content-gated mirrors/variants
- Stars: `0` on all four reviewed identities
- Representative revision: `4ae0be7f4806596e94958ac343379e9c9b3111d2`

**Purpose:** defensive digital-forensics evidence acquisition guidance. Operational command material is intentionally not reproduced in this report.

**Strengths:** structured metadata; evidence-oriented workflow; machine-readable collection integration.

**Gaps:** correctness depends on authorization, evidence handling, external-tool versions and environment; structural repository validation is not a behavioral/forensic correctness test.

**Verdict:** useful operational knowledge only with external authorization/evidence policy and disposable-fixture tests.

# `junefish1414/AgentSkills`

Reports 4–12 use repository revision `b80c9bae2afa109b04be8f1778f2f921708cd98f`; Stars observed: `0`. All nine local Skill bodies were directly read.

## 4. `axure-to-md-cli`

**Purpose:** transform prototype material into a Markdown intermediate artifact for downstream specification work.

**Strengths:** narrow adapter responsibility and explicit artifact handoff.

**Gaps:** source/export conventions and external tooling can change; no representative conversion fixtures surfaced.

**Verdict:** useful ingestion adapter; add deterministic conversion/provenance fixtures.

## 5. `blocker-overview`

**Purpose:** produce a consistent blocker/status overview artifact.

**Strengths:** visible output contract and presentation template.

**Gaps:** severity/ownership remain model-judged unless source-system fields are normalized; no behavioral evals surfaced.

**Verdict:** useful reporting contract; add normalized source schema and grading fixtures.

## 6. `confluence-to-md`

**Purpose:** convert Confluence content into local Markdown for later specification workflows.

**Strengths:** creates a reviewable intermediate artifact instead of leaving downstream work coupled to a live page.

**Gaps:** Atlassian tool/API and rich-content behavior are version-sensitive; macros/attachments can lose semantics without fixtures.

**Verdict:** good boundary adapter; validate rich-content and provenance preservation.

## 7. `jira-analyzer`

**Purpose:** inspect Jira issues and derive structured requirement/work context.

**Strengths:** isolates source analysis from later generation stages.

**Gaps:** semantic completeness remains model-dependent; needs fixtures for linked issues, sparse tickets, conflicts and stale status.

**Verdict:** useful analysis layer; add normalized schema plus evidence-linked outputs.

## 8. `jira-to-spec-iterate`

**Purpose:** update an existing specification from Jira changes while preserving unaffected sections.

**Strengths:** explicit anti-drift rule; treats iterative maintenance differently from first-generation authoring.

**Gaps:** impact detection is not deterministically checked; unresolved conflicts can still produce silent drift.

**Verdict:** strong iterative-edit pattern; add section ownership/change-map fixtures.

## 9. `jira-to-spec`

**Purpose:** generate a specification artifact from Jira context and supporting references.

**Strengths:** explicit composite/templates and clean role within a larger pipeline.

**Gaps:** inspected automation can replace an existing generated output area, so generic reuse needs collision-safe output/backup/authorization policy; no behavioral eval suite surfaced.

**Verdict:** useful spec-generation contract; externalize side-effect policy.

## 10. `spec-md-to-po-html`

**Purpose:** render specification Markdown into product-owner-facing HTML.

**Strengths:** separates presentation concerns from source requirement content and bundles presentation assets.

**Gaps:** static inspection does not prove visual/accessibility correctness; no browser regression suite surfaced.

**Verdict:** clean presentation boundary; add deterministic build/browser/accessibility checks.

## 11. `spec-reviewer`

**Purpose:** review specification implementation readiness and human readability.

**Strengths:** separates readiness from readability instead of using one opaque aggregate score.

**Gaps:** rubric scoring remains model judgment without calibrated examples; evidence gaps should remain distinct from writing-quality defects.

**Verdict:** strong review decomposition; add gold/anti-gold fixtures and disagreement handling.

## 12. `spec-to-prd`

**Purpose:** transform a specification into a product-requirements artifact.

**Strengths:** downstream transformation is isolated from source ingestion/technical review.

**Gaps:** rationale/priority can be invented unless field-level provenance and explicit unknowns are enforced.

**Verdict:** useful artifact transformation; require provenance and unknown-state handling.

# `ever-just/agentskills`

Reports 13–14 use revision `6c1ec73a213da4b8b72714e530c4bfd3cdd6f9c7`; Stars observed: `3`. The 115+ inventory/tree was verified, but only these two bodies were directly reviewed in this batch.

## 13. `deployment-testing`

**Purpose:** organization-specific deployment and verification runbook for a concrete production stack.

**Strengths:** combines deploy, health verification, UI checks and known-issue tracking in one operational reference.

**Gaps:** tightly coupled to live infrastructure; external side effects are described inside the Skill rather than governed by a reusable authorization contract; environment facts age quickly. Operational addresses/commands are intentionally omitted here.

**Verdict:** useful private runbook, not a portable generic Skill; separate environment facts from reusable verification logic.

## 14. `programmatic-osint-sources`

**Purpose:** progressively disclose a categorized public-data/research source catalog through focused reference files.

**Strengths:** clear reference router; source caveats include authorization/privacy/ToS/freshness concerns; explicitly acknowledges source churn.

**Gaps:** source/API/free-tier claims are time-sensitive; historical connector-test material is not current validation; broad aggregation can create privacy/compliance risk without purpose limitation and minimization. Operational lookup instructions are intentionally omitted here.

**Verdict:** good progressive-disclosure catalog structure; reverify time-sensitive claims at use time and enforce policy-level privacy boundaries.

## 15. `data-agent`

- Repository: `dgallitelli/aws-data-agent-skill-strands-agentcore`
- Stars: `0`
- Revision: `6c297673421bdf027268630c273bdd03c9186f04`
- Sources read: `data-agent/SKILL.md`, selected execution/generation references, `src/main.py`
- Tests/evals: none surfaced; execution **not_executed**

**Purpose:** discover governed AWS data assets, inspect schemas, generate schema-grounded read queries, request approval, then execute through Athena while respecting Lake Formation governance.

**Strengths:** schema-before-query grounding; explicit approval gate; access-denied boundary; progressive references; real Strands/AgentCore/MCP implementation aligns with the documented architecture.

**Gaps:** application code imports the MCP tool surface dynamically rather than enforcing a deterministic read-only allowlist; approval is prompt-level rather than application-enforced state; no repository-local tests demonstrate grounding, approval, governance or failure recovery.

**Verdict:** strong executable Skill integration pattern; enforce capability/approval state in code and add behavioral tests.

# Existing-body mapping

## `zephyr-index` — direct reread, no new report

- Repository: `HannanSolo/zephyr-agent-skills`
- Stars: `0`
- Revision: `6dc057cf3eee08a36a801e66428e8a6c22cd175b`
- Source: `skills/zephyr-index/SKILL.md`

The routing hub and supporting reference/script surfaces were directly read again. AI-handbook already contains the Zephyr family body report from Batch 027, so this read increases repository coverage but adds **0** to the canonical body-report count.

# Deduplication record

- Four Cybersecurity repository identities produced one new representative body report, not four duplicates.
- Three of those identities share exact tree `5dd2ce82978a50cd014d4b310f5993bf5bba6f43`; the fourth has a distinct repository tree but the sampled body maps to the same newer body lineage.
- `design-code-architecture` appeared previously only as a Wondel inventory identity; Batch 039 explicitly marked inventory-only entries as needing body review, so its direct Batch 043 body read is a new report.
- Searches before writing returned no prior body reports for `memory-system-ops`, the Junefish family, `deployment-testing`, `programmatic-osint-sources`, the sampled Cybersecurity slug, or `data-agent`.

**Batch 043 new body-report total: 15. Cumulative body-report total: 2911.**
