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

## April 2026 partition — in progress

Verified persisted coverage:

```text
2026-04-01 .. 2026-04-29
per_page=100
29 exact single-day shards with terminal pagination probes
```

The `2026-04-29` shard returned `26` repositories on page 1 and `0` on page 2. Independent rechecks returned `20,6,0` with `per_page=20` and `26,0` with `per_page=33`. Case-insensitive `owner/repository` deduplication produced `26` unique identities and `0` internal duplicates.

April staging now contains `1243` unique identities across `2026-04-01` through `2026-04-29`, with `0` cross-shard duplicates asserted under the established connector-search partition contract.

### April provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 13 |
| `skill_collection` | 713 |
| `single_skill_or_domain_package` | 406 |
| `awesome_index` | 1 |
| `skill_tooling` | 26 |
| `adjacent_search_hit` | 83 |
| `unclear_search_hit` | 1 |
| **Total** | **1243** |

Classification remains repository-identity/name plus repository-metadata-only and provisional. Metadata descriptions/fork metadata were used only where the name was ambiguous; no target repository content was inspected. In the latest shard, `elagizi/agentskills`, `SabrinaLameiras/agentskills`, `chase-qi/agentskills`, `devzzk/agentskills`, and `gsdv/agentskills` are forks of `agentskills/agentskills` whose repository description is “Specification and documentation for Agent Skills”; `zunhuang/googleAgentskills` is a fork of `google/skills`; `CD22333/zephyr-agent-skills` describes a complete Zephyr RTOS Agent Skills catalog; `mi-24v/agent-skills` describes coding agent skills in the AgentSkills format; and `wky114/AnythingButLaw` describes a domain-focused Claude Code AgentSkill package.

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

Current run report: [`runs/2026-08-09-agentskills-april-2026-04-29.md`](runs/2026-08-09-agentskills-april-2026-04-29.md).

## Evidence boundary

Index collection only. No target repository README, `SKILL.md`, scripts, references, evaluations, implementation code, or runtime behavior was inspected, and no repository was marked complete from metadata. Repository metadata such as descriptions/fork relationships was used only for index-stage classification of ambiguous names.

## Next index action

Continue with the `2026-04-30` exact single-day shard and keep canonical totals frozen until reconciliation is complete.
