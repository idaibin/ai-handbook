# anthropics/skills

## Metadata

- Repository: https://github.com/anthropics/skills
- Category: Official Skills Collection
- Verification status: repository metadata and tree verified
- Star count observed during scan: 166655

## Purpose

Official Agent Skills repository containing reusable skill packages and examples.

## Repository Structure Evidence

The repository contains multiple independent skill directories, including:

- algorithmic-art
- brand-guidelines
- canvas-design
- claude-api
- doc-coauthoring
- docx
- frontend-design
- mcp-builder
- pdf
- pptx
- skill-creator
- webapp-testing
- xlsx

## Skill Architecture Pattern

Observed architecture:

```
skill/
├── instructions
├── resources
├── scripts (optional)
└── validation/evaluation (optional)
```

The exact contents of each skill require individual inspection before final adoption.

## High Value Patterns

### 1. Self-contained capability package

Each skill represents a focused capability instead of a large framework module.

### 2. Progressive disclosure

Only load relevant skill information when the capability is required.

### 3. Resource separation

Instructions, reference materials, and executable helpers are separated.

## Individual Skill Reports

Pending:

- skill-creator
- frontend-design
- mcp-builder
- webapp-testing
- document skills

Each will receive an independent report after file-level review.

## Relation To idaibin/skills

Potentially reusable:

- skill package boundaries;
- SKILL.md conventions;
- resource organization;
- evaluation metadata.

Not yet accepted as design decisions until compared with additional repositories.

## Evidence Level

Verified:

- repository identity;
- star count;
- skill directory list;
- repository category.

Pending verification:

- every individual skill implementation detail;
- runtime behavior;
- evaluation effectiveness.
