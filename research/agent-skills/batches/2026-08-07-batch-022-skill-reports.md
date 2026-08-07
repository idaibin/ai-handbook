# Agent Skills Deep Analysis — Batch 022 Skill Reports

Observed: 2026-08-07

Status: `structure-reviewed`

Runtime validation: `not_executed`

This artifact contains **27 repository-scoped Skill reports** from **10 repositories** in the existing indexed queue. Every `SKILL.md` represented below was directly read in this run. Demo and fixture skills are explicitly labeled and are not promoted to production-grade capabilities. External skills returned by registries are not counted as local repository skills.

## 1. gepeiyu/agentskills-proxy — `example-skill`

- Path: `skills/example-skill/SKILL.md`
- Repository role: TypeScript remote Agent Skills proxy/tooling; the local skill is a bundled demonstration fixture.
- Purpose: demonstrates the proxy's progressive skill loading and execution/artifact model rather than providing a production domain capability.
- Structure read: root `README.md`, `package.json`, `SKILL.md`, JavaScript demo script, Python demo script.
- Scripts: JavaScript example is designed for the repository's VM2 execution path and writes an artifact; Python example runs as a subprocess using environment-provided parameters and artifact directory.
- Design value: useful as an executable contract fixture showing how metadata/instructions/resources map to runtime execution and artifact creation.
- Caveat: classify the repository as tooling with a demo skill, not as a one-skill production collection. No scripts were executed in this review.

## RisorseArtificiali/agent-ready-skill

### 2. `agent-ready`

- Path: `skills/agent-ready/SKILL.md`
- Role: router/orchestrator for the agent-readiness suite.
- Purpose: routes requests into scan, report, fix, diff, or init rather than duplicating their implementation logic.
- Structure: delegates scoring authority to shared references and specialized sibling skills.
- Design value: keeps a stable user-facing entry point while allowing operational responsibilities to remain separated.
- Caveat: correctness depends on the sibling skills and shared rubric remaining synchronized; runtime routing was not executed.

### 3. `agent-ready-scan`

- Path: `skills/agent-ready-scan/SKILL.md`
- Role: repository readiness assessment.
- Purpose: inspect a codebase against a seven-dimension v2 readiness rubric and persist structured scores/evidence.
- References read: canonical `skills/agent-ready/references/scoring.md` defines dimensions, sub-criteria, layer semantics, calculation, output schema, and helper-script signals.
- Design value: scoring is centralized in one canonical reference rather than re-derived independently by report/fix consumers.
- Safety: helper scripts are intended as read-only repository inspection; representative `repo_map.py` parses Python with `ast` and uses lower-confidence regex heuristics for other languages without importing project code.
- Caveat: the scanner and helper scripts were read, not run.

### 4. `agent-ready-fix`

- Path: `skills/agent-ready-fix/SKILL.md`
- Role: brownfield remediation.
- Purpose: consume persisted readiness gaps, prioritize them, generate only supported remediations, and surface manual work separately.
- Authority model: canonical remediation registry maps each sub-criterion to `skill`, `partial`, or `manual` handling, with rationale, fix reference, and effort.
- Change control: requires a file-by-file confirmation gate before writes and states that existing files must not be overwritten.
- Design value: separates assessment from mutation and prevents a score from silently authorizing arbitrary repository changes.
- Caveat: no remediation generation or rescan was executed.

### 5. `agent-ready-report`

- Path: `skills/agent-ready-report/SKILL.md`
- Role: presentation/rendering.
- Purpose: render persisted v2 scores into a layered Markdown report, optional HTML, and badge.
- Boundary: explicitly renders persisted scores instead of recalculating them; missing/stale score state is routed back through scan.
- Design value: reporting cannot drift into an independent scoring implementation if the canonical JSON contract is respected.
- Caveat: output rendering was not executed in this review.

### 6. `agent-ready-diff`

- Path: `skills/agent-ready-diff/SKILL.md`
- Role: longitudinal comparison.
- Purpose: compare a current v2 assessment against a previous v2 baseline, including dimension and portable/target layer deltas.
- Gate: refuses to force a comparison when the prior schema is absent or not v2; establishes a fresh baseline instead.
- Design value: schema compatibility is treated as a precondition for meaningful historical comparison.
- Caveat: no baseline archive, rescan, or delta calculation was executed.

