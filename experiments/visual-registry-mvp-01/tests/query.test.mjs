import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { catalogSnapshot, findCatalogRecord, loadCatalog, queryCatalog } from "../prototype/catalog.mjs";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const catalog = loadCatalog(root);

assert.equal(catalog.length, 5);
assert.equal(new Set(catalog.map((record) => record.id)).size, catalog.length);
assert.equal(catalog.filter((record) => record.kind === "contract").length, 3);
assert.equal(catalog.filter((record) => record.kind === "image_case").length, 2);

const firstSnapshot = catalogSnapshot(catalog);
const secondSnapshot = catalogSnapshot(loadCatalog(root));
assert.deepEqual(firstSnapshot, secondSnapshot, "catalog snapshot is not deterministic");

const exact = queryCatalog(catalog, "historical_han_realism");
assert.equal(exact[0].id, "historical_han_realism");

const chinese = queryCatalog(catalog, "班超");
assert.equal(chinese[0].id, "han_writing_room_prompt_comparison");
assert.ok(chinese[0].matched_fields.includes("name") || chinese[0].matched_fields.includes("description"));

const dashboard = queryCatalog(catalog, "dashboard", { consumer: "ui_spec" });
assert.ok(dashboard.some((item) => item.id === "saas_bento_dashboard"));
assert.ok(dashboard.some((item) => item.id === "saas_dashboard_prompt_comparison"));

const examples = queryCatalog(catalog, "prompt", { kind: "image_case" });
assert.equal(examples.length, 2);
assert.ok(examples.every((item) => item.kind === "image_case"));

const targetFilter = queryCatalog(catalog, "", { kind: "image_case", target: "gemini" });
assert.equal(targetFilter.length, 2);

assert.equal(findCatalogRecord(catalog, "minimal_tech_cover")?.kind, "contract");
assert.equal(findCatalogRecord(catalog, "unknown"), null);

const cli = spawnSync(
  process.execPath,
  ["prototype/query-cli.mjs", "search", "班超", "--json"],
  { cwd: root, encoding: "utf8" },
);
assert.equal(cli.status, 0, cli.stderr);
const cliResult = JSON.parse(cli.stdout);
assert.equal(cliResult[0].id, "han_writing_room_prompt_comparison");

const promptSet = spawnSync(
  process.execPath,
  ["prototype/query-cli.mjs", "prompt-set", "han_writing_room_prompt_comparison", "--json"],
  { cwd: root, encoding: "utf8" },
);
assert.equal(promptSet.status, 0, promptSet.stderr);
assert.equal(JSON.parse(promptSet.stdout).variants.length, 3);

const invalid = spawnSync(
  process.execPath,
  ["prototype/query-cli.mjs", "show", "unknown", "--json"],
  { cwd: root, encoding: "utf8" },
);
assert.notEqual(invalid.status, 0);
assert.match(invalid.stderr, /Unknown registry id/);

process.stdout.write(`${JSON.stringify({
  status: "passed",
  records: catalog.length,
  contracts: 3,
  image_cases: 2,
  checks: [
    "stable_catalog",
    "exact_id_query",
    "unicode_query",
    "field_filters",
    "image_case_query",
    "cli_json_output",
    "unknown_id_rejected"
  ]
}, null, 2)}\n`);
