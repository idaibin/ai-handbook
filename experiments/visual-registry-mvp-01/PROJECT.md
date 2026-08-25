# Prompts Hub project pointer

## Decision

Runnable application code does not belong in `ai-handbook`.

Active product repository:

```text
repository: idaibin/prompts-hub
visibility: private
role: Next.js Web application for visual Style and PromptCase browsing
status: repository_verified_deployment_not_verified
branch: main
application initialization commit: 2d9b9640228023e2e0c775a349a34124b4d8573a
current verified commit: 3ca6519195b070ea3f69e8265321ad1bea2a0cbc
current commit message: ci: verify Next.js project
```

The repository, visibility, default branch, and application initialization commit were read back through the GitHub connector on 2026-08-25.

## Verification state

### User-provided local evidence

```text
npm run verify: passed
production build: passed
static pages generated: 16
local and remote SHA at initialization: matched
working tree at initialization: clean
```

### GitHub Actions evidence

A repository-native verification workflow was added at:

```text
.github/workflows/verify.yml
```

Verified remote execution:

```text
workflow: Verify
run ID: 32834969574
head SHA: 3ca6519195b070ea3f69e8265321ad1bea2a0cbc
result: success
install dependencies: success
validate, typecheck, and build: success
16-page static export assertion: success
artifact upload: success
```

Static export artifact:

```text
artifact ID: 9558241090
name: prompts-hub-static-export
bytes: 317335
digest: sha256:a5e78fca8fe4314d213e41e98ca0b5e33d674175aae2c3d5d2175d5c491c3547
expires: 2026-11-23T10:00:28Z
```

The artifact was downloaded and inspected. It contains exactly 16 `index.html` files, including the home page, one PromptCase detail route, twelve Style detail routes, and two not-found routes. HTTP serving and content checks passed for the home page, PromptCase route, and transparent-watercolor Style route.

Current product boundary:

```text
repository initialization: verified
source push and remote readback: verified
remote CI production build: verified
static export structure and key content: verified
production deployment: not verified
live deployed browser behavior: not verified
custom domain: not configured or verified
valid independent Prompt images: 0/4
```

## Drive migration handoff

```text
folder: Prompts Hub
folder ID: 1a3gAeZIYih6UQS0GRvANTf-ji78srtOa

source ZIP:
  file ID: 1eINmADaD5BQsJ_3_dIjRxqBzKmWrAfqP
  bytes: 21453
  SHA-256: 99f449fbd61c744487d8ff346472493b3cf7154c4d22c8ceaaa9c6071620cd48

Git bundle:
  file ID: 116_kUaperuJBpPTYmAChiddDCayAQJo8
  bytes: 16612
  SHA-256: d426dd547cf309ca1947a0eca75f24c156235e70d6f25b1a937a64f667b0bf9b

manifest:
  file ID: 1yjnrSy152b1w3zyQ2yXt6Z_YS_A8_3eO
  bytes: 4488
  SHA-256: 407b46b089ada80e72f935c5c5d928f1e05fa193b5ac0b61cb6f1233a5e771ee
```

These files remain migration evidence, not the current code authority.

## Authority boundary

- `idaibin/ai-handbook`: experiment contracts, research, validation evidence, and project pointer.
- `idaibin/prompts-hub`: application code, application releases, CI, deployment configuration, and product issues.
- Google Drive: migration evidence and future large original image assets.

## Deployment boundary

The connected Vercel team `abin-projects` has no `prompts-hub` project. The available Vercel connector can inspect existing projects and deploy the current bound workspace, but does not expose a safe action to create a new project linked to this GitHub repository. No unrelated Vercel project was reused.

## Next gate

Create or link a Vercel project for `idaibin/prompts-hub`, deploy exact commit `3ca6519195b070ea3f69e8265321ad1bea2a0cbc`, then preserve:

```text
Vercel project ID and team ID
deployment ID and commit SHA
production URL
build/deployment receipt
HTTP availability
browser validation at desktop and mobile sizes
prompt search and detail-route checks
custom domain prompt.idaibin.dev state
```

Until those checks pass, deployment and online operation remain `not_verified`.