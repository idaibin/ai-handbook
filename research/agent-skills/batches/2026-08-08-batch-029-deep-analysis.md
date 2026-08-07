# Agent Skills Deep Analysis — Batch 029

- Batch ID: `2026-08-08-batch-029`
- Stage: repository deep analysis
- Queue source: `sources/catalog/batches/agentskills-created-2026-03-30-deterministic.json`
- Repositories completed: **10**
- Direct `SKILL.md` bodies reviewed: **9**
- Individual skill reports added: **9**
- Runtime/build/test/eval execution: **not_executed**

## Completion gate

A repository is counted only after its GitHub identity and point-in-time star count were verified, an exact revision was pinned, and actual repository contents were read. Repository-search `stars:0` qualifiers were used to verify that all ten selected repositories had exactly zero stars at observation time. Metadata-only candidates are not accepted as complete.

Six repositories in this batch resolve to the same Git commit SHA and the same README blob. Because a Git commit is content-addressed and captures the repository tree, the shared revision is treated as strong full-tree duplicate evidence. The common specification/reference implementation was deeply reviewed once and applied to all six repository identities; no duplicate individual skill reports were generated for them.

## Repository results

| Repository | ID | Stars observed | Reviewed revision | Content-proven class | Skill reports | Result |
|---|---:|---:|---|---|---:|---|
| `OmarQV/agentskills` | `1195799142` | 0 | `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4` | Agent Skills specification/reference SDK snapshot | 0 | exact full-tree duplicate of the same specification/reference revision used by five other repositories |
| `LamVu22/agentskills` | `1196459379` | 0 | `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4` | Agent Skills specification/reference SDK snapshot | 0 | exact full-tree duplicate |
| `MAGArENKO/agentskills` | `1196624050` | 0 | `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4` | Agent Skills specification/reference SDK snapshot | 0 | exact full-tree duplicate |
| `Centaurioun/agentskills` | `1196677457` | 0 | `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4` | Agent Skills specification/reference SDK snapshot | 0 | exact full-tree duplicate |
| `duyvhh/agentskills` | `1195999182` | 0 | `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4` | Agent Skills specification/reference SDK snapshot | 0 | exact full-tree duplicate |
| `D4RK-777/agentskills-D4rk` | `1195711087` | 0 | `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4` | Agent Skills specification/reference SDK snapshot | 0 | exact full-tree duplicate |
| `carabase/carabase-claw-skills` | `1195769636` | 0 | `25581dcd481c3a46f62299231c59335fc169e648` | four-skill OpenClaw integration collection | 4 | four real AgentSkill templates for Carabase core/tasks/knowledge/daily workflows |
| `vstorm-co/pydantic-ai-skills` | `1196328175` | 0 | `308cd9339009761989ab85e080a1aaf4601ea1eb` | skill runtime/tooling + three example skills | 3 | Python Pydantic-AI integration with filesystem/programmatic skills, progressive disclosure and executable scripts |
| `rohan-tessl/Agentic-MCP-Skill` | `1196037426` | 0 | `7d7ebbed34aeb6fead9a7f3c1904e47b937567c1` | single skill + executable MCP tooling | 1 | socket-daemon MCP wrapper with a root `agentic-mcp` skill and three-layer caller-facing disclosure |
| `Aston1690/skill-authoring` | `1195779624` | 0 | `6af042bfc15e582f3a92338d22f7a62185a6d06f` | single skill package | 1 | authoring guidance with detailed references, but its advertised local validation commands point at absent package metadata |

## 1–6. Six exact Agent Skills specification/reference snapshots

The six `agentskills` repositories above expose the same commit SHA, `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4`, and the same README blob. The README states that the repository contains the Agent Skills specification, documentation, and reference SDK and points readers to a different repository for example skills. There are therefore no repository-owned example `SKILL.md` packages to report as independent skills at this revision.

### Specification structure

`docs/specification.mdx` defines the skill directory model: required `SKILL.md`, optional `scripts/`, `references/`, and `assets/`; YAML frontmatter; name/description constraints; progressive disclosure; relative file references; and validation via `skills-ref validate`.

