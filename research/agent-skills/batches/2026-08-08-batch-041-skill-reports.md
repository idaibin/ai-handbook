# Agent Skills Individual Reports — Batch 041

- Batch ID: `2026-08-08-batch-041`
- Completed repository identities: **10**
- Direct `SKILL.md` reads: **11**
- Direct unique skill bodies reviewed: **5**
- New canonical individual skill reports: **2**
- Existing canonical content mappings: **8 repository identities**
- Runtime/build/test/eval execution: **not_executed**

## Repository → canonical content mapping

| Repository identity | Direct body read in this batch | Canonical action |
|---|---|---|
| `francktienta-lgtm/Anthropic-Cybersecurity-Skills` | `performing-memory-forensics-with-volatility3` | map exact `2c88b96...` collection content to Batch 039 canonical analysis |
| `AbuAli1393/Anthropic-Cybersecurity-Skills` | `performing-memory-forensics-with-volatility3` | same exact `2c88b96...` mapping; no duplicate report |
| `sirameshg/Anthropic-Cybersecurity-Skills` | `performing-memory-forensics-with-volatility3` | same exact `2c88b96...` mapping; no duplicate report |
| `CYPKNFT/Anthropic-Cybersecurity-Skills` | `performing-memory-forensics-with-volatility3` | map `c15f73db...` lineage to Batch 040 canonical analysis |
| `young9471/Anthropic-Cybersecurity-Skills` | `performing-memory-forensics-with-volatility3` | same exact `2c88b96...` mapping; no duplicate report |
| `ABe-er/dreamina-cli-skill` | `dreamina-cli` | exact `75e0a69...` Dreamina content already canonicalized in Batch 040 |
| `barrettsoron/civic-skills` | `canadian-civic-data`, `news-analysis` | **2 new canonical reports below** |
| `justanotherkevin/almost-social-skills` | `top-design` | exact `955115...` Wondel snapshot mapping; no duplicate report |
| `welma-git/wondelai-skills` | `top-design` | exact `955115...` Wondel snapshot mapping; no duplicate report |
| `bmersereau/skills` | `top-design` | exact `955115...` Wondel snapshot mapping; no duplicate report |

The mapping deliberately separates repository identity coverage from canonical skill-body coverage. Exact Git-content mirrors are content-gated at the repository level but do not generate duplicate canonical reports.

---

## New canonical report 1 — `canadian-civic-data`

### Identity

- Repository: `barrettsoron/civic-skills`
- Pinned repository revision: `087758437fb95a73769823619c76a0a9f2206c9d`
- Skill path: `canadian-civic-data/SKILL.md`
- Skill blob: `efdac13753a9acc62419ec1b93bee9c319d85485`
- Declared version: `1.0`
- Declared license: MIT
- Runtime requirement: internet access; declared no API keys required for routed sources

### Purpose and routing model

The skill is a knowledge/router skill for Canadian public civic data. It routes four request classes to four source-specific references:

- elected officials → Represent API;
- MP votes / Hansard → openparliament.ca;
- bills / committee evidence → LEGISinfo;
- election results / campaign finance → Elections Canada.

It explicitly instructs the agent to load only the relevant reference before making an API call. That is a useful context-control pattern: routing decisions stay in the small `SKILL.md`, while endpoint detail is deferred to references.

### What is actually implemented

- **Implemented:** structured frontmatter, operation router, source-specific reference documents, source/coverage caveats, pagination/API usage examples.
- **Not implemented:** repository-local HTTP client, typed response schemas, retry/backoff policy, freshness checks, response normalization, executable validation, fixtures, or behavioral evals.
- **Execution model:** the LLM/host is expected to translate reference documentation into live HTTP calls.

### Strengths

1. **Narrow source routing.** The skill avoids loading all civic documentation for every question.
2. **Source boundaries are explicit.** Coverage dates and ambiguities such as federal/provincial/municipal officials are called out.
3. **Public/open-data posture is clear.** The repository explicitly rejects surveillance, mass scraping, and access-control circumvention.
4. **References contain usable operational detail.** The openparliament reference includes endpoint patterns, filters, pagination, and multi-step query examples.

### Findings / risks

1. **Documentation drift — high.** The root repository README still gives a lobbying example, while the current Skill routes only four sources and has removed lobbying. A stale `references/lobbying.md` remains. An agent can therefore receive contradictory capability signals depending on which file it reads.
2. **Static freshness — medium.** The reference material embeds time-sensitive facts such as the “current” parliamentary session. These facts can become stale independently of the Skill version.
3. **No contract verification — high.** Endpoint shapes, availability, paging, and source coverage are described but not exercised by fixture/live tests.
4. **No provenance output contract — medium.** The Skill does not require a normalized result structure containing source URL, retrieval time, query parameters, and uncertainty, which matters for research use.
5. **No deterministic error model — medium.** Network errors, schema changes, partial responses, and rate limits are left to the host agent.

### Recommended reusable design

Keep the small router/reference separation, but add a minimal deterministic adapter layer:

```text
request intent
→ source router
→ typed source adapter
→ normalized provenance result
→ fixture/live-contract verification
```

