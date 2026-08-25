# Visual Registry Web MVP — Next.js Delivery

Status: `nextjs_react_mvp_built_and_browser_verified`

## Active implementation

```text
experiments/visual-registry-mvp-01/web/
```

Framework boundary:

- Next.js App Router
- React Client Components
- TypeScript
- static export from `next build`
- no hand-authored standalone HTML application
- no hand-authored browser JavaScript application

The earlier Drive-only `index.html` prototype is superseded and is not an active deliverable.

## Implemented routes

```text
/
/prompts/[promptId]
```

The home route supports free-text search and filters over typed Registry projection data. The prompt route keeps Prompt text, metadata, and ImageResult slots as separate UI regions; Prompt content is never embedded into an image asset.

## Data boundary

The web app is a read-only projection over the experiment Registry:

```text
VisualContract
PromptCase
GenerationBatch
ImageResult
```

Current image state remains truthful:

```text
provider_native_images: 0/4
saved_result_files: 0/4
```

No collage, report image, contact sheet, Dashboard, or infographic is presented as an independent result.

## Verification

Clean-checkout validation sequence:

```bash
npm install --no-audit --no-fund
node scripts/validate-nextjs-source.mjs
npm run typecheck
npm run build
npm run assert:export
```

Browser verification used the static export and checked:

- desktop `1440x1000` home rendering;
- search interaction;
- Prompt detail navigation;
- mobile `390x844` rendering.

The corrected source validator scans only authored application roots and excludes `node_modules`, `.next`, `out`, `.git`, `.vercel`, and coverage artifacts.

## Delivery artifacts

Drive and local delivery packages contain:

- Next.js source archive;
- static export archive;
- browser screenshot evidence;
- delivery manifest with SHA-256 identities.

## Remaining boundary

This delivery verifies the searchable React/Next.js web projection. It does not verify four independent provider-native Prompt images, because those assets do not yet exist.
