# Agent Skills Individual Reports — Batch 047

Observed: 2026-08-09

This file materializes the 36 repository-scoped Skill reports whose bodies were directly read in Batch 047. Exact-tree mirrors and previously analyzed content are mapped rather than duplicated. Static source inspection is not treated as runtime, test, build, or behavioral-eval execution.

## `me-pankajmunde/AgentSkills`

Pinned revision: `acc11be629ffd58aa72ebb921cead21e265ee59b` · tree: `5558cffc4e02edcbe2dd7416942f69bfae8b76dc`.

### 1. `wiki-agent`
- Path: `WiKi_Skills/SKILL.md`; supporting code includes `wiki.py`, `wiki_compiler.py`, `bm25_retriever.py`, `qdrant_store.py`, and `fusion.py`.
- Purpose: persistent document-to-wiki knowledge compilation plus hybrid BM25/Qdrant retrieval, RRF fusion, reranking, and cited answer synthesis.
- Strength: separates raw sources, compiled knowledge, and retrieval index instead of treating RAG output as disposable chat context.
- Gap: no repository-local retrieval benchmark or fixture corpus was found to establish retrieval quality, citation fidelity, or regression behavior.
- Validation: source and implementation inspected; execution not performed.

### 2. `copilot-sdk`
- Path: `copilot-sdk/SKILL.md`.
- Purpose: guide construction of agentic applications with GitHub Copilot SDK across TypeScript, Python, Go, and .NET.
- Strength: broad coverage of sessions, streaming, tools, MCP, and custom agents in one procedural reference.
- Risk: examples prominently use approve-all permission handlers; this is convenient for demos but is not a safe default authorization policy for autonomous or production agents.
- Validation: documentation inspected; SDK examples were not executed or version-checked against a live installation.

### 3. `adk-agent-builder`
- Path: `google-adk-skill/SKILL.md`; supporting `templates.md` is present.
- Purpose: scaffold and design Google ADK agents, tools, workflows, multi-agent systems, callbacks, session state, and deployment.
- Strength: explicit entry-point, tool-schema, and orchestration conventions make the instructions implementation-oriented rather than generic prompting advice.
- Gap: the repository provides guidance/templates but no local compatibility matrix or behavioral test suite proving examples across all claimed language SDKs.
- Validation: Skill body inspected; examples not executed.

## `profbernardoj/morpheus-skill`

Pinned revision: `40580ea1d0882b6c4d56502f37c6f3d90a45c456` · tree: `e8d90d3e168622578ab50f46b27f79d16d5d1a53`.

### 4. `everclaw`
- Path: root `SKILL.md`; repository also contains setup/service scripts, Docker assets, CI workflows, security configuration, wallet/proxy logic, and deployment helpers.
- Purpose: configure and operate a multi-provider inference stack with local services, fallback routing, external network calls, optional blockchain credentials, and self-healing automation.
- Strength: unusually complete operational surface, including dry-run-oriented setup documentation, persistent-service metadata, outbound-network declaration, secret-storage guidance, CI, and security scanning assets.
- Risk: this Skill can mutate local configuration, restart services, handle credentials, call external inference providers, and interact with blockchain/network resources. Those effects require a policy layer above the Skill rather than implicit authorization from invocation alone.
- Validation: source/CI definitions inspected; CI, installer, service, wallet, network, and inference paths were not executed.

### 5. `cron-packs`
- Path: `cron-packs/SKILL.md` with JSON packs for essential, family, investor, developer, briefings, and cyclic execution patterns.
- Purpose: reusable scheduled-job templates for OpenClaw-style agents.
- Strength: schedules, placeholders, model roles, destinations, and job purposes are externalized into data files rather than hidden in prose.
- Risk: some packs imply external messaging, market-data access, repository inspection, or recurring execution; template installation must not be interpreted as blanket authorization for those side effects.
- Validation: definitions inspected; jobs were not registered or run.

## `essentialsoft/agentskills`

Pinned revision: `fd2d437db59e140d88bba84a8fe04a29d566a17b` · tree: `582ae52a4e46d10d22446f3b3cc259a05e9b82dd`.

The repository README defines `skills/` as the installed Skill store and `skills-lock.json` as version state. The tree contains 21 Skill bodies plus references/scripts for several Skills and a separate web catalog application with tests. The `skill-test` subsystem also contains an explicit Codex-runner → persisted artifacts → LLM judge → dashboard evaluation pipeline. None of those executable paths were run in this batch.

