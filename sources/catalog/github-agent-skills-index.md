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
2026-04-01 .. 2026-04-20
per_page=100
20 exact single-day shards with terminal pagination probes
```

The `2026-04-20` shard returned `100` repositories on page 1, `32` on page 2, and `0` on page 3. Independent rechecks returned `20,20,20,20,20,20,12,0` with `per_page=20` and `33,33,33,33,0` with `per_page=33`. Case-insensitive `owner/repository` deduplication produced `132` unique identities and `0` internal duplicates.

April staging now contains `903` unique identities across `2026-04-01` through `2026-04-20`, with `0` cross-shard duplicates asserted under the established connector-search partition contract.

### April provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 490 |
| `single_skill_or_domain_package` | 320 |
| `awesome_index` | 1 |
| `skill_tooling` | 16 |
| `adjacent_search_hit` | 76 |
| `unclear_search_hit` | 0 |
| **Total** | **903** |

Classification remains identity/name-metadata-only and provisional. No target repository content was used to promote classifications.

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

Current run report: [`runs/2026-08-09-agentskills-april-2026-04-20.md`](runs/2026-08-09-agentskills-april-2026-04-20.md).

## Evidence boundary

Index collection only. No target repository README, `SKILL.md`, scripts, references, evaluations, stars, implementation code, or runtime behavior was inspected, and no repository was marked complete from metadata.

## Next index action

Continue with the `2026-04-21` exact single-day shard and keep canonical totals frozen until reconciliation is complete.
