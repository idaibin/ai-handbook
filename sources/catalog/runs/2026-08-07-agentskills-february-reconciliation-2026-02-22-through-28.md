# GitHub Agent Skills index run — February 22–28 reconciliation

## Scope

Index-only. No target repository README, `SKILL.md`, scripts, references, evals, stars, implementation code, or runtime behavior was read.

## Queries

Seven exact single-day GitHub repository searches were executed:

```text
agentskills in:name,description created:2026-02-22..2026-02-22
...
agentskills in:name,description created:2026-02-28..2026-02-28
```

Each shard used `per_page=100` plus an explicit `page=2` terminal probe.

| Date | Page 1 | Page 2 |
| --- | ---: | ---: |
| 2026-02-22 | 15 | 0 |
| 2026-02-23 | 10 | 0 |
| 2026-02-24 | 12 | 0 |
| 2026-02-25 | 16 | 0 |
| 2026-02-26 | 19 | 0 |
| 2026-02-27 | 23 | 0 |
| 2026-02-28 | 12 | 0 |

## Verified result

- Raw identities: `107`
- Case-insensitive unique identities: `107`
- Internal duplicates: `0`
- All seven page-2 probes: `0`
- Matches to the three original February paging artifacts: `107 / 107`
- Missing from original paging artifacts in this run: `0`
- New staged identities in this run: `0`

The earlier deterministic reconciliation had already recovered one repository omitted by the unstable whole-month pagination pass: `UCTooCom/agentskills-runtime` from the exact `2026-02-16` shard.

Combining the previously verified daily shards (`2026-02-01..2026-02-21`, 295 unique) with this run (`2026-02-22..2026-02-28`, 107 unique) yields a full February deterministic daily union of **402 distinct repository identities**. This exactly matches the February staging union after the single recovered identity was added.

Therefore deterministic reconciliation for `2026-02-01..2026-02-28` is complete. Canonical catalog totals are not changed here because reconciliation against unpartitioned staging and the complete historical canonical ledger is still pending.

## Provisional classification for this run

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 80 |
| `single_skill_or_domain_package` | 4 |
| `awesome_index` | 2 |
| `skill_tooling` | 9 |
| `adjacent_search_hit` | 10 |
| `unclear_search_hit` | 2 |
| **Total** | **107** |

Classifications are preserved from exact identities already present in the original February paging artifacts. No repository contents were used for classification.

## Artifact

- `sources/catalog/batches/agentskills-created-2026-02-22-through-28-reconciliation.json`

## Next index action

Reconcile the verified January (`368`) and February (`402`) partition unions against the unpartitioned staging set and the historical canonical ledger before asserting any canonical additions. Then continue the next created-date partition.
