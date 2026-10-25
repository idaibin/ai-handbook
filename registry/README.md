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

## Optional reference projection (bounded pilot)

`references.json` is the Handbook-owned `handbook-reference-index/1` metadata
projection for five fixed-source references. It extends this Registry, not the
route or capability catalog. The source documents remain canonical; this file
contains no executable instructions or full prompt bodies. It is not complete
Handbook coverage or proof of cross-domain effectiveness.

Contract owner: `idaibin/ai-handbook`. Consumer: Forgeway's optional reference
lookup seam (separately versioned); existing professional capability discovery
and required delivery Gates remain unchanged. Unknown schema versions fail
validation; retirement requires an explicit version change and consumer migration.

- Index: `schema_version`, `owner`, `basis {repository, revision}`, `entries`.
- Entry: `id`, `kind`, `title`, `summary`, `topics`, `stages`, `applies_to`,
  `excludes`, `source`, `status`, `evidence`, `rights`, `freshness`.
- Source: `repository`, safe repository-relative `path`, immutable 40-hex
  `revision`, and content `sha256`; all entries share the declared basis.
- `kind`: method, interaction-pattern, prompt-case, audit-case, design-candidate.
- `status`: reference, candidate, historical. These are lifecycle labels, not proof.
- `evidence.level`: source-read, local-experiment, not-verified;
  `evidence.limitations` retains the original status and missing verification.
- `rights.status`: unknown, reference-only, licensed. `allowed_use` contains
  reference/adapt/copy; unknown/reference-only may only allow reference.
  Reference means read/link/analyze, not copy, adopt or publish. Licensed status
  is a declaration to recheck against the original license before reuse, not a
  permission grant from this validator. All pilot entries retain unknown rights.
- `freshness.checked_at`: ISO date; `recheck_when`: explicit change triggers.
  This is not a live freshness guarantee or a universal expiry period.

### Metadata-first consumption

The existing task owner decides whether a concrete knowledge need exists. No need
or empty topics means no snapshot load. Otherwise load metadata once, require the
caller's expected revision, and match exact topic tags (all requested tags), optional
stage (empty entry stages means cross-stage), kind/status/evidence restrictions,
all `applies_to` constraint tags and no `excludes` intersections. Do not infer semantic
constraints from keywords or run fuzzy ranking. Related candidates are not hits.
Default eligible status/evidence is reference/source-read; candidate or local
experiment access must be explicit and never upgrades evidence.

Only selected fixed source references may be handed to the current authorized
reader. The lookup itself reads no bodies and runs no tool, Skill or generator.
No match skips this optional input. Unavailable, malformed or stale snapshots are
not no-match. Never silently replace a fixed locator with main. Current project
facts, accepted design, components and tokens always outrank reference material;
missing required inputs/capabilities still retain their existing Gates. Unselected
private-media entries can describe candidates but cannot approve or fetch media.

### Maintenance and validation

On source revision/content, applicability, rights or evidence change, revise the
entry and recheck its source. Maps link this projection rather than repeating the
metadata. Do not relabel old evidence as current or auto-ingest entire libraries.
The producer verifies source bytes explicitly; normal metadata validation performs
no source-body reads. No network is used by either validator.

```bash
python3 registry/validate.py
python3 registry/validate.py --check-reference-sources
python3 -m unittest registry/test_validate.py registry/test_references.py
```

`source_bytes_checked` distinguishes these two checks. Source hashing against an
available local copy proves those bytes, not remote availability or runtime effect.
The fixed pilot basis is 1859577953ae342dadf265a7e1172d4e62574c5f; it does not merge
or supersede separate research branches.

### Bounded acceptance matrix

Consumer tests must observe actual snapshot/body call counts, not merely these
statements. This producer's tests cover metadata validity and source identities.

| Need | Exact query/condition | Expected consumer result |
| --- | --- | --- |
| Sticky UI guidance | topic sticky; stage design | hit scroll-interactions; metadata only |
| Database sharding | topic database-sharding | miss in this sample, not proof of global absence |
| Routine typo correction | no reference need | skipped; snapshot/body reads 0/0 |
| Empty query | no topics | skipped; snapshot/body reads 0/0 |
| Verified mobile touch | topic scroll; constraint verified-mobile-touch | related, not hit; no body read |
| Wrong snapshot revision | expected revision differs | stale, not miss; no body read |
| Prompt comparison | topic prompt-comparison | candidate excluded by default; explicit candidate/not-verified allowance may return reference only |
| Project design conflict | topic image-first; constraint replace-project-design-system | excluded/related; target design authority preserved |
| Accepted UI design | topic forgeway-ui; constraint accepted-design | not hit; candidate must not become accepted |

Unknown rights, a prompt's imperative text, or a matching topic never authorize
copying, generation, private access, implementation or publication.

### Unicode and consumer resource bounds

Titles, summaries, tags and safe relative source paths accept Unicode, including
Chinese. Tags use exact string identity: no case folding, transliteration or Unicode
normalization is implied. A consumer must not reject otherwise valid Chinese tags
or paths merely because they are not ASCII; the real scroll entry includes Chinese
lookup tags. A synthetic Unicode path test proves metadata compatibility only, not
source existence. Controls, traversal and other unsafe paths remain forbidden.

Consumers may impose explicitly documented memory/input bounds. An otherwise valid
snapshot exceeding such a bound must report a distinct `resource-limit` outcome,
not `miss`, not a schema-invalid claim, and never silent truncation. Such limits do
not redefine this producer's versioned metadata contract.
