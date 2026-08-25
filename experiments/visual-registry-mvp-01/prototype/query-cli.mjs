#!/usr/bin/env node
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { compilePrompt } from "../dist/prototype/compiler.js";
import { catalogSnapshot, findCatalogRecord, loadCatalog, queryCatalog } from "./catalog.mjs";
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
  process.stderr.write(`Usage:\n  node prototype/query-cli.mjs list [--kind contract|image_case] [--category X] [--consumer X] [--status X] [--target X] [--json]\n  node prototype/query-cli.mjs search <query> [filters] [--limit N] [--json]\n  node prototype/query-cli.mjs show <id> [--json]\n  node prototype/query-cli.mjs compile <contract-id> --subject <text> --target gemini|flux|midjourney [--json]\n  node prototype/query-cli.mjs examples [query] [filters] [--json]\n  node prototype/query-cli.mjs prompt-set <image-case-id> [--json]\n`);
  process.exitCode = 2;
}

function filtersFrom(flags) {
  const limit = flags.limit === undefined ? undefined : Number(flags.limit);
  if (limit !== undefined && (!Number.isInteger(limit) || limit <= 0)) {
    throw new Error(`Invalid limit: ${flags.limit}`);
  }
  return {
    kind: flags.kind,
    category: flags.category,
    consumer: flags.consumer,
    status: flags.status,
    target: flags.target,
    limit,
  };
}

function print(value, json) {
  if (json) {
    process.stdout.write(`${JSON.stringify(value, null, 2)}\n`);
    return;
  }

  if (Array.isArray(value)) {
    for (const item of value) {
      const context = [item.kind, item.category, item.status, ...(item.consumers ?? [])]
        .filter(Boolean)
        .join(" | ");
      process.stdout.write(`${item.id}\t${item.name}\t${context}\n`);
    }
    return;
  }

  process.stdout.write(`${JSON.stringify(value, null, 2)}\n`);
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
      const query = parsed.positional.join(" ").trim();
      if (!query) throw new Error("search requires a query");
      print(queryCatalog(catalog, query, filtersFrom(parsed.flags)), asJson);
    } else if (command === "examples") {
      const query = parsed.positional.join(" ").trim();
      print(queryCatalog(catalog, query, { ...filtersFrom(parsed.flags), kind: "image_case" }), asJson);
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
