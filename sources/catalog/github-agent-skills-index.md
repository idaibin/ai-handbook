# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `2009`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `2013`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1897`
- Exact duplicates removed across current inputs: `116`
- New unique repositories collected in this run: `20`
- Net catalog delta versus the previous verified manifest: `+20`
- Provisionally eligible for later deep analysis: `1483`
- Held as adjacent or unclear search hits: `414`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `1877`-repository canonical manifest with page `9` of the `agent skills registry` discovery query.

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

- `"agent skills registry" in:name,description`, pages `1-9` complete at `20` results per page; page `10` was probed and returned `20` repositories, so the next merge boundary is page `10`.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed page `9` at `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Confirmed duplicates against the prior verified catalog: `0`
- Added as new repositories: `20`
- Previous verified catalog: `1877`
- Updated composed catalog: `1897`
- Added to provisional deep-analysis queue: `20`
- Added to held-for-review: `0`

All page-9 identities were directly compared against persisted `agent-skills-registry` pages `1-8`, plus directly inspected overlapping `skill-registry` pages `1-10`, `skill-hub` pages `1-10`, `agent-skills-hub` pages `1-2`, and `mcp-skills` pages `1-10` batch artifacts. No exact case-insensitive `owner/repository` identity was found in those persisted overlap sets.

Empty AI-handbook code-search results were not used as uniqueness proof because earlier runs demonstrated false negatives for known persisted identities.

The 20 new identities were provisionally classified only from repository identity and GitHub search context: `2 skill_collection` and `18 skill_tooling`. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, and verification notes are stored in [`batches/agent-skills-registry-page-9.json`](batches/agent-skills-registry-page-9.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 611 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 104 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 567 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 152 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 262 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `5c3fc57cfd8c5d9b1fc006dde306a08fc477c8dc` (`1877` repositories).
- `agent skills registry` page-9 batch commit: `b3ab373d93f1bf551bf1340bda267fa1390cd1e8`.
- Composed latest-manifest commit: `37a6ac658cf3eec3bf31c864aef1dc985bd68d5c`.
- `1877 + 20 = 1897` current unique repositories.
- `2013 - 116 = 1897` raw-to-unique reconciliation.
- Classification totals resolve to `1897`.
- `1483 + 414 = 1897`, matching the eligible and held partitions.
- Next index boundary: `"agent skills registry" in:name,description`, page `10`, `per_page=20`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
