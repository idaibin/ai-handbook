# Agent Skills Deep Analysis — Batch 037

- Batch ID: `2026-08-08-batch-037`
- Stage: repository deep analysis
- Queue source: `sources/catalog/batches/agentskills-created-2026-04-02-deterministic.json`
- Repositories completed: **10**
- Repository `SKILL.md` reads: **10**
- Repository README reads: **10**
- Unique Git commit trees directly reviewed: **6**
- New canonical individual skill reports after content deduplication: **0**
- Runtime/build/test/eval execution: **not_executed**

## Completion gate

A repository is counted only after GitHub identity, exact observed star count, a pinned Git revision, and actual repository content were verified. All ten identities matched exact GitHub repository-search queries constrained with `stars:0`, so the observed star count for every completed repository was **0** during this review. Latest revisions were pinned through GitHub commit search. Root `SKILL.md` and README were directly fetched from every repository identity at its pinned revision.

Repository code search across all ten identities returned no matches for `scripts`, `references`, `eval`, or `package.json`. These revisions are therefore treated as document/policy skill packages, not as repositories with a local executable harness or evaluation suite. Runtime/build/test/eval success is not inferred from prose.

## Repository results

| Repository | GitHub ID | Stars | Reviewed revision | Content-proven class | New canonical reports | Result |
|---|---:|---:|---|---|---:|---|
| `4ccsds/smart-memory-guard` | `1199649094` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `smart-memory-guard` review |
| `drcaonet/self-rationalization-guard` | `1198990114` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `self-rationalization-guard` review |
| `howknows/adversarial-verification` | `1199419855` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `adversarial-verification` review |
| `howknows/self-rationalization-guard` | `1199422364` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact full-tree duplicate | 0 | same tree as `drcaonet/self-rationalization-guard` |
| `4ccsds/worker-prompt-craft` | `1199651297` | 0 | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `worker-prompt-craft` review |
| `4ccsds/coordinator-orchestrator` | `1199650563` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `coordinator-orchestrator` review |
| `4ccsds/lightweight-explorer` | `1199649751` | 0 | `ba11d7eaab78fafd3982d36bff78c0f3fba633b1` | exact full-tree duplicate of reviewed single skill | 0 | maps to existing `lightweight-explorer` review |
| `4ccsds/self-rationalization-guard` | `1199652508` | 0 | `3df614e3ae87d80b3be338d247a2fc2488dc22a2` | exact full-tree duplicate | 0 | same tree as other `self-rationalization-guard` identities |
| `howknows/worker-prompt-craft` | `1199422775` | 0 | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | exact full-tree duplicate | 0 | same tree as `4ccsds/worker-prompt-craft` |
| `drcaonet/coordinator-orchestrator` | `1198989947` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | exact full-tree duplicate | 0 | same tree as `4ccsds/coordinator-orchestrator` |

## Content review

### `smart-memory-guard`

The skill proposes typed memory admission (`user`, `feedback`, `project`, `reference`), drift checks before acting on remembered facts, and pruning rules intended to reduce stale or noisy memory. The strongest transferable idea is validating remembered paths, symbols, endpoints, and project state against current evidence before relying on them.

Its fixed 5 KB pruning threshold and seven-day summary rule are heuristics without repository-local retrieval-quality evaluation. The absolute rule refusing some requested memories can also conflict with explicit user-authorized retention. The README's reported memory-size reduction is a repository claim, not a reproducible benchmark in this repository.

### `self-rationalization-guard`

The skill is a prompt-level anti-shortcut checklist that distinguishes source inspection from execution evidence and asks for an explicit completion self-check. That can reduce false completion claims.

Several prescriptions are overly universal: always run commands rather than explain, do the hardest task first, handle unlikely edge cases, and write documentation immediately. These should be risk-, scope-, and authorization-aware conditions rather than unconditional rules.

### `adversarial-verification`

The skill frames verification as falsification rather than happy-path confirmation and asks for observed command output, non-happy-path checks, and adversarial probes. That is useful as a validation discipline.

The repository itself contains no executable harness or eval proving adherence. Mandatory command execution is too broad for analysis-only work, unavailable tooling, or actions that require separate authorization; a risk-matched verification ladder would be safer and more reusable.

### `worker-prompt-craft`

The strongest pattern is making delegated prompts self-contained with exact paths, purpose, completion criteria, and verification expectations. This reduces failures caused by hidden coordinator context.

Its Git examples normalize branch creation, commits, pushes, PR creation, and reviewer changes inside generic prompt templates. Those are external side effects and should be separated behind explicit authorization rather than being treated as routine delegation defaults.

### `coordinator-orchestrator`

The four-stage model — research, coordinator synthesis, worker implementation, independent verification — is a useful separation of responsibilities. The Continue-vs-Spawn guidance also captures context reuse versus fresh-perspective tradeoffs.

The rule that independent tasks should always run in parallel is too absolute because rate limits, shared files, databases, credentials, locks, deployment targets, and external side effects can couple otherwise independent-looking work. The fixed two-failure/three-failure escalation sequence is likewise heuristic rather than evidence-based.

### `lightweight-explorer`

The read-only exploration boundary, search-depth modes, and concise evidence-oriented output are useful. Separating exploration from mutation lowers accidental-change risk.

However, the claim that read-only work does not need full project rules is unsafe as a general policy: repository rules may govern restricted paths, generated files, secrets, or evidence requirements. Generic use of `head`-style truncation can hide decisive results, and mandatory parallel search can conflict with resource limits.

## Cross-repository findings

1. **Mirror density remains high.** Ten repository identities collapse to six exact Git content trees, all already represented in prior canonical reviews.
2. **Repository coverage and unique-content coverage remain separate metrics.** This batch legitimately adds ten content-verified repository identities while adding zero new canonical skill bodies.
3. **These are policy/document packages, not executable systems.** No repository-local scripts, references, evals, or package manifests surfaced in the artifact searches.
4. **Several rules are expressed as absolutes where conditional gates are safer.** Command execution, parallelism, retries, memory retention, Git side effects, and output truncation all depend on context, authorization, resource coupling, and risk.
5. **Self-declared provenance is not canonical-upstream proof.** Multiple README installation/source references point to another owner; this is documentation evidence only, not proof of upstream ownership.

## Validation status

- Repository identity: **verified for all 10**.
- Stars: exact observed value **0** verified for all 10.
- Exact revision: **pinned for all 10**.
- `SKILL.md`: **directly fetched for all 10 repository identities**.
- README: **directly fetched for all 10 repository identities**.
- Unique content trees: **6**.
- Scripts/references/evals/package manifests: **none surfaced** in repository code search.
- Runtime/build/tests/evals: **not_executed / not_verified**.
- Unselected indexed entries remain **pending** and are not counted complete.
