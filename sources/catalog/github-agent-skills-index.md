# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits already composed into the canonical catalog: `2630`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across composed inputs: `2634`
- Unique repositories after case-insensitive `owner/repository` deduplication: `2502`
- Exact duplicates removed across composed inputs: `132`
- Provisionally eligible for later deep analysis: `2088`
- Held as adjacent or unclear search hits: `414`

Canonical totals remain frozen while the newer `agentskills` staging and created-date partitions are reconciled against the complete historical ledger. Machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## Unpartitioned `agentskills`

```text
agentskills in:name,description
```

- Persisted pages: `1-50`
- Requested results per page: `20`
- Raw staging records: `1000`
- Page `51`: GitHub first-1000-results limit
- Full historical reconciliation: pending for the unreconciled staging tail

## January 2026 created-date partition — complete

```text
agentskills in:name,description created:2026-01-01..2026-01-31
```

Pages `1-19` are persisted: `368` raw identities / `368` unique identities. Page `20` returned `0` repositories.

| Classification | Count |
| --- | ---: |
| `specification` | `2` |
| `skill_collection` | `275` |
| `single_skill_or_domain_package` | `32` |
| `awesome_index` | `11` |
| `skill_tooling` | `21` |
| `adjacent_search_hit` | `12` |
| `unclear_search_hit` | `15` |
| **Total** | **`368`** |

## February 2026 created-date partition — deterministic reconciliation in progress

```text
agentskills in:name,description created:2026-02-01..2026-02-28
```

The original pagination pass searched through page `22`. Pages `1-21` produced `402` raw records and `401` case-insensitive unique identities; page `22` returned `0`. One cross-run duplicate, `irfiacre/agentskills`, proved GitHub best-match ordering drifted, so that pagination result alone is not treated as gap-free.

Daily deterministic reconciliation has now found an actual omission from the original paging union: `UCTooCom/agentskills-runtime`, observed in the exact `2026-02-16` shard. It was absent from all three original February paging artifacts, and an exact AI-handbook code search returned no match before this run. The repository is therefore added to staging as a new identity and provisionally classified `skill_tooling` from identity/search metadata only.

| Metric | Value |
| --- | ---: |
| Original paging raw records | `402` |
| Original paging distinct identities | `401` |
| Confirmed paging duplicate | `irfiacre/agentskills` |
| New identity recovered by deterministic reconciliation | `UCTooCom/agentskills-runtime` |
| Current deduplicated February staging | **`402`** |
| Canonical additions asserted | `0` |

### February provisional classification, current deduplicated staging

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `313` |
| `single_skill_or_domain_package` | `16` |
| `awesome_index` | `3` |
| `skill_tooling` | `36` |
| `adjacent_search_hit` | `30` |
| `unclear_search_hit` | `4` |
| **Total** | **`402`** |

Classification remains provisional and uses only repository identity plus GitHub repository-search metadata. It is not merged into canonical classification totals.

### Deterministic February reconciliation — verified through 2026-02-21

Reconciliation uses exact single-day `created:` shards with `per_page=100` plus an explicit page-2 terminal probe.

```text
verified date range: 2026-02-01 .. 2026-02-21
next shard:          2026-02-22
```

| Metric | Value |
| --- | ---: |
| Completed daily shards | **`21`** |
| Unique identities observed across completed shards | **`295`** |
| Matches to original February paging staging | **`294`** |
| Missing from original paging staging | **`1`** |
| New staged identities after merge | **`1`** |
| New February staging total | **`402`** |

The new coverage advanced in this run is `2026-02-16..2026-02-21`: **92 raw / 92 unique identities**. All six page-2 probes returned `0`. Of these 92 identities, 91 were already present in the original February paging artifacts and one was missing: `UCTooCom/agentskills-runtime`.

Provisional classification for the six newly advanced daily shards:

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `70` |
| `single_skill_or_domain_package` | `2` |
| `awesome_index` | `1` |
| `skill_tooling` | `13` |
| `adjacent_search_hit` | `6` |
| `unclear_search_hit` | `0` |
| **Total** | **`92`** |

A separate reconciliation artifact also records the complete live search performed for `2026-02-12..2026-02-21`. The already committed `2026-02-12..2026-02-15` artifact remains the authority for those four earlier shards; the superset artifact supplies the newly advanced `2026-02-16..2026-02-21` evidence and the recovered identity.

Dates `2026-02-22` through `2026-02-28` remain unreconciled, so February is still **not** marked complete.

### February artifacts

- [`batches/agentskills-created-2026-02-pages-1-2.json`](batches/agentskills-created-2026-02-pages-1-2.json)
- [`batches/agentskills-created-2026-02-pages-3-12.json`](batches/agentskills-created-2026-02-pages-3-12.json)
- [`batches/agentskills-created-2026-02-pages-13-21.json`](batches/agentskills-created-2026-02-pages-13-21.json)
- [`batches/agentskills-created-2026-02-01-reconciliation.json`](batches/agentskills-created-2026-02-01-reconciliation.json)
- [`batches/agentskills-created-2026-02-02-through-11-reconciliation.json`](batches/agentskills-created-2026-02-02-through-11-reconciliation.json)
- [`batches/agentskills-created-2026-02-12-through-15-reconciliation.json`](batches/agentskills-created-2026-02-12-through-15-reconciliation.json)
- [`batches/agentskills-created-2026-02-12-through-21-reconciliation.json`](batches/agentskills-created-2026-02-12-through-21-reconciliation.json)
- [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json)

## Canonical classification totals

These remain unchanged until deterministic historical reconciliation completes.

| Classification | Count |
| --- | ---: |
| `specification` | `163` |
| `skill_collection` | `611` |
| `single_skill_or_domain_package` | `104` |
| `awesome_index` | `38` |
| `skill_tooling` | `1172` |
| `adjacent_search_hit` | `152` |
| `unclear_search_hit` | `262` |

## Evidence boundary

This phase is index-only. No target repository README, `SKILL.md`, scripts, references, eval contents, stars, implementation code, or runtime behavior was inspected. Repository completion for deep-analysis purposes is not asserted from these records.

## Next index action

Continue deterministic February reconciliation with the `2026-02-22` single-day created-date shard. After `2026-02-28` is reconciled, compare the verified February union against unpartitioned staging and the complete historical ledger. Canonical `2502 / 2088 / 414` remains unchanged until that reconciliation is complete.
