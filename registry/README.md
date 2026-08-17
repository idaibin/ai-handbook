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

- `routes.yaml`: Content Output System/Createway and Product Delivery System/Forgeway route definitions and task cardinality.
- `domains.yaml`: retained research-domain and capability classification.
- `projects.yaml`: project identity, primary/secondary routes, capabilities and repository mappings.
- `assets.yaml`: external asset references and migration state.
- `relationships.yaml`: typed relationships between objects.

## Routing rules

1. A project may declare one primary route and zero or more secondary routes.
2. Every executable delivery Task must select exactly one route.
3. Shared AI Capabilities may support either route but are not a third delivery route.
4. A project default does not override a Task's explicit route.
5. `Createway` is architecture-defined but has no implementation repository yet. Registry must not imply runtime verification.

## Principles

- One object has one stable id.
- GitHub and Drive are not mirrors.
- Private assets remain in Google Drive.
- Public repositories must not contain sensitive information.
- Historical domains remain queryable while Maps use output-oriented routes.
- Schema and metadata should remain simple and extensible.

## Relationship vocabulary

- `uses`
- `implements`
- `tested-by`
- `indexes-asset`
- `distills-into`
- `depends-on`
- `derived-from`
