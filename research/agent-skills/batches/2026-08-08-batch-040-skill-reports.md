# Agent Skills Individual Reports — Batch 040

- Batch ID: `2026-08-08-batch-040`
- Completed repository identities: **10**
- Direct `SKILL.md` reads: **29**
- Direct unique skill bodies reviewed: **26**
- New canonical skill-body reports: **24**
- Existing canonical bodies directly reverified/mapped: **2**
- Runtime/build/test/eval execution: **not_executed**

This file records individual reports only for bodies actually read in this batch. Large collection inventories are kept separate from body-reviewed reports. A skill listed in a collection manifest is not counted as reviewed until its body is directly inspected or it is proven to be an exact body/tree already reviewed canonically.

Pre-write AI-handbook searches found no prior deep-analysis report hits for the new Kagura and `rb-*` bodies, `open-claw-seedance`, the two changed/new cybersecurity bodies, or the directly reviewed Dreamina wrapper body. `37signals-way` appeared in the Batch 039 Wondel inventory but did not have an individual body report there; it is body-reviewed here for the first time.

## Kagura collection — 13 new canonical body reports

### 1. `agent-memes`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `agent-memes/SKILL.md`
- Supporting implementation: `agent-memes/scripts/memes.sh`
- Execution: **not_executed**

**Purpose.** Select, track, and send reaction memes across agent communication channels.

**Strengths.** Real Bash implementation, usage tracking, freshness/diversity logic, category resolution, health/audit commands, and platform-aware delivery.

**Risks / gaps.** The skill encourages proactive sending on many conversational triggers, which can create unsolicited external side effects. The script sources local configuration files as shell code, expanding the trust boundary. Host-specific paths and OpenClaw channel context reduce portability. No behavioral eval was surfaced.

**Verdict.** **Concrete and feature-rich, but needs an explicit user/effect policy and safer configuration boundary before general reuse.**

### 2. `cove-ops`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `cove-ops/SKILL.md`
- Supporting implementation: `cove-ops/scripts/cove-webhook-send.mjs`
- Execution: **not_executed**

**Purpose.** Operate a Cove/Discord-compatible communication environment, including cross-channel messaging and administration.

**Strengths.** Real Node helper, strict argument parsing, API error handling, channel resolution, webhook reuse, and configuration fallback.

**Risks / gaps.** The helper reads bot credentials from local OpenClaw configuration and caches webhook IDs/tokens in a JSON file without an explicit restrictive file-mode policy. Admin/write operations need a single authorization gate rather than relying on scattered prose. Environment assumptions are strong.

**Verdict.** **Useful operational tooling; credential-at-rest and external-effect authorization should be formalized.**

### 3. `discord-ops`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `discord-ops/SKILL.md`
- Execution: **not_executed**

**Purpose.** Describe direct Discord operational workflows for an agent.

**Strengths.** Clear operational scope and explicit status labeling as a proposal.

**Risks / gaps.** Despite proposal status, the body describes privileged server/channel operations. Destructive or permission-changing effects need explicit authorization, dry-run/preview, and audit logging. No repository-local implementation/eval was surfaced for this body.

**Verdict.** **Keep as a proposal/reference until effect authorization and verification are made executable.**

### 4. `flowforge`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `flowforge/SKILL.md`
- Reference read: `flowforge/references/setup.md`
- Execution: **not_executed**

**Purpose.** Route multi-step work through a persistent workflow/state-machine CLI.

**Strengths.** State-machine framing, SQLite persistence, resumability, and explicit workflow definitions are strong patterns for long-running agent work.

**Risks / gaps.** The body uses mandatory routing language that is appropriate only when FlowForge is actually installed and relevant. It links `setup.md` as if local to the body while the file is under `references/`. It also depends on a workspace-local goal-drift script not surfaced in this repository. No local eval proves routing improves outcomes.

**Verdict.** **Strong orchestration concept; fix broken/hidden dependencies and make routing conditional on host capability.**

### 5. `gogetajob`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `gogetajob/SKILL.md`
- Execution: **not_executed**

**Purpose.** Orchestrate open-source contribution discovery, implementation, and pull-request workflow.

**Strengths.** Structured issue selection, branch/PR workflow, verification expectations, rate-limit awareness, and maintainer-facing quality checks.

