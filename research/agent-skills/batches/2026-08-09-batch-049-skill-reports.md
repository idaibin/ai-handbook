# Repository-scoped Skill Reports — Batch 049

- observed_at: `2026-08-09`
- repository identities completed: `10`
- new individual Skill reports: `45`
- status: `structure-reviewed`
- runtime_validation: `not_executed`

Only directly inspected Skill bodies are reported as new individual reports. Four independently content-gated Wondel repository identities map to an exact tree already reviewed, so they do not create duplicate reports.

## `ballbadboy/agentskills` — 21 reports

Repository context: all 21 `SKILL.md` bodies were directly read. The repository also contains plugin manifests, command wrappers, three agent prompts, four root references, an `idea-refine` support bundle, hook scripts, a hook regression script and plugin-install CI. No repository-level behavioral eval suite for Skill selection/execution was found.

### `api-and-interface-design`
- **Pinned revision:** `82ceff41ed4d3c644e3dcca8a0514390b2911223`
- **Verified capability:** contract-first API/interface design guidance covering stable boundaries, errors, compatibility and validation before implementation.
- **Strengths:** makes interfaces and failure semantics explicit instead of letting implementation details become the contract.
- **Gaps / risks:** methodology only; no repository-local API fixture/eval proves generated contracts are correct for a target stack.
- **Validation:** source-reviewed only.

### `browser-testing-with-devtools`
- **Verified capability:** browser runtime verification using DevTools signals such as DOM, console, network, screenshots and performance evidence.
- **Strengths:** explicitly treats page/browser content as untrusted data and distinguishes runtime evidence from code inspection.
- **Gaps / risks:** depends on host/browser tooling; navigation and page-side effects need external authorization policy. No behavioral browser eval is stored here.
- **Validation:** source-reviewed only; browser not launched.

### `ci-cd-and-automation`
- **Verified capability:** CI/CD workflow design with repeatable quality gates, deployment checks and rollback awareness.
- **Strengths:** pushes validation into automation rather than relying on prose review.
- **Gaps / risks:** example commands and deployment policies are stack-dependent; no pipeline fixture demonstrates portability across repositories.
- **Validation:** source-reviewed only.

### `code-review-and-quality`
- **Verified capability:** structured code review across correctness, maintainability, testing, security/performance concerns and actionable severity.
- **Strengths:** emphasizes concrete failure scenarios and evidence rather than cosmetic commentary.
- **Gaps / risks:** review precision/recall and severity calibration are not benchmarked by repository-local evals.
- **Validation:** source-reviewed only.

### `code-simplification`
- **Verified capability:** behavior-preserving simplification with scope discipline and verification after edits.
- **Strengths:** explicitly resists speculative abstractions and unnecessary cleanup.
- **Gaps / risks:** “simpler” remains partly judgmental; repository does not provide a corpus proving behavior preservation across transformations.
- **Validation:** source-reviewed only.

### `context-engineering`
- **Verified capability:** selects and stages task-relevant context instead of loading the whole repository/session indiscriminately.
- **Strengths:** progressive context loading and explicit context-budget thinking are useful for agent reliability.
- **Gaps / risks:** performance claims about context size are guidance rather than in-repository measurements; no context-selection benchmark is present.
- **Validation:** source-reviewed only.

### `debugging-and-error-recovery`
- **Verified capability:** reproduce → inspect → localize → fix → regression-guard debugging workflow.
- **Strengths:** separates symptoms, hypotheses and evidence and discourages speculative fixes.
- **Gaps / risks:** effectiveness depends on executable target/test access; no bug corpus/eval is included.
- **Validation:** source-reviewed only.

### `deprecation-and-migration`
- **Verified capability:** staged deprecation/migration planning with compatibility, consumer discovery, rollout and removal gates.
- **Strengths:** treats migration as a contract/lifecycle problem rather than a one-shot rename.
- **Gaps / risks:** example schedules and compatibility choices need project-specific evidence; no migration simulator/eval exists.
- **Validation:** source-reviewed only.

### `documentation-and-adrs`
- **Verified capability:** maintainable documentation and ADR creation focused on rationale, alternatives and consequences.
- **Strengths:** preserves decision context rather than only describing the final state.
- **Gaps / risks:** document quality/freshness is not automatically checked beyond normal repository review.
- **Validation:** source-reviewed only.

