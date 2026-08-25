import { createHash } from "node:crypto";
import { access, readFile, readdir } from "node:fs/promises";
import { join } from "node:path";

const root = new URL("../", import.meta.url);
const required = [
  "src/app/layout.tsx",
  "src/app/page.tsx",
  "src/app/styles/page.tsx",
  "src/app/styles/[id]/page.tsx",
  "src/app/prompts/page.tsx",
  "src/app/prompts/[id]/page.tsx",
  "src/components/registry-explorer.tsx",
  "src/components/result-grid.tsx",
  "src/data/registry.ts",
];

for (const relativePath of required) {
  await access(new URL(relativePath, root));
}

async function walk(directoryUrl, prefix = "") {
  const entries = await readdir(directoryUrl, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const relativePath = join(prefix, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await walk(new URL(`${entry.name}/`, directoryUrl), relativePath)));
    } else {
      files.push(relativePath);
    }
  }
  return files;
}

const files = await walk(root);
const forbiddenSources = files.filter((file) => file === "index.html" || file.endsWith(".js"));
if (forbiddenSources.length > 0) {
  throw new Error(`Forbidden plain source files: ${forbiddenSources.join(", ")}`);
}
if (files.some((file) => file.startsWith("app/"))) {
  throw new Error("Duplicate root app/ directory detected; source must live under src/app only.");
}

const source = await readFile(new URL("src/data/registry.ts", root), "utf8");
const promptMatch = source.match(/promptText:\s*"([^"]+)"/u);
const shaMatch = source.match(/promptSha256:\s*"([a-f0-9]{64})"/u);
if (!promptMatch || !shaMatch) throw new Error("Unable to locate frozen Prompt identity.");

const digest = createHash("sha256").update(promptMatch[1], "utf8").digest("hex");
if (digest !== shaMatch[1]) {
  throw new Error(`Prompt SHA mismatch: expected ${shaMatch[1]}, received ${digest}`);
}

const resultIds = [...source.matchAll(/resultId:\s*`([^`]+)`/gu)];
if (resultIds.length !== 1 || !source.includes("[1, 2, 3, 4].map")) {
  throw new Error("Expected one deterministic r01-r04 result identity generator.");
}
if (!source.includes("imageUrl: null")) {
  throw new Error("Blocked PromptCase must keep imageUrl null until independent files exist.");
}

console.log(JSON.stringify({
  status: "passed",
  framework: "nextjs-react-typescript",
  sourceFiles: files.filter((file) => file.startsWith("src/")).length,
  promptSha256: digest,
  independentResultIdentities: 4,
  verifiedImages: 0,
}, null, 2));
