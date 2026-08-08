# Agent Skills Individual Reports — Batch 033

- Batch ID: `2026-08-08-batch-033`
- Repository `SKILL.md` reads: **10**
- Direct unique skill bodies reviewed: **8**
- New canonical skill bodies: **1**
- Existing canonical bodies revalidated: **7**
- Runtime/build/test/eval execution: **not_executed**

This file preserves content-level deduplication. Repositories that resolve to already-reviewed Git commit trees receive repository-to-canonical mappings rather than duplicate canonical skill entries. The new canonical content in this batch is `background-memory-extractor`.

## `task-concurrency-patterns`

- Reviewed repository identity: `camCX/task-concurrency-patterns`
- Revision: `7fa43a3fc72ceb0fb488fedbb09faa37198fcb5e`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: dependency edges, fan-out/fan-in orchestration, read/write concurrency guidance, and worker failure escalation
- Revalidated strengths: explicit dependency modeling; avoids obvious same-area write conflicts; stops workers when direction changes
- Revalidated risks: binary `concurrencySafe` ignores resource scope/rate limits; fixed retry count ignores failure type, cost, and side effects
- Verdict: useful orchestration vocabulary if concurrency is made resource-aware and retries are failure-class aware

## `smart-memory-guard`

- Reviewed repository identity: `ShawnSiao/smart-memory-guard`
- Revision: `802b0f14f8f0fbdc8ee4be39cdc342e5121efbeb`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: memory admission, four-type classification, drift checks, and pruning
- Revalidated strengths: verifies current state before acting on remembered paths/symbols/endpoints; distinguishes memory from stronger authorities
- Revalidated risks: owner-request overrides are rejected too absolutely; 5 KB and seven-day thresholds are unvalidated; README's 62% reduction claim is anecdotal
- Verdict: useful memory-hygiene policy after adding authority-aware exceptions and measured retention criteria

## `memory-type-system`

- Reviewed repository identities: `ajunlonglive/memory-type-system`, `k1w1f1sh/memory-type-system`
- Shared revision: `d3805f3e5a576afd0c55e2de9cddb78511a30c95`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; both repository identities expose the same Git commit tree
- Purpose: typed `user|feedback|project|reference` memory records, per-item frontmatter, drift checks, and a bounded memory index
- Revalidated strengths: clean index-vs-record separation; explicit memory types improve routing and retrieval semantics
- Revalidated risks: fixed 200-line / 25 KB caps lack retrieval-quality evidence; blanket NOT-to-save rules need explicit user-authorized exceptions
- Verdict: structurally useful memory schema, but retention and exception behavior need measurable and authority-aware rules

## `adversarial-verification`

- Reviewed repository identity: `MandyDragon/adversarial-verification`
- Revision: `909a2f70fc0de13aff1175c0b507ec24bf0b4815`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; no surfaced executable harness/eval
- Purpose: require observed execution evidence plus adversarial and non-happy-path checks before claiming success
- Revalidated strengths: explicitly rejects source reading as runtime proof; requires command output, edge checks, and verdicts
- Revalidated risks: prompt-enforced only; unconditional command-running heuristic is too broad for analysis-only or unauthorized operations
- Verdict: strong verification discipline when conditioned on task type, authorization, tool availability, and side-effect risk

## `coordinator-orchestrator`

- Reviewed repository identities: `YTT-CSH/coordinator-orchestrator`, `MandyDragon/coordinator-orchestrator`
- Shared revision: `a6d0311d279b32497a9c952061fafb798309b4e3`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; both repository identities expose the same Git commit tree
- Purpose: research → synthesis → implementation → verification coordination with Continue-vs-Spawn guidance
- Revalidated strengths: synthesis remains with the coordinator; fresh verification agents reduce anchoring
- Revalidated risks: "independent tasks always parallel" ignores shared rate limits, files, databases, credentials, and external systems
- Verdict: useful orchestration model if concurrency decisions are based on resource and side-effect boundaries

## `worker-prompt-craft`

- Reviewed repository identity: `k1w1f1sh/worker-prompt-craft`
- Revision: `8f8a14fc8da0e687457516da3d9f79f8873e9061`
- Existing canonical deep review: Batch 030
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: self-contained prompts for workers/sub-agents
- Revalidated strengths: exact paths, completion criteria, purpose statements, and verification requirements reduce context loss
- Revalidated risks: examples normalize commit/push/PR/reviewer side effects without an explicit authority gate
- Verdict: high-value delegation-contract guidance once external side effects are separated from ordinary completion criteria

