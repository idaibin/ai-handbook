# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1929`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1933`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1818`
- Exact duplicates removed across current inputs: `115`
- New unique repositories collected in this run: `20`
- Net catalog delta versus the previous verified manifest: `+20`
- Provisionally eligible for later deep analysis: `1410`
- Held as adjacent or unclear search hits: `408`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `1798`-repository canonical manifest with page `5` of the `agent skills registry` discovery query.

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

## In-progress search coverage

- `"agent skills registry" in:name,description`, pages `1-5` complete at `20` results per page; page `6` was probed and returned `20` repositories, so the next merge boundary is page `6`.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed page `5` at `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Duplicates against the prior verified catalog: `0`
- Added as new repositories: `20`
- Previous verified catalog: `1798`
- Updated composed catalog: `1818`
- Added to provisional deep-analysis queue: `20`
- Added to held-for-review: `0`

All 20 page-5 identities were compared directly against the persisted `agent-skills-registry` pages `1-4` and the earlier `skill-registry` pages `1-10` batch. Exact AI-handbook code search was also executed for each full `owner/repository` identity and returned no prior exact match. Recent current-query pages were compared directly because GitHub code-search indexing can lag recent writes.

The 20 new identities were provisionally classified only from repository identity and GitHub search context: `3 skill_collection` and `17 skill_tooling`. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, and verification notes are stored in [`batches/agent-skills-registry-page-5.json`](batches/agent-skills-registry-page-5.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 592 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 102 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 515 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 151 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 257 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `75b6627d2446f2a79f1950c441bc24a425df2d2a` (`1798` repositories).
- `agent skills registry` page-5 batch commit: `ecef0e2d10027bfa3a70a69d11efe2d1e4bffd51`.
- Composed latest-manifest commit: `9703c4f0b159fa8c0aeb91139e6b4ecf2e0d8eb7`.
- `1798 + 20 = 1818` current unique repositories.
- `1933 - 115 = 1818` raw-to-unique reconciliation.
- Classification totals resolve to `1818`.
- `1410 + 408 = 1818`, matching the eligible and held partitions.
- Next index boundary: `"agent skills registry" in:name,description`, page `6`, `per_page=20`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
