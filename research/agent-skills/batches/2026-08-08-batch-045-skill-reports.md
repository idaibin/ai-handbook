# Agent Skills individual reports — Batch 045

Date: 2026-08-08

This file contains only the 14 new canonical individual Skill reports created from bodies directly read in Batch 045. Exact-tree mirrors that already had a canonical report are mapped in the repository report and are not duplicated here.

Validation notation:

- **Verified source**: body/source/references were directly read at the pinned revision.
- **Behavioral validation**: no Skill in this file was executed by this batch unless explicitly stated. For Batch 045, all runtime/build/test/LLM-eval execution is `not_executed`.

---

## `beadflow`

**Repository:** `stehessel/agentskills`  
**Path:** `.apm/skills/beadflow/SKILL.md`  
**Category:** task planning / execution workflow  
**Verified source:** yes

### What it does

Uses the Beads issue graph as durable task state. It defines entry checks, planning decomposition, batch issue creation, dependency wiring, execution/close loops, blocked-work handling, and session-end persistence.

### Strong patterns

- Durable task state is externalized instead of depending on conversation memory.
- Planning guidance requires concrete file/function/behavior descriptions and explicit coverage-review tasks.
- It distinguishes blocked, discovered, oversized, and completed work states.
- It repeatedly prefers machine-readable JSON and explicit verification after changes.

### Limitations / risks

- “Every strategic action = Beads update” is too absolute for a reusable Skill; state overhead should be proportional to task importance.
- Initialization policy is internally inconsistent: one path initializes automatically for a supplied goal, while later error handling says to confirm before initialization.
- Several command semantics and “always” rules are tightly coupled to a particular Beads CLI generation and need versioned compatibility tests.
- No repository-local behavior/eval suite was found for the pinned revision.

### Reuse recommendation

Reuse the durable task graph, explicit blocked-state handling, and verification-first task descriptions. Do not copy the unconditional state-write rules; make issue creation and external side effects policy-controlled.

---

## `reviewer`

**Repository:** `stehessel/agentskills`  
**Path:** `.apm/skills/reviewer/SKILL.md`  
**Category:** code/repository review  
**Verified source:** yes

### What it does

Performs discovery first, selects language/framework/infrastructure checklist modules, builds spec traceability when a spec exists, then emits separate spec-deviation and code-quality findings with concrete `file:line` evidence.

### Strong patterns

- Explicitly forbids reviewing files that were not actually read.
- Separates requirements compliance from implementation quality.
- Uses risk-specific checklist modules rather than applying every rule to every stack.
- Requires expected/actual evidence for findings and preserves a structured report format.
- The checklist reference covers general quality, testing, production readiness, architecture, documentation, multiple languages, frontend, database and HTTP concerns.

### Limitations / risks

- “Read at least 10–15 representative files” is a sampling heuristic, not a completeness guarantee. Sampling should depend on repository size, risk, dependency topology, and changed surface.
- Several checklist thresholds are conventions rather than universal correctness rules and can create false positives if treated as hard gates.
- The Skill calls itself read-only but writes `code-review.md`; the intended boundary is “do not modify product source,” which should be stated more precisely.
- No local eval suite was found that measures false-positive rate, missed defects, or file/line citation accuracy.

### Reuse recommendation

High-value basis for `repo-review`: retain discovery-before-judgment, spec traceability, evidence-backed findings, and stack-aware modules. Replace fixed file counts with coverage/risk criteria and separate advisory heuristics from hard checks.

---

## `sculptor`

**Repository:** `stehessel/agentskills`  
**Path:** `.apm/skills/sculptor/SKILL.md`  
**Category:** ideation / specification workflow  
**Verified source:** yes

### What it does

Moves an idea through intake, research, draft, user annotation, technical specification, implementation plan, finalization, and feedback. State is stored in Markdown artifacts and implementation is explicitly out of scope.

### Strong patterns

- Strong phase boundary between research/design and implementation.
- File-backed continuity makes the workflow resumable without relying on chat history.
- Explicit user approval gates prevent silent progression across major design stages.
- Annotation format creates a concrete review loop and preserves user authority over decisions.
- Encourages early assumption testing and explicit non-goals.

### Limitations / risks

- Mandatory 2–3 alternatives and “every idea gets designed” can create unnecessary work on trivial or already-constrained tasks.
- The workflow is intentionally interactive and therefore unsuitable as-is for unattended automation.
- Multiple approval pauses can become an optimization/review loop if the exit criteria are not explicit.
- No repository-local eval demonstrates that the process reduces implementation rework or improves spec completeness.

### Reuse recommendation

Reuse the artifact-backed research → design → approval boundary and annotation loop where human review is required. Add a fast path for low-complexity tasks and explicit “sufficient to execute” exit criteria.

---

## `session-viewer`

**Repository:** `stehessel/agentskills`  
**Path:** `.apm/skills/session-viewer/SKILL.md`  
**Executable:** `.apm/skills/session-viewer/claude_session.py`  
**Category:** session inspection / debugging  
**Verified source:** yes

