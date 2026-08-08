# Agent Skills Deep Analysis — Batch 044

- Batch ID: `2026-08-08-batch-044`
- Completed qualified repository identities: **10**
- Direct README reads: **10**
- Direct `SKILL.md` reads: **16**
- Direct unique Skill bodies reviewed: **12**
- Unique Git content trees: **6**
- New canonical Skill reports: **2**
- Existing canonical bodies directly reverified/mapped: **10**
- Runtime/build/test/eval execution: **not_executed**

## Executive result

This batch resumed the deterministic April 8 queue and did not promote metadata-only candidates. Six `agentskills` hits were content-gated and reclassified as Agent Skills specification/reference-SDK copies rather than catalog Skill collections. The batch then continued until ten genuinely qualified repository identities had been verified by GitHub identity, observed Stars, pinned revision, README/repository structure and actual Skill content.

The ten completed identities collapse to six unique Git trees. Four Wondel forks share one exact tree, and two Anthropic-Cybersecurity-Skills forks share another exact tree. Repeated repository identities were still directly reread at the README/Skill level before coverage was counted; duplicate trees did not create duplicate canonical Skill reports.

Only two new canonical Skill reports were added in this batch: `chainlink-cre-skill` and `chainlink-ccip-skill`. Dreamina, the four Fernandez/Omaclaren skills, Wondel `clean-architecture`, Zephyr `devicetree`, and the sampled Cybersecurity body map to bodies already represented in earlier catalog analysis.

## Completed repositories

| Repository | Stars observed | Pinned revision | Git tree | Content gate / canonical action |
|---|---:|---|---|---|
| `JimmyZhangJW/dreamina-cli-skill` | 0 | `75e0a69a99f21a9c706045a0f6227b1b0804f886` | `dcd5dd83daec1b0786f92740876c949310bba95c` | README, root `SKILL.md`, Python wrapper and integration reference read; maps to prior Dreamina canonical body |
| `fernandezbaptiste/agent-skills-public` | 0 | `61e547e86d2c424f2ab6e54a4741948d37459665` | `0aa6ed76981d9daa8db35704c9edc47defe13d81` | README and all four Skill bodies read; existing canonical bodies reverified |
| `gregvanhorn/skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + `clean-architecture/SKILL.md` read; Wondel lineage mapping |
| `navneet10sep/skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + same representative Skill body directly read; exact tree duplicate |
| `yamisoto/skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + same representative Skill body directly read; exact tree duplicate |
| `leviathannexusprime-bot/skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + same representative Skill body directly read; exact tree duplicate |
| `chethanuk/chainlink-agent-skills` | 0 | `8d6f777a3e3c4a28449f98dbbfb29e108cd75ff5` | `5dcf050c2a97c7f57b7355c68426531145609be5` | README, both shipped Skill bodies, official-source reference, Promptfoo eval surface and rubric read; **2 new reports** |
| `bunjunwang/zephyr-agent-skills` | 0 | `ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce` | `60d5d8ad4dd3785d80eaca96f2587e3a755b4eba` | README, umbrella/index/devicetree Skill bodies, repository validator, devicetree helper and overlay reference read; maps to prior Zephyr canonical bodies |
| `rwe137/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README and one defensive API-log Skill body directly read; maps to Batch 043 lineage |
| `chillux/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README and same representative body directly reread; exact tree duplicate |

## Repository findings

### `JimmyZhangJW/dreamina-cli-skill`

This is a real operational Skill rather than a prompt-only package. The root Skill routes broad requests through capability discovery, recommends `--dry-run` for ambiguous/expensive operations, and uses `submit_id` for follow-up instead of blindly re-submitting jobs. The Python wrapper implements typed command specifications, local-path validation, enum/range constraints, JSON normalization and explicit CLI-error handling. `references/integration.md` makes the intended layering explicit: `SKILL.md` for policy, `scripts/` for deterministic execution, and `references/` for runtime integration.

The main limitation is verification depth: this review found a real deterministic wrapper but did not execute it, and no repository-local behavioral eval suite was used in this batch. Dry-run is valuable for command construction but cannot prove the downstream Dreamina service behavior.

### `fernandezbaptiste/agent-skills-public`

The repository contains four small, manually invoked skills: `guide-mode`, `critique-skill`, `annotated-reply-skill`, and `preview-browser-skill`. Their strongest reusable idea is explicit interaction-mode control: `guide-mode` requires sign-off before mutations/commits/long jobs, while `critique-skill` explicitly treats reviewed content as data rather than instructions.

Two bodies also demonstrate why side-effect policy cannot remain implicit. `annotated-reply-skill` writes to the OS clipboard, and `preview-browser-skill` writes temporary files and opens a browser/process. Those effects are operational even though the repository has no separate scripts. The collection has clear prose contracts but no repository-local eval harness establishing that the sign-off rules are consistently followed by a host agent.

### Wondel fork group — four identities, one exact tree

`gregvanhorn/skills`, `navneet10sep/skills`, `yamisoto/skills`, and `leviathannexusprime-bot/skills` all resolve to commit `4d322538...` / tree `32d2d4cb...`. Each identity was independently checked and its README plus representative `clean-architecture/SKILL.md` was directly read before repository coverage was counted.

