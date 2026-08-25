import { readFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { compilePrompt } from "../dist/prototype/compiler.js";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const casesDir = join(root, "cases");
const contractsDir = join(root, "contracts");
const caseFiles = readdirSync(casesDir).filter((name) => name.endsWith(".json")).sort();
const outputs = [];

for (const file of caseFiles) {
  const testCase = JSON.parse(readFileSync(join(casesDir, file), "utf8"));
  const contract = JSON.parse(
    readFileSync(join(contractsDir, testCase.contract), "utf8"),
  );

  for (const target of testCase.targets) {
    outputs.push({
      case_id: testCase.id,
      ...compilePrompt({ target, subject: testCase.subject, contract }),
    });
  }
}

process.stdout.write(`${JSON.stringify({ generated_at: "deterministic", outputs }, null, 2)}\n`);
