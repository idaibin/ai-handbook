# Agent Skills Deep Analysis — Batch 022

Observed: 2026-08-07

Status: `structure-reviewed`

Runtime validation: `not_executed`

## Scope

This batch completed content-level review of **10 repositories** selected from the existing persisted GitHub Agent Skills indexed queue. Repository identity and current GitHub star counts were verified before content review. Actual repository files were then read: README, `SKILL.md` or equivalent local skill definitions, implementation/scripts, references, tests/eval surfaces when available.

A repository is counted as complete for this batch only after content evidence was read. Metadata-only evidence is insufficient.

## Batch summary

| Repository | Stars observed | Content-level classification | Local Skill reports |
|---|---:|---|---:|
| `gepeiyu/agentskills-proxy` | 16 | `skill_tooling_with_demo_skill` | 1 |
| `RisorseArtificiali/agent-ready-skill` | 4 | `skill_collection_readiness_assessment` | 6 |
| `cablate/Agentic-MCP-Skill` | 39 | `single_skill_experimental_mcp_tooling` | 1 |
| `octolens/skill` | 3 | `single_skill_external_service_adapter` | 1 |
| `agentskill-sh/mcp-server` | 3 | `skill_tooling_registry_mcp_server` | 0 |
| `OthmanAdi/codebase-knowledge-builder` | 17 | `single_skill_repository_research_documentation` | 1 |
| `valence-works/agentskillsdotnet` | 4 | `skill_specification_sdk_tooling_dotnet` | 0 |
| `black-forest-labs/skills` | 95 | `skill_collection_image_generation_api_guidance` | 2 |
| `Tencent/SkillHone` | 109 | `skill_collection_skill_optimization_harness` | 6 |
| `truefoundry/skills` | 13 | `skill_collection_gateway_platform_operations` | 9 |
| **Total** | — | — | **27** |

All **27 reported `SKILL.md` bodies were directly read** in this run.

## Queue provenance

The persisted staging batch `sources/catalog/batches/agentskills-pages-4-6.json` contains all ten selected identities. This batch uses that existing queue; it does not substitute a fresh metadata search for queue state.

## Repository analyses

### 1. `gepeiyu/agentskills-proxy`

**Verified**

- Repository is TypeScript tooling for exposing Agent Skills through remote gRPC/HTTP surfaces.
- `package.json` defines TypeScript build/start/dev commands and depends on gRPC, Express, Chokidar, VM2, YAML, logging, and related runtime packages.
- `skills/example-skill/SKILL.md` is a local demonstration skill.
- Directly read demo JavaScript and Python scripts show two execution paths and artifact writing.

**Inference**

- The bundled skill is best treated as a contract/demo fixture for proxy behavior, not evidence that the repository is a domain skill collection.

**Not verified**

- Proxy server startup, sandbox isolation, gRPC/HTTP behavior, artifact transport, and demo-script execution were not run.

### 2. `RisorseArtificiali/agent-ready-skill`

**Verified**

- Six local skills were directly read: `agent-ready`, `agent-ready-scan`, `agent-ready-fix`, `agent-ready-report`, `agent-ready-diff`, and `agent-ready-init`.
- `skills/agent-ready/references/scoring.md` declares the canonical v2 readiness model: seven weighted dimensions totaling 100, portable/target-specific layers, sub-criteria, helper-script signals, and a persisted JSON output schema.
- `skills/agent-ready/references/remediation.md` is a canonical remediation registry keyed by the same sub-criterion identifiers and separates `skill`, `partial`, and `manual` fixes.
- Representative `repo_map.py` is documented and implemented as read-only analysis: Python AST parsing without importing target code, with lower-confidence regex extraction for other languages.
- Scan/report/fix/diff/init responsibilities are separated; mutation workflows include explicit confirmation/change gates.

**Inference**

- The strongest reusable design is not the particular score weights but the contract architecture: one rubric authority, one remediation registry, persisted score schema, and consumers that do not silently re-score.

**Not verified**

- No readiness scan, fixer, report renderer, diff, init workflow, or helper script was executed.

### 3. `cablate/Agentic-MCP-Skill`

**Verified**

- Repository explicitly presents itself as experimental/early tooling rather than production-ready infrastructure.
- `SKILL.md` and implementation describe three-stage MCP progressive disclosure: server metadata, schema-light tool list, and individual tool schemas on demand.
- `package.json` defines TypeScript build, ESLint, Vitest, and coverage commands.
- `tests/unit/client.test.ts` directly exercises connection state, metadata, schema-free tool listing, on-demand schema retrieval, error paths, and a tool call against a filesystem MCP server.

