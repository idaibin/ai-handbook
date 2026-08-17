# AI Engineering Lab Output-Oriented Architecture v2.0

> Historical decision. Superseded by
> [`2026-08-17-ai-engineering-lab-product-systems.md`](./2026-08-17-ai-engineering-lab-product-systems.md).
> The stable v2 route ids remain compatibility inputs to the product systems architecture.

- Date: 2026-08-17
- Status: Accepted
- Scope: AI Engineering Lab architecture, Maps and Registry routing
- Supersedes: capability-domain routing as the primary execution architecture

## Decision

AI Engineering Lab uses two output-oriented delivery systems:

```text
AI Engineering Lab
├── Shared AI Capabilities
├── Content Output System
│   └── Createway
└── Product Delivery System
    └── Forgeway
```

`Createway` owns the route from content intent to publication. `Forgeway` owns the route from product intent to verified software delivery. Shared AI Capabilities support both and are not a third delivery route.

## Route cardinality

A project declares one primary route and may declare secondary routes. Every executable Task selects exactly one route. Project defaults guide routing but never make a mixed-route Task valid.

## Design System

Shared Design System capability is layered into Design Tokens, Content View and Product View. Content View serves content templates and media style; Product View serves UI tokens, components and React/Tauri product implementation.

## Compatibility and migration

The three prior domains remain in `domains.yaml` for classification and historical queries. Their Maps become historical entrypoints:

- AI Engineering → Shared AI Capabilities;
- AI Creative & Media → Content Output System;
- AI Product Experience → Product Delivery System.

The prior decision to govern Creative inside Forgeway is superseded. Existing Forgeway Creative pilot records remain evidence, but their target route/product is Createway and migration status is explicit.

Createway has an accepted name and architecture role but no implementation repository. This decision does not prove a runtime, release or production workflow.
