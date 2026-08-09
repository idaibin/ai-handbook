# GitHub Agent Skills Repository Index

## Current verified catalog

- Canonical unique repositories: `2502`
- Provisionally eligible for later deep analysis: `2088`
- Held for review: `414`
- Canonical delta asserted in this index phase: `0`

Canonical totals remain frozen while created-date partitions are reconciled with historical staging. Machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## Completed partitions

| Partition | Verified unique | Status |
| --- | ---: | --- |
| `2026-01` | 368 | complete |
| `2026-02` | 402 | deterministic reconciliation complete |
| `2026-03` | 831 | 31 daily shards complete; historical reconciliation pending |
| `2026-04` | 1272 | 30 daily shards complete; historical reconciliation pending |

## April 2026 partition — daily staging complete

Verified persisted coverage:

```text
2026-04-01 .. 2026-04-30
per_page=100
30 exact single-day shards with terminal pagination probes
```

The `2026-04-30` shard returned `29` repositories on page 1 and `0` on page 2. Independent rechecks returned `20,9,0` with `per_page=20` and `29,0` with `per_page=33`. Case-insensitive `owner/repository` deduplication produced `29` unique identities and `0` internal duplicates.

April staging now contains `1272` unique identities across `2026-04-01` through `2026-04-30`, with `0` cross-shard duplicates asserted under the established connector-search partition contract.

### April provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 24 |
| `skill_collection` | 720 |
| `single_skill_or_domain_package` | 411 |
| `awesome_index` | 1 |
| `skill_tooling` | 29 |
| `adjacent_search_hit` | 85 |
| `unclear_search_hit` | 2 |
| **Total** | **1272** |

Classification remains repository-identity/name plus repository-metadata-only and provisional. Metadata descriptions/fork metadata were used only where the name was ambiguous; no target repository content was inspected. In the latest shard, several generic `agentskills` repositories are forks of `agentskills/agentskills` and are therefore classified as `specification`; `Jethro7723/agentskills` is a fork of `obra/superpowers` whose metadata describes an agentic skills framework/software-development methodology; `codingr47/agentskills-framework-poc` describes a Rust AgentSkills framework implementation; `anatolykoptev/skillkit` describes a reference Go implementation of the agentskills.io standard; `Watermelon4000/typewriter-video` and `Nixer-2301/webpage-skill` describe single AgentSkill-compatible packages; `Nifflesvibe001/skills` is a fork of the Wondel.ai multi-skill collection; `wenni2005-ai/openclaw-skills` describes custom OpenClaw AgentSkills; `suhas-24/ai-engineering-2026` is an AI-engineering curriculum that mentions Agent Skills among many topics; and `dimayip/learn-agent-skills` is a learning workshop about the Agent Skills specification. `HenriqueGomesHub/agentskills` remains `unclear_search_hit` because repository metadata only says it is testing skill creation.

### April artifacts

- [`batches/agentskills-created-2026-04-01-deterministic.json`](batches/agentskills-created-2026-04-01-deterministic.json)
- [`batches/agentskills-created-2026-04-02-deterministic.json`](batches/agentskills-created-2026-04-02-deterministic.json)
- [`batches/agentskills-created-2026-04-03-deterministic.json`](batches/agentskills-created-2026-04-03-deterministic.json)
- [`batches/agentskills-created-2026-04-04-deterministic.json`](batches/agentskills-created-2026-04-04-deterministic.json)
- [`batches/agentskills-created-2026-04-05-deterministic.json`](batches/agentskills-created-2026-04-05-deterministic.json)
- [`batches/agentskills-created-2026-04-06-deterministic.json`](batches/agentskills-created-2026-04-06-deterministic.json)
- [`batches/agentskills-created-2026-04-07-deterministic.json`](batches/agentskills-created-2026-04-07-deterministic.json)
- [`batches/agentskills-created-2026-04-08-deterministic.json`](batches/agentskills-created-2026-04-08-deterministic.json)
- [`batches/agentskills-created-2026-04-09-deterministic.json`](batches/agentskills-created-2026-04-09-deterministic.json)
- [`batches/agentskills-created-2026-04-10-deterministic.json`](batches/agentskills-created-2026-04-10-deterministic.json)
- [`batches/agentskills-created-2026-04-11-deterministic.json`](batches/agentskills-created-2026-04-11-deterministic.json)
- [`batches/agentskills-created-2026-04-12-deterministic.json`](batches/agentskills-created-2026-04-12-deterministic.json)
- [`batches/agentskills-created-2026-04-13-deterministic.json`](batches/agentskills-created-2026-04-13-deterministic.json)
- [`batches/agentskills-created-2026-04-14-deterministic.json`](batches/agentskills-created-2026-04-14-deterministic.json)
- [`batches/agentskills-created-2026-04-15-deterministic.json`](batches/agentskills-created-2026-04-15-deterministic.json)
- [`batches/agentskills-created-2026-04-16-deterministic.json`](batches/agentskills-created-2026-04-16-deterministic.json)
- [`batches/agentskills-created-2026-04-17-deterministic.json`](batches/agentskills-created-2026-04-17-deterministic.json)
- [`batches/agentskills-created-2026-04-18-deterministic.json`](batches/agentskills-created-2026-04-18-deterministic.json)
- [`batches/agentskills-created-2026-04-19-deterministic.json`](batches/agentskills-created-2026-04-19-deterministic.json)
- [`batches/agentskills-created-2026-04-20-deterministic.json`](batches/agentskills-created-2026-04-20-deterministic.json)
- [`batches/agentskills-created-2026-04-21-deterministic.json`](batches/agentskills-created-2026-04-21-deterministic.json)
- [`batches/agentskills-created-2026-04-22-deterministic.json`](batches/agentskills-created-2026-04-22-deterministic.json)
- [`batches/agentskills-created-2026-04-23-deterministic.json`](batches/agentskills-created-2026-04-23-deterministic.json)
- [`batches/agentskills-created-2026-04-24-deterministic.json`](batches/agentskills-created-2026-04-24-deterministic.json)
- [`batches/agentskills-created-2026-04-25-deterministic.json`](batches/agentskills-created-2026-04-25-deterministic.json)
- [`batches/agentskills-created-2026-04-26-deterministic.json`](batches/agentskills-created-2026-04-26-deterministic.json)
- [`batches/agentskills-created-2026-04-27-deterministic.json`](batches/agentskills-created-2026-04-27-deterministic.json)
- [`batches/agentskills-created-2026-04-28-deterministic.json`](batches/agentskills-created-2026-04-28-deterministic.json)
- [`batches/agentskills-created-2026-04-29-deterministic.json`](batches/agentskills-created-2026-04-29-deterministic.json)
- [`batches/agentskills-created-2026-04-30-deterministic.json`](batches/agentskills-created-2026-04-30-deterministic.json)

Current run report: [`runs/2026-08-09-agentskills-april-2026-04-30.md`](runs/2026-08-09-agentskills-april-2026-04-30.md).

## Evidence boundary

Index collection only. No target repository README, `SKILL.md`, scripts, references, evaluations, implementation code, or runtime behavior was inspected, and no repository was marked complete from metadata. Repository metadata such as descriptions/fork relationships was used only for index-stage classification of ambiguous names.

## Next index action

Begin the deterministic May partition with the `2026-05-01` exact single-day shard. Keep canonical totals frozen until historical reconciliation is complete.