**Inference**

- The notable reusable pattern is that progressive disclosure is expressed as a testable API contract instead of only prompt prose.

**Not verified**

- Vitest/coverage were not run. Any README test-count or coverage percentages remain repository claims, not runtime evidence from this batch.

### 4. `octolens/skill`

**Verified**

- One local `SKILL.md` was directly read.
- The skill treats MCP as the preferred operation surface and keeps a REST fallback/reference.
- `references/REST-API.md` contains a detailed v2 endpoint contract including auth scopes, filters, pagination, resource shapes, analytics/organization surfaces, and error codes; it also points to the service OpenAPI endpoint as machine-readable authority.

**Inference**

- This is a strong example of progressive disclosure for external-service skills: common operations in `SKILL.md`, exhaustive contract detail in a reference.

**Not verified**

- No Octolens MCP/REST call, live OpenAPI fetch, authentication, or service behavior was executed.

### 5. `agentskill-sh/mcp-server`

**Verified**

- Repository is TypeScript MCP tooling for search/discovery/installation against the agentskill.sh catalog.
- `src/index.ts` directly defines MCP tools such as skill search/detail access and maps many agent platforms to skill directories.
- Returned catalog metadata includes external skill contents and security/quality fields.
- No repository-local user-facing Agent Skill bundle was found in the reviewed implementation surfaces.

**Content-level correction**

- Classify as **registry MCP tooling**, not as a local Skill collection. Externally retrieved catalog Skills are not counted as repository-scoped reports.

**Not verified**

- MCP server startup, agentskill.sh API access, search/install actions, and filesystem writes were not executed.

### 6. `OthmanAdi/codebase-knowledge-builder`

**Verified**

- One local skill was directly read.
- Supporting references define reconnaissance and dependency-order deep reading.
- Methodology requires happy-path, error-path, and edge-case tracing and asks the analyst to persist notes every few files instead of relying on context memory.
- The final knowledge artifact template requires architecture, component paths, control/data flow, functions, configuration, gotchas, extension points, and a Mermaid flow.

**Inference**

- The durable pattern is a read-first/write-later research protocol with an explicit artifact contract; this is useful for repository research because it makes evidence locations part of the deliverable.

**Not verified**

- The skill was not applied to a new target repository during this batch.

### 7. `valence-works/agentskillsdotnet`

**Verified**

- Repository is a .NET implementation/tooling surface for the Agent Skills specification, with loader, validation, prompts, fixtures, docs, and tests.
- Security documentation explicitly treats skill scripts as data by default: no implicit execution, no core network fetches, advisory `allowed-tools`, diagnostics for normal validation errors, and host-owned sandbox/tool/content policy.
- Fixtures cover valid/minimal/complete examples plus malformed/invalid cases and are documented as test/example fixtures.
- Actual validator source and unit/performance/progressive-disclosure test files exist.

**Content-level correction**

- Classify as **specification/SDK tooling**, with **0 repository-scoped production Skill reports**. Fixture/example skills are test inputs and are not counted as catalog capabilities.

**Not verified**

- .NET build, validator tests, performance tests, progressive-disclosure tests, and host security guarantees were not executed in this run.

### 8. `black-forest-labs/skills`

**Verified**

- Official repository contains two directly reviewed local skills: `flux-best-practices` and `bfl-api`.
- `flux-best-practices` keeps a compact routing/quick-reference body and pushes detailed model/workflow guidance into `rules/` references.
- `bfl-api` separately covers API integration concerns and links to deeper endpoint/auth/polling/error/webhook/code references.
- Representative model-selection reference was directly read.

**Inference**

- The valuable split is responsibility-based: **how to construct/use FLUX prompts and model workflows** vs **how to integrate the API transport/runtime**. This reduces duplicated policy and makes each Skill easier to load selectively.

**Not verified**

- No model/API call or image generation was executed. Pricing, model behavior, and performance claims in repository documentation were not independently benchmarked here.

### 9. `Tencent/SkillHone`

**Verified**

- Six directly reviewed local skills: `skillhone`, `skillhone-optimization`, `skillhone-evaluation`, `skillhone-prd`, `skillhone-synthesis`, and `forgejo`.
- The architecture distinguishes a public Skill repo from a private eval repo, isolated per-item solver workdirs, and redacted observation evidence.
- `references/evaluation.md` defines line-delimited eval items with `question` and executable verification that produces mechanical score keys, plus solver trajectory evidence.
- `scripts/eval.py` was directly read: it supports `skill`, `seed`, and `direct` modes, split selection, seed worktree checkout, output parsing, and cleanup.
- Evaluation separates iterative probe/PR-validation signals from held-out final test measurement.
- Optimization directs diagnosis toward the actual failed layer—skill instructions, solver/tool execution, infrastructure, compiler/validator, or verifier—rather than treating every score loss as a prompt failure.
- PRD artifacts are split so the improver does not receive the full evaluation rubric; synthesis aims for closed-form, mechanically verifiable eval data; Forgejo access is isolated behind a VCS backend skill.