### What it does

Parses Claude Code JSONL sessions and exposes transcript, compact, JSON, summary, errors, file-operation, and tool-only views. It can inspect subagent sessions and optionally redact common secret patterns.

### Strong patterns

- Multiple views support progressive disclosure instead of loading an entire session by default.
- Structured JSON is the documented agent-default output.
- The parser aggregates token usage, turn duration, file operations, tools and errors.
- Secret redaction is available and thinking blocks are opt-in rather than default.

### Limitations / risks

- Redaction is regex-based and therefore cannot guarantee removal of all sensitive values; `--redact` should be treated as best-effort, not a security boundary.
- Persisted-output expansion opens paths recorded inside session data. That capability needs explicit trust/path-boundary rules when consuming untrusted session artifacts.
- The parser silently skips malformed JSON lines and catches some broad exceptions, which improves robustness but can hide incomplete-analysis conditions unless surfaced in output metadata.
- It depends on Claude Code's current local storage schema and path conventions; schema drift needs fixtures across versions.
- No repository-local tests/evals were found in the pinned tree.

### Reuse recommendation

Useful model for an evidence/session-inspection Skill: keep structured modes, progressive disclosure, and error/file summaries. Add versioned fixtures, parse-warning counts, and stronger path/redaction guarantees.

---

## `treeflow`

**Repository:** `stehessel/agentskills`  
**Path:** `.apm/skills/treeflow/SKILL.md`  
**Executable:** `.apm/skills/treeflow/tf.py`  
**Category:** multi-agent orchestration  
**Verified source:** yes

### What it does

Defines a pure orchestrator that delegates source-code work to named workers, tracks worker/bead state in a JSON registry, layers context, checks file-conflict safety, reuses workers by domain/context budget, performs phase gates, and provides build/wiring smoke-test hooks.

### Strong patterns

- Clear orchestrator/worker responsibility boundary.
- Explicit file-conflict analysis before parallel dispatch.
- Worker identity and state are externalized to a registry rather than held only in model context.
- `tf.py` writes registry changes through temp-file replacement.
- Phase gates distinguish task completion from integration/build checks.
- Context summaries are deliberately smaller than full worker transcripts.

### Limitations / risks

- `tf.py` uses shell execution for dynamically constructed commands. Command arguments should be passed as arrays with validated identifiers/paths wherever possible.
- Registry discovery selects a matching `context-*` directory rather than requiring an explicit plan identifier; multiple context directories can produce ambiguous state selection.
- Temp-file replacement improves single-process durability but does not provide inter-process locking; concurrent writers can still race.
- File-existence checks in the smoke-test helper are only wiring sanity checks; they do not prove API, UI, runtime, or behavioral correctness.
- Hard-coded assumptions about worker tools, naming, model selection, context percentages, and maximum concurrency are runtime-specific policy rather than portable Skill semantics.
- No local tests/evals were found for orchestration races, late notifications, malformed registry state, command failure, or multi-context behavior.

### Reuse recommendation

High-value reference for orchestration architecture: reuse named-worker state, explicit dispatch/notify lifecycle, layered context, file-conflict gating, and phase-level verification. Before production use, replace shell-string execution, add locking/explicit registry identity, and build deterministic integration tests around worker lifecycle races.

---

# `mkobit/chezmoi-skills`

The nine reports below share a common repository architecture: compact `SKILL.md` bodies route into focused `references/` files; repository-level validation checks metadata, internal links and tokenizer-based budgets; JSON eval definitions and Promptfoo configuration provide a behavioral-testing surface.

Important boundary: `scripts/test-contracts.ts` is partly tautological. Its rule-based skill-selection branch returns the test's declared target skill, and command tests can return the declared expected command. Those local contract results must not be reported as autonomous-agent correctness. Promptfoo is the stronger behavioral path, but it was not executed in this batch.

## `chezmoi-cli-commands`

**Path:** `skills/cli-commands/SKILL.md`  
**Category:** CLI operation guidance  
**Verified source:** yes

### Strengths

- Covers inspection, preview, add/edit/apply/state operations through a compact router.
- Eval definitions include positive and negative trigger cases plus non-destructive preview expectations.
- Explicitly avoids forceful operations in safety-oriented test cases.

### Limitations

Command correctness depends on the installed chezmoi version. Static expected commands can drift from upstream CLI behavior and should be contract-tested against a pinned/current CLI binary.

### Reuse recommendation

Good example of pairing operational guidance with negative triggers and safety assertions; add live CLI compatibility tests.

---

## `chezmoi-configuration`

**Path:** `skills/configuration/SKILL.md`  
**Category:** configuration guidance  
**Verified source:** yes

### Strengths

Separates config discovery, file format, Git integration, source directory behavior and reference material instead of putting all configuration details into one Skill body.

### Limitations

Configuration keys are external-product contracts and can become stale. Repository-local validation checks document structure, not whether every key remains valid in the latest chezmoi release.