### 6. `bio-ai-product-manager`
- Path: `skills/bio-ai-product-manager/SKILL.md`; six focused references cover discovery, PRDs, biology context, API gaps, user stories, and AI feature evaluation.
- Strength: explicitly separates facts, assumptions, hypotheses, open questions, API dependencies, and scientific/compliance uncertainty.
- Gap: quality depends on supplied domain evidence; no local behavioral eval demonstrates PRD correctness or scientific accuracy.

### 7. `brainstorming`
- Path: `skills/brainstorming/SKILL.md`; supporting scripts implement a visual companion/server flow.
- Strength: clear design-before-implementation gate, scoped decomposition, spec self-review, and transition contract to planning.
- Risk: its universal hard gate and mandatory approval sequence can over-constrain trivial, already-specified, or non-interactive work; this should be policy/context sensitive rather than absolute.

### 8. `code-reviewer`
- Path: `skills/code-reviewer/SKILL.md`.
- Strength: isolates review as a dedicated workflow rather than mixing review and implementation authority.
- Gap: no repository-local benchmark establishes precision/recall of findings or protection against style-only noise and false positives.

### 9. `codebase-doc-writer`
- Path: `skills/codebase-doc-writer/SKILL.md`; references plus `bootstrap_doc_plan.py` and `repo_inventory.py` support the workflow.
- Strength: combines repository inventory, output policy, documentation templates, and analysis rules instead of relying only on free-form generation.
- Gap: generated documentation still needs freshness/coverage verification against real call paths; scripts alone do not prove semantic accuracy.

### 10. `container-security-review`
- Path: `skills/container-security-review/SKILL.md`; dedicated references cover multiple scanners, normalization/triage, image/prebuild modes, action plans, and fix execution.
- Strength: scanner-specific details are progressively disclosed and normalized into a common review workflow.
- Risk: security findings and remediation depend on current scanner output and environment; static guidance cannot establish vulnerability-detection efficacy.

### 11. `dockerfile-twistlock-zero-high`
- Path: `skills/dockerfile-twistlock-zero-high/SKILL.md`.
- Strength: narrow, outcome-oriented container remediation scope.
- Risk: a target such as “zero high” can encourage metric gaming if severity suppression or package removal is accepted without functional/runtime regression checks.

### 12. `email-generator`
- Path: `skills/email-generator/SKILL.md`; references provide style and invitation templates.
- Strength: templates and style rules are separated from the routing instructions.
- Gap: no eval checks factual preservation, recipient correctness, or whether generated mail remains within the supplied facts.

### 13. `git-commit-push`
- Path: `skills/git-commit-push/SKILL.md`.
- Strength: treats Git commit/push as an explicit operational workflow rather than an incidental implementation step.
- Risk: push is an external side effect. Authorization and branch/protection checks should be governed centrally so this Skill cannot silently override another Skill's confirmation policy.

### 14. `git-commit`
- Path: `skills/git-commit/SKILL.md`.
- Strength: provides a focused commit boundary separate from broader implementation.
- Risk: repository state, unrelated changes, generated files, secrets, and user authorization must be verified before commit; local Skill prose should not be the sole authority for permission.

### 15. `image-comparison`
- Path: `skills/image-comparison/SKILL.md`; executable helper `scripts/compare-images.mjs` and its package manifest are present.
- Strength: delegates pixel/image comparison mechanics to deterministic code instead of asking the model to infer all differences visually.
- Gap: no repository-local fixtures establish tolerance behavior, perceptual quality, or robustness across image formats/resolutions.

### 16. `implementation-executor`
- Path: `skills/implementation-executor/SKILL.md`.
- Strength: separates plan execution from planning and review concerns.
- Risk: execution Skills need a higher-level contract for scope, side effects, validation depth, and stop conditions; otherwise a plan can be followed faithfully while still producing unsafe or unverified changes.

### 17. `junit5-spring-testing`
- Path: `skills/junit5-spring-testing/SKILL.md`; `references/test-patterns.md` and OpenAI agent metadata are present.
- Strength: domain-specific test patterns are externalized into a reference, keeping the main Skill focused on routing and workflow.
- Gap: no local Spring fixture project or CI run demonstrates that generated examples compile and test across supported framework versions.