**Inference**

- The most reusable pattern is **private measurement contract + public behavior under test + isolated execution traces + redacted improvement evidence + regression-aware iteration**.

**Not verified**

- No Forgejo instance, solver agent, synthesis job, eval runner, optimizer, PR flow, or private benchmark was executed.

### 10. `truefoundry/skills`

**Verified**

- Nine local skill bodies were directly read: onboarding, gateway, gateway integration/migration, observability, platform/access, MCP server registry, prompt registry, agent UI workflow, and Skills Registry.
- Shared material is centralized under `skills/_shared`; the pack uses shared references/scripts to reduce duplication.
- Root `scripts/validate-skills.sh` checks frontmatter delimiters, required metadata, name-to-directory convention, `allowed-tools` formatting, shared symlink integrity/content, installer coverage, and CLI-reference consistency.
- Skills are separated by product responsibility rather than being one large operational document.
- Multiple mutating flows use preflight, reviewed manifest/diff, dry-run, and explicit confirmation before final application; several destructive actions are intentionally dashboard-only.
- `truefoundry-agents` explicitly states agent authoring is a UI workflow rather than inventing unsupported API automation.
- `truefoundry-skills-registry` explicitly refuses to invent unsupported upload commands or unknown manifest fields and requires verified CLI/product surfaces.
- Shared intent-clarification guidance limits clarification to one useful routing question and favors a default path when applicable.

**Inference**

- The strongest reusable pattern is **role-separated operational Skills + centralized shared references/scripts + repository-level validator enforcing cross-Skill consistency and supported capability boundaries**.

**Not verified**

- The repository validator, installer, TrueFoundry CLI, tenant APIs, UI/browser paths, gateway operations, MCP registry operations, prompt/agent/skill registry writes, and external services were not executed.

## Content-level corrections from metadata classifications

1. `agentskill-sh/mcp-server`: content shows registry/MCP tooling; external catalog skills must not be counted as local skills. **0 local Skill reports.**
2. `valence-works/agentskillsdotnet`: content shows specification/SDK/tooling; fixture skills are test inputs. **0 local Skill reports.**
3. `gepeiyu/agentskills-proxy`: repository is primarily proxy tooling. Its single local `example-skill` is counted only as a directly reviewed **demo fixture**, not promoted to a production domain skill.
4. `cablate/Agentic-MCP-Skill`: content and README explicitly describe an experimental project. Existing tests are source evidence only; they are not recorded as passing because this batch did not run them.

## Reusable engineering patterns

1. **Canonical rubric + canonical remediation registry** — `RisorseArtificiali/agent-ready-skill`: keep scoring authority, remediation authority, and persisted score schema separate from renderers/mutators.
2. **Private eval contract + isolated execution evidence** — `Tencent/SkillHone`: protect held-out measurement while preserving enough redacted trajectory/compiler evidence to make improvements attributable.
3. **Role-separated Skill pack + shared assets + consistency validator** — `truefoundry/skills`: split by responsibility, centralize repeated references/scripts, then validate cross-package invariants mechanically.
4. **Scripts are data by default** — `valence-works/agentskillsdotnet`: parsing/loading a Skill should not implicitly grant execution or network capability; the host owns the permission boundary.
5. **Testable progressive disclosure** — `cablate/Agentic-MCP-Skill`: metadata → tool names/descriptions → one schema on demand is represented in tests and client API boundaries.
6. **Prompt/model behavior vs API transport separation** — `black-forest-labs/skills`: keep domain prompting guidance independent from API integration mechanics.
7. **Read-first research with durable evidence artifacts** — `OthmanAdi/codebase-knowledge-builder`: dependency-order reading, explicit execution-path tracing, frequent persisted notes, and a fixed output template reduce context-only reasoning.

## Runtime boundary

This batch did **not** run third-party package builds, CLIs, test suites, eval runners, model calls, image generation, browser/UI flows, network services, remote APIs, cloud mutations, or external installer workflows. Source code/tests/eval definitions being present is not recorded as runtime success.

Completion state for all ten repositories is therefore:

```text
status: structure-reviewed
runtime_validation: not_executed
```
