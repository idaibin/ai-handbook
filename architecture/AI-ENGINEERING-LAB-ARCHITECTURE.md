# AI Engineering Lab Architecture Specification

- Version: v1.0
- Status: Baseline
- Effective date: 2026-08-16
- Scope: AI Engineering Lab workspace, ai-handbook governance, GitHub project repositories, and Google Drive private assets
- Authority: This document defines the architecture baseline. It does not replace the current user instruction, the ai-handbook workflow README, or repository-specific runtime facts.

## 1. Positioning

AI Engineering Lab is the total workspace for a personal AI Engineering System. It coordinates research, knowledge, experiments, engineering implementation, product delivery, and commercial validation.

It is not a single GitHub repository and not a standalone knowledge base. It is a shared context, research, experiment, asset, and project-coordination space.

Target loop: AI capability research -> knowledge distillation -> experiment -> engineering implementation -> product delivery -> commercial value.

## 2. Authority and storage boundaries

The system uses three complementary layers. They are not three copies of the same content.

| Layer | System | Authority | Stores | Must not become |
|---|---|---|---|---|
| Private workspace | Google Drive / AI Engineering Lab | private process and asset source | raw sources, research packages, media, project material, review packages, exports | code repository or public knowledge authority |
| Governance and knowledge | GitHub / idaibin/ai-handbook | versioned public workflow, schema, maps, decisions, distilled knowledge | maps, Registry contracts, standards, workflows, research summaries, decision records | large media store or secret store |
| Engineering delivery | GitHub project repositories | code and runtime engineering truth | code, schemas, tests, CI, releases, deployment-facing docs | cross-project knowledge center |

Conflict rule: current user instructions have highest priority; then the current ai-handbook workflow and Registry contract; then repository-specific verified runtime facts; then Drive process records. A historical report cannot override current repository or production evidence.

## 3. Google Drive workspace

Root workspace: AI Engineering Lab.

Initial folders: 00-Inbox, 10-Sources, 20-Media, 30-Datasets, 40-Exports, and 90-Archive.

Create 40-Projects, 50-Experiments, and 70-Knowledge-Outputs only when a real asset requires them. Do not create empty directory trees in advance.

Drive stores private or large assets: source material, images, video, audio, design files, datasets, review packages, and exports. Every durable asset referenced by GitHub must have an asset_id, canonical Drive URL or file ID, access classification, and sync status.

## 4. ai-handbook role

Repository: idaibin/ai-handbook.

ai-handbook is the governance and knowledge layer for AI Engineering Lab. It owns maps and navigation; Registry contracts and cross-system index; research methods and summaries; workflows and standards; decision records; and distilled reusable knowledge.

It does not own private source files, large media, credentials, customer data, or unverified project claims.

Expected structure: maps/, registry/, research/, experiments/, workflows/, standards/, decisions/.

The authoritative workflow entrypoint remains workflows/ai-engineering-system/README.md. Before important work, read that entrypoint and record the exact commit SHA.

## 5. Three research domains

### AI Engineering

How AI systems work and how to engineer with them: Model, Agent, Skill, Plugin, MCP, Tool, Harness, Workflow, Memory, Context, RAG, Evaluation, and Automation.

Outputs: reusable Skills, Agent methods, workflows, engineering standards, and verification methods.

### AI Creative & Media

How AI produces digital content assets: Image, Photography, Graphic Design, Poster, Social Content, Video, Animation, Comic, Digital Human, Audio, and 3D.

The primary unit is a content-production workflow, not a model list: Idea -> Script -> Storyboard -> Generation -> Editing -> Publish -> Feedback.

### AI Product Experience

How AI becomes a real product: Product Strategy, UX, UI, Web, Desktop, Mobile, Design System, Prototype, Frontend, AI Interface, Data Visualization, and Growth.

The key product transition is: Intent -> Plan -> Execution -> Artifact -> Review -> Commit.

Domains are classification and routing dimensions. A project may belong to more than one domain, but each relationship must be explicit in Registry.

## 6. Registry

Registry is the machine-readable routing and indexing layer. It is not a fourth knowledge repository and must not duplicate complete GitHub or Drive content.

It answers where an object is; what domain it belongs to; which repository or Drive asset is authoritative; what it relates to; and its lifecycle and sync state.

Minimum object requirements: stable id; type; human-readable name; canonical source reference; domain or project relationship; status; updated_at; evidence or provenance reference; and sync_status where cross-system references exist.

Current logical collections: domains, projects, assets, and relationships.

Allowed relationship types: uses, implements, tested-by, indexes-asset, distills-into, depends-on, and derived-from.

Registry rules:

