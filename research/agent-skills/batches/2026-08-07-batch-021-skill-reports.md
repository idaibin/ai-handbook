# Agent Skills deep analysis — Batch 021 individual skill reports

Observed: 2026-08-07

Scope: repository-scoped formal Skill definitions verified from actual repository content during Batch 021. A report is created only when a concrete `SKILL.md` body/path was verified or, for the BMAD inventory-only entries, when the exact `SKILL.md` path and dispatch role were verified from the live repository. External skills referenced by catalogs are not counted as local skills.

Runtime validation was not executed in this batch.

## ersinkoc/project-architect

### 1. `project-architect`

- Path: `SKILL.md`
- Verification: direct body read.
- Type: methodology / project-planning Skill.
- Core flow: structured discovery followed by `SPECIFICATION.md`, `IMPLEMENTATION.md`, `TASKS.md`, optional `BRANDING.md`, then synthesized `PROMPT.md`.
- Supporting material: `references/` contains elicitation, tech-stack, design-pattern, specification, implementation, tasks, branding, and prompt guides; `references/elicitation-guide.md` was directly read.
- Design value: separates discovery from artifact generation and places explicit review gates between major planning outputs instead of generating an opaque one-shot plan.
- Validation boundary: no repository-local eval runner was observed in the reviewed root/reference paths; no workflow was executed.

## zht043/AgentSkills

This repository is explicitly deprecated and documents a migration to independent repositories. Reports below describe formal Skill definitions that still physically exist in the repository; they are not treated as current recommended distribution targets.

### 2. `agent-skills`

- Path: `SKILL.md`
- Verification: direct body read.
- Status: legacy repository-level router/instruction Skill.
- Purpose: requires deep reading of selected Skill trees, including scripts/config where present, and defines progressive loading plus a capability index.
- Important caveat: its capability index still names suites that the current README says have been split into independent repositories, so the root Skill is historical/partially stale relative to the repository's current deprecation notice.

### 3. `skill-creator`

- Path: `skill-creator/SKILL.md`
- Verification: direct body read.
- Status: legacy copy; README says this capability moved to the independent `agent-skill-architect` repository.
- Purpose: meta-Skill for turning exploration results into reusable Skills; distinguishes capability vs process Skills and single-Skill vs suite layouts.
- Notable pattern: defines explicit frontmatter fields, extraction-to-validation workflow, and requires a fresh-session trial before considering a new Skill verified.

### 4. `markdown-mermaid-illustrator`

- Path: `skills/markdown-mermaid-illustrator/SKILL.md`
- Verification: direct body read.
- Status: README marks it canonical but pending migration.
- Purpose: generate/refactor Mermaid diagrams for Markdown, with chart-type routing, dark/light compatibility rules, semantic shapes, layout constraints, and user confirmation before replacement.
- Supporting assets: the Skill references template YAML files for multiple Mermaid chart families; no template execution was performed.

### 5. `doc-illustrator`

- Path: `skills/doc-illustrator/SKILL.md`
- Verification: direct body read.
- Status: README marks it legacy and recommends `markdown-mermaid-illustrator` instead.
- Purpose: analyze technical documents, generate Mermaid candidates by template match or model reasoning, preview, confirm, then replace.
- Design note: useful as historical evidence of the narrower predecessor that the canonical Skill supersedes.

### 6. `export-history`

- Path: `skills/export-history/SKILL.md`
- Verification: direct body read; implementation script also read.
- Purpose: export local Claude Code JSONL conversation history into a single searchable HTML file.
- Script: `skills/export-history/scripts/export-claude-history.mjs` traverses local project-session files, parses user/assistant text, escapes HTML, and generates the viewer.
- Validation boundary: script body was reviewed but not executed against local conversation data.

## armelhbobdad/bmad-module-skill-forge

Content-level correction: `src/README.md` still describes Ferris plus 14 workflow Skills, but the live repository also contains `src/skf-campaign/SKILL.md`. Batch 021 therefore records 16 formal repository-scoped `SKILL.md` definitions: Ferris + 14 documented workflows + Campaign.

Direct-body-reviewed entries are marked separately from inventory/path-verified entries. Inventory/path-verified does not mean the full body was read.

### 7. `skf-forger`

- Path: `src/skf-forger/SKILL.md`
- Verification: direct body read.
- Role: central Ferris persona/dispatcher across Architect, Surgeon, Audit, Delivery, and Management modes.
- Pattern: exact capability routing, file-backed sidecar state, explicit pipeline aliases, and a zero-hallucination/AST-first evidence policy.

### 8. `skf-setup`

