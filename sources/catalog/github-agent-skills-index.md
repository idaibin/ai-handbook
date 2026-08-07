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
| `2026-03` | 831 | 31 deterministic single-day shards complete; historical reconciliation pending |

## March 2026 created-date partition — deterministic indexing complete

Verified persisted coverage:

```text
2026-03-01 .. 2026-03-31
per_page=100
31 exact single-day shards with explicit terminal pagination probes
```

Final March staging is `831 / 831` identities with no intra-March duplicate asserted.

### March final provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 606 |
| `single_skill_or_domain_package` | 106 |
| `awesome_index` | 4 |
| `skill_tooling` | 38 |
| `adjacent_search_hit` | 71 |
| `unclear_search_hit` | 6 |
| **Total** | **831** |

Latest March artifact: [`batches/agentskills-created-2026-03-31-deterministic.json`](batches/agentskills-created-2026-03-31-deterministic.json).

## April 2026 created-date partition — in progress

Verified persisted coverage:

```text
2026-04-01 .. 2026-04-03
per_page=100
3 exact single-day shards with explicit terminal pagination probes
```

The `2026-04-03` shard returned `27` repositories on page 1 and `0` on page 2. A second pagination check using `per_page=20` returned `20,7,0`, confirming the same 27-record result set. Case-insensitive `owner/repository` deduplication produced `27` current-shard unique identities and `0` internal duplicates.

The April staging union now contains `175` unique identities across the exact `2026-04-01`, `2026-04-02`, and `2026-04-03` creation-date shards, with `0` cross-shard duplicates asserted.

### April staging provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 56 |
| `single_skill_or_domain_package` | 106 |
| `awesome_index` | 0 |
| `skill_tooling` | 0 |
| `adjacent_search_hit` | 13 |
| `unclear_search_hit` | 0 |
| **Total** | **175** |

Classification is index-stage only and uses repository identity/name metadata. Ambiguous metadata-only hits remain adjacent rather than being promoted by assumption.

### April artifacts

- [`batches/agentskills-created-2026-04-01-deterministic.json`](batches/agentskills-created-2026-04-01-deterministic.json)
- [`batches/agentskills-created-2026-04-02-deterministic.json`](batches/agentskills-created-2026-04-02-deterministic.json)
- [`batches/agentskills-created-2026-04-03-deterministic.json`](batches/agentskills-created-2026-04-03-deterministic.json)

Current run report: [`runs/2026-08-08-agentskills-april-2026-04-03.md`](runs/2026-08-08-agentskills-april-2026-04-03.md).

## Evidence boundary

This phase is index-only. No target repository README, `SKILL.md`, scripts, references, eval contents, stars, implementation code, or runtime behavior was inspected. Repository completion for deep-analysis purposes is not asserted from these records.

## Next index action

Continue the deterministic April partition with the `2026-04-04` exact single-day shard. Keep canonical totals frozen until created-date partition unions are reconciled against unpartitioned staging and the complete historical canonical ledger.
