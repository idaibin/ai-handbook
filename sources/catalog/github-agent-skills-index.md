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
| `2026-04` | 1272 | 30 daily shards complete; historical reconciliation pending |

## April 2026 partition — daily staging complete

Verified persisted coverage:

```text
2026-04-01 .. 2026-04-30
per_page=100
30 exact single-day shards with terminal pagination probes
```

The `2026-04-30` shard returned `29` repositories on page 1 and `0` on page 2. Independent rechecks returned `20,9,0` with `per_page=20` and `29,0` with `per_page=33`. Case-insensitive `owner/repository` deduplication produced `29` unique identities and `0` internal duplicates.

April staging contains `1272` unique identities across `2026-04-01` through `2026-04-30`, with `0` cross-shard duplicates asserted under the established connector-search partition contract.

### April provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 24 |
| `skill_collection` | 720 |
| `single_skill_or_domain_package` | 411 |
| `awesome_index` | 1 |
| `skill_tooling` | 29 |
| `adjacent_search_hit` | 85 |
| `unclear_search_hit` | 2 |
| **Total** | **1272** |

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
- [`batches/agentskills-created-2026-04-21-deterministic.json`](batches/agentskills-created-2026-04-21-deterministic.json)
- [`batches/agentskills-created-2026-04-22-deterministic.json`](batches/agentskills-created-2026-04-22-deterministic.json)
- [`batches/agentskills-created-2026-04-23-deterministic.json`](batches/agentskills-created-2026-04-23-deterministic.json)
- [`batches/agentskills-created-2026-04-24-deterministic.json`](batches/agentskills-created-2026-04-24-deterministic.json)
- [`batches/agentskills-created-2026-04-25-deterministic.json`](batches/agentskills-created-2026-04-25-deterministic.json)
- [`batches/agentskills-created-2026-04-26-deterministic.json`](batches/agentskills-created-2026-04-26-deterministic.json)
- [`batches/agentskills-created-2026-04-27-deterministic.json`](batches/agentskills-created-2026-04-27-deterministic.json)
- [`batches/agentskills-created-2026-04-28-deterministic.json`](batches/agentskills-created-2026-04-28-deterministic.json)
- [`batches/agentskills-created-2026-04-29-deterministic.json`](batches/agentskills-created-2026-04-29-deterministic.json)
- [`batches/agentskills-created-2026-04-30-deterministic.json`](batches/agentskills-created-2026-04-30-deterministic.json)

## May 2026 partition — staging in progress

Verified persisted coverage:

```text
2026-05-01 .. 2026-05-03
per_page=100
3 exact single-day shards with terminal pagination probes
```

The `2026-05-03` shard returned `19` repositories on page 1 and `0` on page 2. Independent rechecks returned `19,0` with both `per_page=20` and `per_page=33`. Case-insensitive `owner/repository` deduplication produced `19` within-shard unique identities and `0` internal duplicates. One identity already exists in an earlier catalog artifact, leaving `18` actual new identities.

May daily staging now contains `66` unique created-date identities across `2026-05-01` through `2026-05-03`. Canonical totals remain frozen while historical reconciliation is pending.

### May provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 21 |
| `skill_collection` | 24 |
| `single_skill_or_domain_package` | 17 |
| `awesome_index` | 0 |
| `skill_tooling` | 1 |
| `adjacent_search_hit` | 2 |
| `unclear_search_hit` | 1 |
| **Total** | **66** |

Classification remains repository-metadata-only and provisional. In the `2026-05-03` shard, all 18 topic-relevant identities were held below the `1000`-star eligibility gate; one adjacent agent UI was rejected. The ready snapshot is valid but empty. Identical default-branch HEAD clusters were recorded without collapsing repository identity counts.

### May artifacts

- [`batches/agentskills-created-2026-05-01-deterministic.json`](batches/agentskills-created-2026-05-01-deterministic.json)
- [`batches/agentskills-created-2026-05-02-deterministic.json`](batches/agentskills-created-2026-05-02-deterministic.json)
- [`batches/agentskills-created-2026-05-03-deterministic.json`](batches/agentskills-created-2026-05-03-deterministic.json)

Current run report: [`runs/2026-08-09-agentskills-may-2026-05-03.md`](runs/2026-08-09-agentskills-may-2026-05-03.md). Retrospective: [`retrospectives/skills-index-20260809T054833Z.json`](retrospectives/skills-index-20260809T054833Z.json).

## Evidence boundary

Index collection only. No target repository README, `SKILL.md`, scripts, references, evaluations, implementation code, or runtime behavior was inspected, and no repository was marked complete from metadata. Repository metadata such as descriptions/fork relationships was used only for index-stage classification of ambiguous names.

## Next index action

Continue the deterministic May partition with the `2026-05-04` exact single-day shard. Apply and measure `skills-index-action-001`; keep canonical totals frozen until historical reconciliation is complete.
