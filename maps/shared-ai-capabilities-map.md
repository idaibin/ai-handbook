# Shared AI Capabilities Map v1.0

- Status: active
- Architecture: AI Engineering Lab v2.0
- Role: reusable capabilities shared by Createway and Forgeway

## Purpose

Shared AI Capabilities describe what the Lab can use. They do not form a third delivery route and do not own Content or Product outputs.

## Capability map

```text
Shared AI Capabilities
├── Model
├── Agent
├── Skill
├── Tool / MCP / Plugin
├── Context / Memory / RAG
├── Workflow / Automation
├── Evaluation / Verification
├── Knowledge / Research
└── Design System
    ├── Design Tokens
    ├── Content View
    └── Product View
```

## Design System boundary

### Design Tokens

Shared primitives and semantic roles that may be referenced by either view. A token becomes authoritative only inside its owning product or content contract.

### Content View

Supports Createway outputs:

- poster and social templates;
- image and photography direction;
- video visual and motion rules;
- content typography, composition and channel variants.

### Product View

Supports Forgeway and target product repositories:

- UI tokens;
- components and interaction states;
- `ui-spec` selected-source direction and page/component UI contracts;
- target-owned React/Tauri/Web implementation and design-system adapters;
- responsive, keyboard, failure-state and accessibility evidence;
- versioned browser-report consumers that bind runtime evidence to the delivered result.

`ui-spec` owns reusable UI semantics; it does not own a target project's tokens,
components or source. A Forgeway Product UI module remains internal when Forgeway is
the only real consumer. A framework adapter does not justify a separate shared Skill.
Images, video, audio, posters and other content-production outputs remain in
Createway's Content View route.

Content View and Product View may share selected tokens, but neither silently overrides the other.

## Use rule

A Task first selects exactly one delivery route, then resolves only the Shared AI Capabilities required by that route. Capability availability does not select or widen the route.

## Historical source

This Map succeeds `ai-engineering-map.md`. The old Map remains as a historical capability-domain entry.