1. A new durable object must be registered or explicitly declared out of scope.
2. A Registry entry points to the source; it does not copy the source body.
3. Unknown, historical, and verified states must not be collapsed into one status.
4. A path is not a stable identity; use a repository path plus commit SHA or a canonical Drive file ID/URL.
5. Existing Registry records are updated in place. Do not create parallel registries.

The existing Google Drive AI Engineering Registry is a current operational registry record and must be reconciled with the GitHub Registry contract rather than replaced by another spreadsheet.

## 7. Project mapping

| Project | Primary domains | Responsibility |
|---|---|---|
| idaibin/skills | AI Engineering | reusable Skills, Agent capabilities, and workflows |
| idaibin/forgeway | AI Engineering; AI Product Experience | AI-native software delivery, artifact workflow, and product engineering |
| idaibin/rustzen-admin | AI Product Experience; AI Engineering | local-first desktop UX and macOS product experience |
| idaibin/feeds-hub | AI Product Experience; AI Engineering; AI Creative & Media | information product, feed system, AI-assisted content processing and display |

Repository-specific facts remain authoritative for implementation and runtime behavior.

## 8. AI task routing

For a task that concerns AI Engineering Lab or a registered project:

1. Read the ai-handbook workflow entrypoint and exact baseline SHA.
2. Read the Registry entry or query the smallest relevant Registry slice.
3. Determine the relevant domain and project.
4. Read the domain Map and project repository entry.
5. Resolve only the required GitHub files and Drive assets.
6. Execute the task under the applicable workflow.
7. Record evidence, update Registry references, and sync only affected records.

AI agents must not blindly scan every repository or treat the entire Drive workspace as a knowledge source. Direct repository inspection is allowed when the task is explicitly repository-scoped and the authoritative workflow permits it.

## 9. Security and publication

Never publish to GitHub: API keys, tokens, cookies, credentials, account information; private access-granting links; customer or private source material; copyrighted source text beyond permitted excerpts; or large media assets.

Drive is the default location for private sources, media, experiments, and review packages. Before publishing any derived result, check secrets, privacy, copyright, and whether the artifact is actually a distilled engineering fact.

## 10. Synchronization protocol

GitHub is the versioned authority for code, contracts, workflows, and distilled public knowledge. Drive is the private authority for raw material and large assets. Neither side is a mirror of the other.

For a cross-system change:

1. Identify the source object and target object.
2. Update the authoritative source first.
3. Update Registry metadata and relationship edges.
4. Add canonical references, commit SHA or Drive file ID, and timestamp.
5. Verify target readback.
6. Record synced, partial, or write_failed with the next action.

Do not silently overwrite an existing record. Preserve historical evidence, but mark obsolete claims as historical or archived.

## 11. Current state

Verified baseline decisions: AI Engineering Lab is the single total workspace; GitHub, Drive, and ai-handbook boundaries are defined; Registry is the routing/index layer; three research domains are defined; skills, forgeway, rustzen-admin, and feeds-hub have explicit domain mappings; and no additional parallel Lab or Registry should be created.

Not yet complete: full domain Maps; complete knowledge graphs; tool and model registries; domain case libraries; experiment asset catalog; and reusable practice workflows for all domains.

These are backlog items, not evidence that the architecture baseline is incomplete.

## 12. Phased roadmap

Phase 1 — Stabilize foundation: maintain Registry contracts, Maps entrypoints, Drive routing, and authority rules.

Phase 2 — Build domain Maps: expand the three Maps only from verified research and actual project needs.

Phase 3 — Build knowledge graph: add capabilities, tools, models, cases, workflows, evaluations, and typed relationships.

Phase 4 — Validate in real projects: use skills, forgeway, rustzen-admin, feeds-hub, and future projects as validation environments. Promote a Skill or Workflow only after reproducible evidence.

## 13. Maintenance constraints

1. Do not create a parallel Lab.
2. Do not duplicate GitHub and Drive bodies.
3. Do not make a project repository the knowledge center.
4. Do not create large empty directory structures.
5. Register every new durable cross-system object.
6. Build Maps before expanding graph detail.
7. Validate before promoting a Skill or Workflow.
8. Keep Verified, Inference, Historical, and Not verified claims distinct.
9. Do not use a design proposal or build result as proof of runtime success.
10. Prefer the smallest change that closes the current verified gap.

## 14. Maintenance entrypoint

Read this baseline -> read ai-handbook/workflows/ai-engineering-system/README.md -> record baseline SHA -> query Registry -> resolve the smallest relevant sources -> execute and verify -> update affected Registry records -> sync GitHub and Drive readback.

This document is the architecture baseline and maintenance contract. It is not a substitute for current repository code, current production evidence, or the latest user instruction.