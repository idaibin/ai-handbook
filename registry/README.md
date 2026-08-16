# Registry

`registry/` is the machine-readable relationship index for AI Engineering Lab.

It connects:

- `ai-handbook`: knowledge governance and routing
- GitHub repositories: engineering implementation
- Google Drive: private process assets and large files

Registry does not store full content. It only stores stable identity, relationships, routing metadata and references.

## Principles

- One object has one stable id.
- GitHub and Drive are not mirrors.
- Private assets remain in Google Drive.
- Public repositories must not contain sensitive information.
- Schema should remain simple and extensible.

## Files

- `domains.yaml`: research domains and capabilities.
- `projects.yaml`: project identity and repository mappings.
- `assets.yaml`: external asset references.
- `relationships.yaml`: typed relationships between objects.

## Relationship vocabulary

Initial controlled verbs:

- `uses`
- `implements`
- `tested-by`
- `indexes-asset`
- `distills-into`
- `depends-on`
- `derived-from`
