# Agent Skills Individual Reports — Batch 052

Observed: 2026-08-09

Validation boundary: every report below is based on direct `SKILL.md` content inspection at the pinned repository revision, plus repository-local scripts/references/tests where noted. No Skill was executed and no behavioral pass result is claimed.

## 1. `Ckzzz1/claude-code-longrun-skill::claude-code-longrun`

- **Pinned revision:** `9ca7634840f9ee865f09d4dba76b33ac2fc80f43`
- **Role:** unattended/long-running Claude Code task orchestration.
- **Structure:** one Skill plus two operational references; no scripts, tests, or evals in the pinned tree.
- **Useful design:** dedicated tmux session, persistent task file, low-frequency observation, resume/recovery rather than repeated restart, explicit escalation conditions, and instructions not to store secrets in task state.
- **Risk:** the documented preferred worker launch uses `--permission-mode bypassPermissions`. This weakens the normal execution-approval boundary and should not become a catalog-wide default.
- **Verification gap:** no repository-local harness proves restart behavior, timeout/termination handling, side-effect containment, or task recovery.
- **Catalog lesson:** separate long-running state/recovery design from authorization. The orchestration layer should enforce workspace, command, network and side-effect policy.

## 2. `iflow-mcp/kambleakash0-agent-skills::code-review`

- **Pinned Skill blob:** `85c0e55951b76d54f1dbadca88118fa48d97d9c8`
- **Role:** prioritized review of diffs/files/PRs across correctness, security, performance, maintainability, tests and project conventions.
- **Useful design:** requires gathering the actual diff plus surrounding code/tests/configuration before judging; output severity is separated into must-fix, should-fix and suggestions; findings are expected to include concrete locations/fixes.
- **Risk:** fetching a PR or evaluating dependency vulnerability status may require external tooling/current data, but the Skill does not define a deterministic source/provenance contract for those checks.
- **Verification gap:** no behavioral eval proving issue recall, false-positive rate, severity calibration or merge-readiness decisions.
- **Catalog lesson:** review Skills should bind conclusions to actual diff/context evidence and keep severity/actionability explicit.

## 3. `iflow-mcp/kambleakash0-agent-skills::deep-codebase-audit`

- **Role:** repository-wide audit/refactor workflow with progressive disclosure.
- **Useful design:** inspect architecture and evidence first, separate findings from changes, require confirmation before refactoring, then verify after modifications. Long supporting material is moved into references rather than overloading the dispatcher.
- **Risk:** a broad audit can expand without a resource or stopping budget; the Skill should ideally define bounded scope, maximum passes and evidence needed to reopen an area.
- **Verification gap:** references describe the method, but there is no repository-local behavioral benchmark for audit coverage or regression avoidance.
- **Catalog lesson:** progressive disclosure plus explicit transition from review to mutation is preferable to an audit Skill that immediately edits code.

## 4. `iflow-mcp/kambleakash0-agent-skills::domain-glossary`

- **Role:** derive a domain glossary from repository/product evidence.
- **Useful design:** definitions should be grounded in code/docs, uncertainty should be visible, and the agent should avoid inventing domain meaning that cannot be supported by the repository.
- **Risk:** terms can have competing meanings across bounded contexts; a single flat glossary can accidentally collapse context-specific language.
- **Verification gap:** no fixture corpus tests term extraction, source attribution, context separation or confidence calibration.
- **Catalog lesson:** domain-modeling Skills should record source/evidence and bounded context with each term, not only the final definition.

## 5. `iflow-mcp/kambleakash0-agent-skills::english-humanizer`

- **Role:** rewrite generated/unnatural English into more human prose.
- **Useful design:** focused transformation responsibility rather than bundling content research and rewriting into one Skill.
- **Risk:** “human” style is subjective and can erase technical precision, author voice or required terminology if applied indiscriminately.
- **Verification gap:** no style rubric/eval set proving meaning preservation, tone adherence or reduction of stereotyped AI-writing patterns.
- **Catalog lesson:** writing Skills benefit from explicit invariants—meaning, facts, terminology, audience and format—plus preference-based style criteria.

