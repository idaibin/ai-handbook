# Agent Skills Individual Reports — Batch 029

- Batch ID: `2026-08-08-batch-029`
- Individual repository-scoped skill reports: **9**
- Runtime/build/test/eval execution: **not_executed**

The six exact Agent Skills specification/reference SDK snapshots in this batch contain no repository-owned example skill packages at the pinned revision, so they intentionally produce zero individual skill reports.

## 1. `carabase-core`

- Repository: `carabase/carabase-claw-skills`
- Revision: `25581dcd481c3a46f62299231c59335fc169e648`
- Skill version: `2.1.0`
- Type: integration/router skill

### Purpose

Establish and verify a Carabase connection, explain required environment variables, inventory the canonical MCP tools, and route users toward the more specialized tasks/daily/knowledge skills. MCP is the preferred interface and REST is the documented fallback.

### Structure and dependencies

The skill requires `CARABASE_HOST` and `CARABASE_WORKSPACE_ID`. It documents health checking, SSE MCP configuration, task/daily/knowledge tool inventories and fallback REST endpoints. It functions as the collection's navigation and compatibility layer rather than implementing host behavior itself.

### Assessment

The skill has a clear responsibility boundary and gives agents a deterministic tool-selection table. The main risk is API/version coupling: the documented surface must stay synchronized with `carabase-host`. The tool inventory includes write-capable operations, so actual authorization and workspace isolation must be enforced by the host. No live Carabase connection was exercised in this review.

## 2. `carabase-tasks`

- Repository: `carabase/carabase-claw-skills`
- Revision: `25581dcd481c3a46f62299231c59335fc169e648`
- Skill version: `2.0.0`
- Type: task-management integration skill

### Purpose

Create, list, filter and toggle tasks through MCP, with REST fallback. The skill explains that tasks are embedded in TipTap/ProseMirror daily-note structures rather than stored in a standalone task table.

### Design

The primary tools are `create_task`, `list_tasks`, and `toggle_task`. The skill documents composite task IDs, date/filter parameters and the underlying `logCard > taskList > taskItem` structure. It also provides manual block construction for advanced fallback scenarios.

### Assessment

The normal path is simple and host-mediated, while lower-level document construction is isolated as advanced behavior. Composite IDs based on date and node position create a potential stability concern if document edits reorder nodes; whether the host protects against stale IDs requires runtime validation. No MCP or REST operation was executed in this batch.

## 3. `carabase-knowledge`

- Repository: `carabase/carabase-claw-skills`
- Revision: `25581dcd481c3a46f62299231c59335fc169e648`
- Skill version: `2.1.0`
- Type: retrieval/knowledge-management integration skill

### Purpose

Provide six canonical retrieval paths: semantic search, graph traversal, entity candidate resolution, metadata filtering, natural-language routing and hypothesis verification. It also covers folios, artifacts and memories.

### Progressive disclosure

Search results can return lazy `carabase://artifact/{id}` resources instead of embedding complete artifact bodies. The agent reads a body only when needed. This is a concrete progressive-disclosure mechanism that can reduce context use for broad discovery queries.

### Recovery and verification

The skill teaches Doctor-RAG `[hint:]` / `[trace:]` repair behavior and a FLARE-style `carabase_verify_hypothesis` workflow with `corroborated`, `contradicted`, `mixed`, or `inconclusive` verdicts. This gives agents explicit branches instead of encouraging unsupported certainty.

### Assessment

The routing/recovery design is strong, but the skill's correctness depends almost entirely on the corresponding Carabase host implementation. Host-version drift is therefore its main maintenance risk. No retrieval quality, hypothesis-verification accuracy or host integration was executed in this batch.

## 4. `carabase-daily`

- Repository: `carabase/carabase-claw-skills`
- Revision: `25581dcd481c3a46f62299231c59335fc169e648`
- Skill version: `2.0.0`
- Type: daily-note integration skill

### Purpose

Read rendered daily notes and write timestamped log entries through MCP, with raw TipTap/ProseMirror REST fallbacks for advanced operations.

### Safety-relevant data handling

The skill explicitly warns that full-document `PATCH` must first read the current state and preserve existing blocks; replacing the document with only new content would delete prior entries. It also documents an append-style injection endpoint as a safer path for simple additions.

### Assessment

The distinction between append and replace semantics is valuable and reduces accidental data loss when followed. The remaining risk is that the skill documents mutable structured data contracts that may change with the host. No actual document mutation was performed in this review.

## 5. `arxiv-search`

- Repository: `vstorm-co/pydantic-ai-skills`
- Revision: `308cd9339009761989ab85e080a1aaf4601ea1eb`
- Type: executable research skill
- Compatibility: Python environment with `arxiv` package and network access

### Purpose

Search arXiv for papers and return title, abstract/summary and entry URL. The skill is designed as an example of a script-backed Agent Skill.

### Script implementation

