# Agent Skills Individual Reports — Batch 054

- observed_at: `2026-08-09`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- new_repository_scoped_skill_reports: `30`
- dedup_rule: exact previously reviewed Skill blobs are not reported again; a distinct blob may receive a repository-scoped variant report when its content identity differs.

## `aaditagrawal/agentskills` — 5 reports

### `no-useeffect`

- **Verified:** React guidance Skill focused on avoiding unnecessary lifecycle synchronization and preferring derivation/event-driven state flow.
- **Value:** clear routing heuristic for reviewing component state and data flow.
- **Risk/gap:** deliberately absolute framing can reject legitimate effect-based synchronization; no behavioral evals or example-test harness was present.
- **Validation:** source review only.

### `no-slop`

- **Verified:** coding-style Skill that constrains low-signal generated-code patterns and pushes toward smaller, intentional edits.
- **Value:** useful as a review/style layer rather than a code-generation engine.
- **Risk/gap:** rules are qualitative and repository-local; no evaluator demonstrates consistent enforcement across projects.
- **Validation:** source review only.

### `ai-taste`

- **Verified:** implementation/review taste guide aimed at simplifying generated solutions and reducing unnecessary abstraction.
- **Value:** captures reusable design heuristics for agent-generated code.
- **Risk/gap:** subjective judgment criteria are not converted into measurable acceptance tests.
- **Validation:** source review only.

### `md-site`

- **Verified:** Skill for a deliberately plain-text/Markdown-like website aesthetic.
- **Value:** gives the agent a strong, bounded visual/product direction.
- **Risk/gap:** some visual choices intentionally trade semantic HTML conventions for appearance; no accessibility or browser validation suite is included.
- **Validation:** source review only.

### `openrouter-expert`

- **Verified:** large domain Skill with helper scripts for refreshing documentation/model inventories from live sources before producing answers.
- **Value:** strong fail-closed source-of-truth pattern: current documentation is treated as authority instead of relying on model memory.
- **Risk/gap:** helper scripts depend on network/tool availability; repository has no regression or behavioral eval suite proving routing/answer quality.
- **Validation:** scripts and Skill body read; not executed.

## `JarvAmrit/AgentSkills` — 4 equivalent-skill reports

### `azdo-implement`

- **Verified:** reusable agent workflow for implementing an Azure DevOps work item through repository inspection, code changes, validation, and delivery steps.
- **Value:** explicit end-to-end execution checklist and validation expectations.
- **Risk/gap:** combines code mutation, Git state, external work-item/PR operations, and credentials; authorization should be external to the workflow.
- **Validation:** source review only; no Azure/Git/test execution.

### `azdo-create-workitem`

- **Verified:** workflow for collecting requirements and creating Azure DevOps work-item state.
- **Value:** structured input collection reduces under-specified external writes.
- **Risk/gap:** creates persistent external state; no independent schema/eval harness was found.
- **Validation:** source review only.

### `sonarqube-fix`

- **Verified:** remediation workflow driven by SonarQube findings with repository changes and follow-up validation steps.
- **Value:** treats scanner findings as inputs to inspect rather than as self-proving fixes.
- **Risk/gap:** external service state and code changes are coupled in one workflow; no repository-local behavioral eval exists.
- **Validation:** source review only.

### `veracode-fix`

- **Verified:** security-remediation workflow using Veracode findings to guide code changes and validation.
- **Value:** preserves a finding → inspect → modify → validate workflow shape.
- **Risk/gap:** high-side-effect integration and security findings require explicit authorization and independent verification; no live scanner or test execution occurred.
- **Validation:** source review only.

## `VTSTech/skills` — 5 reports

### `acp`

- **Verified:** session-control/orchestration Skill with stop state, activity lifecycle, orphan handling, agent identity/ownership, TODO restoration, and A2A messaging concepts.
- **Value:** strong execution-truth pattern: actions have pre-execution logging and explicit completion rather than inferred success.
- **Risk/gap:** development-default security settings documented by the Skill should not be treated as production-safe; behavior depends on an external ACP service not present in this repository.
- **Validation:** Skill body read; service not executed.

### `codebase-audit`

- **Verified:** two-mode codebase orientation/audit workflow that produces a compact reusable brief plus detailed evidence-grounded findings.
- **Value:** strong evidence discipline, critical-file indexing, and explicit separation between orientation and detailed audit artifacts.
- **Risk/gap:** load mode treats an existing brief as authoritative without a mandatory repository revision/content fingerprint, creating stale-brief risk.
- **Validation:** Skill and reference structure read; no target repository audit executed.

