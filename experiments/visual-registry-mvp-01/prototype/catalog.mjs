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

function unique(values) {
  return [...new Set(values.filter((value) => value !== null && value !== undefined && value !== ""))];
}

function field(name, weight, values) {
  return {
    name,
    weight,
    values: unique(values.map((value) => String(value))),
  };
}

function resultHasImage(result) {
  return Boolean(result.drive_file_id && result.image_sha256 && result.width && result.height);
}

function resultHasReceipt(result) {
  return Boolean(result.provider_receipt);
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
    style_id: document.id,
    providers: [],
    models: [],
    has_image: false,
    has_receipt: false,
    result_count: 0,
    document,
    fields: [
      field("id", 14, [document.id]),
      field("name", 11, [document.name]),
      field("description", 7, [document.description]),
      field("category", 6, [document.category]),
      field("style", 9, [document.id]),
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
    style_id: document.contract_id,
    providers: [document.target],
    models: [],
    has_image: false,
    has_receipt: false,
    result_count: 0,
    document,
    fields: [
      field("id", 14, [document.id]),
      field("name", 11, [document.title]),
      field("description", 7, [document.description]),
      field("contract", 9, [document.contract_id, contract?.name]),
      field("style", 9, [document.contract_id]),
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

function promptCaseRecord(root, path, document) {
  const batches = document.generation_batches ?? [];
  const results = batches.flatMap((batch) => batch.results ?? []);
  const validResults = results.filter(resultHasImage);
  return {
    kind: "prompt_case",
    id: document.prompt_id,
    name: `${document.style_id}: ${document.subject}`,
    description: document.subject,
    path: relative(root, path).replaceAll("\\", "/"),
    category: "illustration",
    consumers: document.metadata?.consumers ?? [],
    status: document.metadata?.status ?? "unknown",
    target: null,
    style_id: document.style_id,
    providers: unique(batches.map((batch) => batch.provider)),
    models: unique(batches.map((batch) => batch.model)),
    has_image: validResults.length > 0,
    has_receipt: results.some(resultHasReceipt),
    result_count: validResults.length,
    requested_count: batches.reduce((sum, batch) => sum + Number(batch.requested_count ?? 0), 0),
    document,
    fields: [
      field("id", 14, [document.prompt_id]),
      field("style", 12, [document.style_id]),
      field("subject", 10, [document.subject]),
      field("prompt", 7, [document.prompt_text]),
      field("tag", 8, document.tags ?? []),
      field("consumer", 6, document.metadata?.consumers ?? []),
      field("status", 4, [document.metadata?.status]),
      field("batch", 3, batches.map((batch) => batch.batch_id)),
      field("provider", 3, batches.map((batch) => batch.provider)),
      field("model", 3, batches.map((batch) => batch.model)),
      field("failure", 2, stringsFrom(batches.map((batch) => batch.failure ?? {}))),
    ],
  };
}

function generationBatchRecord(root, promptPath, promptDocument, batch) {
  const validResults = (batch.results ?? []).filter(resultHasImage);
  return {
    kind: "generation_batch",
    id: batch.batch_id,
    name: `Generation batch for ${promptDocument.prompt_id}`,
    description: batch.failure?.summary ?? `${batch.requested_count} requested image results`,
    path: relative(root, promptPath).replaceAll("\\", "/"),
    category: "generation_batch",
    consumers: promptDocument.metadata?.consumers ?? [],
    status: batch.status,
    target: batch.provider,
    style_id: promptDocument.style_id,
    providers: unique([batch.provider]),
    models: unique([batch.model]),
    has_image: validResults.length > 0,
    has_receipt: (batch.results ?? []).some(resultHasReceipt),
    result_count: validResults.length,
    requested_count: batch.requested_count,
    document: {
      prompt_id: promptDocument.prompt_id,
      style_id: promptDocument.style_id,
      batch,
    },
    fields: [
      field("id", 14, [batch.batch_id]),
      field("prompt", 10, [promptDocument.prompt_id, promptDocument.subject, promptDocument.prompt_text]),
      field("style", 9, [promptDocument.style_id]),
      field("provider", 7, [batch.provider]),
      field("model", 7, [batch.model]),
      field("status", 5, [batch.status]),
      field("failure", 5, stringsFrom(batch.failure ?? {})),
      field("parameter", 3, stringsFrom(batch.parameters ?? {})),
    ],
  };
}

function imageResultRecord(root, promptPath, promptDocument, batch, result) {
  return {
    kind: "image_result",
    id: result.result_id,
    name: result.file_name,
    description: promptDocument.subject,
    path: relative(root, promptPath).replaceAll("\\", "/"),
    category: "image_result",
    consumers: promptDocument.metadata?.consumers ?? [],
    status: result.status,
    target: batch.provider,
    style_id: promptDocument.style_id,
    providers: unique([batch.provider]),
    models: unique([batch.model]),
    has_image: resultHasImage(result),
    has_receipt: resultHasReceipt(result),
    result_count: resultHasImage(result) ? 1 : 0,
    requested_count: 1,
    document: {
      prompt_id: promptDocument.prompt_id,
      style_id: promptDocument.style_id,
      batch_id: batch.batch_id,
      result,
    },
    fields: [
      field("id", 14, [result.result_id]),
      field("file", 11, [result.file_name]),
      field("prompt", 9, [promptDocument.prompt_id, promptDocument.subject]),
      field("style", 9, [promptDocument.style_id]),
      field("batch", 8, [batch.batch_id]),
      field("provider", 6, [batch.provider]),
      field("model", 6, [batch.model]),
      field("status", 5, [result.status]),
      field("source", 4, [result.source_kind]),
      field("invalid_reason", 4, [result.invalid_reason]),
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

  const promptCasesDir = join(root, "prompt-cases");
  if (existsSync(promptCasesDir)) {
    for (const name of readdirSync(promptCasesDir).filter((item) => item.endsWith(".json")).sort()) {
      const path = join(promptCasesDir, name);
      const document = readJson(path);
      records.push(promptCaseRecord(root, path, document));
      for (const batch of document.generation_batches ?? []) {
        records.push(generationBatchRecord(root, path, document, batch));
        for (const result of batch.results ?? []) {
          records.push(imageResultRecord(root, path, document, batch, result));
        }
      }
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
  if (filters.style && record.style_id !== filters.style) return false;
  if (filters.provider && !record.providers.includes(filters.provider)) return false;
  if (filters.model && !record.models.includes(filters.model)) return false;
  if (typeof filters.has_image === "boolean" && record.has_image !== filters.has_image) return false;
  if (typeof filters.has_receipt === "boolean" && record.has_receipt !== filters.has_receipt) return false;
  if (Number.isInteger(filters.count_min) && record.result_count < filters.count_min) return false;
  return true;
}

function scoreRecord(record, query) {
  const normalizedQuery = normalize(query);
  if (!normalizedQuery) {
    return {
      score: 0,
      matched_fields: [],
      matched_terms: [],
      missing_terms: [],
      exact: true,
    };
  }

  const tokens = [...new Set(normalizedQuery.split(" ").filter(Boolean))];
  const matchedFields = new Set();
  const matchedTerms = [];
  const missingTerms = [];
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

    if (tokenScore === 0) {
      missingTerms.push(token);
      continue;
    }

    matchedTerms.push(token);
    total += tokenScore;
    if (tokenField) matchedFields.add(tokenField);
  }

  for (const group of record.fields) {
    if (group.values.some((value) => normalize(value).includes(normalizedQuery))) {
      total += group.weight * 4;
      matchedFields.add(group.name);
    }
  }

  return {
    score: total,
    matched_fields: [...matchedFields].sort(),
    matched_terms: matchedTerms,
    missing_terms: missingTerms,
    exact: missingTerms.length === 0,
  };
}

function resultView(record, scored) {
  return {
    kind: record.kind,
    id: record.id,
    name: record.name,
    description: record.description,
    path: record.path,
    category: record.category,
    consumers: record.consumers,
    status: record.status,
    target: record.target,
    style_id: record.style_id,
    providers: record.providers,
    models: record.models,
    has_image: record.has_image,
    has_receipt: record.has_receipt,
    result_count: record.result_count,
    requested_count: record.requested_count ?? null,
    score: scored.score,
    matched_fields: scored.matched_fields,
    matched_terms: scored.matched_terms,
    missing_terms: scored.missing_terms,
  };
}

function sortResults(results) {
  return results.sort(
    (a, b) => b.score - a.score || a.kind.localeCompare(b.kind) || a.id.localeCompare(b.id),
  );
}

export function queryCatalog(catalog, query = "", filters = {}) {
  const limit = Number.isInteger(filters.limit) && filters.limit > 0 ? filters.limit : 20;
  const results = [];

  for (const record of catalog) {
    if (!matchesFilter(record, filters)) continue;
    const scored = scoreRecord(record, query);
    if (!scored.exact) continue;
    results.push(resultView(record, scored));
  }

  return sortResults(results).slice(0, limit);
}

export function queryCatalogWithRelated(catalog, query = "", filters = {}) {
  const limit = Number.isInteger(filters.limit) && filters.limit > 0 ? filters.limit : 20;
  const exactResults = [];
  const relatedResults = [];

  for (const record of catalog) {
    if (!matchesFilter(record, filters)) continue;
    const scored = scoreRecord(record, query);
    if (scored.exact) {
      exactResults.push(resultView(record, scored));
    } else if (scored.matched_terms.length > 0 && scored.missing_terms.length === 1) {
      relatedResults.push(resultView(record, scored));
    }
  }

  return {
    query,
    filters: {
      kind: filters.kind ?? null,
      category: filters.category ?? null,
      consumer: filters.consumer ?? null,
      status: filters.status ?? null,
      target: filters.target ?? null,
      style: filters.style ?? null,
      provider: filters.provider ?? null,
      model: filters.model ?? null,
      has_image: typeof filters.has_image === "boolean" ? filters.has_image : null,
      has_receipt: typeof filters.has_receipt === "boolean" ? filters.has_receipt : null,
      count_min: Number.isInteger(filters.count_min) ? filters.count_min : null,
      limit,
    },
    exact_results: sortResults(exactResults).slice(0, limit),
    related_results: sortResults(relatedResults).slice(0, limit),
  };
}

function stripQuotes(value) {
  if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
    return value.slice(1, -1);
  }
  return value;
}

export function parseQueryExpression(input) {
  const tokens = String(input ?? "").match(/"[^"]*"|'[^']*'|\S+/g) ?? [];
  const queryTerms = [];
  const filters = {};

  for (const token of tokens) {
    const count = token.match(/^count:>=(\d+)$/i);
    if (count) {
      filters.count_min = Number(count[1]);
      continue;
    }

    if (/^has:image$/i.test(token)) {
      filters.has_image = true;
      continue;
    }
    if (/^has:receipt$/i.test(token)) {
      filters.has_receipt = true;
      continue;
    }
    if (/^has:no-image$/i.test(token)) {
      filters.has_image = false;
      continue;
    }
    if (/^has:no-receipt$/i.test(token)) {
      filters.has_receipt = false;
      continue;
    }

    const structured = token.match(/^(kind|category|consumer|status|target|style|provider|model):(.+)$/i);
    if (structured) {
      filters[structured[1].toLowerCase()] = stripQuotes(structured[2]);
      continue;
    }

    queryTerms.push(stripQuotes(token));
  }

  return {
    query: queryTerms.join(" ").trim(),
    filters,
  };
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
    style_id: record.style_id,
    providers: record.providers,
    models: record.models,
    has_image: record.has_image,
    has_receipt: record.has_receipt,
    result_count: record.result_count,
    requested_count: record.requested_count ?? null,
  }));
}
