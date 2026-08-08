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
2026-04-01 .. 2026-04-27
per_page=100
27 exact single-day shards with terminal pagination probes
```

The `2026-04-27` shard returned `31` repositories on page 1 and `0` on page 2. Independent rechecks returned `20,11,0` with `per_page=20` and `31,0` with `per_page=33`. Case-insensitive `owner/repository` deduplication produced `31` unique identities and `0` internal duplicates.

April staging now contains `1175` unique identities across `2026-04-01` through `2026-04-27`, with `0` cross-shard duplicates asserted under the established connector-search partition contract.

### April provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 688 |
| `single_skill_or_domain_package` | 378 |
| `awesome_index` | 1 |
| `skill_tooling` | 25 |
| `adjacent_search_hit` | 83 |
| `unclear_search_hit` | 0 |
| **Total** | **1175** |

Classification remains repository-identity/name plus repository-metadata-only and provisional. Metadata descriptions/topics were used only where the name was ambiguous; no target repository content was inspected.

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

Current run report: [`runs/2026-08-09-agentskills-april-2026-04-27.md`](runs/2026-08-09-agentskills-april-2026-04-27.md).

## Evidence boundary

Index collection only. No target repository README, `SKILL.md`, scripts, references, evaluations, implementation code, or runtime behavior was inspected, and no repository was marked complete from metadata. Repository metadata such as descriptions/topics was used only for index-stage classification of ambiguous names.

## Next index action

Continue with the `2026-04-28` exact single-day shard and keep canonical totals frozen until reconciliation is complete.
