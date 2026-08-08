# Agent Skills Deep Analysis — Batch 034

- Batch ID: `2026-08-08-batch-034`
- Stage: repository deep analysis
- Queue source: `sources/catalog/batches/agentskills-created-2026-04-01-deterministic.json`
- Queue slice: entries 60–69 of the April 1 deterministic shard
- Repositories completed: **10**
- Repository `SKILL.md` reads: **10**
- Unique Git commit trees directly reviewed: **7**
- Unique `SKILL.md` bodies reviewed: **7**
- New canonical individual skill reports after content deduplication: **0**
- Runtime/build/test/eval execution: **not_executed**

## Completion gate

A repository is counted only after GitHub identity, exact observed star count, a pinned Git revision, and actual repository content were verified. All ten identities matched exact GitHub repository-search queries constrained with `stars:0`, so the observed star count for every repository was **0** during this review. Latest revisions were pinned through GitHub commit search. Root `SKILL.md` was directly fetched for all ten identities. README bodies were directly reviewed for all seven unique commit trees.

Identical Git commit SHAs across repository identities are treated as deterministic full-tree duplicate evidence because the commit object binds the repository tree. Every unique tree in this batch was already deeply reviewed in Batch 030 or Batch 031, so this batch increases repository-identity coverage without creating duplicate canonical skill-content entries.

## Repository results

| Repository | GitHub ID | Stars | Reviewed revision | Content-proven class | New canonical skill reports | Result |
|---|---:|---:|---|---|---:|---|
| `ShawnSiao/task-concurrency-patterns` | `1198484689` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `task-concurrency-patterns` |
| `ShawnSiao/coordinator-orchestrator` | `1198483056` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `coordinator-orchestrator` |
| `alexchenyu/worker-prompt-craft` | `1198043569` | 0 | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `worker-prompt-craft` |
| `MandyDragon/smart-memory-guard` | `1197911411` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `smart-memory-guard` |
| `camCX/coordinator-orchestrator` | `1198537252` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | exact full-tree duplicate | 0 | same tree as `ShawnSiao/coordinator-orchestrator` |
| `wbxjj2008/memory-type-system` | `1198102579` | 0 | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `memory-type-system` |
| `alexchenyu/adversarial-verification` | `1198042580` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 030 `adversarial-verification` |
| `ShawnSiao/worker-prompt-craft` | `1198483571` | 0 | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | exact full-tree duplicate | 0 | same tree as `alexchenyu/worker-prompt-craft` |
| `alexchenyu/self-rationalization-guard` | `1198044202` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact full-tree duplicate of reviewed single skill | 0 | maps to Batch 031 `self-rationalization-guard` |
| `ajunlonglive/self-rationalization-guard` | `1198087694` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact full-tree duplicate | 0 | same tree as `alexchenyu/self-rationalization-guard` |

## Structure and artifact inspection

The reviewed revisions are small document/policy skill packages centered on root `README.md` and root `SKILL.md`. Repository code search across all ten identities for `scripts references eval package.json` returned **0 matches**. The reviewed README and skill bodies expose no repository-local executable harness, script bundle, reference bundle, package manifest, test suite, or eval suite.

This batch therefore records content review only. No runtime, build, test, deployment, or evaluation success is inferred from prompt/document content.

## Revalidated skill groups

### `task-concurrency-patterns`

Revision `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` was directly re-read through `ShawnSiao/task-concurrency-patterns`. It defines read/write separation, a three-state task lifecycle, explicit `blocks`/`blockedBy` dependency edges, fan-out/fan-in patterns, worker stopping, and fixed three-attempt escalation.

The useful part remains explicit dependency modeling and avoiding obvious same-area write conflicts. The main weakness remains the binary `concurrencySafe` model: actual safety also depends on resource scope, locks, rate limits, shared credentials, external side effects, and transaction boundaries. Fixed retry counts are not calibrated by failure class or cost.

### `coordinator-orchestrator`

Revision `a6d0311d279b32497a9c952061fafb798309b4e3` was directly re-read through both `ShawnSiao/coordinator-orchestrator` and `camCX/coordinator-orchestrator`; both expose the same commit tree. It defines research → synthesis → implementation → verification, keeps synthesis with the coordinator, and distinguishes Continue from Spawn based on context overlap.

