# AI Engineering Lab Product-System Architecture Decision

- Date: 2026-08-17
- Status: Accepted; effective
- Scope: shared capabilities, product-system ownership, task routing and migration
- Supersedes: [`2026-08-17-output-oriented-architecture-v2.md`](./2026-08-17-output-oriented-architecture-v2.md)
- Fixed basis: `591815e5c9ed692f6b5e949c7c27551a91eb38a9`

## Confirmed decision

AI Engineering Lab has one non-product shared-capability layer (5 approved shared systems:
Knowledge, Writing, Visual, Workflow, Evaluation) and four independent product systems:
feeds-hub for Knowledge & Intelligence, Createway for Content Creation, Story Studio for
Media Production and Forgeway for Product Delivery.

Shared capability systems provide reusable methods, contracts and evaluations. They
do not own product artifacts or silently choose an execution route.

Supporting assets:
- `ai-handbook`: verified methods, stable standards and reusable experience
- `skills`: repeatable executable capabilities with inputs, outputs and validation

## Resolved language and boundaries

- **Knowledge System** is reusable ingestion/understanding capability;
  **Knowledge & Intelligence** is the feeds-hub product outcome (Sources → Feeds → Research → Insights).
- **Writing System** is reusable text production/evaluation capability; reports,
  articles, scripts and product specifications remain owned by their product route.
- **Visual System** is reusable prompt/reference/evaluation capability; Content View,
  story continuity and Product View remain separate product authorities.
- **Content Creation** is audience expression and publishing (Knowledge → Writing → Visual Enhancement → Publishing);
  **Media Production** is IP/story continuity plus image-sequence, motion and audio production
  (IP → Character → Script → Storyboard → Media Asset → Distribution).
- **Product Delivery** remains software delivery (Requirement → Spec → Design → Development → Verification → Delivery)
  and does not absorb content/media.

## Lifecycle and route decision

The existing `content-output-system` id has current consumers, so its meaning is narrowed
to Createway Content Creation without breaking the stable id. Two routes are added:

- `knowledge-intelligence-system` for feeds-hub;
- `media-production-system` for Story Studio.

`product-delivery-system` remains unchanged for Forgeway. Every executable Task still selects
exactly one route; cross-system work uses explicit artifact handoffs.

## Conflict resolutions

1. The proposal's `feeds-hub/knowledge` directory does not transfer existing durable
   Knowledge IR ownership from `knowledge-distillation`. feeds-hub owns source-bound,
   time-bounded intelligence and emits knowledge candidates.
2. Createway keeps covers, posters and editorial graphics used by authored content,
   but narrative image sequences, comics, animation, video, voice and audio move to
   Story Studio.
3. Visual System does not become a universal design authority. Forgeway/target
   Product UI, Createway Content View and Story Studio continuity references remain
   independent.
4. The Drive tree follows the same product owners. The 2026-08-17 migration moved
   existing assets without changing their file IDs and retained old structural folders
   under `99_Archive`; folder presence is storage evidence only.

## Not verified

- Story Studio repository, implementation, pilot, cost and quality;
- feeds-hub research-report and insights runtime and publication flow beyond its existing Feed role;
- Audio/Voice runtime, voices, music or evaluation implementation;
- Createway remote repository and runtime;
- Drive content completeness beyond the inventoried and moved assets;
- cross-product automated handoffs or a shared capability runtime.

## Promotion decision

This change establishes architecture and Registry contracts only. It does not promote
the proposed systems into Workflow/Skill/runtime completion. Each promotion requires a
real consumer, validator, repeated tasks and evidence at the claimed level.
