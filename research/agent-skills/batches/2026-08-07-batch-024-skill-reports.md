# Agent Skills Deep Analysis — Batch 024 Skill Reports

Observed: 2026-08-07
Status: `structure-reviewed`
Runtime validation: `not_executed`
Direct skill bodies reviewed: **23**

These are repository-scoped reports. A report means the current skill body was read from the repository default branch (or the repository's current equivalent skill definition), not inferred from index metadata. Supporting scripts/references were inspected when present. No third-party skill was executed.

## jeffy-w/AgentSkills

### `ask`
- Path: `ask/SKILL.md`
- Role: local second-opinion/advisor wrapper for Claude, Gemini, and Codex CLIs.
- Structure: skill body + `ask/scripts/ask.js` + design note. The script validates provider selection, optionally loads a named local role prompt, constrains Codex to a read-only sandbox, captures stdout/stderr, and writes a reusable Markdown artifact under `.artifacts/ask/`.
- Strength: deterministic provider dispatch and persisted evidence rather than an informal "ask another model" convention.
- Risk/gap: successful behavior depends on external CLI installation/authentication; not executed in this review.

### `ios-device-build-run`
- Path: `ios-device-build-run/SKILL.md`
- Role: repeatable physical-iOS-device build/install/launch/log workflow.
- Structure: skill body + Python helper + OpenAI UI metadata. The helper creates durable sessions under `~/.codex/ios-device-build-run/sessions/`, discovers workspace/project/scheme/device, wraps `xcodebuild`/`devicectl`, and stores bounded/searchable logs.
- Strength: makes real-device evidence durable and separates build/runtime artifacts instead of dumping terminal output into model context.
- Risk/gap: requires a macOS/Xcode/device environment; runtime behavior was not executed.

## juncaifeng/agentskills

### `agentskill-builder`
- Path: `skills/agentskill-builder/SKILL.md`
- Role: full Agent Skills authoring workflow.
- Structure: current body plus four references: specification, best practices, evaluating skills, and optimizing descriptions.
- Strength: progressive-disclosure design; separates format rules, authoring heuristics, output-quality evaluation, and trigger-description optimization.
- Eval posture: describes with-skill/baseline comparisons, assertions, benchmarks, and trigger-eval iteration, but no dedicated repository eval runner was verified.

### `agentskill-builder-lite`
- Path: `skills/agentskill-builder-lite/SKILL.md`
- Role: standalone skill-authoring guide without external reference loading.
- Structure: embeds directory, frontmatter, writing, evaluation, and description-optimization guidance directly in one file.
- Strength: portable single-file variant.
- Trade-off: duplicates material that the full version moves into references, so maintenance drift is possible.

## danecwalker/agentskills

### `architecture`
- Path: `skills/architecture/SKILL.md`
- Role: repository topology, module boundaries, dependency direction, and structural migration guidance.
- Structure: skill body + topology/core/frontend/backend/public-pattern references.
- Strength: treats architecture as enforceable dependency boundaries rather than folder aesthetics; prefers adapting to framework-native conventions.
- Gap: guidance is source-level; no repository-level executable architecture rule suite was run here.

### `build-design-system`
- Path: `skills/build-design-system/SKILL.md`
- Role: derive and maintain production design systems from DESIGN.md, projects, screenshots, or authorized references.
- Structure: references cover source audit, component engineering, tokens/theming, system structure, framework adapters, testing/accessibility, and public sources.
- Strength: evidence ledger (`explicit/observed/derived/unresolved`), semantic-token model, accessibility contracts, incremental migration.
- Gap: the skill tells consumers to perform visual/accessibility/build verification; no target project was executed in this catalog review.

### `gauntlet`
- Path: `skills/gauntlet/SKILL.md`
- Role: builder/fresh-critic iterative quality loop against a concrete bar.
- Structure: method plus live progress-board references/template.
- Strength: requires real-artifact inspection, fresh critic separation, explicit score/evidence, and persistent progress state.
- Risk/gap: its default 10/10 stopping rule can be expensive or loop-prone if the bar is subjective; the user/cost stop conditions are therefore important. No loop was executed here.

### `hero-fx`
- Path: `skills/hero-fx/SKILL.md`
- Role: production hero/background animation design and implementation.
- Structure: references for rendering-stack selection, effect recipes, original-effect invention, and quality/performance checks.
- Strength: lightweight-stack ladder (CSS → SVG → Canvas → WebGL), reduced-motion requirement, off-screen pause guidance, and explicit anti-cloning rule.
- Gap: quality claims require actual browser/device rendering; not executed here.

## gustavhartz/agentskills

### `cf-worker-logs`
- Path: `skills/cf-worker-logs/SKILL.md`
- Role: Cloudflare Worker historical logs, metrics, and live tailing.
- Structure: one skill + dependency-light `cf-worker-logs.mts` helper. The helper discovers Wrangler config, derives account/worker identifiers, validates time/filter arguments, normalizes telemetry events, queries Cloudflare APIs, and delegates live tailing to Wrangler.
- Strength: clear distinction between stored historical telemetry and live tailing; deterministic filtering and bounded output.
- Gap: requires Cloudflare credentials/configuration and Node/Wrangler; no API or tail operation was run.

## cifuentescossio/agentskills

### `obsidian-grammar-review`
- Path: `obsidian-grammar-review/SKILL.md`
- Role: review English Markdown grammar/clarity while preserving original text.
- Structure: single self-contained skill; no scripts/references/evals observed in the inspected repository content.
- Strength: explicit non-rewrite constraint, minimal-fix output contract, and protection for code/identifiers/project terms.
- Gap: output quality is judgment-based; no eval fixtures were present in reviewed content.

## DragonL641/AgentSkills

### `your-tech-panel`
- Path: `skills/your-tech-panel/SKILL.md`
- Role: interactive product/architecture/development/QA/DevOps planning panel.
- Structure: one large orchestration skill with bundled project-document templates (PRD, architecture, development/test/DevOps planning material) in repository history/current package structure.
- Strength: deliberately elicits constraints and user decisions instead of silently choosing stack/architecture.
- Gap: very large monolithic body mixes five expert roles and document production; progressive disclosure would reduce context cost and drift risk.

## A2Y-D5L/agentskills

### `epic`
- Path: `skills/epic/SKILL.md`
- Role: dispatcher for long-running, resumable multi-phase software epics.
- Structure: subworkflow references (`run`, `implement`, `review`, `recap`, `learn-lessons`, `init`, `config`, `control`, lessons) plus deterministic shell helpers for argument parsing, path/config resolution, bounds/locks, listing, polling, lint gates, and review dispatch.
- Strength: durable state outside transient conversation context, explicit bounds/locking, phase gates, findings ledger, and premise verification.
- Risk/gap: cross-provider review and external helper assumptions create environment dependencies; scripts/review flows were read but not executed.

## svier0/agentskills

### `caveman`
- Path: `skills/caveman/SKILL.md`
- Role: persistent terse-response mode.
- Structure: single instruction file with trigger/stop behavior and clarity exceptions.
- Strength: explicitly suspends terseness for safety warnings, irreversible-operation confirmation, sequence-sensitive steps, and clarification.
- Gap: the claimed token reduction is not backed by a repository eval artifact in reviewed content.

### `github-proxy`
- Path: `skills/github-proxy/SKILL.md`
- Role: GitHub access fallback through two proxy mirrors when direct access is unavailable.
- Structure: single instruction file with primary/fallback routing and stated limitations.
- Strength: simple deterministic fallback policy.
- Risk/gap: trust, privacy, integrity, uptime, and operator guarantees of third-party mirrors are not independently verified by the repository; consumers should not treat mirrored transport as equivalent to GitHub-origin trust.

## MarieEustace/AgentSkills

### `architecture-planner`
- Path: `.agent/skills/architecture-planner/SKILL.md`
- Role: pre-implementation architecture/dependency/error-handling review.
- Strength: forces dependency justification, assumptions, error strategy, data flow, and explicit approval before implementation.
- Gap: human confirmation gate makes it intentionally non-autonomous.

### `code-reviewer`
- Path: `.agent/skills/code-reviewer/SKILL.md`
- Role: spec-grounded code review.
- Strength: separates spec matches, deviations, scope creep, and cross-cutting quality issues; asks for exact file/line evidence.
- Gap: no automated grader/eval artifact was verified.

### `commit-message-writer`
- Path: `.agent/skills/commit-message-writer/SKILL.md`
- Role: conventional commit proposal from staged diff.
- Strength: refuses to infer when staged diff is empty, constrains taxonomy/format, and requires showing the proposal before committing.

### `handover`
- Path: `.agent/skills/handover/SKILL.md`
- Role: generate a session-to-session `HANDOVER.md` from conversation plus git/project state.
- Strength: preserves goals, actions, failed approaches, rationale, next steps, file map, and current state.
- Risk/gap: depends on the agent being able to reconstruct session context accurately; generated handover still needs evidence checking.

### `refactoring-assistant`
- Path: `.agent/skills/refactoring-assistant/SKILL.md`
- Role: identify duplication and plan/apply focused refactors.
- Strength: incremental changes, explicit trade-offs, minimal diffs, strict typing preference.

### `spec-analyst`
- Path: `.agent/skills/spec-analyst/SKILL.md`
- Role: find blockers/clarifications in non-trivial specs before planning.
- Strength: distinguishes blockers from defaults and refuses to silently invent missing requirements.
- Trade-off: mandatory serial clarification can be slow for large specs.

### `spec-interview`
- Path: `.agent/skills/spec-interview/SKILL.md`
- Role: interactive feature-spec interview.
- Format finding: file is named `SKILL.md` but current frontmatter has no `name`; therefore it is an agent-specific workflow file, not fully conformant to the common Agent Skills `name` + `description` contract.
- Strength: forces deeper requirements/edge-case/trade-off discovery before writing the spec.

### `test-planner`
- Path: `.agent/skills/test-planner/SKILL.md`
- Role: derive a test plan from the specification before implementation.
- Strength: requirement-first testing, explicit setup data/mocks, happy/error/boundary/security categories, AAA structure, and refusal to invent unspecified expectations.

## Eshwari07/AgentSkills

### `anti-sycophancy-guard`
- Path: `skills/anti-sycophancy-guard/SKILL.md`
- Role: critical-evaluation behavior for architecture, research, strategy, and brainstorming.
- Structure: skill body + references for sycophancy patterns, critical-evaluation dimensions/intensity, and response examples; README also stores comparison artifacts as motivation/evidence examples.
- Strength: evaluate-before-endorse rule, evidence-based resistance to unsupported pushback, explicit assumptions/alternatives/complexity checks, and calibrated critique rather than automatic contrarianism.
- Gap: repository examples are demonstrations rather than a controlled reusable eval harness; cited research claims were not independently revalidated in this batch.

## Batch-wide observations

- 23 current skill bodies/equivalent definitions were directly read.
- No repository in this batch was marked complete from stars/name/description metadata alone.
- Supporting executable code was directly inspected for `jeffy-w/AgentSkills` and `gustavhartz/agentskills`; A2Y-D5L and Colonel-like system-skill tooling was inspected only for the selected A2Y repository, while this batch intentionally did not execute third-party helpers.
- Dedicated repository eval runners were not verified for this batch. Several skills contain evaluation methodology or example artifacts, especially `juncaifeng/agentskills`, `danecwalker/agentskills`, and `Eshwari07/AgentSkills`; these are not equivalent to an executed eval result.
- Runtime status for every report remains `not_executed`.