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

## January 2026 created-date partition

```text
agentskills in:name,description created:2026-01-01..2026-01-31
```

Complete within the persisted partition: `368 / 368` case-insensitive unique identities; page `20` returned `0`.

| Classification | Count |
| --- | ---: |
| `specification` | 2 |
| `skill_collection` | 275 |
| `single_skill_or_domain_package` | 32 |
| `awesome_index` | 11 |
| `skill_tooling` | 21 |
| `adjacent_search_hit` | 12 |
| `unclear_search_hit` | 15 |
| **Total** | **368** |

## February 2026 created-date partition — deterministic reconciliation complete

```text
agentskills in:name,description created:2026-02-01..2026-02-28
```

The original whole-month paging pass produced `402` raw records and `401` distinct identities. A cross-run duplicate, `irfiacre/agentskills`, proved best-match pagination drift. Deterministic reconciliation therefore used 28 exact single-day `created:` shards with `per_page=100` and explicit page-2 terminal probes.

The exact `2026-02-16` shard recovered one identity omitted by the unstable paging pass: `UCTooCom/agentskills-runtime`. The final seven shards (`2026-02-22..2026-02-28`) produced `107 / 107` distinct identities, all already present in the original paging artifacts; all seven page-2 probes returned `0`.

Full deterministic February result:

| Metric | Value |
| --- | ---: |
| Completed daily shards | 28 |
| Verified daily-shard unique union | **402** |
| Original paging unique union | 401 |
| Recovered missing identities | 1 |
| Final deduplicated February staging | **402** |
| Canonical additions asserted | 0 |

### February provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 313 |
| `single_skill_or_domain_package` | 16 |
| `awesome_index` | 3 |
| `skill_tooling` | 36 |
| `adjacent_search_hit` | 30 |
| `unclear_search_hit` | 4 |
| **Total** | **402** |

Artifact: [`batches/agentskills-created-2026-02-22-through-28-reconciliation.json`](batches/agentskills-created-2026-02-22-through-28-reconciliation.json).

Run report: [`runs/2026-08-07-agentskills-february-reconciliation-2026-02-22-through-28.md`](runs/2026-08-07-agentskills-february-reconciliation-2026-02-22-through-28.md).

## March 2026 created-date partition — deterministic indexing in progress

March indexing continues with exact single-day `created:` shards rather than unstable best-match whole-month pagination.

Verified coverage in the current run:

```text
2026-03-01 .. 2026-03-10
per_page=100
page 1 + explicit page 2 terminal probe for every day
```

| Date | Page 1 | Page 2 |
| --- | ---: | ---: |
| 2026-03-01 | 12 | 0 |
| 2026-03-02 | 18 | 0 |
| 2026-03-03 | 17 | 0 |
| 2026-03-04 | 25 | 0 |
| 2026-03-05 | 14 | 0 |
| 2026-03-06 | 15 | 0 |
| 2026-03-07 | 10 | 0 |
| 2026-03-08 | 13 | 0 |
| 2026-03-09 | 22 | 0 |
| 2026-03-10 | 16 | 0 |
| **Total** | **162** | **0** |

The 162 records are `162 / 162` distinct under case-insensitive `owner/repository` deduplication. No March identity is promoted into canonical totals in this phase.

### March provisional classification through 2026-03-10

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 116 |
| `single_skill_or_domain_package` | 16 |
| `awesome_index` | 2 |
| `skill_tooling` | 11 |
| `adjacent_search_hit` | 14 |
| `unclear_search_hit` | 3 |
| **Total** | **162** |

Classification is index-stage only and uses repository identity/name metadata. It is not a deep-content determination.

Artifact: [`batches/agentskills-created-2026-03-01-through-10-deterministic.json`](batches/agentskills-created-2026-03-01-through-10-deterministic.json).

Run report: [`runs/2026-08-07-agentskills-march-2026-03-01-through-10.md`](runs/2026-08-07-agentskills-march-2026-03-01-through-10.md).

## Evidence boundary

This phase is index-only. No target repository README, `SKILL.md`, scripts, references, eval contents, stars, implementation code, or runtime behavior was inspected. Repository completion for deep-analysis purposes is not asserted from these records.

## Next index action

Continue the deterministic March partition with the `2026-03-11` exact single-day shard. Keep canonical totals frozen until created-date partition unions are reconciled against unpartitioned staging and the complete historical canonical ledger.