The specification recommends keeping the main `SKILL.md` under 500 lines and below roughly 5,000 tokens, with detailed material moved to on-demand resources. This is a useful architectural pattern for context control because metadata, activation instructions, and resources are explicitly separated.

### Reference SDK

`skills-ref` is a Python 3.11+ demonstration/reference library using Click and StrictYAML. Its CLI supports `validate`, `read-properties`, and `to-prompt`. The package README explicitly warns that it is intended for demonstration rather than production use.

The validator checks required frontmatter, field allowlisting, name length, description length, compatibility length, lowercase naming, hyphen rules, and parent-directory/name matching. Tests cover valid and invalid names, unexpected fields, directory mismatches, lengths, and internationalized names.

### Source-level specification tension

The human-readable specification describes the `name` field in terms of lowercase `a-z`, digits, and hyphens. The reference validator instead uses Unicode-aware `isalnum()` and its test suite explicitly accepts Chinese and lowercase Russian names. This is a source-level contract tension between prose specification and validator behavior. It should be resolved by the upstream specification rather than silently normalized by catalog consumers.

### Assessment

These repositories are useful as snapshots of the Agent Skills format and its reference validator, but they are not six independent skill collections. The shared Git commit makes content deduplication deterministic. Tests were inspected as source evidence only; they were not executed in this batch.

## 7. `carabase/carabase-claw-skills`

### Structure

The repository currently contains four AgentSkill templates:

- `carabase-core`
- `carabase-tasks`
- `carabase-knowledge`
- `carabase-daily`

An earlier commit explicitly moved the Claude Desktop MCP server to a different repository, leaving this repository focused on OpenClaw AgentSkill templates. The README documents two required environment variables, `CARABASE_HOST` and `CARABASE_WORKSPACE_ID`, and maps skill versions to compatible Carabase host phases.

### Skill architecture

`carabase-core` provides health checks, connection setup, canonical MCP tool inventory and REST fallback guidance. `carabase-tasks` exposes create/list/toggle task workflows and documents the underlying TipTap task block structure. `carabase-daily` handles rendered daily-note reads and log-entry writes while warning that full-document PATCH operations require read/modify/write preservation. `carabase-knowledge` defines six canonical retrieval tools, entity resolution, metadata filtering, routing, FLARE-style hypothesis verification, Doctor-RAG hint repair, and lazy `carabase://artifact/{id}` resources.

The collection demonstrates useful progressive disclosure at two levels: task-specific skills separate domain workflows, and knowledge retrieval returns lazy artifact resource identifiers rather than eagerly embedding all document bodies.

### Risks and limits

The skills are tightly coupled to the Carabase host API, tool names and host phase/version. The templates therefore require synchronization with `carabase-host`; documentation drift is a material maintenance risk. Several workflows can write user workspace data, so correctness depends on the host's authorization and workspace scoping rather than on the skill text alone. No runtime host, MCP, REST or integration test was executed in this batch.

## 8. `vstorm-co/pydantic-ai-skills`

### Structure and runtime model

This repository is a Python library for integrating Agent Skills with Pydantic AI. The core `SkillsToolset` exposes four agent tools: `list_skills`, `load_skill`, `read_skill_resource`, and `run_skill_script`. It supports programmatic skills, filesystem directories, remote registries, automatic directory reload, and `exclude_tools` for capability restriction such as disabling script execution.

The system instruction template explicitly requires `load_skill` before resource reads or script execution, which is a strong progressive-disclosure and sequencing contract.

### Example skills reviewed

Three repository-owned examples were directly reviewed:

- `arxiv-search` — network-backed arXiv search with a Python script.
- `pydanticai-docs` — Pydantic AI framework documentation with on-demand reference files.
- `web-research` — methodology-only research guidance with no executable scripts.

The arXiv script uses `arxiv.Client`, relevance sorting, a result cap, and a required `--query` argument. It catches broad exceptions and converts failures to strings, which simplifies agent consumption but can hide structured failure categories.

### Tests and coupling

