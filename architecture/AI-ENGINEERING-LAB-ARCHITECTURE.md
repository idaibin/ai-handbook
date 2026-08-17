# AI Engineering Lab Architecture Specification

- Status: Accepted baseline; effective
- Effective date: 2026-08-17
- Authority: AI Engineering Lab product-system and shared-capability architecture
- Basis: `591815e5c9ed692f6b5e949c7c27551a91eb38a9`

## 1. Positioning

AI Engineering Lab is a project system for researching, validating and maintaining
AI-assisted engineering, information, content and media-production methods. Shared
capabilities are reusable inputs; independent product systems own their outcomes,
product-specific artifacts and release evidence.

```text
AI Engineering Lab

Shared AI Capabilities
├── Knowledge System
├── Writing System
├── Visual System
├── Workflow System
└── Evaluation System

Product Systems
├── feeds-hub: Sources → Feeds → Research → Insights
├── Createway: Knowledge → Writing → Visual Enhancement → Publishing
├── Story Studio: IP → Character → Script → Storyboard → Media Asset → Distribution
└── Forgeway: Requirement → Spec → Design → Development → Verification → Delivery

Supporting Assets
├── ai-handbook: verified methods, stable standards and reusable experience
└── skills: repeatable executable capabilities with inputs, outputs and validation
```

This architecture is organized by owned outcome. A shared capability does not become
a product, a publication owner or an extra delivery route.

## 2. Product systems

### Knowledge & Intelligence — feeds-hub

Answers: **What is happening, and what source-grounded intelligence can be derived?**

Outcome: `Sources → Feeds → Research → Insights`

Owns source identity, collection, normalization, deduplication, time-bounded analysis,
research reports, insights and knowledge-candidate handoffs. It does not silently
promote an observation into durable Knowledge IR or publish authored marketing content.
It does not own final content publishing, courses or video production.

The existing Feed runtime is active and real. Research-report and insights generation,
storage, review and publication in feeds-hub remain architecture-defined and runtime
`Not verified` unless the target repository proves otherwise.

Lifecycle:

`Collect → Normalize → Analyze → Verify → Publish Intelligence → Handoff Candidate`

### Content Creation — Createway

Answers: **How should knowledge, an idea or product information be expressed and
published for an audience?**

Outcome: `Knowledge → Writing → Visual Enhancement → Publishing`

Owns articles, blogs, newsletters, social content, product-marketing content,
campaigns and their supporting covers, posters and editorial graphics.

Lifecycle:

`Idea → Brief → Outline → Draft → Human-style Rewrite → Review → Publish → Feedback`

Createway owns text and lightweight text+visual publishing outputs. It does not own
complex video, IP management, long-lived hierarchical media assets, Product UI or
software delivery. The stable route id remains `content-output-system` for current
consumers, with narrowed Createway semantics.

### Media Production — Story Studio

Answers: **How is an IP, story or episode produced into coherent visual and audio
media?**

Outcome: `IP → Character → Script → Storyboard → Media Asset → Distribution`

Owns IP, world and character bibles, timelines, episode plans, scripts, storyboards,
character/scene references, image sequences, comics, animation, video, voice, audio,
subtitles, media assets/masters and distribution evidence.

Lifecycle:

`Idea → World/Character Basis → Episode Plan → Script → Storyboard → Visual Generation → Motion/Edit → Audio → Subtitle → Review → Publish`

Story Studio is independent and currently architecture/experiment only. Its Drive
asset root exists and was read back, but no repository, runtime, 60-second pilot
execution, cost result or release is currently verified. Do not treat an empty asset
directory as production capability.

### Product Delivery — Forgeway

Answers: **How does product intent become verified software delivery?**

Outcome: `Requirement → Spec → Design → Development → Verification → Delivery`

Owns product specification, selected visual-source evidence, UI confirmation,
architecture, implementation coordination, verification, review and delivery evidence.
Target repositories remain authoritative for source, project-native design systems,
tests, configuration and runtime truth.

Lifecycle:

`Intent → Specification → Visual Source → Design → Confirmation → Implementation → Verification → Review → Delivery`

Forgeway remains software Product Delivery. Preserve its current Product UI and
delivery contracts; do not transfer Story/Createway responsibility into it.

## 3. Shared AI Capabilities

| Capability | Reusable responsibility | Does not own |
| --- | --- | --- |
| Knowledge System | source management, extraction, summarization, retrieval, citation and knowledge-card methods | feeds, research-report identity or durable product knowledge assets |
| Writing System | structure, style, tone, editing, fact-checking, human-writing and text evaluation | a product's article, report, script or specification |
| Visual System | prompt schema, shared visual primitives, composition methods, references and visual evaluation | product-specific style authority, UI source, IP references or published media |
| Workflow System | composable orchestration and handoff patterns | product lifecycle authority or automatic promotion |
| Evaluation System | quality review, benchmarks, human feedback and regression methods | self-approval, evidence-level promotion or production acceptance |