### 7. `agent-ready-init`

- Path: `skills/agent-ready-init/SKILL.md`
- Role: greenfield baseline scaffolding.
- Purpose: create a minimal agent-ready foundation for an empty/near-empty project and defer populated repositories to scan/fix.
- Change control: contains a populated-project guard and a confirmation gate; generates only missing files and treats placeholders as explicit greenfield placeholders.
- Design value: separates greenfield scaffolding from brownfield remediation rather than using one mutation workflow for both.
- Caveat: no scaffolding or quick scan was executed.

## 8. cablate/Agentic-MCP-Skill — `agentic-mcp`

- Path: `SKILL.md`
- Repository role: experimental MCP progressive-disclosure tooling and a single companion skill.
- Purpose: expose MCP server capabilities in three layers: server metadata, tool list without schemas, then individual tool schema on demand.
- Implementation surfaces read: `README.md`, `package.json`, `SKILL.md`, and `tests/unit/client.test.ts`.
- Test design observed: unit tests exercise connection state, Layer 1 metadata, Layer 2 schema-free tool listing, Layer 3 schema fetch, missing-tool/disconnected failures, and tool invocation against a filesystem MCP server.
- Design value: the progressive-disclosure contract is represented directly in tests rather than only prose.
- Caveat: repository describes itself as experimental; test-count/coverage statements are repository claims. Vitest was not run here.

## 9. octolens/skill — `octolens`

- Path: `SKILL.md`
- Repository role: single external-service adapter skill.
- Purpose: operate Octolens through its preferred MCP surface with REST API fallback/reference material.
- Structure read: `README.md`, `SKILL.md`, and `references/REST-API.md`.
- Reference design: common workflows stay in the skill body while the reference holds the larger v2 endpoint/field/filter/error catalog and points to the service OpenAPI surface as the machine-readable authority.
- Design value: good progressive disclosure for service adapters—activation and common behavior remain concise while exhaustive contracts are offloaded to references.
- Caveat: no local eval/test surface was observed in the reviewed material and no Octolens API call was made.

## 10. OthmanAdi/codebase-knowledge-builder — `codebase-knowledge-builder`

- Path: `skills/codebase-knowledge-builder/SKILL.md`
- Repository role: single repository-research/documentation skill.
- Purpose: produce durable engineering knowledge from a codebase through reconnaissance, dependency-aware deep reading, artifact authoring, and delivery.
- References read: reconnaissance checklist and deep-dive methodology; template read: `templates/knowledge_artifact.md`.
- Method: read files in dependency order; trace happy, error, and edge paths; save notes every few files rather than relying on context memory; require file paths/components/config/gotchas/extension points in the final artifact.
- Design value: converts "read the repo" into an auditable evidence workflow with a defined artifact schema.
- Caveat: no target repository analysis was executed using this skill in the current review.

## black-forest-labs/skills

### 11. `flux-best-practices`

- Path: `skills/flux-best-practices/SKILL.md`
- Repository role: official Black Forest Labs guidance skill.
- Purpose: provide model-aware FLUX image-generation/editing prompting guidance.
- Structure: compact activation/quick-reference body plus `rules/` documents for core principles, model families, text/image workflows, structured prompting, color, typography, multi-reference editing, and model selection.
- Representative reference read: `rules/model-selection-guide.md`.
- Design value: clean split between an always-needed routing layer and detailed model/task rules loaded only when relevant.
- Caveat: model capability, pricing, and performance statements in the repository were not independently benchmarked in this run; no image generation was executed.

### 12. `bfl-api`

- Path: `skills/bfl-api/SKILL.md`
- Repository role: API integration companion to `flux-best-practices`.
- Purpose: cover FLUX API integration concerns such as endpoint selection, asynchronous result handling, rate-limit/error behavior, webhooks, and code examples.
- Structure: core workflow in `SKILL.md`, detailed references for endpoint/auth/error/polling/webhook topics, and language/client examples.
- Design value: separates **prompt/model-use guidance** from **transport/integration guidance**, reducing responsibility overlap between the two official skills.
- Caveat: external endpoints, prices, and service behavior were not exercised in this review.

## Tencent/SkillHone

### 13. `skillhone`