### `godot-engine`

- **Verified:** Godot development knowledge/workflow Skill with progressive references for GDScript and project patterns.
- **Value:** broad domain routing and reference decomposition keeps detailed material outside the primary activation body.
- **Risk/gap:** primarily knowledge/instruction content; no executable test/eval package in the repository establishes correctness against engine versions.
- **Validation:** source review only.

### `ps2-elf`

- **Verified:** specialized binary-analysis/server-emulation workflow packaged as a single Skill.
- **Value:** clear domain boundary and tool/workflow documentation.
- **Risk/gap:** operational reverse-engineering behavior is not validated here and should remain subject to external safety/authorization constraints.
- **Validation:** structural source review only; no binary, network, or tooling execution.

### `terminal-video-recorder`

- **Verified:** video-recording Skill backed by `scripts/record-demo.sh` and demo assets under `scripts/tests/`.
- **Value:** unlike prose-only Skills, it has an actual deterministic shell implementation for producing an artifact.
- **Risk/gap:** the `tests/test-demo.sh` file is a demo workload without assertions, so it is not a meaningful regression suite. The implementation also assumes specific host utilities, display number, and output path, limiting portability/concurrency.
- **Validation:** script/test source read; recording not executed.

## `fiorellarmartins/skills` — 9 reports

> These reports evaluate workflow/engineering structure only. They do not validate medical, financial, regulatory, or legal correctness.

### `eps-audit`

- **Verified:** example Skill demonstrating the repository's preferred trigger → procedure → pitfalls → verification structure.
- **Value:** useful concrete template for evidence-oriented domain Skills.
- **Risk/gap:** domain rules depend on external/current reference data and are not backed by executable fixtures/evals here.
- **Validation:** source review only.

### `medical-invoice-admin-audit`

- **Verified:** administrative sub-audit with explicit rule IDs, evidence fields, output shape, and independence from other sub-auditors.
- **Value:** traceable evidence and invariant-style verification conditions are strong design patterns.
- **Risk/gap:** high-stakes domain rules and reference datasets have no automated freshness/version validation in this repository.
- **Validation:** source review only.

### `medical-invoice-claim-denial-generator`

- **Verified:** versioned document-generation workflow that preserves prior document versions and consumes consolidated findings.
- **Value:** explicit non-overwrite/version history is a strong artifact-governance pattern.
- **Risk/gap:** legal/regulatory text and rendering behavior are not validated by repository-local tests or current-authority checks.
- **Validation:** source review only.

### `medical-invoice-claim-denial-gmail-sender`

- **Verified:** outbound-delivery workflow that requires a ready/approved state, records delivery identifiers, and guards against duplicate sending.
- **Value:** clear approval precondition, idempotency check, and delivery traceability.
- **Risk/gap:** sending email is an irreversible external side effect and must remain under centralized authorization; Gmail behavior was not exercised.
- **Validation:** source review only.

### `medical-invoice-consolidator-audit`

- **Verified:** consolidation workflow that merges three independent audit streams, deduplicates root causes, prioritizes findings, and emits workflow state.
- **Value:** explicit deduplication and provenance from multiple auditors are reusable orchestration patterns.
- **Risk/gap:** confidence/decision formulas are domain assumptions rather than empirically validated models in this repository.
- **Validation:** source review only.

### `medical-invoice-financial-audit`

- **Verified:** financial/anti-fraud sub-audit with rule identifiers, explicit calculation evidence, independent execution boundary, and verification invariants.
- **Value:** requiring calculations and citable source evidence is stronger than prose-only judgment.
- **Risk/gap:** tariff/reference freshness and domain correctness are high-stakes and not established by an executable evaluation suite.
- **Validation:** source review only.

### `medical-invoice-fix-review`

- **Verified:** human-comment reconciliation workflow with structured intent classification, append-style audit log, idempotency marker, version regeneration, and role check before approval.
- **Value:** human authority is explicit and traceable rather than inferred from free-form comments.
- **Risk/gap:** LLM intent classification and patch correctness lack repository-local behavioral evals; external case mutation remains a side effect.
- **Validation:** source review only.

### `medical-invoice-gmail-intake`

- **Verified:** intake workflow that classifies messages, inventories attachments, structures case metadata, applies duplicate/error guards, and files external case state.
- **Value:** clear stage boundary and structured handoff to downstream auditors.
- **Risk/gap:** combines email/file parsing with persistent external writes; no fixture suite verifies classification, extraction, or duplicate handling.
- **Validation:** source review only.

