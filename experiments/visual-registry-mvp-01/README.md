# Visual Registry MVP 01

Status: `application_extracted_repository_creation_blocked_generation_blocked`

## Purpose

This directory contains the experiment protocol, provider-neutral Visual Contracts, Prompt compiler, file-backed query prototype, Prompt 1:N contract, tests, and execution evidence.

It does **not** contain the runnable product application.

## Application project

The Next.js application has been extracted from this repository and prepared as:

```text
target repository: idaibin/prompts-hub
framework: Next.js + React + TypeScript
local initial commit: b58624698cc2bcc4ef7bf3ea90e3b6e14127d1df
```

Repository creation is not yet verified because the connected GitHub tool can write existing repositories but does not expose repository creation. See [`PROJECT.md`](./PROJECT.md).

## Experiment assets retained here

```text
schema/
contracts/
cases/
image-cases/
prompt-cases/
prototype/
tests/
evidence/
SOURCES.md
EXECUTION.md
```

## Verified experiment result

```text
Visual Contracts: 3
Adapters: 3
queryable records: 11
PromptCase: 1
GenerationBatch: 1
independent result identities: 4
provider-native images: 0/4
```

Verified:

- provider-neutral contract and provider adapter separation;
- deterministic Prompt compilation;
- file-backed exact and related query separation;
- PromptCase → GenerationBatch → ImageResult relationship;
- canonical images require independent files and evidence identities;
- report pages, collages, dashboards, and contact sheets are excluded from canonical image counts.

Not verified:

- four independent provider-native images;
- provider receipts, image hashes, and dimensions;
- deployed `prompts-hub` application;
- readiness for promotion into `skills`.

The experiment remains authoritative for contracts and evidence. The future `idaibin/prompts-hub` repository will be authoritative for runnable application code.