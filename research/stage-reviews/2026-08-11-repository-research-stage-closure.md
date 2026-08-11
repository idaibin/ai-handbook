# Repository Research Stage Closure — 2026-08-11

## Decision

The quantity-driven repository research stage is closed at
`ai-handbook/main@214c78c403202678bf699c32ebe77f367b8f0283`.

- Skills discovery and sequential deep analysis are paused.
- Agents broad queue processing is paused after the first source-level sample.
- Workflows discovery is closed for the current sample; all current eligible items are
  analyzed.
- No topic has an active claim. Existing catalogs, queues, reports, snapshots and
  fixed revisions are retained as evidence and restart inputs.
- The next stage is pattern distillation plus falsifiable experiments in real
  repositories. More repository research is allowed only to close a named evidence
  gap.

This is a stage closure, not a claim that the GitHub ecosystem has been exhaustively
covered.

## Basis and evidence boundary

Freshness date: 2026-08-11 (Asia/Tokyo).

| Topic | Indexed state | Deep-analysis state | Runtime evidence | Stage decision |
| --- | ---: | ---: | ---: | --- |
| Skills | 2,502 canonical repository identities | 580 repository identities structurally reviewed; 3,088 repository-scoped reports; unique-content total unresolved | No reliable aggregate runtime count in canonical state | Pause; reconcile before any new scan |
| Agents | 121 identities: 94 eligible, 6 held, 21 rejected | 10 fixed-revision source reviews | 0 runtime-validated | Pause broad queue; retain targeted research capacity |
| Workflows | 41 identities: 25 eligible, 8 held, 8 rejected | 25/25 current eligible fixed-revision reviews | 1 narrow runtime validation (Hexabot core runner only) | Close current sample; distill and experiment |

Evidence boundaries:

- A repository-scoped report is not necessarily a unique Skill or unique content.
- Source inspection verifies that a mechanism exists in the inspected revision; it
  does not verify behavior under process failure, external services or production load.
- The Workflows 25/25 count covers only current query shards and eligibility rules.
- Stars and report counts are discovery/coverage metadata, not value proof.

Primary internal evidence:

- `research/agent-skills/state.json`
- `research/agents/state.json`
- `research/agents/batches/agents-deep-20260809T152200Z.md`
- `research/workflows/state.json`
- the three `research/workflows/batches/workflows-deep-*.md` batch summaries

## Stage conclusions by topic

### Skills

Verified:

- The catalog contains substantial identity coverage and reusable evidence.
- Canonical state does not know the total number of unique contents:
  `unique_content_deep_reviews = null`.
- The latest deep-analysis batch produced no new report and reused existing analyses.
- Repository identity and content identity are now separated, but historical
  reconciliation remains incomplete.

Judgment:

Continuing the remaining queue in order would optimize repository count while
duplicate/fork density is already reducing new knowledge yield. The correct next step
is reconciliation and synthesis, not another discovery shard.

Closure state:

- New indexing: paused.
- Sequential deep analysis: paused.
- Existing catalog and reports: retained.
- Resume prerequisite: unique-content reconciliation, runtime-evidence inventory and
  adoption mapping must be complete enough to measure marginal value.

### Agents

Verified:

- Ten fixed-revision repositories were source-reviewed and all ten contained genuine
  executable agent assets.
- The batch identified explicit differences in permission enforcement, durable state,
  termination, concurrency and usage accounting.
- None of the ten repositories was built or run in this research stage.

Judgment:

The sample is sufficient to define an initial permission/recovery vocabulary, but not
to rank frameworks or generalize runtime reliability. Processing all remaining 84
eligible identities would be premature. Further Agent research must be selected by an
engineering question, such as code-enforced approval or crash-resume behavior.

Closure state:

- Broad queue processing: paused.
- Existing pending queue: retained, not claimed.
- Targeted source/runtime study: allowed only when a real experiment exposes a named
  gap and the candidate can answer it.
- Maximum targeted follow-up before another decision review: 10 repositories, selected
  by mechanism rather than popularity.

### Workflows

Verified:

- All 25 currently eligible identities across three discovery shards have fixed-source
  reports.
- The strongest recurring findings are:
  durable state is not side-effect safety; human gates vary in enforcement strength;
  configured controls may be declared but never consumed; duplicate workflow copies
  may drift; checkpoint/resume must be paired with stable operation identity.