**Risks / gaps.** Broad GitHub and code-write side effects require strong user/project authorization. Some execution assumptions are specific to a particular coding-agent environment. Contribution quality cannot be inferred from checklist completion alone.

**Verdict.** **Good contribution workflow reference; require repo authorization and evidence-based verification before autonomous execution.**

### 6. `kagura-canvas`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `kagura-canvas/SKILL.md`
- Execution: **not_executed**

**Purpose.** Provide a thin image/canvas workflow tied to Kagura/OpenClaw channels and session state.

**Strengths.** Narrow task surface and straightforward handoff semantics.

**Risks / gaps.** Hard-coded host/channel/session assumptions dominate the body; timing and delivery behavior depend on infrastructure not shipped in this repository. No local implementation/eval was surfaced.

**Verdict.** **Local environment skill, not yet a portable Agent Skill contract.**

### 7. `kagura-storyteller`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `kagura-storyteller/SKILL.md`
- Execution: **not_executed**

**Purpose.** Turn verified agent experiences into public-facing stories/content while maintaining persona continuity.

**Strengths.** Strong source-first fact-checking language, provenance awareness, content structure, and privacy considerations.

**Risks / gaps.** It is deeply persona/project-specific. Public publishing is an external side effect and should require explicit approval. Memory-derived content also needs a clear privacy/data-minimization boundary beyond stylistic anonymization.

**Verdict.** **Useful provenance-aware content pattern; public publishing and memory use need stronger consent contracts.**

### 8. `memos-memory-guide`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `memos-memory-guide/SKILL.md`
- Execution: **not_executed**

**Purpose.** Guide use of MemOS/OpenClaw long-term memory, local sharing, team sharing, and reusable skills.

**Strengths.** Explicitly distinguishes local-agent sharing from team/hub sharing, requires consent for team/hub sharing, and separates search/get/timeline/share operations.

**Risks / gaps.** The security/privacy model depends on host-enforced ownership/isolation that is not implemented in this repository. It permits proactive local-agent sharing, which may still be sensitive. The large tool contract is easy to drift from the host implementation without versioning.

**Verdict.** **Good conceptual sharing-plane separation; bind it to a versioned host permission contract and stricter data-minimization policy.**

### 9. `moltbook-community`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `moltbook-community/SKILL.md`
- Execution: **not_executed**

**Purpose.** Read and post to an external social platform for AI agents.

**Strengths.** Clear API surface, passive feed options, and guidance against low-quality spam.

**Risks / gaps.** It is documentation-only in this repository. Registration, posting, comments, votes, and cron-driven replies are external side effects and should require explicit user policy/authorization. No rate-limit/error/retry/eval implementation was surfaced.

**Verdict.** **Useful API/operator reference; not safe for default-autonomous posting without an effect policy.**

### 10. `pulse-todo`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `pulse-todo/SKILL.md`
- Execution: **not_executed**

**Purpose.** Maintain one persistent TODO source and synchronize scheduled work with cron.

**Strengths.** Single source of truth, explicit dependency grouping, verification-before-done, and separation of heartbeat work from timed/recurring tasks.

**Risks / gaps.** “Everything is a TODO”, three-day staleness, mandatory cron coupling, and task-selection heuristics are local policy choices, not validated universals. Two-source synchronization (`TODO.md` + scheduler) creates drift unless enforced transactionally.

**Verdict.** **Strong local task convention; make scheduler synchronization machine-checkable and policy values configurable.**

### 11. `seedling`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `seedling/SKILL.md`
- Execution: **not_executed**

**Purpose.** Drive a Discord-based agent “tamagotchi” onboarding/growth experience using an external CLI.

**Strengths.** Explicit state transitions, milestone checks, periodic review concepts, and CLI-oriented contracts.

**Risks / gaps.** The body depends on a separate local repository and Discord permission tooling. The “Progressive Channel Unlocks” section is duplicated with overlapping rules. Permission changes and scheduled public messages require authorization/audit gates.

**Verdict.** **Interesting stateful experience skill; fix duplicated contract and externalize the runtime dependency/version.**

### 12. `self-portrait`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `self-portrait/SKILL.md`
- Execution: **not_executed**

**Purpose.** Maintain a persistent public identity through journals, stories, profile updates, and related media.

**Strengths.** Distinguishes raw memory from curated public expression, contains privacy rules, and uses source artifacts as inputs rather than pure model memory.

