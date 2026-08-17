# Product Delivery System Map v1.0

- Status: active
- Product: Forgeway
- Product implementation: active
- Architecture: AI Engineering Lab v2.0

## Outcome

Turn product intent into verified software delivery.

```text
Intent
  ↓
Product Definition
  ↓
Requirement
  ↓
Solution / UI / Data / Interface
  ↓
Task
  ↓
Implementation
  ↓
Verification / Review
  ↓
Delivery / Runtime Readback
```

## Product scope

- product strategy and requirements;
- architecture, domain, data and interfaces;
- UX, UI and Product View design systems;
- web, desktop and mobile implementation;
- tests, evidence, review and release;
- AI-native intent, plan, execution, artifact, review and commit flows.

## Authority boundary

Forgeway owns cross-project delivery coordination, artifact identity, handoff, evidence and Gates. Target repositories remain authoritative for product facts, `DESIGN.md`, source, tests, configuration and runtime truth.

## Gates

- fixed repository basis;
- accepted product/requirement authority;
- explicit mutation scope;
- applicable UI/accessibility and interface/data contracts;
- automated, artifact and runtime evidence kept distinct;
- review and delivery readback bound to exact artifacts.

## Task route rule

A software engineering Task selects `product-delivery-system` even when the product's primary route is Createway. Content generation performed by the product is a separate Createway Task.

## Related projects

- forgeway;
- rustzen-admin;
- feeds-hub as a secondary route;
- future software products registered through `projects.yaml`.

## Historical source

This Map succeeds `ai-product-experience-map.md`.
