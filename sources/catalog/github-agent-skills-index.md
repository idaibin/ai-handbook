# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1949`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1953`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1838`
- Exact duplicates removed across current inputs: `115`
- New unique repositories collected in this run: `20`
- Net catalog delta versus the previous verified manifest: `+20`
- Provisionally eligible for later deep analysis: `1429`
- Held as adjacent or unclear search hits: `409`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `1818`-repository canonical manifest with page `6` of the `agent skills registry` discovery query.

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

- `"agent skills registry" in:name,description`, pages `1-6` complete at `20` results per page; page `7` was probed and returned `20` repositories, so the next merge boundary is page `7`.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed page `6` at `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Duplicates against the prior verified catalog: `0`
- Added as new repositories: `20`
- Previous verified catalog: `1818`
- Updated composed catalog: `1838`
- Added to provisional deep-analysis queue: `19`
- Added to held-for-review: `1`

All 20 page-6 identities were compared directly against the persisted `agent-skills-registry` pages `1-5` and the earlier `skill-registry` pages `1-10` batch. Exact AI-handbook code search was also executed for each full `owner/repository` identity and returned no prior exact match. Recent current-query pages were compared directly because GitHub code-search indexing can lag recent writes.

The 20 new identities were provisionally classified only from repository identity and GitHub search context: `4 skill_collection`, `1 single_skill_or_domain_package`, `14 skill_tooling`, and `1 unclear_search_hit`. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, and verification notes are stored in [`batches/agent-skills-registry-page-6.json`](batches/agent-skills-registry-page-6.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 596 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 103 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 529 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 151 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 258 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `9703c4f0b159fa8c0aeb91139e6b4ecf2e0d8eb7` (`1818` repositories).
- `agent skills registry` page-6 batch commit: `765879411e3f615d034031e78faeb2b973ee2077`.
- Composed latest-manifest commit: `021bab3cf22813ab41d968c3e3f5fab832c5af7f`.
- `1818 + 20 = 1838` current unique repositories.
- `1953 - 115 = 1838` raw-to-unique reconciliation.
- Classification totals resolve to `1838`.
- `1429 + 409 = 1838`, matching the eligible and held partitions.
- Next index boundary: `"agent skills registry" in:name,description`, page `7`, `per_page=20`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
