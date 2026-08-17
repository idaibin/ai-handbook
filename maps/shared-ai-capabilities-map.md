# Shared AI Capabilities Map

- Status: active
- Role: reusable inputs for feeds-hub, Createway, Story Studio and Forgeway

## Boundary

Shared AI Capabilities define reusable methods, schemas and evaluations. They are not
user-facing products, do not own final artifacts and do not form another delivery
route.

```text
Shared AI Capabilities
├── Knowledge System
│   ├── source-management
│   ├── extraction / summarization
│   ├── knowledge-card / retrieval
│   └── citation
├── Writing System
│   ├── structure / style / tone
│   ├── editing / fact-checking
│   └── human-writing / evaluation
├── Visual System
│   ├── prompt-schema / composition
│   ├── style and reference methods
│   └── visual evaluation
├── Workflow System
│   ├── composable orchestration patterns
│   └── handoff contracts
└── Evaluation System
    ├── quality review / benchmark methods
    ├── regression cases
    └── human feedback loops
```

Audio and Agent capabilities remain product-local or future capabilities (such as
Story Studio media experiment voice/audio contracts and Forgeway/Skills agent execution
patterns), not top-level current shared systems.

## Consumer/authority rule

| Shared capability | Example consumers | Product-owned authority remains with |
| --- | --- | --- |
| Knowledge System | feeds-hub, Createway, Story Studio, Forgeway | source/report/brief/product owner |
| Writing System | reports, articles, scripts, product specs | feeds-hub, Createway, Story Studio or Forgeway |
| Visual System | feed graphics, covers, story frames, UI directions | the corresponding product route |
| Workflow System | all products as needed | selected Task route and product lifecycle |
| Evaluation System | all products | named reviewer and owning acceptance gate |

A shared asset needs a real consumer, version, validator and drift policy. Availability
does not justify a new Skill, select a route or override product-specific facts.

## Visual System boundary

The shared visual prompt vocabulary may describe subject, environment, style,
composition, camera, lighting, color, emotion, references and negative constraints.
It does not own:

- Createway Content View styles and publication templates;
- Story Studio character, scene and continuity references;
- Forgeway or target-repository Product View/UI tokens and components;
- feeds-hub event/source identity.

## Use rule

A Task selects exactly one route first, then consumes only the shared capabilities
needed for that outcome. Shared results are inputs; the owning product records the
final artifact, review and release evidence.

## Historical source

This Map succeeds `ai-engineering-map.md` and prior capability maps. Historical domain
Maps remain navigation evidence, not execution authority.
