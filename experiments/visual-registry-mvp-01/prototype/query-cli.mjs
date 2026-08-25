#!/usr/bin/env node
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { compilePrompt } from "../dist/prototype/compiler.js";
import {
  catalogSnapshot,
  findCatalogRecord,
  loadCatalog,
  parseQueryExpression,
  queryCatalog,
  queryCatalogWithRelated,
} from "./catalog.mjs";
import { buildPromptSet } from "./image-case-demo.mjs";

function parse(argv) {
  const positional = [];
  const flags = {};
  for (let index = 0; index < argv.length; index += 1) {
    const value = argv[index];
    if (!value.startsWith("--")) {
      positional.push(value);
      continue;
    }
    const key = value.slice(2).replaceAll("-", "_");
    const next = argv[index + 1];
    if (next && !next.startsWith("--")) {
      flags[key] = next;
      index += 1;
    } else {
      flags[key] = true;
    }
  }
  return { positional, flags };
}

function usage(message) {
  if (message) process.stderr.write(`${message}\n\n`);
  process.stderr.write(`Usage:\n  node prototype/query-cli.mjs list [filters] [--json]\n  node prototype/query-cli.mjs search <query expression> [filters] [--related] [--limit N] [--json]\n  node prototype/query-cli.mjs show <id> [--json]\n  node prototype/query-cli.mjs compile <contract-id> --subject <text> --target gemini|flux|midjourney [--json]\n  node prototype/query-cli.mjs examples [query expression] [filters] [--related] [--json]\n  node prototype/query-cli.mjs prompt-set <image-case-id> [--json]\n  node prototype/query-cli.mjs results <prompt-id> [--json]\n\nFilters:\n  --kind contract|image_case|prompt_case|generation_batch|image_result\n  --category X --consumer X --status X --target X --style X\n  --provider X --model X --has-image true|false --has-receipt true|false\n  --count-min N\n\nQuery expression fields:\n  style:X provider:X model:X status:X kind:X consumer:X target:X\n  has:image has:receipt has:no-image has:no-receipt count:>=N\n`);
  process.exitCode = 2;
}

function parseBoolean(name, value) {
  if (value === undefined) return undefined;
  if (value === true || value === "true") return true;
  if (value === false || value === "false") return false;
  throw new Error(`Invalid ${name}: ${value}`);
}

function filtersFrom(flags) {
  const limit = flags.limit === undefined ? undefined : Number(flags.limit);
  if (limit !== undefined && (!Number.isInteger(limit) || limit <= 0)) {
    throw new Error(`Invalid limit: ${flags.limit}`);
  }

  const countMin = flags.count_min === undefined ? undefined : Number(flags.count_min);
  if (countMin !== undefined && (!Number.isInteger(countMin) || countMin < 0)) {
    throw new Error(`Invalid count-min: ${flags.count_min}`);
  }

  return {
    kind: flags.kind,
    category: flags.category,
    consumer: flags.consumer,
    status: flags.status,
    target: flags.target,
    style: flags.style,
    provider: flags.provider,
    model: flags.model,
    has_image: parseBoolean("has-image", flags.has_image),
    has_receipt: parseBoolean("has-receipt", flags.has_receipt),
    count_min: countMin,
    limit,
  };
}

function compactFilters(filters) {
  return Object.fromEntries(Object.entries(filters).filter(([, value]) => value !== undefined));
}

function printArray(value) {
  for (const item of value) {
    const context = [
      item.kind,
      item.category,
      item.status,
      item.style_id,
      ...(item.providers ?? []),
      ...(item.consumers ?? []),
    ]
      .filter(Boolean)
      .join(" | ");
    process.stdout.write(`${item.id}\t${item.name}\t${context}\n`);
  }
}

function print(value, json) {
  if (json) {
    process.stdout.write(`${JSON.stringify(value, null, 2)}\n`);
    return;
  }

  if (Array.isArray(value)) {
    printArray(value);
    return;
  }

  if (value && Array.isArray(value.exact_results) && Array.isArray(value.related_results)) {
    process.stdout.write("EXACT\n");
    printArray(value.exact_results);
    process.stdout.write("RELATED\n");
    printArray(value.related_results);
    return;
  }

  process.stdout.write(`${JSON.stringify(value, null, 2)}\n`);
}