### 18. `memgraph-cypher-assistant`
- Path: `skills/memgraph-cypher-assistant/SKILL.md`; large model/index YAML references and `scripts/query_memgraph.py` are present.
- Strength: couples query generation to explicit schema/index reference data instead of relying on model memory alone.
- Risk: the large checked-in schema/index references can become stale; live schema reconciliation or version metadata is needed before treating them as authoritative.

### 19. `requirements-to-plan`
- Path: `skills/requirements-to-plan/SKILL.md`.
- Strength: establishes a dedicated transformation boundary between requirements and executable planning.
- Gap: no local traceability validator checks that every requirement, non-goal, dependency, and acceptance criterion is represented in the resulting plan.

### 20. `site-crawl`
- Path: `skills/site-crawl/SKILL.md`; `scripts/crawl-urls.mjs` provides executable crawling support.
- Strength: crawling mechanics are implemented in code rather than reproduced as fragile shell recipes.
- Risk: network scope, robots/site policy, rate limits, authentication, and data-handling boundaries require explicit environment/user authorization outside the Skill.

### 21. `site-snapshots`
- Path: `skills/site-snapshots/SKILL.md`; `scripts/capture-images.mjs` provides executable capture support.
- Strength: turns visual evidence collection into a repeatable artifact-producing step.
- Gap: no local cross-browser/viewport fixture suite establishes reproducibility or guards against dynamic-page nondeterminism.

### 22. `skill-test` (`llm-evaluation-pipeline`)
- Path: `skills/skill-test/SKILL.md`; `SYSTEM_DESIGN.md`, Excel example, judge prompt, JSON schema, Codex runner, test-case runner, evaluation runner, pipeline coordinator, and dashboard generator are present.
- Strength: strongest verification architecture in this batch: test inputs, raw traces, metadata, structured judge output, run summary, and dashboard are persisted as separate artifacts.
- Important boundary: an LLM judge is an evaluation mechanism, not ground truth. Reproducibility also depends on pinned model/config, deterministic fixtures where possible, and independent checks for critical invariants.
- Validation: implementation and design inspected; the pipeline was not run.

### 23. `superpowers-executing-plans`
- Path: `skills/superpowers-executing-plans/SKILL.md`.
- Strength: makes plan execution a distinct lifecycle stage.
- Gap: execution progress should be tied to observed test/build/runtime evidence rather than task-checkbox completion alone.

### 24. `superpowers-writing-plans`
- Path: `skills/superpowers-writing-plans/SKILL.md`; includes a plan-document reviewer prompt.
- Strength: explicit plan-review step improves handoff quality and decomposability.
- Gap: a reviewed plan still needs requirement traceability and real execution evidence; prose review cannot establish implementability.

### 25. `technical-interview-question-generator`
- Path: `skills/technical-interview-question-generator/SKILL.md`; references include role calibration, question design, output template, career guidance, and a spreadsheet source.
- Strength: role calibration and reference-backed question design reduce generic interview generation.
- Gap: no behavioral eval checks difficulty calibration, answerability, bias, or alignment with current role requirements.

### 26. `test-cases`
- Path: `skills/test-cases/SKILL.md`; `references/testing-principles.md` is present.
- Strength: isolates test-case design as a reusable capability and gives it an explicit testing-principles reference.
- Gap: no repository-local validator proves generated cases cover requirements, boundaries, failures, and state transitions; downstream execution is still required.

## `shucenliu333-eng/investment-analysis-skills`

Pinned revision: `946ea534124e478a8c677728ac6a267776bf4a0a` · tree: `c3e1de8fc855078f6c0609fab44fb6a9ec6ca268`. The collection is reference-driven rather than executable: its nine Skills encode research workflows, formulas, source priorities, and cross-Skill dependencies, but no local calculation harness or behavioral eval suite was found.

### 27. `company-valuation`
- Purpose: multi-method company valuation using DCF, comparables, precedents, SOTP/LBO and sensitivity analysis, with dependencies on forecast/financial/competitive analysis.
- Strength: explicitly requires cross-checking multiple methods and exposes assumptions instead of presenting a single opaque target value.
- Gap: calculations are prose/template driven; no deterministic model validates formulas, units, source freshness, or numerical reconciliation.