The synthesis requirement and fresh-agent verification pattern remain useful. The universal claim that independent tasks should always run in parallel is too broad because logically independent tasks can still contend for files, databases, rate limits, credentials, deployment targets, or other shared resources.

### `worker-prompt-craft`

Revision `8f8a14fc8da0e687457516da3d9f79f8873e9061` was directly re-read through both `alexchenyu/worker-prompt-craft` and `ShawnSiao/worker-prompt-craft`; both expose the same commit tree. The skill requires self-contained worker prompts with exact paths, completion criteria, purpose statements, and verification expectations.

This remains strong delegation-contract guidance. The material risk is that examples normalize commit, push, PR creation, and reviewer changes as ordinary completion steps without a separate authority gate for external side effects.

### `smart-memory-guard`

Revision `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` was directly re-read through `MandyDragon/smart-memory-guard`. It combines four memory types, a NOT-to-save list, drift verification, `Why`/`How to apply` feedback metadata, and pruning heuristics.

Current-state verification before acting on remembered paths, functions, endpoints, or project status remains strong. Risks remain around blanket rejection of some user-requested memories, fixed 5 KB / seven-day thresholds without repository-local evaluation, and the README's `13.4KB → 5.0KB` example being an anecdotal claim rather than a reproducible benchmark.

### `memory-type-system`

Revision `d3805f3e5a576afd0c55e2de9cddb78511a30c95` was directly re-read through `wbxjj2008/memory-type-system`. It formalizes `user`, `feedback`, `project`, and `reference` memory records, per-item frontmatter, drift checks, and a bounded `MEMORY.md` index.

The index-versus-record separation is structurally useful. Fixed 200-line / 25 KB limits still lack measured retrieval-quality evidence, and blanket NOT-to-save rules need an explicit user-authorized exception model for facts the user intentionally wants persisted.

### `adversarial-verification`

Revision `909a2f70fc0de13aff1175c0b507ec24bf0b4815` was directly re-read through `alexchenyu/adversarial-verification`. It requires actual command execution, observed output, non-happy-path checks, at least one adversarial probe, and an explicit final verdict.

The distinction between source inspection and runtime proof remains valuable. The repository itself provides no harness or eval proving that an agent follows the policy reliably. The unconditional heuristic to run commands whenever explanation is being written is too broad for analysis-only work, unavailable tools, or operations requiring authorization.

### `self-rationalization-guard`

Revision `3df614e3ae87d80b3be338d247a2fc2488dc22a2` was directly re-read through both `alexchenyu/self-rationalization-guard` and `ajunlonglive/self-rationalization-guard`; both expose the same commit tree. It lists execution, communication, quality, and delegation rationalizations and maps them to counter-actions.

The anti-handwaving intent remains useful, especially distinguishing code reading from execution evidence. Several counter-rules remain over-generalized: always running commands, always doing the hardest item first, handling every unlikely edge case, and always writing documentation immediately can conflict with authorization, risk, expected value, and task scope.

## Cross-batch findings

1. **Mirror density remains high.** All ten repository identities in this slice map to seven skill-content trees already represented in the canonical review set.
2. **Three duplicate pairs are visible inside this batch.** Coordinator, worker-prompt, and self-rationalization repositories each contain two identities sharing an identical commit SHA.
3. **Repository coverage and unique content coverage must remain separate metrics.** This batch adds ten verified repository identities but zero new canonical skill bodies.
4. **Provenance remains separate from repository identity.** The reviewed READMEs instruct installation from `Arxchibobo/...` while the indexed repository owners are `ShawnSiao`, `alexchenyu`, `MandyDragon`, `camCX`, `wbxjj2008`, and `ajunlonglive`. That is self-declared upstream provenance, not proof that the indexed repositories are the canonical source.
5. **The recurring design gap is missing policy gates.** Concurrency, memory retention, command execution, retries, and external Git side effects are described with broad rules that need resource, authority, and risk-aware conditions.

## Validation status

- Repository identity: **verified for all 10**.
- Stars: exact observed value **0** verified for all 10 with GitHub repository-search `stars:0` constraints.
- Exact revision: **pinned for all 10**.
- `SKILL.md`: **directly fetched for all 10 repository identities**.
- README: **7 unique bodies directly reviewed**, covering every unique commit tree in this batch.
- Scripts/references/evals/package manifests: **none surfaced** in repository code search or reviewed docs.
- Runtime/build/tests/evals: **not_executed / not_verified**.
