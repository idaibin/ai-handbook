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

The canonical total remains `2502` because the current `agentskills in:name,description` search is staged but has not completed exhaustive historical identity reconciliation. This run persisted pages `17-20`, bringing staging coverage to pages `1-20`.

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

Persisted staging coverage now includes pages `1-20`, each observed with `20` GitHub repository identities. Page `21` was also probed and returned `20` results, but it is not claimed as persisted staging coverage yet.

Current staging state:

| Metric | Value |
| --- | ---: |
| Raw identities persisted | `400` |
| Confirmed cross-staging duplicates in reconciled pages `1-16` | `1` |
| Staged unique identities reconciled through page `16` | `319` |
| New identities unique within pages `17-20` | `80` |
| Exact prior-catalog duplicates directly confirmed | `3` |
| Unresolved identity records awaiting full reconciliation | `396` |
| Global staged-unique total | `not asserted` |
| Canonical delta asserted | `0` |

The three directly confirmed prior-catalog duplicates remain:

- `agentskills/agentskills`
- `darkrishabh/agent-skills-eval`
- `pratikxpanda/agentskills-sdk`

Across reconciled pages `1-16`, the confirmed cross-staging repeat remains `0xsarawut/agentskills`, which appeared at page `3` rank `20` and page `4` rank `1`. Pages `17-20` contain no duplicate identity within their own 80-hit batch, but cross-staging reconciliation against pages `1-16` is still pending. This boundary is recorded explicitly rather than treating mutable search ordering or absence from a partial lookup as proof of uniqueness.

Staging artifacts:

- [`batches/agentskills-page-1.json`](batches/agentskills-page-1.json)
- [`batches/agentskills-pages-2-3.json`](batches/agentskills-pages-2-3.json)
- [`batches/agentskills-pages-4-6.json`](batches/agentskills-pages-4-6.json)
- [`batches/agentskills-pages-7-10.json`](batches/agentskills-pages-7-10.json)
- [`batches/agentskills-pages-11-16.json`](batches/agentskills-pages-11-16.json)
- [`batches/agentskills-pages-17-20.json`](batches/agentskills-pages-17-20.json)

## Pages 17-20 provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `76` |
| `single_skill_or_domain_package` | `1` |
| `awesome_index` | `0` |
| `skill_tooling` | `1` |
| `adjacent_search_hit` | `0` |
| `unclear_search_hit` | `2` |

Classification uses repository identity and GitHub search context only. It is intentionally provisional and is not added to canonical classification totals until historical identity reconciliation is complete.

## Canonical classification totals

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

This remains an index-only catalog. GitHub repository search verified repository identity and accessibility. Classification is provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Current canonical state remains: `2502 unique / 2088 eligible / 414 held`.
- Newly persisted pages in this run: `17-20`.
- Raw identities newly persisted in this run: `80`.
- Internal duplicates within pages `17-20`: `0`.
- Cross-staging reconciliation for pages `17-20`: `pending`.
- New identities unique within the new batch: `80`.
- Total staged raw identities across pages `1-20`: `400`.
- Directly confirmed prior-catalog duplicates across earlier reconciled staging: `3`.
- Pages `17-20` staging commit: `afe3208d2950d1b4cdde3680c1b35485a65b317f`.
- Latest-manifest staging-state commit: `a415b94cf768dadda42285dd07cef6b02de8f0bd`.
- `2088 + 414 = 2502`, matching the canonical eligible and held partitions.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
