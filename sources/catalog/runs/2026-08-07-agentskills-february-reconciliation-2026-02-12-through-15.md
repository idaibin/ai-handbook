# GitHub Skills Repository Index — February deterministic reconciliation through 2026-02-15

## Scope

Index collection only. No target repository README, `SKILL.md`, scripts, references, eval contents, stars, implementation code, or runtime behavior was inspected.

## Live queries executed

Four exact single-day GitHub repository searches were executed with `per_page=100`, each followed by a page-2 terminal probe:

```text
agentskills in:name,description created:2026-02-12..2026-02-12
agentskills in:name,description created:2026-02-13..2026-02-13
agentskills in:name,description created:2026-02-14..2026-02-14
agentskills in:name,description created:2026-02-15..2026-02-15
```

Observed page-1 counts were `18`, `10`, `8`, and `14`; every page-2 probe returned `0` repositories.

## Merge and deduplication result

- Raw identities observed: `50`
- Unique identities across the mutually exclusive created-date shards: `50`
- Internal case-insensitive duplicates: `0`
- Exact matches in previously persisted February staging: `50`
- Missing from prior February staging: `0`
- New staged identities after merge: `0`

This extends deterministic February coverage from `2026-02-01..2026-02-11` to `2026-02-01..2026-02-15`. Across the first fifteen exact daily shards, `203` unique identities have now been observed and all `203` match the existing deduplicated February staging union.

## Provisional classification for this run

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `43` |
| `single_skill_or_domain_package` | `0` |
| `awesome_index` | `0` |
| `skill_tooling` | `4` |
| `adjacent_search_hit` | `3` |
| `unclear_search_hit` | `0` |
| **Total** | **`50`** |

Classification remains metadata-only and provisional. Existing staged classifications were retained for exact identity matches and were not merged into canonical totals.

## Canonical state

Canonical totals remain frozen pending full reconciliation:

```text
unique:    2502
eligible:  2088
held:       414
canonical delta asserted: 0
```

## Artifacts and commits produced in this automation run

Authoritative progress artifacts:

```text
7fdccc392bf2101d992a4521a76a68ddc2339be6
chore(research): reconcile February agentskills Feb 12-15
sources/catalog/batches/agentskills-created-2026-02-12-through-15-reconciliation.json

6d321fa46567aa129e1723616fbd3c8477c6774a
chore(research): extend February reconciliation through Feb 15
sources/catalog/github-agent-skills-index-latest.json

5e58312b5e9530676b4c66872f638a32f3d40218
docs(research): record February reconciliation through Feb 15
sources/catalog/github-agent-skills-index.md
```

A supplemental overlapping artifact was also created earlier in this run while the repository state was concurrently advancing:

```text
9936b4797568693b803fe841c2c72d6a06d40bbd
chore(research): reconcile February agentskills Feb 2-4
sources/catalog/batches/agentskills-created-2026-02-02-through-04-reconciliation.json
```

That supplemental file contains verified index-only observations, but it is intentionally not referenced by the authoritative manifest because a newer existing artifact already reconciles `2026-02-02..2026-02-11` comprehensively.

## Next index action

Continue deterministic February reconciliation with the exact `2026-02-16` created-date shard. Do not mark February complete until all remaining daily shards through `2026-02-28` have been reconciled, then compare the verified February union against unpartitioned staging and the historical canonical ledger.
