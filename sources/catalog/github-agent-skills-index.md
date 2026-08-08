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
2026-04-01 .. 2026-04-13
per_page=100
13 exact single-day shards with terminal pagination probes
```

The `2026-04-13` shard returned `20` repositories on page 1 and `0` on page 2. Recheck with `per_page=20` returned `20,0`. Case-insensitive `owner/repository` deduplication produced `20` unique identities and `0` internal duplicates.

April staging now contains `428` unique identities across `2026-04-01` through `2026-04-13`, with `0` cross-shard duplicates asserted.

### April provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 228 |
| `single_skill_or_domain_package` | 127 |
| `awesome_index` | 1 |
| `skill_tooling` | 14 |
| `adjacent_search_hit` | 58 |
| `unclear_search_hit` | 0 |
| **Total** | **428** |

Classification remains metadata-only and provisional. Ambiguous hits are retained as adjacent rather than promoted by assumption.

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

Current run report: [`runs/2026-08-08-agentskills-april-2026-04-13.md`](runs/2026-08-08-agentskills-april-2026-04-13.md).

## Evidence boundary

Index collection only. No target repository content, stars, scripts, evaluations, implementation code, or runtime behavior was inspected, and no repository was marked complete from metadata.

## Next index action

Continue with the `2026-04-14` exact single-day shard and keep canonical totals frozen until reconciliation is complete.