**Risks / gaps.** Publishing/profile updates are external writes. The persona-specific “identity evolution” framing should not override user intent or privacy. Host paths and publication services are not portable.

**Verdict.** **Good provenance distinction between private memory and curated output; require explicit publish approval and portable path contracts.**

### 13. `team-lead`

- Repository: `kagura-agent/skills`
- Revision: `a034021bb5ceaa918fa843ccbecf1777de81df2b`
- Body: `team-lead/SKILL.md`
- Execution: **not_executed**

**Purpose.** Coordinate developer/QA subagents through issue-driven implementation, review, test, and human approval.

**Strengths.** Strong scope boundaries, one-subtask assignments, acceptance/test commands, PR diff review, human final approval, worktree isolation, single-writer-per-path rule, and explicit timeout/wrap-up behavior.

**Risks / gaps.** “Never code yourself” and fixed timeout budgets are team-specific policy. Mandatory pre-implementation templates can impose large overhead on small tasks despite grade scaling. Several cited inspirations/results are not locally evidenced. The workflow needs evals measuring defect escape, latency, and retry behavior.

**Verdict.** **High-value engineering-agent coordination reference; extract the evidence/validation/worktree rules while keeping role and budget policy configurable.**

## `ndtrongvn/agents-skills` — 6 new canonical body reports

### 14. `rb-audit`

- Revision: `f5fbed26e84db1d378b4bab1b3888f0dc9fcb178`
- Body: `skills/rb-audit/SKILL.md`
- Implementation: `skills/rb-audit/scripts/engine.py`
- Execution: **not_executed**

**Purpose.** Generate a compact deterministic project-truth capsule for downstream skills.

**Strengths.** Stable JSON contract, source refresh, explicit TTL, capped risk findings, and deterministic downstream handoff.

**Risks / gaps.** The engine is presented as reusable but hard-codes a particular Next.js/Solana/Supabase project structure, dependencies, migrations, and source paths. Regex/path rules have unknown false-positive/false-negative rates. No fixture/eval corpus was surfaced.

**Verdict.** **Excellent artifact-contract pattern, but the analyzer must be split into generic engine + project rule pack before general reuse.**

### 15. `rb-idea`

- Revision: `f5fbed26e84db1d378b4bab1b3888f0dc9fcb178`
- Body: `skills/rb-idea/SKILL.md`
- Execution: **not_executed**

**Purpose.** Gate product/design questioning on a current audit capsule and resolve decisions one branch at a time.

**Strengths.** Deterministic missing/invalid failures, one-question-at-a-time interaction, codebase-first fact discovery, and explicit conflict handling.

**Risks / gaps.** The design stage inherits all errors from the audit capsule. Freshness is only as good as the upstream TTL/schema. Strict sequential questioning may be inefficient for independent decisions.

**Verdict.** **Good grounding gate; add capsule provenance/hash checks and an eval for stale/wrong-capsule recovery.**

### 16. `rb-prd`

- Revision: `f5fbed26e84db1d378b4bab1b3888f0dc9fcb178`
- Body: `skills/rb-prd/SKILL.md`
- Execution: **not_executed**

**Purpose.** Turn resolved ideas plus codebase facts into an implementation/testing PRD.

**Strengths.** File-gated input, codebase verification, explicit implementation/testing decisions, out-of-scope capture, and quality checks.

**Risks / gaps.** The instruction to interview “relentlessly” can over-extend interaction after decisions are already sufficient. No machine-readable schema validates the PRD contract. The required-output line contains a malformed Markdown backtick.

**Verdict.** **Useful PRD gate; add a schema/checker and a stop criterion based on unresolved decision risk.**

### 17. `rb-break-task`

- Revision: `f5fbed26e84db1d378b4bab1b3888f0dc9fcb178`
- Body: `skills/rb-break-task/SKILL.md`
- Execution: **not_executed**

**Purpose.** Split the PRD into dependency-aware vertical task slices and maintain a task index.

**Strengths.** Explicit canonical template, working-artifact separation, tracer-bullet slicing, dependency references, story coverage, status tracking, and acyclic-graph requirement.

**Risks / gaps.** Acyclicity and reference integrity are requirements in prose; no surfaced validator was inspected to enforce them. HITL/AFK classification can be ambiguous without an executable policy.

**Verdict.** **Strong task-contract design; add a small validator for graph/reference/story coverage invariants.**

### 18. `rb-tdd`

