# Agent Skills Deep Analysis — Batch 050

- Observed: 2026-08-09
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Selection: continued the existing indexed queue from Batch 049; only repositories that passed live GitHub identity/stars verification plus pinned-revision content gates are counted.
- Completion count: **10 qualified repository identities**
- Runtime boundary: **repository scripts/builds/tests/evals were not executed**.
- Historical cross-repository canonical reconciliation: **pending**.

## Batch metrics

| Metric | Result |
|---|---:|
| Qualified repositories completed | 10 |
| Conventional root README direct reads | 9 |
| Repositories with root documentation directly read | 10 |
| `SKILL.md` direct reads | 14 |
| Unique directly reviewed Skill bodies | 12 |
| Unique Git trees | 8 |
| New repository-scoped individual Skill reports | 9 |
| Cumulative repositories structure-reviewed | 500 |
| Cumulative repository-scoped Skill reports | 3026 |
| Arithmetic remaining from frozen 2088 basis | 1588 |

`Scoheart/agentskills` has no conventional root `README.md` at the pinned revision. Its root tree, `CLAUDE.md`, `skills-lock.json`, and representative Skill were directly inspected instead; it is therefore not falsely counted as a README read.

## Repository evidence table

| Repository | Stars observed | Pinned revision | Git tree | Direct content gate | Report action |
|---|---:|---|---|---|---|
| `stjordanis/Anthropic-Cybersecurity-Skills` | 0 | `673da1f3b0b7be34ffc9624ef3858fe45f1c3bed` | `a1043e71a823ad56c8b7186b8517e8319a61b060` | README, validation CI, representative defensive compliance `SKILL.md`, its `scripts/process.py`, directory references/assets | 1 new report |
| `Thomas-Busch-Waterloo/Anthropic-Cybersecurity-Skills` | 0 | `efbbbba5e233089f8a95b722a6327ce9ae831246` | `822878aa68d8a760149ce36542eb41c7aee429db` | README + representative defensive API-log analysis `SKILL.md` | exact-tree reuse; 0 new reports |
| `peacebaba/Anthropic-Cybersecurity-Skills` | 0 | `efbbbba5e233089f8a95b722a6327ce9ae831246` | `822878aa68d8a760149ce36542eb41c7aee429db` | README + same representative `SKILL.md` body | exact-tree reuse; 0 new reports |
| `Scoheart/agentskills` | 2 | `82fe3f694b9f46af043292def6b769654f0b2a05` | `ab771df49054e31e7b5ec56762908a692e933e40` | root tree, `CLAUDE.md`, `skills-lock.json`, representative `skills/tool/git-commit/SKILL.md` | 1 new report |
| `desaiuditd/skills` | 0 | `47109e81a74fe1b5675cfe1239246ecd59b41335` | `2a9b0bbefe9315980401e609dd696ffaa2a243b2` | README + complete `git-commit-message/SKILL.md` | 1 new report |
| `juicyjusung/juicy-skills` | 0 | `4be83edc06f1ecad686eb883257269440120c196` | `211432bd532e84c57a5018dec127f617bcefdce1` | README + all 5 `SKILL.md` bodies + representative TypeScript market-data client + script/reference inventory | 5 new reports |
| `mihado/wondelai-skills` | 0 | `66de348733ec508b3b8c81717333dbc2ca9f4cf0` | `8950e3a34d2e8ed923f903530d462890e7f62e09` | README + `clean-architecture/SKILL.md` + required boundary/SOLID reference material and reference inventory | 1 new report |
| `ClaudiousAI/jobsTobeDone-skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + representative `clean-architecture/SKILL.md` | previously reviewed exact tree; 0 new reports |
| `lobosan/skills` | 0 | `7c71a845071e8f994253db0d26c7e36fa90e2b5e` | `33a909b3c9ece5dd8e1524796c7ca60d8e8be1f3` | README + representative `37signals-way/SKILL.md` | previously reviewed exact tree; 0 new reports |
| `doveydragon/skills` | 0 | `7c71a845071e8f994253db0d26c7e36fa90e2b5e` | `33a909b3c9ece5dd8e1524796c7ca60d8e8be1f3` | README + same representative `37signals-way/SKILL.md` | exact-tree reuse; 0 new reports |

## Findings

### 1. Cybersecurity collection drift is now measurable at the content level

`stjordanis/Anthropic-Cybersecurity-Skills` is not the old 754-Skill snapshot. Its current README presents **817 Skills / 29 domains / 6 frameworks**, while a later section still says **754/754 skills mapped** and refers to five frameworks. A representative compliance Skill also has frontmatter version `2.0` while its body identifies `1.0.0`. These are repository-internal documentation/version drifts, not metadata guesses.

The repository does have real validation CI: it checks skill structure/frontmatter, Python syntax, index/count consistency, YAML and link/statistics conditions. That is useful deterministic conformance coverage, but it is **not a behavioral eval** of whether an agent selects and follows the Skills correctly. A representative `scripts/process.py` is a generic argument/input/output processor with relatively shallow domain logic, so the README's broad production-ready posture should not be generalized to every individual automation without execution evidence.

The two old-snapshot Cybersecurity identities were independently content-gated before being mapped to the exact same `822878aa...` tree. Repository identity alone was not used as a completion or deduplication shortcut.

### 2. `Scoheart/agentskills` separates catalog mechanics from explicit Git side-effect rules

The repository is a real Skill collection with a lockfile/import catalog, plugin metadata, install material, hooks/scripts, and categorized Skills. Its `git-commit` Skill explicitly checks repository/branch state, limits staging to approved files, and warns against destructive Git operations, bypassing hooks, or unsafe pushes. This is a reusable pattern: **side effects should be explicit steps with safety constraints, not an implicit consequence of routing into a Skill**.

The pinned root has no conventional `README.md`; root operational documentation is instead represented by `CLAUDE.md` plus the lock/catalog files. That absence is recorded rather than silently treated as a successful README read.

### 3. `desaiuditd/skills` provides a narrow, low-side-effect commit-message boundary

`git-commit-message` derives facts from the staged diff, but asks for missing motivation instead of inventing the WHY. It writes a proposed message to `.git/COMMIT_EDITMSG` and intentionally does **not** run `git commit`. The useful abstraction is the separation between **artifact generation** and **external side effect**, with unresolved intent escalated to the user rather than guessed.

### 4. `juicyjusung/juicy-skills` has README inventory drift but useful execution boundaries

The root README lists four Skills, while the pinned tree contains five: `kr-daytrade`, `kr-market`, `persuade`, `stock-research`, and `us-market`. All five Skill bodies were directly read.

For the market-related Skills, the strongest reusable pattern is not any investment heuristic; it is the permission/provenance boundary. The market-data Skills explicitly remain read-only and exclude order placement/account access, while the research Skill requires numerical claims to carry source/time context and prioritizes official filings. A representative TypeScript client uses credential loading, a local token cache with restrictive file permissions, explicit API error handling, and bounded retry delays. No live market API was invoked in this review.

### 5. `mihado/wondelai-skills` is a distinct Clean Architecture revision with progressive references

The directly reviewed `clean-architecture` Skill is a distinct body from the previously reviewed Wondel snapshots. It routes architectural work through dependency direction, boundary placement and SOLID-level reasoning, then requires deeper reference material for boundary anatomy and SOLID principles. This is a good example of progressive disclosure: the routing/operating contract remains in `SKILL.md`, while long-form design doctrine lives in references.

The main gap is verification: the Skill provides substantial methodology and examples but no repository-local behavioral harness was executed here to demonstrate that an agent consistently applies the boundary rules to real code changes.

### 6. Exact-tree reuse continues to prevent duplicate individual reports

`Thomas-Busch-Waterloo/...` and `peacebaba/...` share the already-seen Cybersecurity tree. `ClaudiousAI/jobsTobeDone-skills` maps to a previously reviewed Wondel tree. `lobosan/skills` and `doveydragon/skills` share another previously reviewed Wondel tree. Each repository identity still passed a direct content gate first; only then was exact-tree/body reuse used to avoid generating duplicate Skill reports.

## Validation boundary

Verified in this batch:

- live repository identity and observed Stars;
- pinned commit/tree identity;
- repository documentation/structure;
- 14 actual `SKILL.md` reads representing 12 unique bodies;
- representative scripts, references and validation workflow where present;
- exact-tree equivalence before suppressing duplicate reports.

Not verified in this batch:

- runtime correctness of repository scripts;
- builds or package installation;
- tests/evals execution or pass rates;
- browser/UI behavior;
- live external API behavior;
- historical cross-repository canonical reconciliation.

Therefore Batch 050 is **structure/content reviewed**, not runtime validated.

## Queue continuation

Next unresolved qualified identity: `Player1Taco/morpheus-skill`.

The `1588` remaining value is only arithmetic continuation from the frozen `2088` eligible basis (`2088 - 500`). It is **not** the final canonical-deduplicated repository count.