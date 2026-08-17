> Historical capability-domain Map. Current successor: [`product-delivery-system-map.md`](./product-delivery-system-map.md), owned by the Forgeway route. Retained for evolution history; it no longer selects Task execution.

# AI Product Experience Map v0.1

## Purpose

AI Product Experience defines how AI capabilities become understandable, controllable and valuable user-facing products.

This map focuses on product capability and interaction patterns, not specific frameworks or tools.

## Scope

```text
AI Product Experience

├── Product Strategy
├── UX Research
├── UI Design
├── Web Application
├── Desktop Application
├── Mobile Application
├── Design System
├── AI Interface
├── Frontend Delivery
├── Data Visualization
└── Growth
```

## Capability Tree

### Product Strategy

- user problem
- value definition
- workflow design
- business model

### UX / UI

- information architecture
- interaction design
- visual design
- accessibility
- responsive design

### Design System

- design tokens
- components
- patterns
- themes
- consistency

### AI Interface

AI-native interaction model:

```text
Intent
 ↓
Plan
 ↓
Execution
 ↓
Artifact
 ↓
Review
 ↓
Commit
```

Related capabilities:

- agent interface
- task interface
- timeline
- artifact viewer
- diff review
- approval flow
- memory and context UI

### Application Delivery

- web
- desktop
- mobile
- local-first application
- cloud application

## Artifact Model

Typical artifacts:

- product requirement
- user flow
- prototype
- design token
- component
- frontend implementation
- user feedback

## Evaluation Model

Evaluation should consider:

- usability
- understandability
- efficiency
- accessibility
- trust
- consistency

## Related Projects

Initial related projects:

- forgeway
- rustzen-admin
- feeds-hub

Project relationships are managed through Registry. Forgeway governs Product UI direction previews through the shared Audience-facing Artifact lifecycle, while target repositories remain authoritative for DESIGN.md, UI specs, components, implementation and browser/runtime evidence.
