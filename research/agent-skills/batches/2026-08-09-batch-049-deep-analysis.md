# GitHub Agent Skills Deep Analysis — Batch 049

- observed_at: `2026-08-09`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- selection_policy: continue the existing deterministic indexed queue; complete the next 10 genuinely qualified repository identities, reclassifying metadata-stage false positives instead of counting them.
- qualification rule: repository identity + current Stars + pinned revision + actual repository content must be read before completion.

## Batch result

| Metric | Value |
| --- | ---: |
| Qualified repositories completed | 10 |
| README direct reads | 10 |
| `SKILL.md` direct reads | 49 |
| Unique Skill bodies directly reviewed | 46 |
| Unique Git content trees | 7 |
| New repository-scoped individual Skill reports | 45 |
| Cumulative repositories structure-reviewed | 490 |
| Cumulative repository-scoped Skill reports | 3017 |
| Frozen eligible basis | 2088 |
| Arithmetic remaining estimate | 1598 |
| Runtime/build/test/eval execution | not executed |

## Completed repositories

| # | Repository | Stars observed | Pinned revision | Content action |
| ---: | --- | ---: | --- | --- |
| 1 | `ballbadboy/agentskills` | 0 | `82ceff41ed4d3c644e3dcca8a0514390b2911223` | new tree; README, all 21 Skill bodies, references, hook scripts/tests and install CI inspected |
| 2 | `yhughk/adversarial-verification` | 0 | `909a2f70fc0de13aff1175c0b507ec24bf0b4815` | new tree; README + root Skill inspected |
| 3 | `benjaminyanjd/life-algorithm-skill` | 0 | `d4db60bb56b876d16c5d35355ad58aa85ff146c7` | new tree; README + Skill + all three references inspected |
| 4 | `rogeriochaves/skills` | 0 | `49b5fdb2d8e8ab4b7c1cf5e926101628c0b0f728` | new tree; README + all 6 Skills + `pr-watch.sh` inspected |
| 5 | `zarkob/wondelai-skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | exact-tree mapping to already-reviewed Wondel snapshot; README + representative Skill re-read |
| 6 | `imkepler/hermes-wondelai-skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | exact-tree mapping; README + representative Skill directly read |
| 7 | `mikesmayer/claude-business-skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | exact-tree mapping; README + representative Skill directly read |
| 8 | `srinivasmd/skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | exact-tree mapping; README + representative Skill directly read |
| 9 | `lx-wnk/skills` | 1 | `b66badb0a1f42bbaab2bce01a80f52fc2c6df2da` | new tree; README + all 15 Skills + registry validator/CI + orchestration references inspected |
| 10 | `benjaminyanjd/laoyu-life-algorithm-skill` | 0 | `850214ae14e3ed4e1e323f0e2a1c55faa45a7e5a` | new tree; README + Skill + all three references inspected |

The four Wondel identities resolve to the same pinned content tree already reviewed in an earlier batch, so they increase repository-identity coverage but do not create duplicate Skill reports.

## Queue corrections before/between qualified entries

Five index-stage `skill_collection` labels were rejected after reading real repository content:

- `rickyly/agentskills` — fork of the Agent Skills specification/reference SDK; README describes the open format, docs and reference SDK rather than a local Skill collection.
- `samarameneses/agentskills` — same specification/reference-SDK lineage and exact content snapshot.
- `huqianghui/agentskills` — same specification/reference-SDK lineage and exact content snapshot.
- `s1r-h4x5/agentskills` — same specification/reference-SDK lineage and exact content snapshot.
- `q-qp-p/agentskills` — fork of the format/specification repository; current README presents the Agent Skills standard rather than a qualifying local Skill pack.

Existing index classifications `adjacent_search_hit` / `awesome_index` were also skipped rather than upgraded solely to fill the batch. No rejected item was counted toward the 10 completed repositories.

## Repository analyses

### 1. `ballbadboy/agentskills`

