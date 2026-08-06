# GitHub Agent Skills Repository Index — template pages 2-3

## Result

Query: `"agent skills template" in:name,description`

- Page 2: `20` repositories
- Page 3: `8` repositories
- Page 4: `0` repositories
- Query status: complete at `per_page=20`
- Raw identities this run: `28`
- Internal duplicates: `0`
- Exact prior-catalog duplicates found: `0`
- New unique repositories: `28`
- Previous composed catalog: `1637`
- Verified composed snapshot: `1665`
- Added to provisional deep-analysis queue: `14`
- Added to held-for-review: `14`

## Provisional classifications

- `skill_tooling`: `13`
- `awesome_index`: `1`
- `adjacent_search_hit`: `6`
- `unclear_search_hit`: `8`

Updated totals in the immutable composed snapshot:

- `specification`: `163`
- `skill_collection`: `490`
- `single_skill_or_domain_package`: `89`
- `awesome_index`: `37`
- `skill_tooling`: `490`
- `adjacent_search_hit`: `147`
- `unclear_search_hit`: `249`
- Deep-analysis eligible: `1269`
- Held for review: `396`

Reconciliation: `1637 + 28 = 1665`; `1767 - 102 = 1665`; `1269 + 396 = 1665`.

## Artifacts

- Batch: `sources/catalog/batches/agent-skills-template-pages-2-3.json`
- Immutable composed snapshot: `sources/catalog/snapshots/github-agent-skills-index-1665.json`

The canonical `sources/catalog/github-agent-skills-index-latest.json` update was attempted twice through GitHub's contents API using the blob SHA returned by a fresh fetch. Both writes returned HTTP `409` SHA mismatch while the fetched file continued to report blob `0cf88664b98a2d75773bd793291060ccc55ff3b9d`. To avoid an unsafe overwrite, this run persisted the verified composed state as an immutable snapshot instead of forcing the canonical file.

## Evidence boundary

Repository identities, GitHub IDs, default branches, sizes, archive flags, ordering, and search pagination were collected from GitHub repository search. All 28 exact `owner/repository` identities were checked against the current AI-handbook code-search snapshot and produced no prior exact match. Classification remains provisional from repository identity and search context only.

No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation code were read or analyzed in this run.