- Path: `skills/skillhone/SKILL.md`
- Repository role: primary orchestrator for a skill evaluation/optimization harness.
- Purpose: coordinate status, evaluation, optimization, experiment creation, seeding, synthesis, and webhook/service scripts.
- Core architecture: public skill repository, private eval repository, isolated per-item solver workdirs, and redacted observation records are explicitly separated.
- Implementation read: actual `scripts/eval.py` and `references/evaluation.md` in addition to the skill body.
- Design value: treats evidence provenance and measurement isolation as first-class architecture rather than as reporting conventions.
- Caveat: no Forgejo service, solver, eval, or optimization run was executed.

### 14. `skillhone-optimization`

- Path: `skills/skillhone-optimization/SKILL.md`
- Role: optimization orchestrator.
- Purpose: diagnose failures using probe results, trajectories, compiler/validator feedback, issue/PR history, then land one attributable improvement per cycle.
- Boundaries: private eval data must not leak to the improver; code changes are delegated through PR-oriented roles; one change per cycle preserves attribution.
- Design value: score changes alone are insufficient evidence—the workflow explicitly distinguishes infrastructure, solver, compiler/validator, verifier, and skill-instruction failures.
- Caveat: optimization agents and PR flows were not run.

### 15. `skillhone-evaluation`

- Path: `skills/skillhone-evaluation/SKILL.md`
- Role: evaluation and failure diagnosis.
- Purpose: run/interpret probe, PR validation, and final test measurements while preserving split visibility boundaries.
- Evaluation contract read: JSONL items carry `question` plus executable verification that produces mechanically checkable score keys; solver writes an answer artifact in an isolated workdir and trajectories are retained for diagnosis.
- Important boundary: held-out `test` is explicitly not used during iterative optimization.
- Design value: combines aggregate outcome metrics with lower-level trajectory/compiler evidence and score provenance.
- Caveat: no dataset or evaluator was executed.

### 16. `skillhone-prd`

- Path: `skills/skillhone-prd/SKILL.md`
- Role: requirements/evaluation-contract authoring.
- Purpose: gather a skill PRD around environment, goal, output format, and evaluation, then produce different visibility views.
- Leakage control: full eval-visible PRD is separated from an improver-visible version with evaluation rubric redacted; question/answer transcript stays eval-side.
- Design value: evaluation secrecy is enforced in artifact topology, not left to operator memory.
- Caveat: the interactive interview and PRD validators were not run.

### 17. `skillhone-synthesis`

- Path: `skills/skillhone-synthesis/SKILL.md`
- Role: benchmark/eval data synthesis.
- Purpose: explore a tool environment, build a reusable evidence graph, mine closed-form questions, validate uniqueness/stability/gradability, and deduplicate outputs.
- Design: distinguishes hard questions from merely obscure/broken questions; mechanically checkable acceptance constraints should become verifier score keys.
- Design value: exploration is reusable across many generated items, while miners/dedupers operate over saved evidence rather than repeatedly calling tools.
- Caveat: no synthesis pipeline was executed.

### 18. `forgejo`

- Path: `skills/forgejo/SKILL.md`
- Role: replaceable VCS backend skill.
- Purpose: centralize Forgejo issue, PR, wiki, and repository operations behind dedicated scripts.
- Architecture value: SkillHone orchestration can depend on a stable VCS capability surface without embedding Forgejo-specific credential and HTTP behavior in every workflow.
- Safety boundary: credentials are resolved by backend scripts and should not be printed; direct main-branch pushes are disallowed by the documented workflow.
- Caveat: no Forgejo operation was executed.

## truefoundry/skills

### 19. `truefoundry-onboard`

- Path: `skills/onboard/SKILL.md`
- Role: first-time setup/login.
- Purpose: establish one stable CLI login state and stop before operational configuration.
- Design value: narrowly scoped onboarding prevents setup logic from leaking into every operational skill and defines one explicit credential-state verification surface.
- Caveat: CLI installation/login verification was not performed.

### 20. `truefoundry-gateway`

- Path: `skills/gateway/SKILL.md`
- Role: AI Gateway configuration and operation.
- Purpose: route model access, provider integrations, guardrails, and gateway observability to known API/CLI surfaces.
- Design: differentiates gateway concerns from deployment, platform access, MCP registry, and application instrumentation.
- Safety/change control: credential handling uses secret references; configuration application is designed around reviewed manifests and dry-run/diff before final changes.
- Caveat: no tenant API, model call, or configuration apply occurred.