- Path: `src/skf-setup/SKILL.md`
- Verification: exact path + role inventory verified from live repository and Ferris capability table; body not fully read in this batch.
- Role: initialize the Skill Forge environment, detect tooling, and establish forge tier/configuration.

### 9. `skf-analyze-source`

- Path: `src/skf-analyze-source/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: discover candidate Skill scopes from a source repository and produce recommended briefs.

### 10. `skf-brief-skill`

- Path: `src/skf-brief-skill/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: guided discovery for defining a Skill scope and brief.

### 11. `skf-create-skill`

- Path: `src/skf-create-skill/SKILL.md`
- Verification: direct body read.
- Role: compile a Skill from a brief and source evidence.
- Pattern: staged load/check/extract/enrich/compile/validate/artifact/report flow; outputs provenance map and evidence report; detailed content is progressively moved into `references/`.
- Validation boundary: workflow definitions were read; external validators and compilation were not run.

### 12. `skf-quick-skill`

- Path: `src/skf-quick-skill/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: fast Skill creation from a package name or GitHub URL without a prior brief.

### 13. `skf-create-stack-skill`

- Path: `src/skf-create-stack-skill/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: create a consolidated stack Skill that captures cross-library integration patterns.

### 14. `skf-verify-stack`

- Path: `src/skf-verify-stack/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: pre-code feasibility verification of a proposed stack against architecture/PRD context.

### 15. `skf-refine-architecture`

- Path: `src/skf-refine-architecture/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: refine architecture documentation using verified Skill data and stack-verification findings.

### 16. `skf-update-skill`

- Path: `src/skf-update-skill/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: regenerate/update a Skill while preserving designated manual sections after source changes.

### 17. `skf-audit-skill`

- Path: `src/skf-audit-skill/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: detect drift between a generated Skill and its current source.

### 18. `skf-test-skill`

- Path: `src/skf-test-skill/SKILL.md`
- Verification: direct body read.
- Role: cognitive-completeness/quality gate before export.
- Pattern: coverage/coherence analysis, optional external validators, hard gate, scoring, stable exit codes, and machine-readable result envelopes for orchestration.
- Eval boundary: the test/eval workflow definition was reviewed, but no test run or external validator was executed.

### 19. `skf-export-skill`

- Path: `src/skf-export-skill/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: package a Skill for distribution and inject relevant context into agent instruction surfaces.

### 20. `skf-rename-skill`

- Path: `src/skf-rename-skill/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: transactional rename across Skill versions/artifacts.

### 21. `skf-drop-skill`

- Path: `src/skf-drop-skill/SKILL.md`
- Verification: exact path + role inventory verified; body not fully read.
- Role: deprecate or purge a Skill through the module's managed lifecycle.

### 22. `skf-campaign`

- Path: `src/skf-campaign/SKILL.md`
- Verification: direct body read.
- Role: multi-library Skill-production orchestration across many sessions.
- Pattern: file-backed resumable state, dependency ordering, explicit quality gates, append-only decision log, deterministic state validation, and stable headless result/exit contracts.
- Content-level significance: this formal Skill exists in the live repository but is not included in the current `src/README.md` workflow-count sentence.

Shared tooling observed in the repository includes deterministic helper scripts such as frontmatter validation, package resolution, Skill-name rewriting, and no-trace verification. Their existence was verified from live paths; they were not executed.

## yammaku/typewriter-video

### 23. `typewriter-video`

- Path: `SKILL.md`
- Verification: direct body read.
- Type: single domain Skill for Remotion-based typewriter/video B-roll generation.
- Structure: staged requirements gathering, project setup, engine/reference reading, content authoring, aspect-ratio configuration, optional narration sync, preview, and render.
- Supporting material: README points to `references/API.md`, `references/content-guide.md`, `references/audio.md`, and `references/aroll-sync.md`; the Skill also ships a concrete TypeScript/Remotion template and bundled assets.
- Design value: distinguishes typewriter-domain knowledge from the upstream general Remotion Skill and uses references for deeper API/content/audio timing detail.
- Validation boundary: source/instructions were reviewed, but npm install, preview, render, audio, or Remotion execution was not performed.

## Summary

- Repository-scoped Skill reports created in Batch 021: **23**.
- Direct-body-reviewed Skill reports: project-architect (1), zht043 legacy/residual definitions (5), BMAD direct subset (4), typewriter-video (1) = **11**.
- BMAD inventory/path-verified reports with body not fully read: **12**.
- External catalog entries and generated/example-only Skill forms were intentionally excluded from local Skill counts.
- Runtime validation: **not executed**.