### 28. `competitive-landscape`
- Purpose: player mapping, market share/concentration, competitive dimensions, strategic groups, moat assessment, and competitive dynamics.
- Strength: defines source priority and separates data collection from analytical frameworks.
- Gap: current market facts depend on live research; no provenance schema enforces source/date/metric consistency across generated conclusions.

### 29. `due-diligence`
- Purpose: structured investment due-diligence workflow across business, financial, market, management, risk, and evidence domains.
- Strength: checklist-style decomposition supports coverage and explicit risk surfacing.
- Gap: checklist completion is not evidence quality; contradictory sources, missing primary documents, and unresolved assumptions need machine-visible status.

### 30. `financial-analysis`
- Purpose: historical financial statement and ratio analysis with dedicated formula, methodology, data-source, and analysis references.
- Strength: separates formula/reference material from workflow instructions and promotes primary-source financial data.
- Gap: no executable reconciliation verifies accounting identities, ratio formulas, period alignment, currency/unit normalization, or restatements.

### 31. `financial-forecast`
- Purpose: revenue, margin, cash-flow and corporate-finance forecasting using multiple reference methods.
- Strength: makes assumptions and forecasting methods explicit rather than hiding them in narrative conclusions.
- Gap: no scenario engine, spreadsheet/model artifact, or regression fixture establishes numerical consistency across forecast changes.

### 32. `financial-statement-forensics`
- Purpose: detect accounting-quality and financial-statement warning signs using a dedicated forensics checklist.
- Strength: encourages skeptical evidence review rather than accepting headline metrics.
- Gap: red flags are heuristics until reconciled against filings, notes, periods, and company-specific accounting policy; no local detection benchmark exists.

### 33. `macro-environment`
- Purpose: macroeconomic environment analysis using a dedicated framework reference.
- Strength: supplies a repeatable structure for connecting macro variables to investment context.
- Gap: macro data are freshness-sensitive and revision-prone; no source adapter or timestamp/provenance contract is enforced by code.

### 34. `market-sizing`
- Purpose: top-down/bottom-up market sizing with methodology guidance.
- Strength: encourages triangulation rather than one unsupported market-size figure.
- Gap: no deterministic unit/conversion calculator or source-lineage artifact validates assumptions and arithmetic.

### 35. `porter-five-forces`
- Purpose: structured industry-attractiveness and competitive-pressure analysis using Porter's Five Forces and related references.
- Strength: explicit framework and evidence prompts improve comparability across analyses.
- Gap: qualitative scores remain analyst/model judgments unless backed by sourced metrics and calibrated rubrics; no local eval establishes consistency.

## `zacmoltbot/openclaw-skill-long-task-control`

Pinned revision: `d744ff2f3e22ae140c63657ae654b3a7267936a2` · tree: `6b9e979a8c8125de5c85d91b1da91d2ed604e1af`.

### 36. `long-task-control`
- Path: repository Skill plus Python ledger/control implementation and repository regression/E2E tests.
- Purpose: manage long-running multi-stage work with durable checkpoints, observed-vs-derived state, retries, blocked states, artifact delivery, and verifiable progress reporting.
- Strength: execution truth is modeled as persisted state/artifacts rather than conversational claims; the repository includes tests for partial success, terminal cleanup, retries/block convergence, recovery, and delivery semantics.
- Gap: those test files are evidence of a verification design, not proof of a passing revision until executed. Integration with external task runners also needs idempotency and side-effect policy checks.
- Validation: Skill, implementation, and representative tests inspected; tests/runtime not executed in this batch.

## Existing-content mappings

The following directly content-gated repositories did not create new reports: `hanul93/Anthropic-Cybersecurity-Skills` and `mr-r0w07/Anthropic-Cybersecurity-Skills` map to the already-reviewed Cybersecurity collection at exact revision/tree `4ae0be7f4806596e94958ac343379e9c9b3111d2` / `5dd2ce82978a50cd014d4b310f5993bf5bba6f43`. `manhtx/skills`, `adooylabs/skills`, and `KziGeez/claude-skills` map to the already-reviewed Wondel-derived tree at `4d322538be8b9ce98fca29b0eef26d67bff1fe82` / `32d2d4cb75cf113fbc8e145d7c52672832e34a2` after README plus representative `clean-architecture/SKILL.md` content gates.

Cross-repository canonical reconciliation remains pending; the 36 reports above are therefore recorded as new repository-scoped Skill reports, not a claim that all are globally unique semantic Skills.