### `frontend-ui-engineering`
- **Verified capability:** production UI workflow covering accessibility, responsive behavior, runtime inspection and user-visible verification.
- **Strengths:** backed by an accessibility reference and pushes verification beyond static JSX/CSS inspection.
- **Gaps / risks:** accessibility/performance checklist values are useful defaults but not proof that a generated UI conforms; no visual/accessibility eval corpus is included.
- **Validation:** source-reviewed only.

### `git-workflow-and-versioning`
- **Verified capability:** branch/commit/version-control workflow with atomic changes and verification around Git operations.
- **Strengths:** encourages inspectable history and scoped commits.
- **Gaps / risks:** guidance includes destructive reset operations; a generalized version needs explicit dirty-tree/user-authorization gates before destructive Git commands.
- **Validation:** source-reviewed only; Git commands not executed.

### `idea-refine`
- **Verified capability:** divergent/convergent ideation using supporting frameworks, refinement criteria, examples and a small setup script.
- **Strengths:** references are separated from the main Skill and selected contextually instead of mechanically applying every framework.
- **Gaps / risks:** invocation guidance contains a host-specific absolute `/mnt/skills/...` path even though the script is repository-local; this reduces portability. Evaluation criteria are qualitative rather than benchmarked.
- **Validation:** `frameworks.md`, `refinement-criteria.md`, examples and `idea-refine.sh` were source-reviewed; script not executed.

### `incremental-implementation`
- **Verified capability:** thin-slice implementation with verification checkpoints after each increment.
- **Strengths:** bounds change size and reduces unverified multi-file leaps.
- **Gaps / risks:** “small enough” remains context-sensitive; no repository-local execution benchmark measures defect reduction.
- **Validation:** source-reviewed only.

### `performance-optimization`
- **Verified capability:** measure-first performance workflow spanning frontend/backend diagnosis and post-change comparison.
- **Strengths:** discourages optimization without measurement; root performance reference includes concrete observability commands.
- **Gaps / risks:** bundle/API thresholds are defaults, not universal requirements or repository-measured guarantees.
- **Validation:** source-reviewed only; no benchmark executed.

### `planning-and-task-breakdown`
- **Verified capability:** dependency-ordered decomposition into small tasks with acceptance criteria and verification steps.
- **Strengths:** makes “done” and validation part of each task rather than a final afterthought.
- **Gaps / risks:** decomposition quality is not behaviorally evaluated; file-count/task-size heuristics may not fit every architecture.
- **Validation:** source-reviewed only.

### `security-and-hardening`
- **Verified capability:** defensive application-security workflow covering authn/authz, validation, secrets, dependencies, data exposure and OWASP-style risks.
- **Strengths:** supported by a reusable security checklist; consistently favors least privilege and boundary validation.
- **Gaps / risks:** checklist compliance is not equivalent to a security assessment; no vulnerable-app fixture or exploit/regression eval is included.
- **Validation:** source-reviewed only.

### `shipping-and-launch`
- **Verified capability:** pre-launch gates, deployment, monitoring and rollback planning.
- **Strengths:** requires rollback/observability thinking before declaring a release complete.
- **Gaps / risks:** examples can push/revert/deploy externally; these are consequential side effects and need explicit host-level authorization. Rollout thresholds are heuristic defaults.
- **Validation:** source-reviewed only; no deployment performed.

### `source-driven-development`
- **Verified capability:** implementation grounded in primary/official documentation and version-specific source evidence.
- **Strengths:** directly counters invented APIs and stale-memory implementation.
- **Gaps / risks:** source authority/freshness still requires judgment; no benchmark tests citation selection or API correctness.
- **Validation:** source-reviewed only.

### `spec-driven-development`
- **Verified capability:** gated `SPECIFY → PLAN → TASKS → IMPLEMENT` flow with assumptions, commands, structure, style, testing, boundaries and success criteria.
- **Strengths:** turns vague instructions into explicit, testable conditions and keeps the spec alive as decisions change.
- **Gaps / risks:** its mandatory human-review gates are well suited to interactive work but can block non-interactive automation unless a pre-authorized policy exists.
- **Validation:** source-reviewed only.

### `test-driven-development`
- **Verified capability:** RED → GREEN → REFACTOR, bug-reproduction-first testing, test sizing, state-based assertions and browser runtime verification.
- **Strengths:** explicitly rejects “tests pass” without actual execution and distinguishes unit/integration/E2E confidence.
- **Gaps / risks:** the repository contains guidance/reference examples but no behavioral eval proving agents consistently follow RED-first discipline.
- **Validation:** `SKILL.md` and `references/testing-patterns.md` read; tests not executed.

