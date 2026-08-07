# GitHub Agent Skills Repository Index

## Current verified catalog

- Canonical unique repositories: `2502`
- Provisionally eligible for later deep analysis: `2088`
- Held as adjacent or unclear search hits: `414`
- Canonical delta asserted in the current index phase: `0`

Canonical totals remain frozen while verified created-date partitions are reconciled against unpartitioned staging and the complete historical ledger. Machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## Unpartitioned `agentskills`

```text
agentskills in:name,description
```

- Persisted pages: `1-50`
- Raw staging records: `1000`
- Page `51`: GitHub first-1000-results limit
- Historical reconciliation: pending

## Completed created-date partitions

| Partition | Verified unique | Status |
| --- | ---: | --- |
| `2026-01` | 368 | complete; terminal page `20 = 0` |
| `2026-02` | 402 | deterministic daily reconciliation complete; recovered `UCTooCom/agentskills-runtime` |

## March 2026 created-date partition — deterministic indexing in progress

Verified persisted coverage:

```text
2026-03-01 .. 2026-03-30
per_page=100
30 exact single-day shards with explicit terminal pagination probes
```

March staging through March 29 contained `727 / 727` identities. The `2026-03-30` shard contributed `35 / 35` additional case-insensitive unique identities with page counts `35, 0`. Exact `created:` day shards are disjoint by repository creation date, so cumulative March staging is now `762 / 762` identities with no intra-March duplicate asserted.

### March provisional classification through 2026-03-30

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 593 |
| `single_skill_or_domain_package` | 61 |
| `awesome_index` | 3 |
| `skill_tooling` | 37 |
| `adjacent_search_hit` | 63 |
| `unclear_search_hit` | 5 |
| **Total** | **762** |

The March 30 contribution is `21 skill_collection`, `9 single_skill_or_domain_package`, `3 skill_tooling`, and `2 adjacent_search_hit`. Classification is index-stage only and uses repository identity/name metadata; it is not a deep-content determination.

### March artifacts

- [`batches/agentskills-created-2026-03-01-through-10-deterministic.json`](batches/agentskills-created-2026-03-01-through-10-deterministic.json)
- [`batches/agentskills-created-2026-03-11-through-14-deterministic.json`](batches/agentskills-created-2026-03-11-through-14-deterministic.json)
- [`batches/agentskills-created-2026-03-15-controlled-multipage.json`](batches/agentskills-created-2026-03-15-controlled-multipage.json)
- [`batches/agentskills-created-2026-03-16-deterministic.json`](batches/agentskills-created-2026-03-16-deterministic.json)
- [`batches/agentskills-created-2026-03-17-deterministic.json`](batches/agentskills-created-2026-03-17-deterministic.json)
- [`batches/agentskills-created-2026-03-18-deterministic.json`](batches/agentskills-created-2026-03-18-deterministic.json)
- [`batches/agentskills-created-2026-03-19-deterministic.json`](batches/agentskills-created-2026-03-19-deterministic.json)
- [`batches/agentskills-created-2026-03-20-deterministic.json`](batches/agentskills-created-2026-03-20-deterministic.json)
- [`batches/agentskills-created-2026-03-21-deterministic.json`](batches/agentskills-created-2026-03-21-deterministic.json)
- [`batches/agentskills-created-2026-03-22-deterministic.json`](batches/agentskills-created-2026-03-22-deterministic.json)
- [`batches/agentskills-created-2026-03-23-deterministic.json`](batches/agentskills-created-2026-03-23-deterministic.json)
- [`batches/agentskills-created-2026-03-24-deterministic.json`](batches/agentskills-created-2026-03-24-deterministic.json)
- [`batches/agentskills-created-2026-03-25-deterministic.json`](batches/agentskills-created-2026-03-25-deterministic.json)
- [`batches/agentskills-created-2026-03-26-deterministic.json`](batches/agentskills-created-2026-03-26-deterministic.json)
- [`batches/agentskills-created-2026-03-27-deterministic.json`](batches/agentskills-created-2026-03-27-deterministic.json)
- [`batches/agentskills-created-2026-03-28-deterministic.json`](batches/agentskills-created-2026-03-28-deterministic.json)
- [`batches/agentskills-created-2026-03-29-deterministic.json`](batches/agentskills-created-2026-03-29-deterministic.json)
- [`batches/agentskills-created-2026-03-30-deterministic.json`](batches/agentskills-created-2026-03-30-deterministic.json)

Current run report: [`runs/2026-08-08-agentskills-march-2026-03-30.md`](runs/2026-08-08-agentskills-march-2026-03-30.md).

## Evidence boundary

This phase is index-only. No target repository README, `SKILL.md`, scripts, references, eval contents, stars, implementation code, or runtime behavior was inspected. Repository completion for deep-analysis purposes is not asserted from these records.

## Next index action

Continue the deterministic March partition with the `2026-03-31` exact single-day shard. Keep canonical totals frozen until created-date partition unions are reconciled against unpartitioned staging and the complete historical canonical ledger.
