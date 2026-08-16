# Creative and Product UI Architecture Decision

- Date: 2026-08-16
- Status: Accepted for pilot
- Scope: AI Creative & Media and Product UI design
- Evidence basis: 19 public GitHub repositories, current architecture baseline, and six ImageGen pilot outputs

## Decision

### Creative

Create a separate engineering repository, tentatively named `creative-workflows`.

It owns:

- provider-neutral creative briefs and artifact contracts;
- style packs and prompt specifications;
- storyboard, image, video, audio, and post-processing pipelines;
- provider adapters;
- deterministic renderers such as Remotion;
- validation scripts and reproducible examples;
- metadata, provenance, and review-package schemas.

It does not own:

- large generated media;
- private source material;
- provider credentials;
- general-purpose Agent Skills;
- project-specific product UI specifications.

Large and private artifacts remain in Google Drive. Stable reusable execution entrypoints may later be published as thin Skills in `idaibin/skills`.

Reason: Creative production has its own runtime dependencies, media pipelines, model/provider volatility, renderers, metadata, and validation requirements. Keeping it inside `ai-handbook` would turn governance into implementation; keeping it inside `forgeway` would couple software delivery to media-generation dependencies.

### Product UI

Do not create a standalone Product UI repository at this stage.

Use three ownership layers:

1. `forgeway` owns the UI Spec contract, artifact lineage, status transitions, evidence references, and delivery gates.
2. `idaibin/skills` owns a provider-neutral `product-ui` execution Skill after the pilot is verified.
3. Each product repository owns its actual `DESIGN.md`, tokens, components, screenshots, Storybook, and implementation evidence.

The Product UI Skill should execute:

Context -> UX flow -> design system -> visual directions -> selected target -> UI Spec -> implementation handoff -> browser verification -> review evidence.

Reason: Product UI is inseparable from product intent, component availability, repository conventions, runtime behavior, and implementation evidence. A separate repository would duplicate design-system facts and encourage screenshot-only design. Putting all instructions into UI Spec would overload the artifact contract with execution behavior. The correct split is contract in Forgeway, execution in a Skill, implementation facts in the target project.

## Shared boundary

Creative and Product UI share a `Style Contract`, not a repository.

Minimum shared fields:

- style_id and version;
- palette and semantic roles;
- typography;
- spacing and grid;
- materials and imagery rules;
- motion principles;
- prohibited patterns;
- required output sizes;
- verification checklist;
- provenance.

Creative may consume a product Style Contract to generate campaign assets. Product UI may consume the same contract to keep UI and launch media visually coherent.

## Pilot evidence

Six images were generated with one visual baseline:

- warm ivory base;
- graphite structure;
- muted vermilion signal;
- fog-gray dividers;
- precise grid;
- tactile paper and restrained translucent layers.

Three Creative outputs covered portrait, square, and landscape formats. Three Product UI outputs covered artifact navigation, visual comparison, and evidence-led document layouts.

Observed result:

- palette, materials, grid, and focal signal remained coherent across all outputs;
- the style translated into product UI without requiring neon gradients or generic glassmorphism;
- Product UI remained readable and implementable;
- generated microcopy and dates are not reliable enough to become specifications without structured source data;
- images verify visual direction only, not runtime behavior, accessibility, or implementation fidelity.

## Promotion gates

### Creative repository

Create the repository after these are fixed:

- repository name;
- Style Contract v0.1;
- Creative Brief schema;
- Asset Manifest schema;
- one deterministic image workflow;
- one Remotion workflow;
- output and review-package routing to Drive;
- at least one executable validation script.

### Product UI Skill

Promote to `idaibin/skills` only after:

- one visual direction is selected;
- its UI Spec is represented in Forgeway;
- one real project implements the selected target;
- browser and responsive evidence are recorded;
- failure recovery is exercised;
- the Skill produces less duplication than project-local instructions.

## Rejected alternatives

- Put Creative inside ai-handbook: rejected because implementation dependencies and generated artifacts do not belong in the knowledge-governance repository.
- Put Creative inside Forgeway: rejected because media generation is an optional production domain, not a core software-delivery dependency.
- Put Product UI entirely in UI Spec: rejected because an artifact contract should describe required outcomes, not carry the whole execution method.
- Create a Product UI repository now: rejected because no independent runtime or durable source of truth has been demonstrated.
