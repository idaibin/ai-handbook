# Creative and Product UI Architecture Decision

- Date: 2026-08-16
- Corrected: 2026-08-17
- Status: Accepted v1 implementation slice
- Supersedes: the earlier same-day proposal for a separate `creative-workflows` repository
- Evidence: 19 open-source repository benchmarks, six generated visual fixtures, Forgeway contract tests, GitHub commit `591a6ae12cc7ba246a3fec30db324aec24c3312f`, and Google Drive asset readback

## Decision

Forgeway is the unified governance and delivery plane for Product UI and user-facing Creative content.

Creative includes image, photography, video, audio, poster and time-sensitive event updates such as sports/event briefs. Product UI includes visual directions, prototypes and implementation previews. Both are Audience-facing Artifacts because the end user sees or hears them.

Forgeway owns Requirement/brief/spec references, artifact identity and versions, capability handoff, provenance, evidence, review, approval, publication and readback state. It does not store media bytes, provider credentials, target design tokens or target implementation truth.

- Google Drive stores private and large source media, masters, variants and exports.
- Target product repositories own their `DESIGN.md`, UI specs, components, implementation and runtime evidence.
- Generation, editing, rendering, audio/video and browser capabilities remain replaceable Skills/adapters selected at runtime.
- ai-handbook owns the cross-project map, Registry and this decision record.

## Why this supersedes the earlier decision

The earlier proposal confused execution dependency isolation with lifecycle ownership. Media runtimes can remain isolated adapters without creating a second orchestration product. Product UI and Creative share intent, style, version, provenance, evidence and publication semantics; duplicating those across repositories would create competing asset states.

They do not share one quality model. Forgeway applies class-specific Gates:

- Product UI: target visual authority, states, responsiveness, accessibility and browser/desktop evidence when implementation is claimed.
- Creative: brief fidelity, cross-format style consistency, technical quality, rights/safety and channel fitness.
- Event updates: factual source closure and validity deadline.
- Publication: target-specific readback evidence.

## Validated slice

The v1 contract accepted:

- one Creative set with portrait, square and landscape variants bound to one style contract;
- three Forgeway Product UI direction candidates;
- a reusable metadata template.

It rejected:

- embedded binary payloads;
- Creative kinds under Product UI class;
- reviewed content without Evidence;
- event updates without factual sources and expiry;
- publication without target readback.

The Product UI candidates remain `generated`, not selected or reviewed. Static images do not prove interaction, responsive behavior, accessibility or implementation. The Creative style is provisional after one image campaign; video, audio, photography and repeated campaign tests remain required before stable brand promotion.

## Storage routing

GitHub uses opaque `asset://` identities plus hashes and metadata. The current private binary set is stored at:

`AI Engineering Lab/20-Media/Forgeway-Audience-Artifact-v1`

Private Drive URLs and credentials are not committed.

## Promotion rule

Do not create a separate Creative repository or Product UI Skill merely to organize content. Split only if executable runtime ownership, release cadence and non-Forgeway consumers are demonstrated. Until then, Forgeway coordinates replaceable capabilities through the Audience-facing Artifact workflow.
