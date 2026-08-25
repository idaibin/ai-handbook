import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import {
  catalogSnapshot,
  findCatalogRecord,
  loadCatalog,
  parseQueryExpression,
  queryCatalog,
  queryCatalogWithRelated,
} from "../prototype/catalog.mjs";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const catalog = loadCatalog(root);

assert.equal(catalog.length, 11);
assert.equal(new Set(catalog.map((record) => record.id)).size, catalog.length);
assert.equal(catalog.filter((record) => record.kind === "contract").length, 3);
assert.equal(catalog.filter((record) => record.kind === "image_case").length, 2);
assert.equal(catalog.filter((record) => record.kind === "prompt_case").length, 1);
assert.equal(catalog.filter((record) => record.kind === "generation_batch").length, 1);
assert.equal(catalog.filter((record) => record.kind === "image_result").length, 4);

const firstSnapshot = catalogSnapshot(catalog);
const secondSnapshot = catalogSnapshot(loadCatalog(root));
assert.deepEqual(firstSnapshot, secondSnapshot, "catalog snapshot is not deterministic");

const exact = queryCatalog(catalog, "historical_han_realism");
assert.equal(exact[0].id, "historical_han_realism");

const chinese = queryCatalog(catalog, "班超");
assert.equal(chinese[0].id, "han_writing_room_prompt_comparison");
assert.ok(chinese[0].matched_fields.includes("name") || chinese[0].matched_fields.includes("description"));

const catPrompt = queryCatalog(catalog, "橘猫 图书管理员", { kind: "prompt_case" });
assert.equal(catPrompt.length, 1);
assert.equal(catPrompt[0].id, "anthropomorphic_watercolor_cat_librarian_v01");
assert.equal(catPrompt[0].style_id, "anthropomorphic_watercolor");
assert.equal(catPrompt[0].result_count, 0);
assert.equal(catPrompt[0].has_image, false);

const dashboard = queryCatalog(catalog, "dashboard", { consumer: "ui_spec" });
assert.ok(dashboard.some((item) => item.id === "saas_bento_dashboard"));
assert.ok(dashboard.some((item) => item.id === "saas_dashboard_prompt_comparison"));

const examples = queryCatalog(catalog, "prompt", { kind: "image_case" });
assert.equal(examples.length, 2);
assert.ok(examples.every((item) => item.kind === "image_case"));

const targetFilter = queryCatalog(catalog, "", { kind: "image_case", target: "gemini" });
assert.equal(targetFilter.length, 2);

const pendingResults = queryCatalog(catalog, "", {
  kind: "image_result",
  status: "pending",
  has_image: false,
  has_receipt: false,
});
assert.equal(pendingResults.length, 4);

const batch = queryCatalog(catalog, "output shape violation", { kind: "generation_batch" });
assert.equal(batch.length, 1);
assert.equal(batch[0].status, "blocked");

const grouped = queryCatalogWithRelated(catalog, "anthropomorphic watercolor fox", {
  kind: "prompt_case",
});
assert.equal(grouped.exact_results.length, 0);
assert.equal(grouped.related_results.length, 1);
assert.equal(grouped.related_results[0].id, "anthropomorphic_watercolor_cat_librarian_v01");
assert.deepEqual(grouped.related_results[0].missing_terms, ["fox"]);

const expression = parseQueryExpression(
  'watercolor style:anthropomorphic_watercolor status:generation_blocked has:no-image has:no-receipt count:>=0',
);
assert.equal(expression.query, "watercolor");
assert.deepEqual(expression.filters, {
  style: "anthropomorphic_watercolor",
  status: "generation_blocked",
  has_image: false,
  has_receipt: false,
  count_min: 0,
});

assert.equal(findCatalogRecord(catalog, "minimal_tech_cover")?.kind, "contract");
assert.equal(
  findCatalogRecord(catalog, "anthropomorphic_watercolor_cat_librarian_v01__r01")?.kind,
  "image_result",
);
assert.equal(findCatalogRecord(catalog, "unknown"), null);

const cli = spawnSync(
  process.execPath,
  ["prototype/query-cli.mjs", "search", "班超", "--json"],
  { cwd: root, encoding: "utf8" },
);
assert.equal(cli.status, 0, cli.stderr);
const cliResult = JSON.parse(cli.stdout);
assert.equal(cliResult[0].id, "han_writing_room_prompt_comparison");

const groupedCli = spawnSync(
  process.execPath,
  [
    "prototype/query-cli.mjs",
    "search",
    "anthropomorphic",
    "watercolor",
    "fox",
    "kind:prompt_case",
    "--related",
    "--json",
  ],
  { cwd: root, encoding: "utf8" },
);
assert.equal(groupedCli.status, 0, groupedCli.stderr);
const groupedCliResult = JSON.parse(groupedCli.stdout);
assert.equal(groupedCliResult.exact_results.length, 0);
assert.equal(groupedCliResult.related_results[0].id, "anthropomorphic_watercolor_cat_librarian_v01");

const resultsCli = spawnSync(
  process.execPath,
  [
    "prototype/query-cli.mjs",
    "results",
    "anthropomorphic_watercolor_cat_librarian_v01",
    "--json",
  ],
  { cwd: root, encoding: "utf8" },
);
assert.equal(resultsCli.status, 0, resultsCli.stderr);
const resultRecords = JSON.parse(resultsCli.stdout);
assert.equal(resultRecords.length, 4);
assert.ok(resultRecords.every((item) => item.status === "pending"));
assert.ok(resultRecords.every((item) => item.drive_file_id === null));

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
  prompt_cases: 1,
  generation_batches: 1,
  image_results: 4,
  checks: [
    "stable_catalog",
    "exact_id_query",
    "unicode_query",
    "field_filters",
    "prompt_1vn_query",
    "generation_batch_query",
    "result_id_query",
    "query_expression",
    "exact_related_boundary",
    "cli_json_output",
    "unknown_id_rejected"
  ]
}, null, 2)}\n`);
