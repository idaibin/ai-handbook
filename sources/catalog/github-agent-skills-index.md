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

The canonical total remains `2502` because the current `agentskills in:name,description` search is staged but has not yet completed exhaustive historical identity reconciliation. This run persisted pages `11-16`, bringing staging coverage to pages `1-16`.

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

Persisted staging coverage now includes pages `1-16`, each observed with `20` GitHub repository identities. Page `17` was also probed and returned `20` results, but it is not claimed as persisted staging coverage yet.

Staged totals:

| Metric | Value |
| --- | ---: |
| Raw identities | `320` |
| Batch/internal or cross-staging duplicates | `1` |
| Unique staged identities after cross-staging deduplication | `319` |
| Exact prior duplicates directly confirmed | `3` |
| Identities still requiring full historical reconciliation | `316` |
| Canonical delta asserted | `0` |

The three directly confirmed prior-catalog duplicates remain:

- `agentskills/agentskills`
- `darkrishabh/agent-skills-eval`
- `pratikxpanda/agentskills-sdk`

Across persisted pages `1-16`, the only currently observed cross-staging repeat is `0xsarawut/agentskills`, which appeared at page `3` rank `20` and page `4` rank `1`. Pages `11-16` added `120` raw identities and all `120` were distinct from persisted pages `1-10` under case-insensitive `owner/repository` comparison.

Staging artifacts:

- [`batches/agentskills-page-1.json`](batches/agentskills-page-1.json)
- [`batches/agentskills-pages-2-3.json`](batches/agentskills-pages-2-3.json)
- [`batches/agentskills-pages-4-6.json`](batches/agentskills-pages-4-6.json)
- [`batches/agentskills-pages-7-10.json`](batches/agentskills-pages-7-10.json)
- [`batches/agentskills-pages-11-16.json`](batches/agentskills-pages-11-16.json)

## Pages 11-16 provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `111` |
| `single_skill_or_domain_package` | `2` |
| `awesome_index` | `0` |
| `skill_tooling` | `6` |
| `adjacent_search_hit` | `0` |
| `unclear_search_hit` | `1` |

The mixed page-16 results were classified only from repository identity and search context: obvious SDK, CLI, runtime, MCP, or language-library identities were staged as `skill_tooling`; obvious single-skill identities as `single_skill_or_domain_package`; `upex-galaxy/agentic-qa-boilerplate` remains `unclear_search_hit`. Repository contents were intentionally not read. These classifications are not added to canonical classification totals until historical reconciliation is complete.

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

The current run deliberately does not treat code-search emptiness, mutable page ordering, or an aggregate prior count as proof that an identity is new.

## Validation

- Current canonical state remains: `2502 unique / 2088 eligible / 414 held`.
- Newly persisted pages in this run: `11-16`.
- Raw identities newly persisted in this run: `120`.
- Internal duplicates within pages `11-16`: `0`.
- Cross-staging duplicates against pages `1-10`: `0`.
- New staged-unique identities in this run: `120`.
- Total staged raw identities across pages `1-16`: `320`.
- Total staged unique identities after cross-staging deduplication: `319`.
- Directly confirmed prior-catalog duplicates across staged pages: `3`.
- Unresolved staged identities requiring exhaustive historical reconciliation: `316`.
- Pages `11-16` staging commit: `14e5d601f861ccbde8464679f9d32d1f6e9a3e9c`.
- Latest-manifest staging-state commit: `1459ae4e459d65b6710c21540509a4b44d76c531`.
- `2088 + 414 = 2502`, matching the canonical eligible and held partitions.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