### Reuse recommendation

Use the concise router/reference split; add versioned schema or executable config validation against chezmoi.

---

## `chezmoi-externals`

**Path:** `skills/externals/SKILL.md`  
**Category:** external dependency management  
**Verified source:** yes

### Strengths

Keeps external-source types and refresh semantics in references while the Skill body focuses on when to use them. Test definitions cover refresh behavior and repository-type configuration.

### Limitations

External downloads and repository operations are side effects. A reusable agent Skill should explicitly distinguish planning/preview from network/write execution and apply authorization policy above the Skill.

### Reuse recommendation

Retain the progressive disclosure and config examples; add side-effect/approval classification and live fixture repositories.

---

## `chezmoi-file-attributes`

**Path:** `skills/file-attributes/SKILL.md`  
**Category:** source-state naming / file semantics  
**Verified source:** yes

### Strengths

Encodes a naming convention that is easy for agents to get subtly wrong and links to deeper attribute references. This is a good fit for deterministic examples and table-driven tests.

### Limitations

Filename-prefix combinations can have edge cases across OS/platform and upstream versions. Static prose is insufficient for exhaustive correctness.

### Reuse recommendation

Convert attribute composition examples into generated fixtures against actual chezmoi source/target mappings.

---

## `chezmoi-init`

**Path:** `skills/init/SKILL.md`  
**Category:** repository initialization / bootstrap  
**Verified source:** yes

### Strengths

Focuses on initialization, cloning and immediate apply behavior, with references for setup variants.

### Limitations

Initialization can create local state and applying can modify target files. The Skill needs a host-level approval/preview policy rather than assuming operational permission from routing alone.

### Reuse recommendation

Keep bootstrap knowledge separate from routine apply/edit Skills; enforce explicit preview/authorization for state-changing paths.

---

## `chezmoi-machine-config`

**Path:** `skills/machine-config/SKILL.md`  
**Category:** multi-machine configuration  
**Verified source:** yes

### Strengths

Clearly identifies OS, architecture, hostname and Linux-release variables, then routes detailed branching/data/ignore rules to references. This is a strong progressive-disclosure pattern for environment-dependent configuration.

### Limitations

Environment values are runtime facts. Agents should inspect actual `chezmoi data` output rather than infer machine identity from conversation or templates.

### Reuse recommendation

Good pattern for separating environment discovery from templating logic; require runtime observation before making machine-specific changes.

---

## `chezmoi-scripts`

**Path:** `skills/scripts/SKILL.md`  
**Category:** lifecycle script execution  
**Verified source:** yes

### Strengths

Explains execution triggers, ordering and state history in a compact surface and points to detailed script/state references.

### Limitations

Lifecycle scripts are arbitrary code execution. The Skill body documents invocation semantics but does not itself provide a sandbox, permission gate, or static analysis of the scripts being executed.

### Reuse recommendation

Useful domain reference, but any autonomous use should require host-level execution authorization and pre-execution diff/inspection.

---

## `chezmoi-secrets-management`

**Path:** `skills/secrets-management/SKILL.md`  
**Category:** secrets / encryption guidance  
**Verified source:** yes

### Strengths

Separates dynamic password-manager lookup from encrypted-file storage, explicitly advises keeping private key material outside the source repository, and delegates backend details to references. The inspected encryption reference covers age/GPG/rage/transparent modes without embedding real credentials.

### Limitations

The Skill provides operational secret-management knowledge but cannot guarantee that generated commands, target paths, or repository state will not expose sensitive material. Agent output/logging policy remains a separate control.

### Reuse recommendation

Strong reference architecture for sensitive-domain Skills: compact policy at top level, detailed providers in references, and no secret values in examples. Add redaction/output contracts and executable leakage tests.

---

## `chezmoi-templating`

**Path:** `skills/templating/SKILL.md`  
**Category:** template authoring  
**Verified source:** yes

### Strengths

Provides core Go-template syntax, preview/testing commands, and separate references for built-ins, Sprig, prompts and shared fragments. It explicitly recommends rendering/inspection commands rather than assuming template correctness.

### Limitations

Template behavior is affected by chezmoi and embedded function versions; documentation-only checks cannot prove rendering compatibility. Prompt functions also create interactive assumptions that do not fit unattended workflows.

### Reuse recommendation

High-quality progressive-disclosure example. Pair it with fixture templates rendered by a pinned/current chezmoi binary and separate interactive from non-interactive workflows.

---

## Cross-skill conclusion

The strongest reusable engineering lessons in Batch 045 are:

1. Externalize durable workflow state, but do not turn every action into unconditional state mutation.
2. Separate discovery/traceability from findings in review Skills.
3. Keep top-level Skill bodies small and route details to references.
4. Treat structural validators, deterministic contract tests, and live behavioral evals as different evidence levels.
5. Never promote a test harness to behavioral proof when the evaluator is seeded with the expected answer.
6. For executable orchestration helpers, test concurrency, shell/argument boundaries, schema drift and recovery paths explicitly.