The representative Skill has good progressive reference routing and a clear Dependency Rule / boundary model. Its mandatory `0-10` architecture score is a heuristic without local calibration/evals, so the numeric precision should not be interpreted as measured quality. The commit describes a 41-Skill audit, but this batch does not convert that inventory into 41 body-level completions.

### `chethanuk/chainlink-agent-skills`

This is the most important new content in Batch 044. The pinned fork ships two real Agent Skills.

`chainlink-cre-skill` uses an explicit information-source policy: start from local reference descriptions, write/scaffold first, fetch only a precisely named gap, prefer version-local CLI help for commands, and fall back through WebFetch/curl only when needed. This is a strong pattern for avoiding speculative browsing while still handling fast-changing SDK/runtime facts. Its weakness is that correctness still depends on external live documentation and host tool behavior; those dependencies are not made deterministic by the Skill itself.

`chainlink-ccip-skill` has an unusually explicit external-effect contract. Read-only discovery is allowed, on-chain writes require a preflight approval, high-impact testnet actions require a second confirmation, and all mainnet writes are refused in the reviewed version. `references/official-sources.md` separates conceptual documentation, tools, live route/token inventory, and explorer/message-state sources instead of treating one site as universally authoritative.

The repository also contains a real Promptfoo evaluation surface for CCIP: cases, prompts, rubrics, config, feedback log and a maintainer rubric. The rubric has must-pass conditions for mainnet writes, approval skipping, routing errors and live-source fabrication. These are stronger than documentation-only self-claims. However, **the eval suite was inspected, not executed**, so no pass rate is recorded here.

### `bunjunwang/zephyr-agent-skills`

This Zephyr fork has a concrete registry architecture: generated `index.json`, per-Skill `skill-meta.yaml`, a deterministic `zephyr-cli skills suggest` routing model, generated marketplace data and a repository validator. The validator actually checks frontmatter, required sections, local links, cross-Skill deep links, catalog/marketplace/index consistency and matcher metadata.

The `devicetree` Skill correctly separates its validation levels: a lightweight helper is only a sanity check, while real acceptance requires `west build`, inspection of resolved `zephyr.dts` / generated macros, and eventually target behavior. The helper itself only checks simple text/bracing/status patterns; its printed “passed” message must not be confused with a valid Zephyr build. No scripts were executed in this review.

### Cybersecurity fork pair — one exact tree

`rwe137/Anthropic-Cybersecurity-Skills` and `chillux/Anthropic-Cybersecurity-Skills` both resolve to commit `4ae0be7...` / tree `5dd2ce82...`, the v1.2.0 754-Skill lineage already encountered in Batch 043. Both identities were directly reread rather than completed from fork metadata.

The representative defensive body, `analyzing-api-gateway-access-logs`, is concise and authorization-aware, but the example anomaly thresholds (`>50` distinct IDs, `>100` 401s) are hard-coded heuristics without a local fixture/eval demonstrating their operating characteristics. The 754-item README inventory therefore remains an inventory; it is not treated as 754 body-level deep analyses or 754 behaviorally validated Skills.

## Reclassified index hits — not completed

The following April 8 index candidates were inspected and **not** counted toward the ten completed repositories:

- `edulazaro/agentskills` — root content and README state that the repository contains the Agent Skills specification, documentation and reference SDK.
- `CAgGen/agentskills` — same specification/reference-SDK content and exact README blob lineage.
- `kwakminoo/agentskills` — specification/documentation/reference SDK, not a local Skill collection.
- `jgf-dev/agentskills` — actual root tree matches the specification repository layout/content.
- `michaelsam94/agentskills` — actual root tree matches the specification repository layout/content.
- `JasonZhuGit/agentskills` — actual root tree matches the specification repository layout/content.

`AI-Engineering-at/meta-skills-plugin` and `fernandezbaptiste/skillcraft` remain tooling-class entries and were not promoted as Skill repositories. `dgallitelli/aws-data-agent-skill-strands-agentcore` was skipped at its April 8 queue position because it was already fully completed in Batch 043. Adjacent `project-architect`/other search hits remain excluded by classification.

## Verification boundary

Verified in this batch: GitHub repository identity, Stars observed at review time, pinned commit/tree, root structure, README content, directly read Skill bodies, selected scripts/references/eval definitions, and exact-tree duplicate relationships.

Not verified by execution: runtime behavior, builds, tests, Promptfoo results, external APIs, Dreamina generation behavior, Zephyr compilation/hardware behavior, or on-chain Chainlink operations. No repository is marked runtime-validated from prose, metadata, CI claims, or unexecuted eval definitions.

## Progress

- Structure-reviewed repositories: **440**
- Repository-scoped Skill reports: **2913**
- Frozen canonical eligible basis: **2088**
- Arithmetic remaining estimate: **1648**
- Canonical cross-repository reconciliation: **pending**

The `1648` value remains `2088 - 440`; it is not a reconciled count of unique repositories remaining.

## Queue resumption

Next unresolved qualified identity after this batch: `aminrj/Anthropic-Cybersecurity-Skills`.
