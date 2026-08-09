# enescingoz/awesome-n8n-templates workflow assessment

- Fixed commit: `2546df5f3da5ad12c9bbda4c51da39c3366c0d3e`
- Tree/content: `git-tree:2fb909ecde2d384da2d209621f9b870955598bf3`
- Observed: 24,544 Stars; `main`; not forked or archived
- License: root CC-BY-4.0; README says collected templates retain original authors' rights, so per-template rights remain unverified
- Evidence: `source_validated` through full static shape scan and sampled definitions; runtime not validated
- Subtype/topic fit: `workflow-template-collection`; conditional fit

## Verified

The repository contains 334 JSON files. A reproducible `jq -s` gate requiring one root object, a node array and connections object accepted 326; five files are malformed and three concatenate multiple top-level JSON documents. The accepted definitions contain 5,998 nodes and 205 node types; 321 contain trigger/webhook nodes. Thirty-six carry `active=true`, which is data only and not proof they auto-run after import.

Sampled workflows show real graphs: an email approval branch, research loops, a disk watchdog with static-data alert dedupe and Telegram-to-email fallback, and a Basic Auth webhook that runs unattended `sudo apt update && sudo apt upgrade -y` over SSH. The last sample has high-impact effects but no approval, idempotency or compensation. No collection-wide schema/lint/runtime test exists; the PR workflow is AI review rather than template execution.

## Inference

This is not an “awesome list without executable workflow”, but quality and licensing cannot be inherited from repository popularity. Each template needs import lint, credential cleanup, active-state review and effect analysis.

## Not verified

No template was imported or run. n8n/node version compatibility, community nodes, credential rebinding, retry behavior and original-author licensing remain unverified.

Evidence: [repository](https://github.com/enescingoz/awesome-n8n-templates/tree/2546df5f3da5ad12c9bbda4c51da39c3366c0d3e), [update webhook](https://github.com/enescingoz/awesome-n8n-templates/blob/2546df5f3da5ad12c9bbda4c51da39c3366c0d3e/devops/linux-update-via-webhook.json), [watchdog](https://github.com/enescingoz/awesome-n8n-templates/blob/2546df5f3da5ad12c9bbda4c51da39c3366c0d3e/devops/disk-space-watchdog.json).