### `using-agent-skills`
- **Verified capability:** meta-router mapping development phases to the other Skills, with global rules for assumptions, confusion, pushback, simplicity, scope and verification.
- **Strengths:** makes workflow composition explicit instead of relying on ad-hoc Skill selection.
- **Gaps / risks:** routing accuracy is not evaluated; its “stop and ask” behavior needs an alternative policy in unattended/headless execution.
- **Validation:** source-reviewed only.

### Repository implementation note

`hooks/simplify-ignore.sh` is real stateful code: it temporarily replaces protected blocks with hashed placeholders, keeps backups/cache and restores on stop. `hooks/simplify-ignore-test.sh` defines 10 regression cases covering single/multi-line blocks, multiple blocks, reasons, newline preservation, unclosed blocks, HTML syntax and malformed JSON. `.github/workflows/test-plugin-install.yml` validates plugin structure and installability. These artifacts were inspected but **not executed**, so no passing result is claimed.

## `yhughk/adversarial-verification` — 1 report

### `adversarial-verification`
- **Pinned revision:** `909a2f70fc0de13aff1175c0b507ec24bf0b4815`
- **Verified capability:** evidence-first validation requiring real command execution, verbatim outputs, negative/adversarial probes and explicit PASS/FAIL/PARTIAL outcomes.
- **Strengths:** strongly separates claims from observations and forces failure-path testing.
- **Gaps / risks:** no scripts/tests/evals in the repository. Verification work has no explicit resource/attempt budget, so rigorous behavior can become unbounded on large tasks; external execution authorization is also outside the Skill.
- **Validation:** source-reviewed only.

## `benjaminyanjd/life-algorithm-skill` — 1 report

### `life-algorithm`
- **Pinned revision:** `d4db60bb56b876d16c5d35355ad58aa85ff146c7`
- **Evidence read:** README, root `SKILL.md`, `quick-map.md`, `guide.md`, `examples.md`.
- **Verified capability:** converts uncertain decisions into constraints, a minimal decision model, concrete next action, “do not do” boundary and evidence that would change the conclusion.
- **Strengths:** action-oriented output contract and explicit uncertainty/stop conditions.
- **Gaps / risks:** probability/value formulas and examples are heuristics; no calibration dataset or outcome eval demonstrates predictive quality.
- **Validation:** source-reviewed only.

## `rogeriochaves/skills` — 6 reports

### `orchestrate`
- **Pinned revision:** `49b5fdb2d8e8ab4b7c1cf5e926101628c0b0f728`
- **Verified capability:** multi-stage implementation orchestration combining BDD/integration tests, CI/reviewer loops and dogfooding.
- **Strengths:** requires observed validation before completion and composes multiple verification surfaces.
- **Gaps / risks:** tightly coupled to organization-specific repositories/paths and public screenshot workflows; generalized use needs configurable adapters and authorization gates.
- **Validation:** source-reviewed only.

### `browser-qa`
- **Verified capability:** browser QA using DevTools-style inspection plus screenshots and environment preparation.
- **Strengths:** emphasizes visible runtime evidence.
- **Gaps / risks:** includes process killing, DB seeding and screenshot publishing commands; these are consequential side effects and should not run from Skill activation alone.
- **Validation:** source-reviewed only; no browser/database operation executed.

### `drive-pr`
- **Verified capability:** PR-monitoring/reviewer-driving loop with a substantial `pr-watch.sh` helper, persistent state, REST polling and cache-aware snapshots.
- **Strengths:** external observation is moved into deterministic script state instead of repeated LLM prose polling; the helper includes a diff-test mode.
- **Gaps / risks:** measured cache/TTL guidance is not accompanied by preserved benchmark evidence; persistent polling and comment actions need rate/resource budgets. The built-in test mode was not run.
- **Validation:** source-reviewed only.

### `nexus-room`
- **Verified capability:** workflow for a specific Nexus room/deployment environment using local project configuration and tokens.
- **Strengths:** operational details are concrete rather than abstract.
- **Gaps / risks:** strongly host-/organization-specific (`~/Projects/...`, deployment environment, credentials), so reuse without an adapter layer is low.
- **Validation:** source-reviewed only.

### `reuse-worktree`
- **Verified capability:** reuses/prepares Git worktrees for repeated agent work.
- **Strengths:** attempts to keep parallel work isolated and deterministic.
- **Gaps / risks:** contains `git reset --hard origin/main`; a reusable version needs a strict clean-tree check plus explicit authorization before destructive reset.
- **Validation:** source-reviewed only.

