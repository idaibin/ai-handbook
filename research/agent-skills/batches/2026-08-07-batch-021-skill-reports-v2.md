# Agent Skills deep analysis — Batch 021 individual skill reports (v2)

Observed: 2026-08-07

Status: `structure-reviewed`

Runtime validation: `not_executed`

This supersedes the first Batch 021 skill-report artifact. In this v2 artifact, **all 23 reported repository-scoped `SKILL.md` bodies were directly read from GitHub**, including all 16 formal Skill definitions observed in `armelhbobdad/bmad-module-skill-forge`. External catalog references, templates, generated examples, specification examples, and runtime support code are not counted as local Skills.

## `ersinkoc/project-architect`

### 1. `project-architect`
- Path: `SKILL.md`
- Verification: direct body read.
- Role: documentation-first project architecture/planning workflow.
- Flow: discovery → `SPECIFICATION.md` → `IMPLEMENTATION.md` → `TASKS.md` → optional `BRANDING.md` → synthesized `PROMPT.md`.
- Supporting structure: `references/` separates elicitation, technology selection, design patterns, and output guidance for progressive loading.
- Notable pattern: review gates are explicit between major artifacts; discovery guidance says to extract known facts before asking more questions.
- Runtime/eval: no workflow execution performed; no repository-local eval runner observed in reviewed root/reference paths.

## `zht043/AgentSkills`

The repository README explicitly marks the monorepo deprecated and points users to split repositories. The following five formal definitions still physically exist and were directly read, but their authority/status differs.

### 2. `agent-skills`
- Path: `SKILL.md`
- Verification: direct body read.
- Role: repository-level router/read-depth instruction.
- Pattern: progressive loading, capability index, and requirement to read target Skill scripts/config rather than only entry metadata.
- Status caveat: partially stale because its capability map still names suites that the current README says were moved out.

### 3. `skill-creator`
- Path: `skill-creator/SKILL.md`
- Verification: direct body read.
- Role: meta-Skill for extracting reusable Skills from exploration or source material.
- Pattern: capability-vs-process taxonomy, single-vs-suite layouts, explicit frontmatter fields, exploration → refinement → fresh-session validation.
- Status caveat: legacy copy; README says the maintained successor is the independent `agent-skill-architect` repository.

### 4. `markdown-mermaid-illustrator`
- Path: `skills/markdown-mermaid-illustrator/SKILL.md`
- Verification: direct body read.
- Role: Mermaid generation/refactoring for technical Markdown.
- Pattern: chart-type routing, semantic shapes, layout rules, dark/light constraints, Mermaid capability limits, and confirmation before replacement.
- Status: README calls it the canonical residual version, pending migration.

### 5. `doc-illustrator`
- Path: `skills/doc-illustrator/SKILL.md`
- Verification: direct body read.
- Role: earlier Mermaid illustration workflow using template matching or LLM design, preview, confirm, then replace.
- Status: legacy predecessor; README recommends `markdown-mermaid-illustrator` instead.

### 6. `export-history`
- Path: `skills/export-history/SKILL.md`
- Verification: direct body read; implementation script directly read.
- Role: export local Claude Code JSONL conversation history to one searchable HTML file.
- Script: `skills/export-history/scripts/export-claude-history.mjs` traverses local sessions, parses user/assistant text, HTML-escapes content, and renders a self-contained viewer.
- Runtime/eval: script was not executed.

## `armelhbobdad/bmad-module-skill-forge`

Content-level correction: `src/README.md` documents Ferris plus 14 workflow Skills, while the live repository also contains the full formal `src/skf-campaign/SKILL.md`. The observed live corpus is therefore **16 formal repository-scoped Skill definitions**. Every body below was directly read in Batch 021.

### 7. `skf-forger`
- Path: `src/skf-forger/SKILL.md`
- Role: Ferris persona/dispatcher across Architect, Surgeon, Audit, Delivery, and Management modes.
- Pattern: exact capability routing, file-backed sidecar state, pipeline aliases, AST-first/evidence-first policy, explicit halt/dispatch behavior.

### 8. `skf-setup`
- Path: `src/skf-setup/SKILL.md`
- Role: initialize forge environment, detect tooling, select Quick/Forge/Forge+/Deep tier, and persist sidecar/config state.
- Pattern: staged reference files, deterministic helper delegation, registry/index hygiene, explicit headless result contract and failure phases.

### 9. `skf-analyze-source`
- Path: `src/skf-analyze-source/SKILL.md`
- Role: decompose a large repository into skillable units and emit actionable Skill briefs.
- Pattern: tier-adaptive file/AST/semantic analysis, auto-scope path, docs-only branch, explicit confirmation gates, machine-readable headless result.

### 10. `skf-brief-skill`
- Path: `src/skf-brief-skill/SKILL.md`
- Role: design a tight Skill scope and produce `skill-brief.yaml` for compilation.
- Pattern: favors one cohesive capability, supports ratifying pre-authored briefs, and lazy-loads references/assets only when a branch needs them.

