# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1969`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1973`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1857`
- Exact duplicates removed across current inputs: `116`
- New unique repositories collected in this run: `19`
- Net catalog delta versus the previous verified manifest: `+19`
- Provisionally eligible for later deep analysis: `1446`
- Held as adjacent or unclear search hits: `411`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `1838`-repository canonical manifest with page `7` of the `agent skills registry` discovery query.

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

- `"agent skills registry" in:name,description`, pages `1-7` complete at `20` results per page; page `8` was probed and returned `20` repositories, so the next merge boundary is page `8`.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed page `7` at `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Confirmed duplicates against the prior verified catalog: `1`
- Added as new repositories: `19`
- Previous verified catalog: `1838`
- Updated composed catalog: `1857`
- Added to provisional deep-analysis queue: `17`
- Added to held-for-review: `2`

All page-7 identities were compared directly against persisted `agent-skills-registry` pages `1-6`. `mur-run/skill-registry` was confirmed in the earlier `skill-registry` pages `1-10` batch and was therefore not added again. Additional overlapping historical batch artifacts inspected in this run included the initial `agent skills` index, `agent skill`, `agent skills hub`, `skill hub`, `skill marketplace`, `agent skills marketplace`, `agent skills directory`, and `agent skills examples`; no other page-7 exact identity was found.

AI-handbook code search was attempted for all 20 full identities, but it returned an empty result even for the known `mur-run/skill-registry` duplicate. Therefore empty code-search results were explicitly not used as proof of uniqueness in this run.

The 19 new identities were provisionally classified only from repository identity and GitHub search context: `9 skill_collection`, `8 skill_tooling`, `1 adjacent_search_hit`, and `1 unclear_search_hit`. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, and verification notes are stored in [`batches/agent-skills-registry-page-7.json`](batches/agent-skills-registry-page-7.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 605 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 103 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 537 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 152 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 259 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `021bab3cf22813ab41d968c3e3f5fab832c5af7f` (`1838` repositories).
- `agent skills registry` page-7 batch commit: `26c827f7d9a18aef3e29a845a1615fc22ab9ebf3`.
- Composed latest-manifest commit: `abf814fecb382bdaef545e805339106602089d32`.
- `1838 + 19 = 1857` current unique repositories.
- `1973 - 116 = 1857` raw-to-unique reconciliation.
- Classification totals resolve to `1857`.
- `1446 + 411 = 1857`, matching the eligible and held partitions.
- Next index boundary: `"agent skills registry" in:name,description`, page `8`, `per_page=20`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