## 6. `iflow-mcp/kambleakash0-agent-skills::git-workflow`

- **Role:** guided Git branch/commit/rebase/push/PR workflow.
- **Useful design:** requires user confirmation before Git operations and distinguishes ordinary feature-branch operations from higher-risk history changes; uses safer force semantics (`--force-with-lease`) rather than unconditional force push.
- **Risk:** amend/rebase/push/PR creation are external or history-mutating side effects. A Skill-local confirmation rule can conflict with other Skills unless the orchestrator owns the final authority.
- **Verification gap:** no sandbox Git fixture suite verifies branch detection, dirty-worktree handling, conflicts, upstream tracking, failure recovery or repeated invocation.
- **Catalog lesson:** Git mutation should be governed by a shared side-effect policy; Skills should request operations, not define their own ultimate authorization model.

## 7. `iflow-mcp/kambleakash0-agent-skills::grill-master`

- **Role:** challenge a proposal/implementation through adversarial questioning before accepting it.
- **Useful design:** introduces deliberate skepticism and pressure-testing instead of assuming the first proposed design is correct.
- **Risk:** without a bounded objective, evidence threshold and termination rule, repeated challenge can turn into an optimization loop rather than improve the artifact.
- **Verification gap:** no eval set measures whether questioning discovers real defects versus generating speculative objections.
- **Catalog lesson:** adversarial-review Skills need explicit stop conditions and a rule that new iterations require new evidence, actual failure or changed constraints.

## 8. `iflow-mcp/kambleakash0-agent-skills::incremental-tdd`

- **Role:** implement behavior in small test-first increments.
- **Useful design:** keeps the feedback loop small and treats commit/push/PR creation as opt-in rather than implicit consequences of implementation.
- **Risk:** a purely local red-green-refactor loop can still miss integration/browser/runtime behavior if the validation ladder is not tied to the changed risk surface.
- **Verification gap:** the Skill itself has no behavioral eval proving that generated tests fail before the fix, cover the intended behavior, and avoid duplicating production logic.
- **Catalog lesson:** TDD Skills should record pre-fix failure evidence and map each change to the lowest sufficient validation level plus required integration/runtime gates.

## 9. `iflow-mcp/kambleakash0-agent-skills::script-writer`

- **Role:** produce maintainable automation/utility scripts.
- **Useful design:** separates script-writing conventions from broader implementation planning and encourages explicit inputs, failure handling and usable command surfaces.
- **Risk:** scripts often become a hidden side-effect surface (filesystem, subprocesses, network, credentials); generic guidance needs an execution/safety contract above it.
- **Verification gap:** no fixture-based portability/error-path suite for generated scripts.
- **Catalog lesson:** script Skills should specify idempotency, failure behavior, dry-run/preview expectations and environment assumptions where side effects exist.

## 10. `iflow-mcp/kambleakash0-agent-skills::slice-the-spec`

- **Role:** decompose a larger specification into bounded implementation slices.
- **Useful design:** supports incremental delivery rather than translating a long spec directly into a monolithic task; useful bridge between requirements and executable work.
- **Risk:** slice boundaries can accidentally split invariants or create dependency-heavy “independent” tasks unless dependencies and acceptance evidence are explicit.
- **Verification gap:** no benchmark checks whether produced slices are independently implementable, dependency-complete and collectively cover the source spec.
- **Catalog lesson:** each slice should carry source requirement IDs, dependencies, acceptance criteria and a verification plan.

## 11. `iflow-mcp/kambleakash0-agent-skills::spec-to-plan`

- **Role:** convert an existing specification into an implementation plan.
- **Useful design:** explicitly read-only: planning is separated from editing/executing, which creates a clean authorization and review boundary.
- **Risk:** plans can become speculative if repository reality is not checked against the specification before sequencing work.
- **Verification gap:** no plan-quality eval checks file/path correctness, dependency ordering, acceptance coverage or stale assumptions.
- **Catalog lesson:** keep planning non-mutating and require repository-grounded references for every implementation step that asserts a concrete location or dependency.

## 12. `iflow-mcp/kambleakash0-agent-skills::spec-writer`