- Revision: `f5fbed26e84db1d378b4bab1b3888f0dc9fcb178`
- Body: `skills/rb-tdd/SKILL.md`
- Execution: **not_executed**

**Purpose.** Enforce vertical red-green-refactor loops focused on public behavior.

**Strengths.** Explicit anti-horizontal-slice rule, public-interface testing, one-test-at-a-time tracer bullets, and refactor-after-green discipline.

**Risks / gaps.** Some rules are intentionally opinionated and may not fit legacy/system-test contexts. User approval before every test plan can be too interactive for previously authorized implementation. No empirical eval is provided for its claimed test-quality advantage.

**Verdict.** **High-quality TDD guidance; preserve the behavior-first principle while making interaction depth context-sensitive.**

### 19. `rb-agent-md`

- Revision: `f5fbed26e84db1d378b4bab1b3888f0dc9fcb178`
- Body: `skills/rb-agent-md/SKILL.md`
- Execution: **not_executed**

**Purpose.** Distill, render, and sync a root `AGENTS.md` from project facts and a placeholder template.

**Strengths.** Clear ownership, strict local-source priority, unresolved-placeholder preservation, drift reporting, and anti-hallucination language.

**Risks / gaps.** Source priority is sensible but not a substitute for validating stale generated docs. Bidirectional distill/render can lose semantics without round-trip tests. The required placeholder contract needs a validator.

**Verdict.** **Strong reusable documentation-sync pattern; add round-trip/schema tests and explicit authority/version metadata.**

## Dreamina / Seedance — 2 new canonical body reports

### 20. `dreamina-cli`

- Repository: `Sylvia-awen/dreamina-cli-skill`
- Revision: `75e0a69a99f21a9c706045a0f6227b1b0804f886`
- Body: root `SKILL.md`
- Supporting implementation/reference: `scripts/dreamina_wrapper.py`, `references/commands.md`
- Execution: **not_executed**

**Purpose.** Provide a stable Agent Skill execution surface over an external Dreamina CLI for image/video generation and task/account/session operations.

**Strengths.** Real dry-run, local-path validation, command-spec normalization, structured JSON, async status validation, and machine-readable capability discovery.

**Risks / gaps.** Unpinned remote installer, no surfaced unit/eval suite, future sensitive argument redaction risk, path-convention portability, and unverified external service cost/auth/version behavior.

**Verdict.** **Strong thin-wrapper design; add fixtures/tests and pinned supply-chain controls.**

### 21. `open-claw-seedance`

- Repository: `Marvin-Cypher/openclaw-seedance-skill`
- Revision: `a054285ffeacc3a6eebcc7e24248b0477f551fa4`
- Body: `skills/open-claw-seedance/SKILL.md`
- Reference: `references/jimeng-cli-quickstart.md`
- Execution: **not_executed**

**Purpose.** Document three Seedance video workflows for OpenClaw through the external Dreamina CLI.

**Strengths.** Narrow scope, readable examples, and explicit dependency/source-of-truth guidance.

**Risks / gaps.** Documentation-only at the inspected revision; no local validation, dry-run, structured return, tests, or evals. Unpinned installer and external cost/write effects remain outside the repository contract.

**Verdict.** **Useful operator guide; prefer the wrapper pattern above for deterministic agent execution.**

## Wondel intermediate snapshot — 1 new canonical body report

### 22. `37signals-way`

- Repository: `skbauman3/wondelai-skills`
- Revision: `7c71a845071e8f994253db0d26c7e36fa90e2b5e`
- Collection manifest: **42 skill identities**
- Body: `37signals-way/SKILL.md`
- Reference: `37signals-way/references/shaping-work.md`
- Execution/eval: **not_executed**

**Purpose.** Apply 37signals/Shape Up-inspired product-development principles: shaping, appetite, small teams, fixed cycles, scope cutting, and opinionated defaults.

**Strengths.** Coherent framework, clear terminology, explicit trade-offs, detailed reference material, cross-skill routing, and ethical caveats.

**Risks / gaps.** A framework-specific `10/10` score creates false numerical precision. Fixed team sizes, cycle lengths, no-backlog rules, and other practices are context-dependent rather than universal. No behavioral calibration/eval was surfaced.

**Verdict.** **Useful philosophy skill when invoked intentionally; label its defaults as framework assumptions, not general engineering facts.**

