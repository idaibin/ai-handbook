# Agent Skills Deep Analysis — Batch 047

- Observed: 2026-08-09
- Scope: existing deterministic indexed queue
- Completion rule: repository identity + observed Stars + pinned revision + actual repository content reads. Metadata-only completion is prohibited.
- Runtime/build/test/eval execution: not executed
- Canonical reconciliation: pending

## Result

| Metric | Value |
|---|---:|
| Qualified repositories completed | 10 |
| README direct reads | 10 |
| `SKILL.md` direct reads | 41 |
| Direct unique skill bodies reviewed | 38 |
| Unique Git content trees | 7 |
| New repository-scoped skill reports | 36 |
| Cumulative structure-reviewed repositories | 470 |
| Cumulative repository-scoped skill reports | 2965 |
| Frozen eligible basis | 2088 |
| Arithmetic remaining estimate | 1618 |

The ten repository identities below were not marked complete until their repository content had been read at a pinned Git revision. Exact-tree mirrors were re-read per repository identity, then deduplicated at the content/report layer.

## Completed repositories

| Repository | Stars | Pinned revision | Git tree | Direct content gate | Disposition |
|---|---:|---|---|---|---|
| `hanul93/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + `analyzing-kubernetes-audit-logs/SKILL.md` + recursive tree | Existing Cybersecurity canonical content |
| `mr-r0w07/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + same representative defensive Skill | Existing exact-tree content |
| `me-pankajmunde/AgentSkills` | 0 | `acc11be629ffd58aa72ebb921cead21e265ee59b` | `5558cffc4e02edcbe2dd7416942f69bfae8b76dc` | WiKi README + all 3 Skill bodies + `wiki.py` + tree | 3 new repository-scoped reports |
| `profbernardoj/morpheus-skill` | 19 | `40580ea1d0882b6c4d56502f37c6f3d90a45c456` | `e8d90d3e168622578ab50f46b27f79d16d5d1a53` | README + root Skill + `cron-packs/SKILL.md` + CI workflow + tree | 2 new repository-scoped reports |
| `essentialsoft/agentskills` | 0 | `fd2d437db59e140d88bba84a8fe04a29d566a17b` | `582ae52a4e46d10d22446f3b3cc259a05e9b82dd` | README + all 21 Skill bodies + `skill-test/SYSTEM_DESIGN.md` + tree | 21 new repository-scoped reports |
| `shucenliu333-eng/investment-analysis-skills` | 1 | `946ea534124e478a8c677728ac6a267776bf4a0a` | `c3e1de8fc855078f6c0609fab44fb6a9ec6ca268` | README + all 9 Skill bodies + recursive tree | 9 new repository-scoped reports |
| `zacmoltbot/openclaw-skill-long-task-control` | 0 | `d744ff2f3e22ae140c63657ae654b3a7267936a2` | `6b9e979a8c8125de5c85d91b1da91d2ed604e1af` | README + Skill + ledger implementation + representative E2E regression + tree | 1 new repository-scoped report |
| `manhtx/skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + `clean-architecture/SKILL.md` | Existing Wondel exact-tree content |
| `adooylabs/skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + `clean-architecture/SKILL.md` | Existing Wondel exact-tree content |
| `KziGeez/claude-skills` | 1 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + `clean-architecture/SKILL.md` | Existing Wondel exact-tree content |

## Verified findings

### 1. `essentialsoft/agentskills` contains a real multi-layer Skill evaluation system

This fork is materially different from a simple Skill-document collection. All 21 Skill bodies were directly read. The `skill-test` area also contains an explicit system design plus executor, JSON post-processing, deterministic validators, LLM-as-judge prompt/rubric support, report generation, and persisted evaluation artifacts. That architecture is useful because it separates deterministic checks from semantic judging and preserves evidence instead of treating an LLM answer as the only verdict.

The important validation boundary is unchanged: the existence of these scripts and tests is verified, but none were executed in this batch. No pass rate or behavioral success is claimed.

A second finding is policy fragmentation. Skills such as `git-commit`, `git-commit-push`, `implementation-executor`, crawling, and other operational workflows each encode their own assumptions about side effects. A catalog-level authorization contract would be safer and more consistent than allowing every Skill to invent its own commit/push/execute policy.

### 2. `zacmoltbot/openclaw-skill-long-task-control` has one of the stronger execution-truth designs in this queue segment

The Skill separates observed truth, deterministic derived state, and control actions. The repository contains a durable ledger implementation plus a large set of E2E/regression scripts around partial success, artifact delivery, terminal cleanup, retry/block convergence, and state recovery. The directly read regression source verifies that inconsistent completion claims are expected to converge to a non-success control state rather than silently becoming success.