`arxiv_search.py` uses `argparse`, requires `--query`, supports `--max-papers`, creates an `arxiv.Client`, and sorts results by relevance. The script imports `arxiv` with an explicit dependency error and converts query-time exceptions into formatted error strings.

### Assessment

The implementation is small and understandable. Broad exception-to-string conversion is convenient for an agent but loses structured failure semantics. Results are relevance-sorted rather than guaranteed newest-first, so callers should not interpret the output as a chronological "latest papers" feed unless they change the sorting behavior. Network execution was not performed.

## 6. `pydanticai-docs`

- Repository: `vstorm-co/pydantic-ai-skills`
- Revision: `308cd9339009761989ab85e080a1aaf4601ea1eb`
- Skill metadata version: `1.0`
- Type: documentation/reference skill

### Purpose

Route Pydantic AI questions to a concise activation document and load targeted references for Agent APIs, tools, dependency injection, structured output, models, MCP and other framework topics.

### Progressive disclosure

The root skill provides core examples and routes deeper questions to named reference documents such as `references/AGENT.md`. This is a conventional and effective split between activation context and detailed API material.

### Assessment

The skill is framework-version-sensitive. API examples and reference material can become stale as Pydantic AI evolves. The repository's own runtime code at the pinned revision imports internal Pydantic AI modules, reinforcing the need for version-aware validation. No documentation examples or Pydantic AI runtime calls were executed.

## 7. `web-research`

- Repository: `vstorm-co/pydantic-ai-skills`
- Revision: `308cd9339009761989ab85e080a1aaf4601ea1eb`
- Type: methodology-only skill

### Purpose

Provide a planning → information gathering → synthesis workflow for multi-source web research. It recommends bounded subtopics, a limited number of searches per subtopic, synthesis and source citation.

### Structure

The skill explicitly states that it contains no executable scripts or tools beyond those already available to the agent. Its value is behavioral guidance rather than implementation.

### Assessment

The bounded-search guidance can reduce open-ended research loops, but fixed heuristics such as "3–5 searches per subtopic" are not a substitute for evidence-completeness criteria. There is no repository-local eval demonstrating research quality at this revision.

## 8. `agentic-mcp`

- Repository: `rohan-tessl/Agentic-MCP-Skill`
- Revision: `7d7ebbed34aeb6fead9a7f3c1904e47b937567c1`
- Package version: `@cablate/agentic-mcp` `0.2.4`
- Type: executable MCP integration skill

### Purpose

Use a socket-based daemon to interact with configured MCP servers through four stages: metadata, tool list, selected tool schema and tool invocation.

### Implementation

The TypeScript package wraps the official MCP SDK and supports stdio, Streamable HTTP and SSE transports. The caller API exposes metadata without schemas, a tool list without schemas, and complete schemas only for requested tools.

### Verified progressive-disclosure limitation

On connection, `ProgressiveMCPClient.connect()` calls the MCP server's `listTools()` and caches each tool's full `inputSchema`. Therefore progressive disclosure is real at the **agent-facing presentation layer**, but the implementation still fetches the complete tool-schema set from the MCP server at connection time. Any stronger claim that it avoids upstream schema fetching is not supported by the reviewed source.

### Tests

Vitest source covers connection, metadata, tool-list, schema lookup and tool invocation with the filesystem MCP server. One fixture uses the hard-coded path `C:/temp/mcp-test`, which makes the suite less portable. The tests were not executed in this batch.

## 9. `skill-authoring`

- Repository: `Aston1690/skill-authoring`
- Revision: `6af042bfc15e582f3a92338d22f7a62185a6d06f`
- Self-declared metadata version: `1.0.0`
- Self-declared metadata author: `Microsoft`
- Type: skill-authoring guidance

### Purpose

Teach agents how to write and review Agent Skills: frontmatter rules, trigger descriptions, progressive disclosure, reference loading, token budgets and pre-submission validation.

### References

The reviewed token-budget reference defines soft/hard limits for `SKILL.md`, references and docs. The validation reference calls for checking broken links, orphaned references, oversized references, duplicate content and misplaced guidance.

### Verified contract defect

The root skill directs users to `cd scripts` and run `npm run references` plus `npm run tokens -- check`. At this exact revision, `scripts/package.json` and root `package.json` are absent. The advertised repository-local validation commands therefore cannot be resolved from npm package metadata as written.

### Provenance caution

`metadata.author: Microsoft` is self-declared frontmatter inside a repository owned by `Aston1690`. It is retained as declared metadata, not independently verified organizational authorship.

### Assessment

The conceptual validation checklist is useful, but the missing package metadata makes the automated-validation section incomplete at this revision. No validation command was executed.

## Batch validation note

These reports distinguish source inspection from runtime evidence. Repository contents, scripts, references and tests were inspected where available; **no build, test, network integration, MCP server, REST host or evaluation suite was executed**, so no passing runtime status is claimed.