### 11. `skf-create-skill`
- Path: `src/skf-create-skill/SKILL.md`
- Role: compile a verified Skill from a brief and source evidence.
- Pattern: load/check/extract/enrich/compile/validate/artifact/report stages; outputs provenance map and evidence report; uncitable content is excluded rather than guessed.

### 12. `skf-quick-skill`
- Path: `src/skf-quick-skill/SKILL.md`
- Role: fast source/package → Skill path without a prior brief.
- Pattern: source resolution, ecosystem check, extraction, review, write/validate, stable progress events/result envelope, batch/headless support, no-fabrication rule.

### 13. `skf-create-stack-skill`
- Path: `src/skf-create-stack-skill/SKILL.md`
- Role: create a consolidated project stack Skill.
- Pattern: code-mode derives integrations from manifests/source; compose-mode uses existing Skills/architecture and must label inferred integration claims; maintains provenance/evidence and stable halt/result contracts.

### 14. `skf-verify-stack`
- Path: `src/skf-verify-stack/SKILL.md`
- Role: read-only feasibility verification against architecture/PRD documents.
- Pattern: coverage, integration verification, requirement mapping, evidence-backed verdicts, shared feasibility schema, stable result/exit contracts.

### 15. `skf-refine-architecture`
- Path: `src/skf-refine-architecture/SKILL.md`
- Role: refine architecture using generated Skills and optional feasibility findings.
- Pattern: never delete original content; add evidence-backed gaps/issues/improvements only when supported by concrete API/type evidence.

### 16. `skf-update-skill`
- Path: `src/skf-update-skill/SKILL.md`
- Role: surgical regeneration after source changes.
- Pattern: preserve `[MANUAL]` content, re-extract changed exports only, maintain provenance, PID-file concurrency guard, detect-only/dry-run inspection modes, explicit degraded-mode handling.

### 17. `skf-audit-skill`
- Path: `src/skf-audit-skill/SKILL.md`
- Role: detect source↔Skill drift and produce severity-graded remediation guidance.
- Pattern: re-index → structural diff → optional semantic diff → severity/doc drift → report; every finding must trace to source, with tier-aware degradation and stable headless envelope.

### 18. `skf-test-skill`
- Path: `src/skf-test-skill/SKILL.md`
- Role: cognitive-completeness/quality gate before export.
- Pattern: coverage/coherence checks, optional external validators, hard gate, scoring, stable exit codes, persisted result contracts, explicit inconclusive/drift states.
- Eval boundary: test/eval workflow source was read; no validator or test run was executed.

### 19. `skf-export-skill`
- Path: `src/skf-export-skill/SKILL.md`
- Role: sole publishing gate for packaging and platform context injection.
- Pattern: load → package → snippet → managed context update → token report → summary; supports multi-Skill export and dry-run; owns managed-section/manifest contracts consumed by rename/drop.

### 20. `skf-rename-skill`
- Path: `src/skf-rename-skill/SKILL.md`
- Role: transactional rename across all versions and platform context.
- Pattern: copy → verify → delete-old, never delete before verification, collision guard, PID lock, rollback on verification failure, dry-run support.

### 21. `skf-drop-skill`
- Path: `src/skf-drop-skill/SKILL.md`
- Role: deprecate or purge a Skill/version while keeping manifest/context state coherent.
- Pattern: active-version guard, explicit destructive gate, dry-run, headless-purge policy override, context rebuild, stable halt/result semantics.

### 22. `skf-campaign`
- Path: `src/skf-campaign/SKILL.md`
- Role: multi-library, multi-session Skill-production orchestration.
- Pattern: dependency ordering, file-backed resumable campaign state, deterministic state validation, append-only decision log, explicit quality gates, headless progress/result contracts.
- Content-level significance: this formal workflow is present in live source but absent from the current `src/README.md` workflow-count sentence.

Shared BMAD implementation/tooling observed during review includes deterministic helpers for package resolution, frontmatter validation, Skill-name rewriting, result-envelope emission, state/schema validation, and trace checks. The helper code/test workflows were not executed.

## `yammaku/typewriter-video`

### 23. `typewriter-video`
- Path: `SKILL.md`
- Verification: direct body read.
- Role: Remotion-based typewriter/video B-roll production.
- Flow: gather content/sync/aspect/theme requirements → copy template/install → read engine + API/content/audio references → author timeline → configure layout → optional A-roll sync → preview → render.
- Supporting material: README links `references/API.md`, `references/content-guide.md`, `references/audio.md`, and `references/aroll-sync.md`; repository includes a concrete TypeScript/Remotion template and bundled assets.
- Pattern: cleanly separates typewriter-domain instructions from the upstream general Remotion Skill and uses progressive references for deeper API/timing knowledge.
- Runtime/eval: npm install, preview, render, audio, and Remotion execution were not performed.

## Count and verification boundary

- Repository-scoped individual Skill reports: **23**.
- Individual reports whose `SKILL.md` body was directly read: **23 / 23**.
- External marketplace/catalog references counted as local Skills: **0**.
- Placeholder/template/generated/spec-example definitions counted as local Skills: **0**.
- Runtime validation: **not executed**.
