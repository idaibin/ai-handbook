# Agent Skills Deep Analysis — Batch 030

- Batch ID: `2026-08-08-batch-030`
- Stage: repository deep analysis
- Queue source: `sources/catalog/batches/agentskills-created-2026-04-01-deterministic.json`
- Repositories completed: **10**
- Direct `SKILL.md` bodies reviewed: **6**
- Individual skill reports added: **6**
- Runtime/build/test/eval execution: **not_executed**

## Completion gate

A repository is counted only after its GitHub identity and exact point-in-time star count were verified, an exact Git revision was pinned, and actual repository contents were read. For every repository in this batch, GitHub repository search with the exact qualifier `repo:<owner/name> stars:0` matched the intended repository, verifying an observed star count of zero at review time.

Four repository pairs resolve to identical Git commit SHAs. Because a Git commit is content-addressed and binds the complete tree, each shared revision is treated as deterministic full-tree duplicate evidence. The shared tree was content-reviewed once per unique revision and mapped to both repository identities. Duplicate repositories do not inflate the individual-skill report count.

## Repository results

| Repository | ID | Stars | Reviewed revision | Content-proven class | Skill reports | Result |
|---|---:|---:|---|---|---:|---|
| `camCX/adversarial-verification` | `1198534332` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | document-only single skill | 1 | adversarial runtime-verification procedure with mandatory evidence format |
| `YTT-CSH/adversarial-verification` | `1198117559` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | exact full-tree duplicate | 0 | same tree as `camCX/adversarial-verification` |
| `ajunlonglive/smart-memory-guard` | `1198081842` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | document-only single skill | 1 | memory admission, drift checking and pruning policy |
| `k1w1f1sh/smart-memory-guard` | `1198053675` | 0 | `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb` | exact full-tree duplicate | 0 | same tree as `ajunlonglive/smart-memory-guard` |
| `alexchenyu/coordinator-orchestrator` | `1198043379` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | document-only single skill | 1 | multi-agent research/synthesis/implementation/verification orchestration |
| `k1w1f1sh/coordinator-orchestrator` | `1198054856` | 0 | `a6d0311d279b32497a9c952061fafb798309b4e3` | exact full-tree duplicate | 0 | same tree as `alexchenyu/coordinator-orchestrator` |
| `ajunlonglive/task-concurrency-patterns` | `1198087036` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | document-only single skill | 1 | concurrency, dependency and failure-escalation guidance |
| `k1w1f1sh/task-concurrency-patterns` | `1198061428` | 0 | `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e` | exact full-tree duplicate | 0 | same tree as `ajunlonglive/task-concurrency-patterns` |
| `YTT-CSH/worker-prompt-craft` | `1198154943` | 0 | `8f8a14fc8da0e687457516da3d9f79f8873e9061` | document-only single skill | 1 | self-contained worker/sub-agent prompt construction guidance |
| `camCX/memory-type-system` | `1198538950` | 0 | `d3805f3e5a576afd0c55e2de9cddb78511a30c95` | document-only single skill | 1 | four-type memory taxonomy, per-memory frontmatter and index rules |

## Structure and artifact inspection

The six unique trees are very small single-skill packages. For each unique revision, the root `README.md` and root `SKILL.md` were read directly. Repository code search across all six unique repositories returned no matches for `scripts`, `references`, or `eval`; neither the reviewed README files nor skill bodies identify repository-local executable helpers, reference directories, or evaluation suites. These are therefore prompt/document packages at the reviewed revisions, not script-backed skills.

No runtime, build, command, test, or evaluation execution was performed. Source/document inspection is not promoted to runtime success.

## 1–2. `adversarial-verification` exact duplicate pair

Both repositories point to `909a2f70fc0de13aff1175c0b507ec24bf0b4815`. The reviewed tree contains a root README and `SKILL.md`; the skill body requires verification by running commands, recording observed output, probing at least one adversarial/edge condition, checking non-happy paths, and ending with `PASS`, `FAIL`, or `PARTIAL`.

### Strengths

The skill directly counters a common agent failure mode: replacing execution evidence with code-reading narration. It distinguishes frontend, backend/API, CLI/script, infrastructure, bug-fix and refactor validation paths and requires observed command output rather than a prose-only assertion.

### Limits

The verification discipline is entirely prompt-enforced; there is no repository-local harness or eval proving that an agent follows it reliably. Several triggers and examples are personalized to another user/context (`bobooo`). The README installation commands point to `Arxchibobo/adversarial-verification`, not either reviewed repository identity, creating an installation/provenance mismatch.

## 3–4. `smart-memory-guard` exact duplicate pair

Both repositories point to `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb`. The skill defines four memory classes (`user`, `feedback`, `project`, `reference`), a six-category NOT-to-save policy, explicit `Why`/`How to apply` fields for feedback, drift checks before acting on memory, and periodic pruning rules.

### Strengths

The strongest idea is separating durable user/project context from information that already has a better authority such as source code or Git history. The drift checks also correctly treat remembered file paths, symbols, endpoints and project state as claims to re-verify rather than current truth.

### Limits

