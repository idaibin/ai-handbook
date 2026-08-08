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
2026-04-01 .. 2026-04-05
per_page=100
5 exact single-day shards with terminal pagination probes
```

The `2026-04-05` shard returned `14` repositories on page 1 and `0` on page 2. Recheck with `per_page=20` returned `14,0`. Case-insensitive `owner/repository` deduplication produced `14` unique identities and `0` internal duplicates.

April staging now contains `206` unique identities across `2026-04-01` through `2026-04-05`, with `0` cross-shard duplicates asserted.

### April provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 76 |
| `single_skill_or_domain_package` | 107 |
| `awesome_index` | 0 |
| `skill_tooling` | 1 |
| `adjacent_search_hit` | 22 |
| `unclear_search_hit` | 0 |
| **Total** | **206** |

Classification remains metadata-only and provisional. Ambiguous hits are retained as adjacent rather than promoted by assumption.

### April artifacts

- [`batches/agentskills-created-2026-04-01-deterministic.json`](batches/agentskills-created-2026-04-01-deterministic.json)
- [`batches/agentskills-created-2026-04-02-deterministic.json`](batches/agentskills-created-2026-04-02-deterministic.json)
- [`batches/agentskills-created-2026-04-03-deterministic.json`](batches/agentskills-created-2026-04-03-deterministic.json)
- [`batches/agentskills-created-2026-04-04-deterministic.json`](batches/agentskills-created-2026-04-04-deterministic.json)
- [`batches/agentskills-created-2026-04-05-deterministic.json`](batches/agentskills-created-2026-04-05-deterministic.json)

Current run report: [`runs/2026-08-08-agentskills-april-2026-04-05.md`](runs/2026-08-08-agentskills-april-2026-04-05.md).

## Evidence boundary

Index collection only. No target repository content, stars, scripts, evaluations, implementation code, or runtime behavior was inspected, and no repository was marked complete from metadata.

## Next index action

Continue with the `2026-04-06` exact single-day shard and keep canonical totals frozen until reconciliation is complete.