### 21. `truefoundry-integrate-gateway`

- Path: `skills/integrate-gateway/SKILL.md`
- Role: codebase migration/integration.
- Purpose: deeply inspect an existing codebase for LLM calls/config/credentials, compare against gateway state, plan migration, apply confirmed changes, and verify routing.
- Design value: separates **operating the gateway** from **migrating a customer codebase into it**; analysis is expected to read actual source rather than depend on regex discovery alone.
- Change control: preflight safety checks and a migration plan precede source edits; modification requires confirmation.
- Caveat: scanner, code edits, and gateway verification were not executed.

### 22. `truefoundry-observability`

- Path: `skills/observability/SKILL.md`
- Role: logs and application tracing.
- Purpose: inspect application logs and add OpenTelemetry/Traceloop-style instrumentation when requested.
- Boundary: application/container observability is separate from gateway request observability handled by `gateway`.
- Safety: raw log output is treated as potentially sensitive and should be reviewed before external forwarding or reporting.
- Caveat: no logs were downloaded and no instrumentation dependency/code was changed.

### 23. `truefoundry-platform`

- Path: `skills/platform/SKILL.md`
- Role: platform access/identity/resource discovery.
- Purpose: connection checks, workspace/cluster discovery, RBAC/team/collaborator workflows, secrets, and token lifecycle.
- Design value: centralizes access-management concerns so domain skills can rely on a consistent preflight/identity layer.
- Change control: access grants and sensitive mutations require confirmation; secret/token output is constrained.
- Caveat: no platform call or access mutation occurred.

### 24. `truefoundry-mcp-servers`

- Path: `skills/mcp-servers/SKILL.md`
- Role: MCP Gateway registry management.
- Purpose: list/create/update remote, virtual, hosted-stdio, and OpenAPI-backed MCP server entries, configure tool selection/access, and attach clients.
- Design value: refuses to invent unknown manifest fields and treats the live UI/YAML preview as authority when examples and live product differ.
- Change control: final apply is gated by plain-language summary, full YAML/diff, exact command, and explicit confirmation; destructive removals are intentionally dashboard-only.
- Caveat: no server registry call or apply was made.

### 25. `truefoundry-prompts`

- Path: `skills/prompts/SKILL.md`
- Role: Prompt Registry lifecycle.
- Purpose: list, version, tag, create/update, and retrieve prompt references while routing agent authoring elsewhere.
- Design value: treats prompt edits as new reviewed versions rather than silent overwrite and keeps stable tags as an explicit change surface.
- Caveat: no prompt registry operation occurred.

### 26. `truefoundry-agents`

- Path: `skills/agents/SKILL.md`
- Role: Agent Registry UI workflow.
- Purpose: guide creation/editing/publishing/testing/skill-or-MCP attachment through the dashboard.
- Important content-level finding: the skill explicitly states that agent authoring is not API-driven and directs the workflow to the UI instead of fabricating an unsupported automation surface.
- Design value: capability limits are encoded as workflow rules, reducing hallucinated API operations.
- Caveat: no browser/dashboard interaction occurred.

### 27. `truefoundry-skills-registry`

- Path: `skills/skills-registry/SKILL.md`
- Role: Skill Registry lifecycle.
- Purpose: create/publish/version/download reusable Agent Skills, distinguish single-file from multi-file bundles, and attach versions to agents through the appropriate UI workflow.
- Important content-level finding: the skill explicitly rejects an unsupported upload command and requires live CLI help/product-generated manifests to establish unknown command/schema behavior.
- Repository consistency: root `scripts/validate-skills.sh` checks frontmatter, naming, shared symlink integrity, installer coverage, and CLI-reference consistency across the pack.
- Caveat: validation script, CLI, and registry publishing were not executed.

## Batch boundary

`structure-reviewed` means source/content evidence was directly inspected. It does **not** mean third-party CLIs, package builds, test suites, eval runners, browser flows, external APIs, model/image generation, network services, or cloud writes succeeded. Those runtime surfaces remain `not_executed` for this batch.
