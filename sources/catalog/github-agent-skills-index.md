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

The original whole-month paging pass produced `402` raw records and `401` distinct identities. Deterministic daily reconciliation recovered one omitted identity, `UCTooCom/agentskills-runtime`, and closed at `402 / 402` distinct identities across 28 exact single-day shards.

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

## March 2026 created-date partition — deterministic indexing in progress

Verified persisted coverage now spans:

```text
2026-03-01 .. 2026-03-15
per_page=100
exact single-day shards with explicit terminal pagination probes
```

The first 14 daily shards produced `274 / 274` distinct staged identities. The `2026-03-15` shard was high-volume and therefore persisted from one controlled multi-page snapshot:

| Page | Results |
| --- | ---: |
| 1 | 100 |
| 2 | 13 |
| 3 | 0 |

The March 15 snapshot contains `113 / 113` case-insensitive unique identities. No duplicate identity was observed inside the snapshot. Because exact `created:` day shards are disjoint by repository creation date, cumulative March staging through March 15 is now `387 / 387` identities.

### March provisional classification through 2026-03-15

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 312 |
| `single_skill_or_domain_package` | 28 |
| `awesome_index` | 3 |
| `skill_tooling` | 17 |
| `adjacent_search_hit` | 24 |
| `unclear_search_hit` | 3 |
| **Total** | **387** |

The March 15 contribution is `110 skill_collection`, `1 skill_tooling`, and `2 adjacent_search_hit`. Classification is index-stage only and uses repository identity/name metadata; it is not a deep-content determination.

Artifacts:

- [`batches/agentskills-created-2026-03-01-through-10-deterministic.json`](batches/agentskills-created-2026-03-01-through-10-deterministic.json)
- [`batches/agentskills-created-2026-03-11-through-14-deterministic.json`](batches/agentskills-created-2026-03-11-through-14-deterministic.json)
- [`batches/agentskills-created-2026-03-15-controlled-multipage.json`](batches/agentskills-created-2026-03-15-controlled-multipage.json)

Current run report: [`runs/2026-08-07-agentskills-march-2026-03-15.md`](runs/2026-08-07-agentskills-march-2026-03-15.md).

## Evidence boundary

This phase is index-only. No target repository README, `SKILL.md`, scripts, references, eval contents, stars, implementation code, or runtime behavior was inspected. Repository completion for deep-analysis purposes is not asserted from these records.

## Next index action

Continue the deterministic March partition with the `2026-03-16` exact single-day shard. Keep canonical totals frozen until created-date partition unions are reconciled against unpartitioned staging and the complete historical canonical ledger.
