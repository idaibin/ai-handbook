# Agent Skills Individual Reports — Batch 035

- Batch ID: `2026-08-08-batch-035`
- Repository `SKILL.md` reads: **10**
- Direct unique skill bodies reviewed: **8**
- New canonical skill bodies: **1**
- Existing canonical bodies revalidated: **7**
- Runtime/build/test/eval execution: **not_executed**

This file preserves content-level deduplication. Seven unique Git commit trees in this batch already have canonical deep reviews from Batch 030 or Batch 031. `context-budget-analyzer` is new to the current AI-handbook deep-analysis corpus and receives one new canonical report.

## `worker-prompt-craft`

- Reviewed repository identity: `wbxjj2008/worker-prompt-craft`
- Repository ID: `1198101932`
- Stars observed: `0`
- Revision: `8f8a14fc8da0e687457516da3d9f79f8873e9061`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: self-contained worker/sub-agent prompts using exact paths, completion criteria, purpose statements, and verification expectations
- Strengths: reduces hidden-context assumptions; makes delegation criteria explicit; distinguishes research and implementation prompts
- Risks: Git examples normalize commits, pushes, PR creation, and reviewer changes without an explicit authorization gate
- Verdict: high-value delegation guidance once external side effects are gated separately

## `task-concurrency-patterns`

- Reviewed repository identities: `MandyDragon/task-concurrency-patterns`, `YTT-CSH/task-concurrency-patterns`
- Repository IDs: `1197912503`, `1198155959`
- Stars observed: `0` for both
- Shared revision: `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; both identities expose the same Git commit tree
- Purpose: dependency edges, fan-out/fan-in orchestration, read/write concurrency guidance, worker cancellation, and failure escalation
- Strengths: explicit `blocks`/`blockedBy` modeling and same-area write conflict awareness
- Risks: binary `concurrencySafe` ignores shared resources, locks, rate limits, credentials, side effects, and transaction boundaries; fixed retry counts ignore failure class and cost
- Verdict: useful orchestration vocabulary after adding resource-scoped concurrency and failure-aware retry policy

## `memory-type-system`

- Reviewed repository identity: `MandyDragon/memory-type-system`
- Repository ID: `1197912140`
- Stars observed: `0`
- Revision: `d3805f3e5a576afd0c55e2de9cddb78511a30c95`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: typed `user|feedback|project|reference` memory records, per-record frontmatter, drift checks, and a bounded `MEMORY.md` index
- Strengths: clean separation between index and record content; explicit types improve routing; current-state checks reduce stale-memory errors
- Risks: fixed 200-line / 25 KB limits lack retrieval-quality evidence; blanket NOT-to-save rules need explicit user-authorized exceptions
- Verdict: structurally useful memory schema, but capacity and exception rules should be evidence-driven

## `context-budget-analyzer` — new canonical report

- Reviewed repository identity: `ajunlonglive/context-budget-analyzer`
- Repository ID: `1198092186`
- Stars observed: `0`
- Revision: `7d969967a717beb52538d510d42ee45b9f2d65a8`
- Canonical deep review: Batch 035
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Content class: document/policy skill; no implemented analyzer was found
- Purpose: diagnose context pressure by categorizing message/tool/attachment token use, highlighting repeated file reads, and applying optimization thresholds

### Design summary

The skill proposes six accounting buckets (`Human`, `Assistant`, tool requests, tool results, attachments, system/other), per-tool distributions, duplicate-read estimates, and context-pressure actions at 50%, 75%, and 90% of the model limit. Its optimization advice includes narrower retrieval, avoiding repeated full-file reads, limiting oversized command output, and compacting under high pressure.

### Strengths

- Makes context use an explicit engineering resource rather than an intuition-only concern.
- Separates tool requests from tool results, which is useful because result payloads can dominate tool-heavy sessions.
- Calls out repeated reads as something to measure instead of assuming all retrieval is free.
- Encourages targeted retrieval over indiscriminate full-file loading.
- Provides an understandable diagnostic format that could become a real telemetry report if backed by host data.

### Risks and missing evidence

1. **No token-accounting implementation.** The examples use `XXX tokens`; there is no tokenizer, trace parser, provider integration, script, or package that computes the numbers.
2. **Host visibility is incomplete.** Hidden system content, tool schemas, cached prefixes, compression, and model-specific tokenization may not be observable to a skill, so manual percentages can be materially wrong.
3. **Duplicate read ≠ waste by definition.** Re-reading is valid after file mutation, partial reads, context compression, or when fresh-state verification is required. Cache reuse needs content hash/revision invalidation.
4. **Thresholds are unvalidated.** The 50/75/90% bands have no repository-local eval connecting them to truncation probability, latency, quality, or recall.
5. **Blind output truncation is risky.** Generic `head`/`tail` limits can hide decisive errors. Structured filtering or scoped queries are safer where correctness matters.
6. **Attachment removal can destroy task evidence.** Images/documents may be authoritative task inputs and should only be compacted with preservation rules.
7. **No quality trade-off measurement.** The repository does not measure whether token reduction causes missed files, stale state, omitted evidence, or lower task success.

### Recommended adoption pattern

Use the skill as a checklist only. A production-grade version should consume actual host usage metadata where available, distinguish cached/reused tokens from effective context pressure, track file content revisions before suppressing re-reads, preserve task-critical attachments/evidence, and evaluate token savings together with task accuracy and recall.

- Verdict: **useful diagnostic policy, not a verified analyzer implementation**

## `self-rationalization-guard`

- Reviewed repository identities: `camCX/self-rationalization-guard`, `MandyDragon/self-rationalization-guard`
- Repository IDs: `1198540077`, `1197912299`
- Stars observed: `0` for both
- Shared revision: `3df614e3ae87d80b3be338d247a2fc2488dc22a2`
- Existing canonical deep review: Batch 031
- Structure: root `README.md` + root `SKILL.md`; both identities expose the same Git commit tree
- Purpose: detect execution, communication, quality, and delegation shortcuts and force counter-actions
- Strengths: distinguishes code inspection from executed evidence and pushes against repetitive reasoning loops
- Risks: universal inversion rules can conflict with authorization, risk, expected value, and scope
- Verdict: useful anti-rationalization checklist after adding risk/authority/value gates

## `smart-memory-guard`

- Reviewed repository identity: `alexchenyu/smart-memory-guard`
- Repository ID: `1198042883`
- Stars observed: `0`
- Revision: `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: memory admission control, four-type classification, drift checks, pruning, and feedback metadata
- Strengths: verifies current state before acting on remembered paths/symbols/endpoints; separates durable facts from recoverable repository facts
- Risks: blanket NOT-to-save rules can conflict with explicit user intent; 5 KB and seven-day thresholds are unvalidated; README's 62% reduction is anecdotal
- Verdict: useful memory-hygiene policy after adding user-authorized exceptions and measurable retention criteria