**Verified.** The pinned repository contains 21 actual `SKILL.md` bodies: 20 engineering workflow/domain Skills plus the `using-agent-skills` meta-skill. It also contains Claude plugin manifests, seven command wrappers, three specialized agent prompts, four root references, an `idea-refine` script/reference set, session/simplification hooks, a 10-case shell regression script for the simplification hook, and a GitHub Actions plugin-install workflow.

**Assessment.** This is a coherent process-first engineering system rather than a loose prompt dump. Strong ideas include explicit skill routing, assumptions/scope discipline, source-driven version verification, RED→GREEN testing, browser-content trust boundaries, security checklists, and a living-spec workflow. The repository itself also has real deterministic code around hook filtering and plugin installation.

**Risks / gaps.** The repository does not contain a behavioral eval harness that proves its 21 Skills trigger or behave correctly. The install workflow validates plugin packaging/installability, while `simplify-ignore-test.sh` tests one hook implementation; neither is an end-to-end Skill-quality benchmark. Several Skills contain operational actions that need higher-level authorization guards: destructive reset/cleanup examples, pushing/releasing, and browser/external side effects. `idea-refine` references a host-specific absolute path in its invocation guidance, reducing portability. Several numerical targets are useful defaults but are guidance, not repository-measured universal thresholds.

**Not verified.** CI status, hook tests, plugin installation, browser workflows and any external actions were not executed in this batch.

### 2. `yhughk/adversarial-verification`

**Verified.** The pinned tree contains only `README.md` and a root `SKILL.md`. The Skill requires real commands, verbatim output, negative/adversarial probes and a PASS/FAIL/PARTIAL verdict rather than accepting implementation prose as evidence.

**Assessment.** The evidence discipline is strong and directly applicable to coding-agent validation: observable claims require observable execution evidence, and negative probes are first-class rather than optional.

**Risks / gaps.** There is no repository-local script, fixture, test or eval. The guidance also says time cost should not decide whether verification is performed; without a bounded verification budget/terminal condition this can become excessive or non-terminating on large tasks. Shell/browser execution still needs an external authorization/sandbox policy.

### 3. `benjaminyanjd/life-algorithm-skill`

**Verified.** The repository contains one Skill plus `framework.md`, `quick-map.md` and `examples.md`. The Skill converts an abstract decision problem into constraints, a minimum model, one concrete action, a “do not do” boundary and evidence that would change the judgment.

**Assessment.** The most reusable idea is the decision-output contract: judgment first, explicit uncertainty, validation action and stop condition. That makes a conceptual framework more operational than a plain book summary.

**Risks / gaps.** Probability/decision formulas and examples are heuristic reasoning devices; the repository has no calibrated model, outcome dataset or behavioral eval demonstrating improved decision quality.

### 4. `rogeriochaves/skills`

**Verified.** Six Skills were directly read: `orchestrate`, `browser-qa`, `drive-pr`, `nexus-room`, `reuse-worktree`, and `review`. The repository also contains a substantial `drive-pr/scripts/pr-watch.sh` implementation with persistent local state, GitHub REST polling/caching and a built-in diff-test mode.

**Assessment.** The collection is operational: it binds review, browser QA, PR monitoring and worktree reuse to concrete commands and persistent evidence. `drive-pr` is especially useful as an example of separating a long-running GitHub observation loop from the Skill prose.

**Risks / gaps.** It is strongly environment-specific (`langwatch` repositories, `~/Projects/...`, Nexus deployment details). Several workflows have consequential side effects: public screenshot pushes, review posting, process killing, database seeding and `git reset --hard`. These require explicit authorization and dirty-state checks when generalized. The embedded script test path was inspected but not executed.

### 5–8. Wondel exact-tree identities

**Verified.** `zarkob/wondelai-skills`, `imkepler/hermes-wondelai-skills`, `mikesmayer/claude-business-skills`, and `srinivasmd/skills` all resolve to revision `4d322538be8b9ce98fca29b0eef26d67bff1fe82` and the same Wondel content snapshot. Each identity was content-gated with its README and the `clean-architecture` Skill body rather than accepted from metadata alone.