The policy is too absolute in places: it says some classes should not be saved even when the owner explicitly asks to remember them, which can conflict with user-authorized intent. The 5 KB pruning threshold and seven-day summary rule are fixed heuristics without repository-local evidence. The README claims a 62% memory-size reduction from one example but contains no eval artifact establishing general effectiveness. Installation again points to `Arxchibobo/smart-memory-guard`.

## 5–6. `coordinator-orchestrator` exact duplicate pair

Both repositories point to `a6d0311d279b32497a9c952061fafb798309b4e3`. The skill separates work into research, coordinator synthesis, worker implementation and worker verification. It also defines Continue-vs-Spawn rules and emphasizes parallel read-only research.

### Strengths

The requirement that the coordinator synthesize worker findings before issuing implementation instructions is valuable: it prevents blind forwarding of sub-agent conclusions. The explicit fresh-worker option for verification can reduce anchoring to the implementer's reasoning.

### Limits

The framing "you are coordinator, not executor" can push an agent toward unnecessary delegation even though the same skill says simple tasks should be answered directly. Fixed retry counts (continue, change approach, then report after the third failure) are heuristic rather than risk- or cost-aware. The README cites reverse-engineered Claude Code material as inspiration, but that provenance claim was not independently verified in this batch. Installation points to `Arxchibobo/coordinator-orchestrator`.

## 7–8. `task-concurrency-patterns` exact duplicate pair

Both repositories point to `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e`. The skill defines read/write separation, a `pending -> in_progress -> completed` task state model, `blocks`/`blockedBy` dependency edges, fan-out/fan-in patterns and a three-step failure escalation rule.

### Strengths

The dependency model is simple enough for deterministic orchestration and makes prerequisite relationships explicit. Separating independent research from conflicting writes is a useful baseline for multi-agent execution.

### Limits

`concurrencySafe: true|false` is too coarse for real systems. Read-only calls can still share quotas, locks or expensive external resources, and writes to different files can still conflict through databases, generated artifacts, build outputs or deployment state. The statement that read-only work can run with no limit should therefore be treated as a local heuristic, not a universal concurrency rule. Installation points to `Arxchibobo/task-concurrency-patterns`.

## 9. `YTT-CSH/worker-prompt-craft`

Revision `8f8a14fc8da0e687457516da3d9f79f8873e9061` contains a root README and root skill. It teaches self-contained worker prompts with concrete paths/lines, an explicit definition of done and a purpose statement. It separates research, implementation, correction and Git-operation prompt patterns.

### Strengths

The skill correctly assumes a worker may not see the parent conversation. Requiring objective completion criteria and explicit read-only/write intent can materially reduce ambiguous delegation.

### Limits

The examples can over-anchor a worker to a diagnosis before it has independently verified the cause. Some templates instruct the worker to commit and report a hash, which is inappropriate unless write/commit authorization is already established. There is no repository-local validator for prompt completeness or eval showing improved first-pass task success. Installation points to `Arxchibobo/worker-prompt-craft`.

## 10. `camCX/memory-type-system`

Revision `d3805f3e5a576afd0c55e2de9cddb78511a30c95` defines a four-type memory taxonomy, one-file-per-memory frontmatter (`name`, `description`, `type`), drift verification, and a separate `MEMORY.md` index capped at 200 lines / 25 KB.

### Strengths

The index-versus-body split is a concrete progressive-disclosure pattern: short descriptors support retrieval while full memory bodies remain separate. The skill also normalizes relative project dates to absolute dates and requires present-state verification before acting on remembered code/project claims.

### Limits

One-file-per-memory can create file-count and retrieval-management overhead at scale. The 200-line/25 KB limits are fixed heuristics rather than measured thresholds. The four categories can overlap (`project` versus `reference` especially), so a production memory system would benefit from explicit tie-breaking or multi-tag support. This skill materially overlaps `smart-memory-guard`; the former is more schema/recall oriented while the latter is more admission/pruning oriented. Installation points to `Arxchibobo/memory-type-system`.

## Cross-batch findings

1. **Commit-level deduplication remains necessary.** Four pairs of independent GitHub repository identities are exact full-tree duplicates at their reviewed revisions.
2. **Repository identity and provenance diverge.** All six unique README files instruct installation from `Arxchibobo/...`, not from the repository being reviewed. The catalog should preserve current repository identity separately from self-declared/upstream provenance.
3. **These are policy skills, not executable skills.** No repository-local scripts, references or eval suites were found by content search for the six unique trees; quality claims therefore remain prompt-level unless separately evaluated.
4. **Several rules are useful but overly universal.** Unlimited read-only concurrency, fixed retry counts, fixed memory-size limits and categorical refusal to store certain information should be parameterized by environment, authority and risk.
5. **Memory skills overlap substantially.** `smart-memory-guard` and `memory-type-system` share taxonomy, NOT-to-save and drift-verification concepts; catalog consumers should not assume they are orthogonal capabilities.

## Validation status

- Repository identity: verified for all 10.
- Stars: exact observed value `0` verified for all 10 with GitHub repository-search qualifiers.
- Exact revision: pinned for all 10.
- README: read for all six unique content trees; shared-revision pairs inherit the same content-addressed tree.
- `SKILL.md`: **6 unique bodies directly reviewed**.
- Scripts/references/evals: none surfaced in repository search or reviewed documentation at these revisions.
- Runtime/build/tests/evals: **not_executed**.