### `review`
- **Verified capability:** code/PR review workflow that can post review results while intentionally avoiding approval/merge authority.
- **Strengths:** separates review from merge decisions.
- **Gaps / risks:** posting a review is still an external write side effect; “do not merge” is insufficient as the only authorization boundary.
- **Validation:** source-reviewed only.

## `lx-wnk/skills` — 15 reports

Repository context: all 15 Skill bodies were read. `scripts/sync-registry.mjs` and `.github/workflows/ci.yml` provide deterministic structural conformance and registry-drift checks. ATOM's `runbook.md` and `comms-protocol.md` were also inspected. No repository-level behavioral Skill eval suite was found.

### `agent-context-init`
- **Pinned revision:** `b66badb0a1f42bbaab2bce01a80f52fc2c6df2da`
- **Verified capability:** bootstraps Agent-Context by resolving a release tag, fetching a release-pinned setup prompt and creating shared/project context layers.
- **Strengths:** avoids mutable `main`; explicitly identifies remote prompt execution as a trust boundary and requires confirmation before agent/plugin/settings expansion.
- **Gaps / risks:** pinned tags are not full tamper resistance without protected releases/tags; remote prompt behavior itself was not executed or independently pinned by digest.
- **Validation:** source-reviewed only.

### `agent-context-update`
- **Verified capability:** updates shared Agent-Context infrastructure while preserving project-owned context/memory, with additive configuration merging.
- **Strengths:** explicit “never touched” list and consent before trust-expanding updates.
- **Gaps / risks:** still follows remotely fetched release content; compatibility and merge behavior lack repository-local behavioral fixtures.
- **Validation:** source-reviewed only.

### `architecture-design`
- **Verified capability:** system-level architecture design with explicit boundaries, quality attributes, tradeoffs and evidence.
- **Strengths:** separates architecture decisions from component implementation details and requires decision rationale.
- **Gaps / risks:** design quality remains review-based; no architecture benchmark/eval establishes correctness.
- **Validation:** source-reviewed only.

### `architecture-review`
- **Verified capability:** read-only system-level architecture review grounded in actual repository evidence.
- **Strengths:** explicitly avoids hypothetical failure invention and separates observed facts from recommendations.
- **Gaps / risks:** completeness/severity calibration is not evaluated against a known-defect corpus.
- **Validation:** source-reviewed only.

### `atom-operating-model`
- **Verified capability:** PM/coordinator operating model for worktree-isolated parallel agent streams with topology rules, contracts-first coordination, bounded peer communication and integration checks.
- **Strengths:** clearly distinguishes interactive full mesh from headless synchronous subset; requires `git log`/CI verification instead of trusting worker prose.
- **Gaps / risks:** can spawn many workers/worktrees/PRs and therefore needs a host-level concurrency/cost/side-effect budget. Some referenced external Skills/OFD behavior is outside this repository.
- **Validation:** Skill, runbook and comms protocol source-reviewed; no agents/worktrees spawned.

### `branch-review`
- **Verified capability:** diff-focused review with scope guard, untrusted-diff treatment, multi-agent review dimensions and optional controlled fixes.
- **Strengths:** keeps review evidence tied to the actual diff and avoids inventing speculative failures.
- **Gaps / risks:** host Agent/Task/reporting dependencies reduce portability; multi-agent fan-out needs resource controls. No benchmark measures finding precision/recall.
- **Validation:** source-reviewed only.

### `component-design`
- **Verified capability:** component-level design focused on local interfaces, responsibilities, dependencies and testability.
- **Strengths:** prevents system architecture and component design from collapsing into one oversized document/process.
- **Gaps / risks:** outcome quality is qualitative; no component-design eval corpus.
- **Validation:** source-reviewed only.

### `component-review`
- **Verified capability:** read-only component implementation/design review against evidence and stated contracts.
- **Strengths:** narrow scope reduces unrelated findings and hypothetical architecture criticism.
- **Gaps / risks:** no calibrated known-defect fixture set.
- **Validation:** source-reviewed only.

### `full-project-review`
- **Verified capability:** repository-wide review that composes specialized review dimensions and produces structured findings.
- **Strengths:** broader audit is explicitly separated from branch/diff review.
- **Gaps / risks:** potentially expensive agent fan-out; needs explicit scope/resource limits in large repositories. No behavioral benchmark included.
- **Validation:** source-reviewed only.