This is stronger evidence than prose-only claims, but the regression files were only inspected, not run. Runtime behavior therefore remains unverified in this batch.

### 3. `profbernardoj/morpheus-skill` is operational infrastructure, not merely an instruction document

The pinned repository contains a large root Skill, a separate `cron-packs` Skill, setup/service scripts, container configuration, CI, wallet/proxy tests, secret scanning, and deployment-oriented assets. The root Skill is capable of changing local configuration and starting/restarting services, and it depends on credentials and external inference/blockchain/network services. Its own documentation includes dry-run/review guidance, which is a useful pattern, but the breadth of system/network side effects means authorization should remain explicit and narrowly scoped.

The CI workflow defines syntax checks, wallet tests, proxy tests, secret scanning, and a Docker smoke path. Those definitions were read; the CI or tests were not executed by this run.

### 4. `me-pankajmunde/AgentSkills` mixes useful executable retrieval tooling with permissive integration guidance

`WiKi_Skills` is a real retrieval stack rather than a prompt-only Skill: the tree contains Wikipedia ingestion/retrieval code, Qdrant/vector storage, BM25 retrieval, fusion, templates, and helper modules. The Skill can be useful as a concrete RAG reference, but it has substantial dependency/environment assumptions and no repository-local behavioral retrieval benchmark was found at the pinned revision.

The Copilot SDK Skill includes broad authorization examples. The reusable lesson is not to copy those permissions literally: integrations should use least privilege and explicit approval boundaries. The Google ADK Skill is mainly implementation/template guidance.

### 5. `shucenliu333-eng/investment-analysis-skills` is a coherent reference-driven research collection, but not an executable verification system

All 9 Skill bodies were directly read: valuation, competitive landscape, due diligence, financial analysis, forecasting, statement forensics, macro environment, market sizing, and Porter five forces. The repository has substantial per-Skill reference material, but no repository-local executable calculation harness or behavioral eval suite was observed in the pinned tree.

For reuse, the strongest elements are decomposition and structured methodology. The main missing contract is provenance: source date, source identity, assumptions, calculation inputs, and uncertainty should be machine-recorded so an agent cannot present a prose framework as verified financial fact.

### 6. Exact Git trees remain the correct dedup boundary for Wondel and Cybersecurity mirrors

The two Cybersecurity identities independently passed their content gate but resolve to the already-reviewed `5dd2ce...` tree. Likewise `manhtx/skills`, `adooylabs/skills`, and `KziGeez/claude-skills` each had README and representative Skill content reread, then resolved to the already-reviewed Wondel tree `32d2d4...` at commit `4d322538...`.

They count as repository identities reviewed because their existence and content were independently verified. They do not create duplicate Skill reports simply because the GitHub owner/name differs.

## Reclassified / skipped queue entries

The following index-stage candidates were inspected and not counted toward the ten qualified completions:

| Repository | Result | Evidence |
|---|---|---|
| `ChanglongGuo/agentskills` | reclassified, not completed | README identifies Agent Skills specification/documentation/reference SDK lineage, not a local Skill collection |
| `mythkina/agentskills` | reclassified, not completed | README identifies specification/documentation/reference SDK lineage |
| `aonkhur007-byte/agentskills` | reclassified, not completed | repository metadata plus README identify a fork of the Agent Skills specification/docs repository |
| `Threeboys33/agentskills` | reclassified, not completed | README explicitly says the repo contains the specification, documentation, and reference SDK |
| `LOSGARDIOS/bundles` | skipped by existing index classification | `adjacent_search_hit` |
| `super9du/openclaw-skills-creator` | skipped by existing index classification | `skill_tooling` |

These entries were not substituted into the completion count. The scan continued until ten genuinely qualified repository identities had passed content review.

## Validation boundary

- Repository identity and Stars: verified through GitHub for each completed identity.
- Revisions/trees: pinned before content analysis.
- README / Skill content: directly read for every completed identity.
- Unique/new collections: every Skill body counted as a new report was directly read.
- Exact-tree mirrors: representative bodies were reread per identity and mapped to existing reports.
- References/scripts/evals: inspected when available and relevant to the unique tree.
- Runtime/build/tests/evals: **not executed**.
- Historical cross-repository canonical reconciliation: **pending**.

The `1618` remaining figure is only `2088 - 470` on the frozen eligible basis. It is not a reconciled unique-repository remainder.

## Queue resume

Next unresolved qualified identity: `ColonistOne/colony-skill`.
