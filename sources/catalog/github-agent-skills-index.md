# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `2369`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `2373`
- Unique repositories after case-insensitive `owner/repository` deduplication: `2241`
- Exact duplicates removed across current inputs: `132`
- New unique repositories collected in this run: `20`
- Net catalog delta versus the previous verified manifest: `+20`
- Provisionally eligible for later deep analysis: `1827`
- Held as adjacent or unclear search hits: `414`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `2221`-repository canonical manifest with page `27` of the `agent skills registry` discovery query.

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

- `"agent skills registry" in:name,description`, pages `1-27` processed at `20` results per page; page `28` was probed and returned `20` repositories, so the next merge boundary is page `28`.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed page `27` at `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Confirmed duplicates in directly inspected prior sets: `0`
- Added as new repositories: `20`
- Previous verified catalog: `2221`
- Updated composed catalog: `2241`
- Added to provisional deep-analysis queue: `20`
- Added to held-for-review: `0`

Page-27 identities were directly compared against persisted adjacent `agent-skills-registry` pages `23-26` and the full persisted `skill-hub` pages `1-10`, `agent-skills-hub` pages `1-2`, and `skill-registry` pages `1-10` high-overlap artifacts. No exact case-insensitive `owner/repository` duplicate was found in those directly inspected sets. Earlier catalog coverage is inherited through the verified `2221`-repository canonical manifest. AI-handbook code-search emptiness was not used as uniqueness evidence.

All 20 raw page-27 results were provisionally classified from repository identity and GitHub search context as `skill_tooling`; all 20 were added to the provisional deep-analysis queue. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, duplicate status, and verification notes are stored in [`batches/agent-skills-registry-page-27.json`](batches/agent-skills-registry-page-27.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 611 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 104 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 911 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 152 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 262 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `6c83610c29370a21c44a72f9a909a671f8195b3b` (`2221` repositories).
- `agent skills registry` page-27 batch commit: `93bfb4ef2b13b25be149fa547980b646698dfc66`.
- Composed latest-manifest commit: `e01262b24aaf1e89e201e9f4ea65c48ea2b1c9b0`.
- `2221 + 20 = 2241` current unique repositories.
- `2373 - 132 = 2241` raw-to-unique reconciliation.
- Classification totals resolve to `2241`.
- `1827 + 414 = 2241`, matching the eligible and held partitions.
- Next index boundary: `"agent skills registry" in:name,description`, page `28`, `per_page=20`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