### `medical-invoice-medical-audit`

- **Verified:** clinical sub-audit with independent scope, rule IDs, evidence citations, conditional handling for stale/failed reference extraction, and output invariants.
- **Value:** explicit evidence location and fail/conditional separation are reusable high-stakes review patterns.
- **Risk/gap:** clinical correctness and reference freshness are not established by repository-local execution/evaluation.
- **Validation:** source review only.

## `dsebastien/ai-skill-scholar` — 3 reports

### `scholar-search`

- **Verified:** OpenAlex search Skill backed by a stdlib Python client that normalizes work metadata and reconstructs abstracts.
- **Value:** deterministic structured retrieval keeps source mechanics outside the LLM's judgment path.
- **Risk/gap:** shared timestamp-file throttling is not inter-process locked, so simultaneous callers can race; no tests/evals are present.
- **Validation:** Skill/script source read; network not executed.

### `scholar-citations`

- **Verified:** citation-graph Skill supporting multiple identifier forms, batched reference resolution, cursored citation retrieval, filters, and normalized output.
- **Value:** explicit directionality and bounded staged traversal help prevent uncontrolled graph expansion.
- **Risk/gap:** uses the same unlocked shared throttle mechanism; citation completeness remains dependent on external index coverage.
- **Validation:** Skill/script source read; network not executed.

### `literature-review`

- **Verified:** persistent multi-phase review workflow separating search mechanics, agent screening, fetch planning, full-text reading, and synthesis.
- **Value:** two-pass screening, resumable JSON state, source deduplication, and explicit read-status rules are directly reusable research patterns.
- **Risk/gap:** some Skill/script prose still references Semantic Scholar/S2 after migration to OpenAlex; session JSON writes are not guarded for concurrent writers and no behavioral eval is included.
- **Validation:** Skill/script source read; review workflow not executed.

## `EliseT123/-VTSTech-Modular-Agent-skills` — 1 variant report

### `codebase-audit` — fork variant

- **Verified:** exact blob differs from `VTSTech/skills::codebase-audit`, but direct comparison of the reviewed body shows no material workflow change; the observed difference is textual/frontmatter punctuation-level.
- **Value:** content-addressed tracking correctly distinguishes the blob while the report records semantic equivalence to avoid overstating novelty.
- **Risk/gap:** README/Skill metadata still point to upstream identity; stale-brief risk from the upstream workflow remains.
- **Validation:** source review only. `acp` and `ps2-elf` are exact reviewed upstream blobs and were not duplicated as reports.

## `dsebastien/ai-skill-arxiv` — 3 reports

### `arxiv-search`

- **Verified:** arXiv discovery Skill backed by a stdlib Atom-API client producing structured JSON with topic/category/date filters.
- **Value:** deterministic XML-to-JSON conversion cleanly separates retrieval from model presentation/synthesis.
- **Risk/gap:** repository has no tests/evals; live API behavior and query-quality assumptions were not exercised.
- **Validation:** Skill/script source read; network not executed.

### `arxiv-analyze`

- **Verified:** paper-acquisition Skill with tiered source fallback, disk cache, explicit output/exit-code contract, persistent rate-limit state, and optional source-level acquisition.
- **Value:** source fallback and caching are concrete, deterministic mechanisms that can support reproducible research reads.
- **Risk/gap:** the compatibility fallback for archive extraction can use unrestricted extraction when the safer filter is unavailable; untrusted archive handling therefore needs a fail-closed extraction contract. Rate-limit state uses atomic replacement but no lock around the full read-reserve-write transaction.
- **Validation:** Skill/script source read; no paper fetch or archive extraction executed.

### `arxiv-monitor`

- **Verified:** persistent watchlist Skill that invokes the sibling search script, tracks bounded seen IDs, returns new-only results, and writes state via atomic replacement.
- **Value:** explicit delta state and bounded retention provide a simple reusable monitoring model.
- **Risk/gap:** read-modify-write state has no inter-process lock, so concurrent checks can lose updates; no tests/evals validate idempotency or concurrent behavior.
- **Validation:** Skill/script source read; no scheduled/live check executed.

## Batch validation boundary

These 30 reports are source-level, repository-scoped analyses. `runtime_validation=not_executed` applies to every entry. Test/eval/script presence is recorded as evidence about repository design only and is never interpreted as a passing result.
