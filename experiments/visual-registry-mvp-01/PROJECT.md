# Prompts Hub project pointer

## Decision

Runnable application code does not belong in `ai-handbook`.

Active product repository:

```text
repository: idaibin/prompts-hub
visibility: private
role: Next.js Web application for visual Style and PromptCase browsing
status: repository_ready_deployment_not_verified
branch: main
remote commit: 2d9b9640228023e2e0c775a349a34124b4d8573a
commit message: chore: complete project initialization
parent migration commit: b58624698cc2bcc4ef7bf3ea90e3b6e14127d1df
```

The remote repository, visibility, default branch, and commit SHA were read back through the GitHub connector on 2026-08-25.

## Validation state

User-provided local execution evidence:

```text
npm run verify: passed
production build: passed
static pages generated: 16
local and remote SHA: matched
working tree: clean
```

This local verification report has not been independently rerun by the assistant. The remote commit currently exposes no GitHub commit-status checks, so it must not be described as GitHub Actions validation.

Current product boundary:

```text
repository initialization: verified
source push and remote readback: verified
production deployment: not verified
live browser behavior: not verified
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

The bundle was cloned back successfully before the remote repository was created. These files remain migration evidence, not the current code authority.

## Authority boundary

- `idaibin/ai-handbook`: experiment contracts, research, validation evidence, and project pointer.
- `idaibin/prompts-hub`: application code, application releases, deployment configuration, and product issues.
- Google Drive: migration evidence and future large original image assets.

## Next gate

Deploy `idaibin/prompts-hub@2d9b9640228023e2e0c775a349a34124b4d8573a`, then preserve:

```text
deployment provider and project identity
deployment commit SHA
production URL
build logs or deployment receipt
HTTP availability
browser validation at desktop and mobile sizes
prompt search and detail-route checks
custom domain state
```

Until those checks pass, deployment and online operation remain `not_verified`.