**Assessment.** The snapshot is a broad book/framework-derived methodology catalog; `clean-architecture` uses references and a consistent diagnostic/scoring structure. However, its “10/10” scoring is a rubric, not a measured quality score.

**Canonical action.** No duplicate individual Skill reports were created because the exact tree was already reviewed previously.

### 9. `lx-wnk/skills`

**Verified.** The pinned tree contains 15 Skills and a real Node registry/conformance validator. All 15 Skill bodies were directly read. `scripts/sync-registry.mjs` checks frontmatter/name/description constraints, directory↔name consistency, exact README inventory, and generated manifest drift; CI runs formatting plus `sync:check`. ATOM also has a dedicated runbook and peer-communication protocol.

**Assessment.** This repository has one of the stronger “Skill as maintained software artifact” designs in this queue segment: machine-readable registry, deterministic drift gate, review/read-only boundaries, explicit untrusted-diff handling, reproduce-first debugging, release-pinned remote bootstrap prompts, and explicit consent before trust-expanding Agent/plugin updates. The design/review split (architecture vs component vs branch/full-project) provides clear responsibility boundaries.

**Risks / gaps.** CI proves structural conformance/registry freshness, not behavioral correctness of the Skills. `obsidian` exposes create/update/append/delete operations over a local REST API without a per-write confirmation rule, so activation can imply too much authority. ATOM can fan out many workers/worktrees/PRs and therefore needs host-level resource and external-side-effect budgets. Several Skills depend on Claude-host-specific tools, so portability is not guaranteed even though the format is standard-compatible.

**Not verified.** `npm run sync:check`, CI, external Obsidian calls, remote bootstrap/update prompts, worktree orchestration and review fleets were not executed.

### 10. `benjaminyanjd/laoyu-life-algorithm-skill`

**Verified.** One `SKILL.md` plus three directly read references (`framework.md`, `nine-stages.md`, `eighteen-challenges.md`). The Skill explicitly limits itself to the decision layer and excludes narrow medical/legal/technical diagnosis.

**Assessment.** It uses progressive disclosure correctly: the main Skill is compact and references are loaded only when needed. The default output contract—conclusion, why, biggest risk, validation action, stop-loss line, brief framework mapping—is actionable and keeps theory subordinate to the decision.

**Risks / gaps.** The underlying book-derived categories are interpretive heuristics. No source bibliography, calibration corpus, decision-outcome benchmark or behavioral eval is present, so category mapping and probability language must remain framed as inference rather than validated prediction.

## Cross-batch findings

1. **Structural validation and behavioral validation remain distinct.** `ballbadboy/agentskills` and `lx-wnk/skills` both contain real validators/tests/CI, but those primarily prove packaging, hook behavior, formatting or registry consistency—not whether an LLM selects and follows each Skill correctly.
2. **Authorization should live above individual Skills.** PR posting/pushing, hard resets, browser actions, database seeding, Obsidian writes/deletes and remote plugin installation appear across unrelated Skills. A host-level side-effect policy is safer than trusting every Skill to define authorization consistently.
3. **Exact-tree deduplication is necessary but must follow content gating.** Four Wondel identities were independently read before being mapped to an already-reviewed canonical tree; metadata similarity alone was not used to complete them.
4. **A useful verification Skill needs a budget as well as rigor.** `adversarial-verification` has strong evidence requirements, but a bounded attempt/time/resource policy is needed to avoid turning “verify everything” into an optimization loop.
5. **Deterministic registries are valuable maintenance infrastructure.** `lx-wnk/skills` demonstrates a low-ambiguity pattern: source `SKILL.md` files → conformance validator → committed machine manifest → drift gate in CI.

## Validation boundary

This batch is **source/structure reviewed only**. Repository code, tests, CI, builds, browser workflows, external APIs and evals were not executed. Presence of a test file or CI workflow is recorded as implementation evidence, never as a passing result.

## Queue continuation

The next unresolved qualified repository after this batch boundary is `stjordanis/Anthropic-Cybersecurity-Skills`.

`1598` is only `2088 - 490` on the frozen eligible basis. Canonical reconciliation remains pending, so it is not a claim about the final number of unique remaining repositories.