function runSearch(catalog, rawQuery, flags, forcedFilters = {}) {
  const parsedExpression = parseQueryExpression(rawQuery);
  const filters = {
    ...parsedExpression.filters,
    ...compactFilters(filtersFrom(flags)),
    ...forcedFilters,
  };
  if (flags.related === true) {
    return queryCatalogWithRelated(catalog, parsedExpression.query, filters);
  }
  return queryCatalog(catalog, parsedExpression.query, filters);
}

const parsed = parse(process.argv.slice(2));
const command = parsed.positional.shift();
if (!command) {
  usage();
} else {
  try {
    const here = dirname(fileURLToPath(import.meta.url));
    const root = parsed.flags.root ? resolve(String(parsed.flags.root)) : resolve(here, "..");
    const catalog = loadCatalog(root);
    const asJson = parsed.flags.json === true;

    if (command === "list") {
      print(queryCatalog(catalog, "", filtersFrom(parsed.flags)), asJson);
    } else if (command === "search") {
      const rawQuery = parsed.positional.join(" ").trim();
      if (!rawQuery) throw new Error("search requires a query");
      print(runSearch(catalog, rawQuery, parsed.flags), asJson);
    } else if (command === "examples") {
      const rawQuery = parsed.positional.join(" ").trim();
      print(runSearch(catalog, rawQuery, parsed.flags, { kind: "image_case" }), asJson);
    } else if (command === "show") {
      const id = parsed.positional[0];
      if (!id) throw new Error("show requires an id");
      const record = findCatalogRecord(catalog, id);
      if (!record) throw new Error(`Unknown registry id: ${id}`);
      print({
        kind: record.kind,
        id: record.id,
        path: record.path,
        document: record.document,
      }, true);
    } else if (command === "compile") {
      const id = parsed.positional[0];
      const subject = parsed.flags.subject;
      const target = parsed.flags.target;
      if (!id || typeof subject !== "string" || typeof target !== "string") {
        throw new Error("compile requires <contract-id>, --subject, and --target");
      }
      const record = findCatalogRecord(catalog, id);
      if (!record || record.kind !== "contract") throw new Error(`Unknown contract id: ${id}`);
      print(compilePrompt({ target, subject, contract: record.document }), true);
    } else if (command === "prompt-set") {
      const id = parsed.positional[0];
      if (!id) throw new Error("prompt-set requires an image-case id");
      const imageCase = findCatalogRecord(catalog, id);
      if (!imageCase || imageCase.kind !== "image_case") throw new Error(`Unknown image-case id: ${id}`);
      const contract = findCatalogRecord(catalog, imageCase.document.contract_id);
      if (!contract || contract.kind !== "contract") {
        throw new Error(`Missing contract: ${imageCase.document.contract_id}`);
      }
      print(buildPromptSet(imageCase.document, contract.document), true);
    } else if (command === "results") {
      const id = parsed.positional[0];
      if (!id) throw new Error("results requires a prompt id");
      const promptCase = findCatalogRecord(catalog, id);
      if (!promptCase || promptCase.kind !== "prompt_case") throw new Error(`Unknown prompt id: ${id}`);
      const results = promptCase.document.generation_batches.flatMap((batch) =>
        batch.results.map((result) => ({
          prompt_id: promptCase.document.prompt_id,
          batch_id: batch.batch_id,
          provider: batch.provider,
          model: batch.model,
          ...result,
        })),
      );
      print(results, true);
    } else if (command === "snapshot") {
      print(catalogSnapshot(catalog), true);
    } else {
      usage(`Unknown command: ${command}`);
    }
  } catch (error) {
    process.stderr.write(`${error instanceof Error ? error.message : String(error)}\n`);
    process.exitCode = 1;
  }
}