### `obsidian`
- **Verified capability:** read/search/create/update/append/delete notes through Obsidian Local REST API using environment-held credentials.
- **Strengths:** concrete API contract, path conventions and lifecycle guidance for cross-project memory.
- **Gaps / risks:** write/delete operations are external side effects but the Skill has no per-write confirmation/authorization gate. `curl -k` disables TLS certificate verification, acceptable only for the stated localhost/self-signed assumption and unsafe if the endpoint becomes remote.
- **Validation:** source-reviewed only; no Obsidian API call executed.

### `oss-readiness`
- **Verified capability:** repository readiness review for public/open-source release using probes rather than assumptions and explicit outward-facing metadata checks.
- **Strengths:** keeps the review non-destructive and states not to commit/push automatically.
- **Gaps / risks:** checklist completeness is not tested against a release-failure corpus.
- **Validation:** source-reviewed only.

### `reproduce-first-debug`
- **Verified capability:** hard reproduction gate before hypothesis/code reading; local fixtures only, RED regression commit, minimal fix and red→green evidence.
- **Strengths:** strong epistemic discipline, bounded three-attempt non-repro terminal state, clean-tree/default-branch safeguards, and no production data.
- **Gaps / risks:** it commits a RED test by design; that side effect needs to be consistent with repository/user authorization. No stored bug benchmark proves the workflow's effectiveness.
- **Validation:** source-reviewed only.

### `review-and-fix`
- **Verified capability:** PR-fleet orchestrator using isolated worktrees, delegated branch reviews, archived reports, concurrency limits and batched escalation.
- **Strengths:** explicit fork write-access classification, trust boundary for PR content, failure isolation and confirmation when fan-out exceeds thresholds.
- **Gaps / risks:** optional fix/push mode still creates significant external side effects; fork push behavior is explicitly described by the Skill itself as not yet reproduced end-to-end.
- **Validation:** source-reviewed only; no PRs fetched/reviewed/pushed.

### `session-handoff`
- **Verified capability:** rotates structured session-handoff artifacts using Git history, working-tree state, TODOs, decisions and next steps.
- **Strengths:** preserves previous handoffs rather than overwriting and records uncertainty when session boundary cannot be established.
- **Gaps / risks:** relies on conversation-derived session boundaries and shell heuristics; no fixture tests validate rotation/date/slug edge cases.
- **Validation:** source-reviewed only.

### `tech-gazette`
- **Verified capability:** parallel web-research workflow that generates a self-contained daily/weekly HTML technology gazette from default/custom topics and optional customer radar.
- **Strengths:** explicitly treats web results as untrusted data, requires publication-date-aware labeling and reuses fixed HTML/CSS templates.
- **Gaps / risks:** 18-topic/19-query research can be expensive; no source-quality scoring/eval or generated-HTML regression suite is present. Customer URL fetching requires privacy/scope care.
- **Validation:** source-reviewed only; no web research or HTML generation executed.

## `benjaminyanjd/laoyu-life-algorithm-skill` — 1 report

### `laoyu-life-algorithm`
- **Pinned revision:** `850214ae14e3ed4e1e323f0e2a1c55faa45a7e5a`
- **Evidence read:** README, root `SKILL.md`, `framework.md`, `nine-stages.md`, `eighteen-challenges.md`.
- **Verified capability:** Chinese decision lens derived from a public book framework; outputs conclusion, rationale, largest risk, validation action, stop-loss line and a brief framework mapping.
- **Strengths:** progressive disclosure, action-before-theory, explicit “decision layer only” boundary for medical/legal/technical domains, and instruction to label public-structure facts vs inference.
- **Gaps / risks:** categories and “win-rate” framing are interpretive heuristics; no bibliography/citation ledger, calibration data or decision-outcome behavioral eval exists.
- **Validation:** source-reviewed only.

## Exact-tree mappings without new reports

The following four repository identities were independently content-gated with README + representative `clean-architecture/SKILL.md`, but all resolve to the already-reviewed Wondel snapshot at revision `4d322538be8b9ce98fca29b0eef26d67bff1fe82`:

- `zarkob/wondelai-skills`
- `imkepler/hermes-wondelai-skills`
- `mikesmayer/claude-business-skills`
- `srinivasmd/skills`

No duplicate individual reports were created for that exact-tree content.

## Count check

```text
ballbadboy/agentskills                         21
yhughk/adversarial-verification                1
benjaminyanjd/life-algorithm-skill             1
rogeriochaves/skills                           6
Wondel exact-tree identities                   0
lx-wnk/skills                                 15
benjaminyanjd/laoyu-life-algorithm-skill       1
------------------------------------------------
new repository-scoped individual reports      45
```
