# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits already composed into the canonical catalog: `2630`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across composed inputs: `2634`
- Unique repositories after case-insensitive `owner/repository` deduplication: `2502`
- Exact duplicates removed across composed inputs: `132`
- New unique repositories composed in this run: `0`
- Provisionally eligible for later deep analysis: `2088`
- Held as adjacent or unclear search hits: `414`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The canonical total remains `2502`. A new `agentskills in:name,description` page-1 staging batch has been persisted, but it has **not** been composed into the canonical count because full historical identity reconciliation is not yet complete.

## Completed search coverage

- `"agent skills" in:name,description`, pages `1-10`
- `"codex skills" in:name,description`, pages `1-10`
- `"claude skills" in:name,description`, pages `1-10`
- `"mcp skills" in:name,description`, pages `1-10`
- `"skill catalog" in:name,description`, pages `1-10`
- `"skill registry" in:name,description`, pages `1-10`
- `"agent skill" in:name,description`, pages `1-10`
- `"agentskills cli" in:name,description`, page `1`
- `"skill marketplace" in:name,description`, pages `1-10`
- `"agent skills hub" in:name,description`, pages `1-2`
- `"skill hub" in:name,description`, pages `1-10`
- `"agent skills directory" in:name,description`, pages `1-2`
- `"openai skills" in:name,description`, pages `1-10`
- `"anthropic skills" in:name,description`, pages `1-10`
- `"agent skills marketplace" in:name,description`, pages `1-10`
- `"agentskills specification" in:name,description`, page `1`
- `"skill lint" in:name,description`, complete accessible page-1 result set with `100` requested results
- `"agent skills validator" in:name,description`, complete accessible page-1 result set with `100` requested results
- `"agent skills standard" in:name,description`, pages `1-10`, `20` results per page
- `"agent skills eval" in:name,description`, complete accessible pages `1-3`, `20` requested results per page; page `4` returned `0`
- `"agent skills benchmark" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills test" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agentskills sdk" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills template" in:name,description`, complete accessible pages `1-3`, `20` requested results per page; page `4` returned `0`
- `"agent skills examples" in:name,description`, complete accessible pages `1-2`, `50` requested results per page; page `3` returned `0`
- `"agent skills protocol" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills registry" in:name,description`, complete accessible pages `1-41`, `20` requested results per page; page `42` returned `0`

## In-progress search coverage

Query:

```text
agentskills in:name,description
```

GitHub repository search was run through page `11` at `per_page=20`. Pages `1-10` each returned `20` repository identities, and page `11` also returned `20`, so this query is not terminal. Only page `1` has been persisted as a staging batch in this run; pages `2-11` are not claimed as merged catalog coverage.

Page `1` contains `20` identities and no batch-internal duplicate. Three exact prior identities were directly confirmed in persisted index artifacts:

- `agentskills/agentskills`
- `darkrishabh/agent-skills-eval`
- `pratikxpanda/agentskills-sdk`

The other `17` page-1 identities remain explicitly `unresolved_against_full_prior_catalog`. They are not marked new. The existing canonical manifest is aggregate-only and does not contain a complete identity ledger, and this run did not exhaustively traverse every historical batch. Therefore no canonical delta is asserted from page `1` yet.

The page-1 repository identities, GitHub IDs, default branches, sizes, archived states, provisional classifications, and reconciliation status are persisted in [`batches/agentskills-page-1.json`](batches/agentskills-page-1.json).

## Page-1 provisional classification

| Classification | Raw page-1 count |
| --- | ---: |
| `specification` | 1 |
| `skill_collection` | 6 |
| `single_skill_or_domain_package` | 6 |
| `awesome_index` | 1 |
| `skill_tooling` | 5 |
| `adjacent_search_hit` | 0 |
| `unclear_search_hit` | 1 |

These are raw page-1 classifications only. They are not added to canonical classification totals until each unresolved identity is reconciled against prior index artifacts.

## Canonical classification totals

| Classification | Count |
| --- | ---: |
| `specification` | 163 |
| `skill_collection` | 611 |
| `single_skill_or_domain_package` | 104 |
| `awesome_index` | 38 |
| `skill_tooling` | 1172 |
| `adjacent_search_hit` | 152 |
| `unclear_search_hit` | 262 |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identity and accessibility. Classification is provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

The current run deliberately does not treat code-search emptiness or an aggregate prior count as proof that an identity is new.

## Validation

- Previous canonical state remains: `2502 unique / 2088 eligible / 414 held`.
- Page-1 raw identities: `20`.
- Page-1 internal duplicates: `0`.
- Directly confirmed prior duplicates: `3`.
- Unresolved identities requiring exhaustive historical reconciliation: `17`.
- Staging batch initial commit: `03bda2ed0ad757ec4130d83ee1b0959194a2024b`.
- Metadata correction commit: `7aab4f571229ffb00b53ba8b70a4b5fdebda6bf5`.
- Latest-manifest pending-reconciliation commit: `c1d0f07a8a666d25e60633982723139d63c26ed1`.
- `2088 + 414 = 2502`, matching the canonical eligible and held partitions.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