Each adapter should expose a stable result envelope with `source`, `retrieved_at`, `query`, `records`, `next_page`, and `warnings`. Reference files then describe semantics instead of doubling as executable protocol contracts.

### Verification status

- `SKILL.md`: directly read
- repository tree: directly inspected
- representative reference: directly read
- scripts: none surfaced for this Skill
- tests/evals: none surfaced
- live source calls: **not executed**

### Verdict

**Useful router/reference pattern; not runtime-certified.** Reuse the context-routing design, but fix lobbying drift and add source adapters plus contract tests before depending on it for reproducible civic research.

---

## New canonical report 2 — `news-analysis`

### Identity

- Repository: `barrettsoron/civic-skills`
- Pinned repository revision: `087758437fb95a73769823619c76a0a9f2206c9d`
- Skill path: `news-analysis/SKILL.md`
- Skill blob: `2dd1bf45a9122e87daff51bcf157ca8a3ebc38f9`
- Declared version: `1.0`
- Declared license: MIT
- Runtime requirement: internet access; Guardian key for Guardian API, open access for GDELT/RSS as documented

### Purpose and routing model

The skill routes news-research tasks across three source modes:

- Guardian API for article/full-text search;
- GDELT for cross-language, longitudinal, event, and coverage analysis;
- Canadian RSS feeds for CBC/The Tyee headlines.

Like the civic-data skill, it keeps the root body small and loads one reference according to task intent.

### What is actually implemented

- **Implemented:** source router, source-selection guidance, reference documents for Guardian/GDELT/RSS, caveats about GDELT interfaces and RSS parsing.
- **Not implemented:** repository-local feed/API clients, canonical article schema, deduplication engine, publication-time normalization, source-quality model, rate-limit controller, fixtures, or behavioral evals.
- **Execution model:** the host agent is responsible for issuing and parsing live requests.

### Strengths

1. **Correctly separates two GDELT interfaces.** The reference distinguishes DOC 2.0 article search from the event database rather than treating GDELT as one generic endpoint.
2. **Caveats are visible.** Tone scores are framed as imperfect signals, and source coverage bias is acknowledged.
3. **Routing is task-oriented.** Full text, cross-language trend analysis, and Canadian headline monitoring are not collapsed into one source.
4. **Reference loading is selective.** This scales better than embedding all source details in one monolithic Skill body.

### Findings / risks

1. **No live/source contract verification — high.** API limits, endpoint behavior, result schemas, RSS availability, and source capabilities can change; the repository itself says most endpoints have not been tested in real use cases.
2. **No deduplication/provenance contract — high.** Cross-source news analysis needs canonical URLs, publication timestamps, retrieval timestamps, source identity, language, and duplicate clustering. None is enforced by code.
3. **Static rate/feature claims — medium.** Statements such as Guardian free-tier limits or GDELT behavior are time-sensitive and need a last-verified marker or executable smoke test.
4. **HTTP/raw-data caveat — medium.** The GDELT reference documents raw event files over HTTP. A production adapter should make transport/security policy explicit rather than leaving it to arbitrary host behavior.
5. **Analysis quality is unspecified — medium.** The Skill explains how to retrieve coverage, but there is no eval for whether comparison, trend, tone, or summarization conclusions are accurate or appropriately caveated.

### Recommended reusable design

Retain the router/reference split, then normalize every source into one evidence record before synthesis:

```text
source adapter
→ canonical article/event record
→ dedupe + timestamp/language normalization
→ evidence set with provenance
→ analysis/synthesis
```

A small fixture corpus should cover duplicate articles, missing timestamps, multilingual records, pagination, malformed RSS, and partial API failures. Live smoke tests should be separated from deterministic fixture tests.

### Verification status

- `SKILL.md`: directly read
- repository tree: directly inspected
- GDELT reference: directly read
- scripts: none surfaced for this Skill
- tests/evals: none surfaced
- live source calls: **not executed**

### Verdict

**Good source-routing knowledge Skill; insufficiently deterministic for repeatable news research.** The main gap is executable source normalization and evidence/provenance testing, not additional descriptive prose.

---

## Existing canonical mappings revalidated in this batch

### `performing-memory-forensics-with-volatility3`

Directly reread from five repository identities. Four identities share the exact `2c88b96...` collection revision and one uses the already-reviewed `c15f73db...` lineage. No new canonical report was created. This batch does not reproduce or extend operational cybersecurity instructions and did not execute the procedure.

### `dreamina-cli`

Directly reread from `ABe-er/dreamina-cli-skill`. The pinned revision is the exact wrapper content already reviewed in Batch 040: real Python wrapper, structured JSON, local validation, command normalization, and `--dry-run`; no new canonical report.

### `top-design`

Directly reread from three exact `955115...` Wondel-derived identities. The body is the same versioned content already reviewed in prior batches. The explicit custom-cursor opt-in rule is retained as a useful authorization boundary, while weighted aesthetic scores remain subjective heuristics rather than validated acceptance criteria.

## Batch conclusion

Batch 041 adds **2** new canonical individual reports and **10** repository-identity completions. Exact mirrors were reread at the repository boundary but deduplicated at the canonical skill-body boundary. No runtime/build/test/eval success is claimed.