## `adversarial-verification`

- Reviewed repository identity: `ShawnSiao/adversarial-verification`
- Repository ID: `1198481081`
- Stars observed: `0`
- Revision: `909a2f70fc0de13aff1175c0b507ec24bf0b4815`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; no surfaced executable harness or eval suite
- Purpose: require observed execution evidence plus adversarial and non-happy-path checks before claiming success
- Strengths: explicitly rejects source reading as runtime proof; requires command output, edge probes, and an explicit verdict
- Risks: compliance is prompt-enforced only; unconditional command-running guidance is too broad for analysis-only work, unavailable tools, or unauthorized side effects
- Verdict: strong verification discipline when conditioned on task type, authorization, tool availability, and side-effect risk

## `coordinator-orchestrator`

- Reviewed repository identity: `ajunlonglive/coordinator-orchestrator`
- Repository ID: `1198083717`
- Stars observed: `0`
- Revision: `a6d0311d279b32497a9c952061fafb798309b4e3`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: research → synthesis → implementation → verification coordination, with Continue-vs-Spawn guidance
- Strengths: synthesis remains a coordinator responsibility; fresh verification workers reduce anchoring; prompts are expected to be self-contained
- Risks: “independent tasks always parallel” ignores shared resources, rate limits, databases, credentials, deployment targets, and side effects
- Verdict: strong coordination pattern if parallelism is gated by resource ownership and side-effect boundaries

## Provenance note

The reviewed READMEs instruct installation from `Arxchibobo/...` repositories even though the indexed identities belong to other GitHub owners. This is self-declared provenance and remains separate from verified repository identity and exact content identity until lineage is independently established.

## Deduplication record

Eight unique skill-content trees were directly reviewed. Seven were already represented by canonical reports. Batch 035 therefore adds **1** new canonical skill report while adding **10** repository identities to structure-reviewed coverage. Two within-batch identity pairs share exact commit SHAs: `task-concurrency-patterns` and `self-rationalization-guard`.
