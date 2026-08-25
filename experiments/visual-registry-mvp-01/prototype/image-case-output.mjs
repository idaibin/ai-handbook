import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { generateAllPromptSets } from "./image-case-demo.mjs";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
process.stdout.write(`${JSON.stringify({ generated_at: "deterministic", prompt_sets: generateAllPromptSets(root) }, null, 2)}\n`);