The other 41 manifest entries in this snapshot remain inventory records unless already body-reviewed in another canonical revision; they are not counted as new reports here.

## Newer Anthropic Cybersecurity revision — 2 new canonical body reports

The following are defensive security-analysis skills. This report records architecture/evidence quality and deliberately does not reproduce operational attack instructions.

### 23. `detecting-lateral-movement-with-zeek`

- Repository source: `fernandezbaptiste/Anthropic-Cybersecurity-Skills`
- Shared revision: `c15f73db46149587e31df83c2f9d92a3b578ef21`
- Body: `skills/detecting-lateral-movement-with-zeek/SKILL.md`
- Implementation: `scripts/process.py`
- References: `references/standards.md`, `references/workflows.md`
- Execution/eval: **not_executed**

**Purpose.** Analyze Zeek network telemetry for indicators associated with lateral movement and support defensive investigation/triage.

**Strengths.** Real parser/helper code, configurable network/window inputs, standards references, explicit prerequisites, verification language, and cross-telemetry guidance.

**Risks / gaps.** The body tells the user to run a provided `agent.py`, but the surfaced helper is `scripts/process.py`; this is a concrete documentation/implementation mismatch. Detection thresholds/severities are heuristic and no labeled fixture corpus, precision/recall measurement, or regression suite was surfaced. Automated response recommendations need human authorization.

**Verdict.** **Meaningful upgrade from prose-only skill content; fix the invocation drift and add defensive log fixtures/effectiveness evals.**

### 24. `performing-cloud-native-threat-hunting-with-aws-detective`

- Repository source: `fernandezbaptiste/Anthropic-Cybersecurity-Skills`
- Shared revision: `c15f73db46149587e31df83c2f9d92a3b578ef21`
- Body: `skills/performing-cloud-native-threat-hunting-with-aws-detective/SKILL.md`
- Implementation: `scripts/process.py`
- Reference: `references/standards.md`
- Execution/eval: **not_executed**

**Purpose.** Support defensive AWS investigation using Detective/GuardDuty-oriented entity/investigation data.

**Strengths.** Executable boto3 helper, pagination abstraction, argument validation, exportable structured results, standards links, prerequisites, and verification guidance.

**Risks / gaps.** AWS API/version/permission compatibility was not runtime-verified. The skill contains example expectations that can drift from the external service. No mocked API fixtures or integration evals were surfaced. High-impact response actions should remain human-approved.

**Verdict.** **Promising executable defensive skill; add mocked contract tests plus a versioned AWS compatibility matrix before production use.**

## Existing canonical body mappings directly reverified in Batch 040

### A. `performing-memory-forensics-with-volatility3` — existing canonical body

Directly reread from these identities in this batch:

- `HsinTsao/Anthropic-Cybersecurity-Skills` @ `2c88b96cf758c8a742c5b683e02c01e84497034f`
- `B0llieball/Anthropic-Cybersecurity-Skills` @ `2c88b96cf758c8a742c5b683e02c01e84497034f`
- `fernandezbaptiste/Anthropic-Cybersecurity-Skills` @ `c15f73db46149587e31df83c2f9d92a3b578ef21`
- `cautionsign/Anthropic-Cybersecurity-Skills` @ `c15f73db46149587e31df83c2f9d92a3b578ef21`

The representative body blob remained the same across these inspected revisions/identities. It was already canonicalized in Batch 039, so no duplicate report is added.

### B. `jobs-to-be-done` older Wondel body — existing canonical body

- Directly reread from `Raven5101/skills` @ `955115316fdf18eaef1ba6e7a9860704215e172f`.
- Same old Wondel revision/body family already recorded in Batch 039.
- No duplicate canonical report is added.

## Inventory records not promoted to body-reviewed reports

- `skbauman3/wondelai-skills`: marketplace manifest verifies **42 skill identities**, but only `37signals-way` was newly body-reviewed here.
- Old/new `Anthropic-Cybersecurity-Skills` collections remain very large. Representative bodies and changed/new content were inspected, but the inventory as a whole is not converted into hundreds of body-reviewed reports.
- Exact-tree mirrors receive repository-identity coverage after direct reads, not duplicate canonical reports.

## Batch 040 canonical delta

- Previous canonical/report total: **2827**
- New canonical body reports: **24**
- New total: **2851**

This delta is based on direct body review, not repository metadata or manifest inventory.