- Only Hexabot core runner tests were executed, and that validation did not exercise
  real external effects.

Judgment:

The current sample has reached synthesis saturation for the immediate decision. New
indexing is less valuable than testing the recurring mechanisms in the user's own
workflow.

Closure state:

- New workflow discovery: paused.
- Current sample: closed.
- Resume prerequisite: a real-project experiment must reveal an unresolved workflow
  mechanism that current evidence cannot answer.

## Distilled capabilities to carry forward

Only the following five patterns enter the next-stage candidate set. They are
candidate practices, not production standards yet.

| Pattern | Evidence status | Intended use | Promotion gate |
| --- | --- | --- | --- |
| Permission enforcement classification | Source-supported | Distinguish code-enforced, host-enforced, model-mediated and absent controls | Correctly classifies controlled positive/negative fixtures and one real workflow |
| Declaration-to-consumption audit | Source-supported with counterexamples | Trace retry, timeout, concurrency, approval and budget configuration into every execution path | Finds seeded inert/bypass controls without false production claims |
| Checkpoint plus side-effect safety | Source-supported | Resume long tasks without duplicate GitHub/API effects | Passes interruption/restart and duplicate-delivery experiments |
| Content identity and semantic drift detection | Partly used in research workflow | Deduplicate copied Skills and detect divergent approval/validation semantics | Historical reconciliation plus controlled drift fixture |
| Evidence-level promotion | Already used in reports | Prevent source reading from being reported as runtime success | Every experiment records revision, command, environment, artifact and remaining gap |

The following are not promoted:

- a specific Agent framework recommendation;
- a universal workflow score or ranking;
- automatic exactly-once claims for external APIs;
- broad claims based on Stars, README wording or checked-in tests;
- a new production Skill before an experiment demonstrates repeatable value.

## Next-stage execution plan

### Phase 0 — Reconcile and freeze the research inventory

Goal: make the existing evidence measurable before creating more of it.

Actions:

1. Compute or explicitly bound unique Skill content identities across historical
   reports.
2. Inventory evidence levels: metadata, structure/source, local runtime, target
   repository runtime and production.
3. Map each distilled pattern to: source reports, current adoption in
   `idaibin/skills`, missing control and proposed experiment.
4. Preserve historical counts; publish corrected unique counts as a separate
   reconciliation result instead of silently rewriting history.

Acceptance:

- Every repository identity maps to one content identity or an explicit unresolved
  reason.
- Duplicate/reused counts reconcile without double-counting repository-scoped reports.
- Runtime-validated items have an executable command, environment and result artifact;
  otherwise they are downgraded or marked unresolved.
- A single pattern ledger becomes the navigation entry for all five patterns.
- No new repository discovery occurs during this phase.

### Phase 1 — Distill three executable review contracts

Goal: turn recurring findings into small, testable contracts before modifying stable
Skills.

Contracts:

1. Permission Enforcement Review.
2. Declaration-to-Consumption Review.
3. Checkpoint and Side-effect Safety Review.

Each contract must contain:

- trigger and explicit non-trigger;
- required inputs and immutable basis;
- deterministic checks versus model judgment;
- evidence labels and prohibited claims;
- stop states and allowed effects;
- positive, negative and ambiguous fixtures;
- output schema with finding, evidence path, limitation and remediation.

Acceptance:

- Each contract has at least one fixture that must pass, one seeded failure it must
  catch and one ambiguous case it must leave `Not verified`.
- The contracts reuse current repository/Skill standards where possible; no new Skill
  is created solely to hold prose.
- An independent review confirms that the contracts do not collapse model-mediated
  guidance into code enforcement.

### Phase 2 — Run three real experiments

#### Experiment A: declaration-to-consumption

Target: a bounded real repository or isolated fixture derived from an existing
workflow.

Faults:

- declared timeout not consumed;
- concurrency limit bypassed by one trigger path;
- approval configured but not checked before an effect.

Pass condition:

- All seeded faults are found with exact declaration and consumption/bypass paths.
- A working control is not reported as broken.
- Source-level findings are not labeled runtime-verified.

#### Experiment B: checkpoint and side-effect safety

Target: one long-running, restartable GitHub research or repository-review task.

Faults:

- interruption before write;
- interruption after remote acceptance but before local acknowledgement;
- repeated resume with the same operation ID;
- expired claim/lease.

