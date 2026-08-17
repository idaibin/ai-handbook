# AI Engineering Lab Architecture Specification

- Version: v2.0
- Status: Baseline
- Effective date: 2026-08-17
- Authority: current AI Engineering Lab output-oriented architecture

## 1. Positioning

AI Engineering Lab is the total workspace for research, reusable AI capabilities, content production, software product delivery and commercial validation.

```text
AI Engineering Lab
├── Shared AI Capabilities
├── Content Output System
│   └── Createway
└── Product Delivery System
    └── Forgeway
```

The architecture is organized by final output, not by parallel research domains.

## 2. Output systems

### Content Output System — Createway

Outcome: turn an idea, source or event into reviewed, publishable content.

Scope includes writing, images, photography, posters, video, animation, audio, comics, social/community content and event updates.

Lifecycle:

`Intent → Brief → Source Grounding → Create → Edit → Review → Publish → Feedback`

Createway is architecture-defined. No implementation repository or runtime is currently verified.

### Product Delivery System — Forgeway

Outcome: turn product intent into verified software delivery.

Scope includes product definition, requirements, UX/UI, architecture, domain/data/interface design, tasks, implementation, tests, review, release and runtime readback.

Lifecycle:

`Intent → Specification → Design → Implementation → Verification → Review → Delivery`

Forgeway is implemented in `idaibin/forgeway`.

## 3. Shared AI Capabilities

Shared capabilities include Model, Agent, Skill, Tool/MCP/Plugin, Context/Memory/RAG, Workflow/Automation, Evaluation/Verification, Knowledge/Research and Design System.

Design System is layered:

```text
Design System
├── Design Tokens
├── Content View
└── Product View
```

Content View supports templates and visual rules for content outputs. Product View supports UI tokens, components and React/Tauri product implementation. Shared capabilities never become a third delivery route.

## 4. Task routing

A project has one primary route and may have secondary routes. A Task must select exactly one route before execution.

- Content creation, editing, packaging and publication use `content-output-system`.
- Product specification, APIs, databases, UI implementation, tests and deployment use `product-delivery-system`.
- A mixed project such as feeds-hub uses both at project level, but each Task remains single-route.

## 5. Authority and storage

| Layer | Authority |
| --- | --- |
| Google Drive / AI Engineering Lab | private sources, media binaries, datasets, masters, review packages and exports |
| GitHub / ai-handbook | architecture, Registry, Maps, workflows, standards, research summaries and decisions |
| GitHub project repositories | code, project-native specifications, tests, releases and runtime-facing facts |

GitHub and Drive are complementary authorities, not mirrors. Public repositories must not contain credentials, private links, customer material or large media binaries.

## 6. Registry

Registry separates:

- `routes`: how a Task executes;
- `capabilities`: what reusable abilities it uses;
- `domains`: retained classification and historical compatibility;
- `projects`, `assets` and `relationships`: identity and references.

`routes.yaml` is the current route authority. `projects.yaml` records project defaults and capabilities. Task route selection overrides a project default for that Task without changing the project mapping.

## 7. Maps

Current Maps:

- `shared-ai-capabilities-map.md`;
- `content-output-system-map.md`;
- `product-delivery-system-map.md`.

Prior domain Maps remain as historical entrypoints with successor references. They no longer select execution.

## 8. Migration state

The earlier Creative pilot implemented under Forgeway remains historical evidence. Its binaries stay in Drive and hashes stay in Registry. Governance moves to Createway; the originating Forgeway contract is marked pending migration rather than silently rewritten.

No Createway repository, empty Drive hierarchy or runtime contract is created until a real implementation Task and consumer require it.

## 9. Maintenance sequence

Read this baseline → read `workflows/ai-engineering-system/README.md` at an exact commit → query Registry → select one Task route → load only required capabilities and project/Drive assets → execute and verify → update affected references and readback.

## 10. Constraints

1. Do not create a parallel Lab or Registry.
2. Do not duplicate GitHub and Drive content.
3. Do not let project repositories become the knowledge center.
4. Do not create empty repository or Drive structures.
5. Keep one route per Task.
6. Preserve domains for classification, not execution.
7. Distinguish defined architecture, implemented capability and verified runtime evidence.
8. Validate before promoting a Skill, Workflow or product runtime.