Audio and Agent capabilities remain product-local or future capabilities (such as
Story Studio media experiment voice/audio contracts and Forgeway/Skills agent execution
patterns), not top-level current shared systems.

Shared capability artifacts require a real consumer, validator and drift policy. A
shared prompt or token becomes authoritative only inside the consuming product's
versioned contract.

## 4. Supporting Assets

- `ai-handbook`: verified methods, stable standards, research evidence, experiment
  ledgers and reusable experience governance.
- `skills`: repeatable executable capabilities with explicit inputs, outputs and
  validation.

Do not elevate every prompt into a Skill. A Skill requires repeatability, explicit
inputs/outputs and validation.

## 5. Visual authority boundary

The Visual System supplies tool-neutral description and evaluation semantics. Product
systems retain their own authorities:

- feeds-hub owns source-linked information graphics attached to intelligence records;
- Createway owns Content View style contracts and publication visuals;
- Story Studio owns character/scene continuity references and media masters;
- Forgeway and target repositories own Product View/UI directions, tokens, components
  and browser evidence.

An image's format does not select its route. Its intended outcome and artifact owner
do: an article cover is Createway, a story frame is Story Studio, and a UI direction
is Forgeway.

## 6. Task routing and composition

A project may use several routes, but one executable Task selects exactly one:

| Stable route id | Product owner | Outcome |
| --- | --- | --- |
| `knowledge-intelligence-system` | feeds-hub | Sources → Feeds → Research → Insights |
| `content-output-system` | Createway | Knowledge → Writing → Visual Enhancement → Publishing |
| `media-production-system` | Story Studio | IP → Character → Script → Storyboard → Media Asset → Distribution |
| `product-delivery-system` | Forgeway | Requirement → Spec → Design → Development → Verification → Delivery |

Cross-system work is composed through fixed artifacts and handoffs, not a mixed Task.
For example, feeds-hub research may be input to Createway; a Createway or Story Studio
runtime change is a separate Forgeway/Product Delivery Task.

## 7. Data and artifact ownership

| Owner | Canonical assets |
| --- | --- |
| ai-handbook | architecture, Registry, Maps, workflow governance, research and promotion decisions |
| feeds-hub | source/event identity, feeds, time-bounded research reports and knowledge candidates |
| Createway | briefs, drafts, publication content packages, campaign assets, receipts and feedback |
| Story Studio | IP/world/character records, scripts, storyboards, media sources/masters and production evidence |
| Forgeway | product-delivery artifacts, review/evidence graph and delivery receipts |
| knowledge-distillation | existing Knowledge IR, courses, knowledge cards and knowledge-output packages until an explicit migration changes that authority |
| skills | validated reusable executable capabilities |
| target repositories | source, project-native specifications, tests, releases and runtime truth |

GitHub stores public versioned contracts and metadata. Google Drive stores private,
licensed or large binaries. The current Drive product-system hierarchy was applied by
moving existing assets while preserving file IDs and was read back on 2026-08-17;
folder existence does not prove a product runtime or completed media workflow.

## 8. Migration from prior output-oriented architecture

1. Keep `content-output-system` as a stable id while narrowing its meaning to
   Createway Content Creation.
2. Route source-grounded feeds and research to `knowledge-intelligence-system`.
3. Route narrative video, audio, animation, comic and IP continuity to
   `media-production-system`.
4. Keep `product-delivery-system` and Forgeway delivery responsibilities unchanged.
5. Preserve prior v2 records as historical evidence; do not rewrite their original
   contracts.
6. Do not claim Story Studio runtime, Audio/Voice implementation, new repositories or
   cross-product runtime integrations until separately implemented and verified.

## 9. Maintenance sequence

Read this baseline at an exact commit → query Registry → select one Task route → load
only required shared capabilities and owner assets → execute and verify → write result
to the owning product → update Registry/evidence when authority or maturity changes.

## 10. Constraints

1. Shared capability does not imply shared product ownership.
2. One Task selects one route; multi-system delivery uses explicit handoffs.
3. Do not duplicate product artifacts into the shared layer.
4. Do not create empty repositories or Drive hierarchies.
5. Keep current consumers compatible unless a versioned migration is executed.
6. Separate architecture-defined, implemented, runtime-verified and production states.
7. Validate repeated real use before promoting Workflow, Skill or shared system.
