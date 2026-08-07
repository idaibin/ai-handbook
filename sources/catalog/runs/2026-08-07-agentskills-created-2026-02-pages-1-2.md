# GitHub Agent Skills Repository Index Run — 2026-08-07

## Scope

Index-only collection. No deep repository analysis was performed.

Query:

```text
agentskills in:name,description created:2026-02-01..2026-02-28
```

Pages persisted: `1-2`, `20` results per page.

## Verified progress

| Metric | Value |
| --- | ---: |
| Raw identities | `40` |
| Case-insensitive internal duplicates | `0` |
| Unique identities within batch | `40` |
| Canonical additions asserted | `0` |
| Canonical unique total | `2502` |
| Deep-analysis eligible | `2088` |
| Held for review | `414` |

The February partition is still in progress. Its next page is `3`.

The January and February `created:` ranges are disjoint by repository creation date, so the same repository cannot legitimately belong to both monthly partitions. Reconciliation against the unpartitioned `agentskills` staging set and the complete historical canonical ledger remains pending; therefore no canonical delta is asserted.

## Provisional classification

| Classification | Count |
| --- | ---: |
| `skill_collection` | `30` |
| `skill_tooling` | `5` |
| `adjacent_search_hit` | `4` |
| `unclear_search_hit` | `1` |
| Other classes | `0` |

Classification uses repository identity and search-returned repository metadata only.

## Artifacts and commits

- `sources/catalog/batches/agentskills-created-2026-02-pages-1-2.json`
  - `2f74722f0b8b0da9322c1da7ca3dde1c95389b52`
  - `chore(research): stage February agentskills pages 1-2`
- `sources/catalog/github-agent-skills-index-latest.json`
  - `91973c2823bfd07847f89a76c75def75ba573b0e`
  - `chore(research): begin February agentskills partition index`
- `sources/catalog/github-agent-skills-index.md`
  - `234a2e6caa9fc19a8b7c886fd29ad9049cc72657`
  - `docs(research): record February agentskills pages 1-2`

## Evidence boundary

No target repository README, `SKILL.md`, scripts, references, evals, stars, implementation code, or runtime behavior was inspected. These records do not mark any target repository complete for deep-analysis purposes.