The test suite creates temporary sample skills covering discovery, resources, scripts and instruction generation. These tests were read but not executed. At the pinned revision, `toolset.py` imports Pydantic AI internal modules such as `_griffe` and `_run_context`; this creates compatibility risk across upstream releases. README branding and documentation links also reference the DougTrajano project identity, so this `vstorm-co` repository should be treated as a fork/upstream-derived runtime rather than assumed to be an independently maintained implementation without further provenance analysis.

## 9. `rohan-tessl/Agentic-MCP-Skill`

### Structure

The repository contains one root `agentic-mcp` skill plus a TypeScript/npm package (`@cablate/agentic-mcp`) and a long-running daemon. The skill directs an agent through metadata → tool list → tool schema → tool call steps. The package supports stdio, Streamable HTTP and SSE MCP transports and provides Vitest scripts.

The README explicitly calls the project an early experimental demo and says it is not recommended for production use. It also documents source-level test suites and reported coverage; those reported percentages were not independently reproduced in this batch.

### Progressive-disclosure finding

The caller-facing API does hide schemas until `schema` is requested. However, `ProgressiveMCPClient.connect()` immediately calls the upstream MCP server's `listTools()` and caches each tool's complete `inputSchema`. Therefore the implementation provides progressive disclosure to the agent-facing caller, but it does **not** avoid fetching the complete tool schema set from the MCP server during connection. Claims about reduced agent-context exposure are supported; claims about reduced MCP-server fetch/data transfer are not supported by this implementation path.

### Tests

The reviewed client test file exercises connection, metadata, tool-list, schema and tool calls using `@modelcontextprotocol/server-filesystem`. It also contains a hard-coded `C:/temp/mcp-test` test path, reducing portability. Test source presence is not treated as a passing test run.

## 10. `Aston1690/skill-authoring`

### Structure

This is a single `skill-authoring` package. Its root `SKILL.md` focuses on agentskills.io-compliant frontmatter, progressive disclosure, trigger wording, reference loading, token budgets and validation procedures. References include centralized token budgets and validation checklists for broken links, orphaned references, splitting, duplicates and misplaced guidance.

### Verified tooling contract defect

The skill instructs users to run:

```text
cd scripts
npm run references
npm run tokens -- check
```

At the pinned revision, both `scripts/package.json` and root `package.json` are absent. The advertised npm validation commands therefore have no repository-local package metadata from which to run as written. This is recorded as a source-level repository contract defect, not as an executed command failure.

The frontmatter self-declares `metadata.author: Microsoft`, but repository ownership is `Aston1690`. Catalog provenance should therefore retain that value as self-declared metadata rather than treating it as independently verified Microsoft authorship.

## Cross-batch findings

1. **Commit-level deduplication is high-value.** Six independent GitHub repository identities are exact content snapshots of the same specification/reference SDK revision. Repository identity and content identity must remain separate catalog fields.
2. **Specification and executable validator can diverge.** The shared Agent Skills revision contains a concrete name-character mismatch between prose rules and Unicode-aware validator/tests.
3. **Progressive-disclosure claims require source inspection.** `Agentic-MCP-Skill` progressively filters what the agent sees but eagerly fetches and caches complete upstream tool schemas on connect.
4. **Test/eval presence is not execution evidence.** Multiple repositories contain test code or validation guidance; this batch did not execute those suites.
5. **Documentation commands need existence checks.** `skill-authoring` advertises npm validation commands while the package metadata needed to run those commands is absent at the pinned revision.
6. **Large collections remain gated.** `irishdan/skills` was encountered and its README was inspected, but its large collection was not counted because all individual skills were not reviewed in this run.

## Validation status

- Repository identity: verified for all 10 selected repositories.
- Stars: exact point-in-time value `0` verified for all 10 using GitHub repository search qualifiers matched to repository identity.
- Exact revision: pinned for all 10.
- README/root documentation: read where present.
- `SKILL.md`/equivalent definitions: **9 bodies directly reviewed**.
- Scripts/references/tests: read where materially present, including the Agent Skills reference validator/tests, Carabase skill bodies, Pydantic AI runtime/tests/example scripts, Agentic MCP runtime/tests, and skill-authoring references.
- Runtime/build/tests/evals: **not_executed**. No source-only observation is promoted to runtime success.