- **Role:** turn product/engineering intent into a structured implementation specification.
- **Useful design:** isolates specification quality from coding and creates an artifact that downstream slicing/planning Skills can consume.
- **Risk:** prose-only requirements can remain ambiguous or become hard to validate mechanically if IDs, invariants, contracts and acceptance cases are not made structured enough for downstream tools.
- **Verification gap:** no schema/lint/eval establishes requirement completeness, contradiction detection or traceability into implementation/tests.
- **Catalog lesson:** a strong spec layer should combine readable Markdown with stable IDs and machine-parseable contracts/acceptance data where appropriate.

## 13. `iflow-mcp/kambleakash0-agent-skills::spec-to-plan` workflow companion note

The pinned collection's overall value is not any single planning prompt but the explicit chain `spec-writer → slice-the-spec → spec-to-plan → incremental-tdd → code-review`, with `deep-codebase-audit`, `domain-glossary`, Git and writing utilities as supporting capabilities. This batch therefore counts the eleven actual Skill bodies once each; the companion note is not an additional report in totals.

## 13. `5kon/html-ppt-skill::html-ppt` — 14-deck snapshot

- **Pinned revision:** `9f99b12b1245b05e8db1c3efc9844a3961e041c0`
- **Pinned Skill blob:** `05d9ea037f9a664e9af53403222e7dac7bef6135`
- **Role:** static HTML presentation authoring using themes, page layouts, animations, reusable deck templates and a keyboard runtime.
- **Structure:** 36 themes, 14 full-deck templates, 31 single-page layouts, 27 CSS animations, 20 canvas FX, references, scaffold/render scripts and screenshot artifacts.
- **Useful design:** token-driven visual system, template-first authoring, progressive reference catalogs, no application build step, explicit speaker-note/runtime conventions.
- **Observed drift:** the same Skill advertises 31 layouts but later says to add a new layout only if none of the “30” fit. README's multiplication-style “= 101 PPT skills” slogan is not valid arithmetic and should not be treated as authoritative inventory logic.
- **Script risk:** `scripts/render.sh` hard-codes the macOS Chrome binary and invokes headless Chrome with `--no-sandbox`; that is non-portable and weakens browser isolation.
- **Verification gap:** screenshot inventory and render code exist, but the pinned revision was not rendered or compared in this batch.
- **Catalog lesson:** generate inventory counts from the tree and separate visual artifacts from reproducible visual-regression results.

## 14. `jianyun19999/html-ppt-skill::html-ppt` — presenter-mode intermediate snapshot

- **Pinned revision:** `15fb85f05b3092b00e5a4eb181227339fe1af679`
- **Pinned Skill blob:** `0250b9ac962e2673d8a1b2a88f5782ad0378aba5`
- **Role:** the same static presentation system after adding the 15th presenter-focused full-deck template and richer presenter runtime guidance.
- **New structure/behavior:** `presenter-mode-reveal`, Chinese README, dedicated presenter reference, notes/script guidance, popup presenter cards, iframe `?preview=N`, `BroadcastChannel` synchronization, `postMessage` slide updates, timer and persisted card layout.
- **Useful design:** presenter and audience views reuse the same deck/runtime rather than maintaining an unrelated rendering stack; notes are explicitly separated from audience-facing slide content.
- **Observed drift:** headline inventory says 15 decks while later README quick-start/tree captions and multiple Skill sections still say 14. This is direct evidence that hand-maintained inventory text drifts even within a well-structured package.
- **Script risk:** the render path still hard-codes macOS Chrome and `--no-sandbox`.
- **Verification gap:** no browser/runtime test was executed for popup handling, cross-window synchronization, preview correctness, persistence or visual equivalence. “Pixel-perfect” and “no flicker” remain claims for this review state.
- **Catalog lesson:** UI/output Skills need executable visual/runtime validation; documentation claims should not be promoted to verified behavior without browser evidence.

## Batch report count

The materialized report count for this file is **14**: 1 long-running Skill + 11 Kamble Skills + 2 distinct html-ppt content snapshots. `wanli15nian/skills` and five additional old html-ppt fork identities were directly content-gated but exact-tree reused, so they do not create duplicate individual reports.