## `self-rationalization-guard`

- Reviewed repository identity: `k1w1f1sh/self-rationalization-guard`
- Revision: `3df614e3ae87d80b3be338d247a2fc2488dc22a2`
- Existing canonical deep review: Batch 031
- Structure: root `README.md` + root `SKILL.md`; no surfaced scripts/references/evals/package manifest
- Purpose: detect execution, communication, quality, and delegation shortcuts and force counter-actions
- Revalidated strengths: combats handwaving and distinguishes code reading from execution evidence
- Revalidated risks: universal inversion rules such as always running commands, always doing the hardest item first, handling every unlikely edge case, and always writing docs now can conflict with authorization, risk, and expected value
- Verdict: useful anti-rationalization checklist after adding risk/authority/value gates

## `background-memory-extractor` — new canonical report

- Reviewed repository identity: `ajunlonglive/background-memory-extractor`
- Repository ID: `1198087351`
- Stars observed: `0`
- Revision: `e1fc9103f5714eca3b203d13bbc1ce1130a7e892`
- Structure: root `README.md` + root `SKILL.md`; repository search surfaced no scripts, references, evals, package manifest, tests, or lifecycle-hook implementation
- Content class: document-only single skill
- Runtime/build/test/eval execution: `not_executed`

### Purpose

The skill proposes automatic extraction of durable memory at the end of every conversation turn. It defines duplicate suppression, a two-step read-then-write workflow, four memory types (`user`, `feedback`, `project`, `reference`), and a permission model intended to confine writes to memory artifacts.

### Mechanism

1. After a final response, check whether memory was already written in the current turn.
2. If not, review the turn for user preferences/role facts, feedback, project decisions, or external references.
3. Read `MEMORY.md` and relevant records before writing.
4. Update or create memory records and the index, with a stated preference for parallel writes.
5. Avoid project-code mutation and external API calls during extraction.

### Strengths

- Moves memory capture away from a single explicit phrase such as "remember this".
- Includes deduplication and stale-record update behavior rather than append-only accumulation.
- Reuses typed memory categories, improving consistency with memory routing/retrieval systems.
- Attempts to separate memory writes from project-code mutation.

### High-impact risks

1. **No actual after-turn trigger exists in the repository.** The core promise depends on a host lifecycle hook after the assistant's final response. A Markdown skill cannot guarantee this itself, and no daemon, hook, package, integration, or executable implementation is present. The repository therefore documents desired behavior but does not implement the claimed background mechanism.
2. **Parallel index/content writes are unsafe as a general rule.** Updating `MEMORY.md` concurrently with referenced memory files can expose dangling index entries, lose concurrent edits, or create inconsistent state. Safer designs write/validate content first, then update the index atomically or with compare-and-swap/version checks.
3. **The read permission is over-broad.** "Read any file" permits a retention process to inspect secrets or irrelevant sensitive material. Memory extraction should use explicit allowed scopes and data minimization.
4. **Automatic retention lacks an authority/privacy gate.** Running after every turn can retain data the user did not intend to persist. The document has no consent class, confidence threshold, retention period, sensitive-data exclusion policy, or deletion/override contract.
5. **Skip-on-any-existing-memory-write is lossy.** One memory written earlier in the turn does not prove that every other durable fact has been captured.
6. **No evaluation exists.** There are no precision/recall fixtures, duplicate-rate checks, stale-update tests, privacy false-positive tests, or consistency tests for concurrent writes.

### Provenance

README and `SKILL.md` say the design is inspired by reverse-engineered Claude Code `extractMemories` behavior and instruct installation from `Arxchibobo/background-memory-extractor`, while the indexed repository identity is `ajunlonglive/background-memory-extractor`. This is self-declared provenance and does not independently prove equivalence to Claude Code or to the stated upstream repository.

### Verdict

Useful as a **memory-policy concept**, not as a verified background-memory implementation. To become production-grade it needs a real lifecycle integration, explicit user/tenant memory policy, scoped reads, transactional or versioned writes, and measurable extraction/privacy evaluations.

## Deduplication record

Eight unique skill-content trees were re-read. Seven were already represented by canonical reports and therefore add no duplicate canonical entries. `background-memory-extractor` adds **1** new canonical individual-skill report. Batch 033 adds **10** repository identities to structure-reviewed repository coverage and raises the canonical skill-report total by **1**.