Pass condition:

- Resume produces no duplicate external write.
- Accepted results are recovered by remote reread.
- Expired work can be safely released/reclaimed.
- The artifact records operation ID, fixed basis, checkpoint, effect result and
  terminal state.

#### Experiment C: permission enforcement

Target: one workflow containing read-only, reversible write and high-impact effect
classes.

Pass condition:

- Read-only actions proceed within authorization.
- Reversible writes require the declared approval boundary.
- High-impact/irreversible effects cannot be triggered by prompt text alone.
- Deny, cancel and resume paths are recorded and tested.

### Phase 3 — Apply only validated capability

Promotion choices:

- Stable, repeatable execution capability → `idaibin/skills`.
- Cross-project policy or research method → `ai-handbook`.
- Project-specific control and runtime evidence → target repository.
- Explanatory knowledge content → `knowledge-distillation`.

Acceptance:

- At least one real project consumes each promoted contract.
- Before/after evidence shows a concrete effect: detected seeded defect, prevented
  duplicate effect, enforced approval, or improved recovery.
- Relevant tests and target-runtime verification pass.
- Independent review finds no unsupported evidence upgrade.
- If an experiment fails, retain the result in `ai-handbook`; do not promote the
  pattern as a production Skill.

## Feedback contract

Report at phase or experiment boundaries, not as a stream of activity.

Each report must contain:

| Field | Required content |
| --- | --- |
| Basis | repository, branch/ref, fixed SHA and environment |
| Goal | one decision or behavior being tested |
| Change | files/contracts changed; unrelated changes excluded |
| Evidence | commands, artifacts, source paths and external reread where relevant |
| Result | Pass / Fail / Partial / Blocked |
| Claim level | source / local deterministic / target runtime / production |
| Gaps | exact unverified behavior and why |
| Decision | keep, revise, reject or promote |
| Next | one smallest executable action |
| Git | commit and remote verification status |

A progress count alone is not an acceptable report.

## Retrospective contract

Run one retrospective after each experiment:

1. What prediction was tested?
2. What direct evidence confirmed or contradicted it?
3. Which step added value, and which produced no decision-relevant evidence?
4. Did the method create a false positive, false negative or evidence-level error?
5. What single method change will be tested next?
6. What is its metric and rollback condition?

Only one method change is introduced per next iteration unless a real failure requires
an immediate safety correction.

## Research resume gates

Broad research does not resume because a queue exists. It resumes only if all are true:

1. A named engineering decision remains unresolved.
2. Existing reports and experiments cannot answer it.
3. Candidate selection is tied to the missing mechanism.
4. The expected output has an application target and acceptance test.
5. The previous batch's marginal knowledge yield can be measured.

Topic-specific gates:

- Skills: reconciliation is complete, and a bounded pilot demonstrates materially new
  unique content or executable capability.
- Agents: a real experiment exposes a permission, recovery, orchestration or
  evaluation gap; select at most ten mechanism-relevant candidates.
- Workflows: current patterns fail or leave a specific mechanism unresolved in a real
  project; search only for that mechanism.

If these gates are not met, remain in distillation/application mode.

## Claim-evidence ledger

| ID | Claim | Status | Evidence | Limitation |
| --- | --- | --- | --- | --- |
| C1 | Skills quantity metrics currently overstate unique reusable knowledge | Verified | Skills canonical state has 3,088 repository-scoped reports but unknown unique-content count; latest batch added no report | Full historical reconciliation is pending |
| C2 | Agent permission and recovery mechanisms differ materially | Verified at source level | Ten fixed-revision Agent reports | No runtime comparison |
| C3 | Current Workflow sample is sufficient for first experiments | Inference | 25 source reviews repeatedly converge on the same control gaps | Does not establish ecosystem completeness |
| C4 | The five distilled patterns improve the user's real workflow | Not verified | No complete before/after target-project experiment yet | Phases 1–3 are required |
| C5 | Broad scanning now has lower value than application | Inference | Duplicate-heavy Skills tail, closed Workflow sample and runtime-evidence gap | Could change if a named gap produces a high-yield pilot |

## Completion state

`Complete with gaps`.

The current research stage is safely closed and has a decision-ready next plan.
Unique-content reconciliation and real-project outcome evidence remain incomplete; they
are the next stage's explicit work, not hidden completion claims.
