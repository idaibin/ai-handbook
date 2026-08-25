import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join, relative } from "node:path";

function readJson(path) {
  return JSON.parse(readFileSync(path, "utf8"));
}

function normalize(value) {
  return String(value ?? "")
    .normalize("NFKC")
    .toLocaleLowerCase("en-US")
    .replace(/[\p{P}\p{S}_/\\-]+/gu, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function stringsFrom(value, output = []) {
  if (typeof value === "string") {
    output.push(value);
  } else if (Array.isArray(value)) {
    for (const item of value) stringsFrom(item, output);
  } else if (value && typeof value === "object") {
    for (const item of Object.values(value)) stringsFrom(item, output);
  }
  return output;
}

function field(name, weight, values) {
  return {
    name,
    weight,
    values: [...new Set(values.filter(Boolean).map((value) => String(value)))],
  };
}

function contractRecord(root, path, document) {
  return {
    kind: "contract",
    id: document.id,
    name: document.name,
    description: document.description,
    path: relative(root, path).replaceAll("\\", "/"),
    category: document.category,
    consumers: document.metadata?.consumers ?? [],
    status: document.metadata?.status ?? "unknown",
    target: null,
    document,
    fields: [
      field("id", 14, [document.id]),
      field("name", 11, [document.name]),
      field("description", 7, [document.description]),
      field("category", 6, [document.category]),
      field("consumer", 6, document.metadata?.consumers ?? []),
      field("intent", 5, stringsFrom(document.intent)),
      field("visual_language", 4, stringsFrom(document.visual_language)),
      field("camera", 3, stringsFrom(document.camera)),
      field("lighting", 3, stringsFrom(document.lighting)),
      field("composition", 3, stringsFrom(document.composition)),
      field("constraints", 2, stringsFrom(document.constraints)),
      field("defaults", 2, stringsFrom(document.defaults)),
    ],
  };
}

function imageCaseRecord(root, path, document, contracts) {
  const contract = contracts.get(document.contract_id);
  return {
    kind: "image_case",
    id: document.id,
    name: document.title,
    description: document.description,
    path: relative(root, path).replaceAll("\\", "/"),
    category: contract?.category ?? null,
    consumers: [document.consumer],
    status: document.metadata?.status ?? "unknown",
    target: document.target,
    document,
    fields: [
      field("id", 14, [document.id]),
      field("name", 11, [document.title]),
      field("description", 7, [document.description]),
      field("contract", 9, [document.contract_id, contract?.name]),
      field("subject", 8, [document.subject]),
      field("category", 6, [contract?.category]),
      field("consumer", 6, [document.consumer]),
      field("target", 5, [document.target]),
      field("comparison_axis", 5, [document.comparison_axis]),
      field("variant", 4, stringsFrom(document.variants)),
      field("review", 3, stringsFrom(document.review)),
    ],
  };
}

export function loadCatalog(root) {
  const records = [];
  const contracts = new Map();
  const contractsDir = join(root, "contracts");

  for (const name of readdirSync(contractsDir).filter((item) => item.endsWith(".json")).sort()) {
    const path = join(contractsDir, name);
    const document = readJson(path);
    contracts.set(document.id, document);
    records.push(contractRecord(root, path, document));
  }

  const imageCasesDir = join(root, "image-cases");
  if (existsSync(imageCasesDir)) {
    for (const name of readdirSync(imageCasesDir).filter((item) => item.endsWith(".json")).sort()) {
      const path = join(imageCasesDir, name);
      const document = readJson(path);
      records.push(imageCaseRecord(root, path, document, contracts));
    }
  }

  const seen = new Set();
  for (const record of records) {
    if (seen.has(record.id)) throw new Error(`Duplicate registry id: ${record.id}`);
    seen.add(record.id);
  }

  return records.sort((a, b) => a.kind.localeCompare(b.kind) || a.id.localeCompare(b.id));
}

function matchesFilter(record, filters) {
  if (filters.kind && record.kind !== filters.kind) return false;
  if (filters.category && record.category !== filters.category) return false;
  if (filters.consumer && !record.consumers.includes(filters.consumer)) return false;
  if (filters.status && record.status !== filters.status) return false;
  if (filters.target && record.target !== filters.target) return false;
  return true;
}

function scoreRecord(record, query) {
  const normalizedQuery = normalize(query);
  if (!normalizedQuery) return { score: 0, matched_fields: [] };

  const tokens = [...new Set(normalizedQuery.split(" ").filter(Boolean))];
  const matchedFields = new Set();
  let total = 0;

  for (const token of tokens) {
    let tokenScore = 0;
    let tokenField = null;

    for (const group of record.fields) {
      for (const value of group.values) {
        const normalizedValue = normalize(value);
        if (!normalizedValue) continue;

        let score = 0;
        if (normalizedValue === token) score = group.weight * 5;
        else if (normalizedValue.startsWith(token)) score = group.weight * 3;
        else if (normalizedValue.includes(token)) score = group.weight * 2;
        else if (normalizedValue.split(" ").some((part) => part.startsWith(token))) score = group.weight;

        if (score > tokenScore) {
          tokenScore = score;
          tokenField = group.name;
        }
      }
    }

    if (tokenScore === 0) return null;
    total += tokenScore;
    if (tokenField) matchedFields.add(tokenField);
  }

  for (const group of record.fields) {
    if (group.values.some((value) => normalize(value).includes(normalizedQuery))) {
      total += group.weight * 4;
      matchedFields.add(group.name);
    }
  }

  return { score: total, matched_fields: [...matchedFields].sort() };
}

export function queryCatalog(catalog, query = "", filters = {}) {
  const limit = Number.isInteger(filters.limit) && filters.limit > 0 ? filters.limit : 20;
  const results = [];

  for (const record of catalog) {
    if (!matchesFilter(record, filters)) continue;
    const scored = scoreRecord(record, query);
    if (scored === null) continue;
    results.push({
      kind: record.kind,
      id: record.id,
      name: record.name,
      description: record.description,
      path: record.path,
      category: record.category,
      consumers: record.consumers,
      status: record.status,
      target: record.target,
      score: scored.score,
      matched_fields: scored.matched_fields,
    });
  }

  return results
    .sort((a, b) => b.score - a.score || a.kind.localeCompare(b.kind) || a.id.localeCompare(b.id))
    .slice(0, limit);
}

export function findCatalogRecord(catalog, id) {
  return catalog.find((record) => record.id === id) ?? null;
}

export function catalogSnapshot(catalog) {
  return catalog.map((record) => ({
    kind: record.kind,
    id: record.id,
    name: record.name,
    description: record.description,
    path: record.path,
    category: record.category,
    consumers: record.consumers,
    status: record.status,
    target: record.target,
  }));
}
