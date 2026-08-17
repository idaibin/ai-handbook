# Registry

`registry/` is the machine-readable relationship and routing index for AI Engineering Lab.

It connects:

- `ai-handbook`: architecture, knowledge governance and routing;
- GitHub repositories: engineering implementation;
- Google Drive: private process assets and large files.

Registry stores stable identity, relationships, routing metadata and references. It does not duplicate source content.

## Concepts

- `domains`: retained capability-domain classification and historical compatibility. Domains answer what an object concerns; they do not select execution.
- `routes`: output-oriented delivery paths. Routes answer how a task is executed.
- `capabilities`: reusable abilities used by a selected route.
- `projects`: project identity, default project routes, capabilities and repository mappings.
- `assets`: external asset references.
- `relationships`: typed edges between registered objects.

## Files

- `routes.yaml`: feeds-hub, Createway, Story Studio and Forgeway route definitions, task cardinality and 5 shared capability systems.
- `domains.yaml`: retained research-domain and capability classification.
- `projects.yaml`: project identity, primary/secondary routes, capabilities and repository mappings.
- `assets.yaml`: external asset references and migration state.
- `relationships.yaml`: typed relationships between objects.

## Routing rules

1. A project may declare one primary route and zero or more secondary routes.
2. Every executable delivery Task must select exactly one route.
3. Shared AI Capabilities (Knowledge, Writing, Visual, Workflow, Evaluation) may support any route but are not another delivery route.
4. A project default does not override a Task's explicit route.
5. `content-output-system` is retained as Createway's stable id with narrowed Content Creation meaning.
6. `Story Studio` is architecture/experiment-defined only; Registry must not imply a repository, pilot or runtime.
7. feeds-hub owns source-bound intelligence and knowledge candidates, not durable Knowledge IR promotion.

## Principles

- One object has one stable id.
- GitHub and Drive are not mirrors.
- Private assets remain in Google Drive.
- Public repositories must not contain sensitive information.
- Historical domains remain queryable while Maps use output-oriented routes.
- Schema and metadata should remain simple and extensible.

## Contract lifecycle

- Owner and producer: `idaibin/ai-handbook` architecture/Registry changes.
- Semantic version: `registry/routes.yaml#schema_version`; uses Registry Route
  schema `2.0` while preserving the `content-output-system` stable id.
- Non-LLM consumer and validator: `python3 registry/validate.py`.
- Drift policy: every Registry, route, product-system workflow or routing-eval change
  must pass the validator before review; missing references fail closed.
- Retirement: a route id is removed only through a versioned architecture decision,
  consumer migration and a validator update. Historical evidence is not rewritten.

Validation:

```bash
python3 registry/validate.py
python3 -m unittest registry/test_validate.py
```

## Relationship vocabulary

- `uses`
- `implements`
- `tested-by`
- `indexes-asset`
- `distills-into`
- `depends-on`
- `derived-from`
