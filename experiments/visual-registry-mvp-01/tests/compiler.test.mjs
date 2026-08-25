import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { compilePrompt } from "../dist/prototype/compiler.js";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const casesDir = join(root, "cases");
const contractsDir = join(root, "contracts");
const caseFiles = readdirSync(casesDir).filter((name) => name.endsWith(".json")).sort();
const providerLeakPattern = /midjourney|gemini|flux|--ar|--style|prompt_template|"models"/i;
let compilationCount = 0;
let firstValidContract;

for (const contractFile of readdirSync(contractsDir).filter((name) => name.endsWith(".json"))) {
  const raw = readFileSync(join(contractsDir, contractFile), "utf8");
  assert.equal(
    providerLeakPattern.test(raw),
    false,
    `${contractFile} leaks provider-specific syntax into the durable contract`,
  );
}

for (const file of caseFiles) {
  const testCase = JSON.parse(readFileSync(join(casesDir, file), "utf8"));
  const contract = JSON.parse(
    readFileSync(join(contractsDir, testCase.contract), "utf8"),
  );
  firstValidContract ??= contract;
  const results = [];

  for (const target of testCase.targets) {
    const first = compilePrompt({ target, subject: testCase.subject, contract });
    const second = compilePrompt({ target, subject: testCase.subject, contract });
    assert.deepEqual(first, second, `${testCase.id}/${target} is not deterministic`);
    assert.ok(first.prompt.includes(testCase.subject), `${target} dropped subject`);

    const combined = `${first.prompt} ${first.negative_prompt ?? ""}`.toLowerCase();
    for (const entry of first.trace.filter((item) => item.polarity !== "control")) {
      assert.ok(
        combined.includes(entry.rendered.toLowerCase()),
        `${testCase.id}/${target} dropped ${entry.path}:${entry.value}`,
      );
    }

    if (target === "midjourney") {
      assert.ok(first.prompt.includes(`--ar ${contract.defaults.aspect_ratio}`));
      assert.ok(first.prompt.includes("--style raw"));
      assert.equal(/--v\s+\d/.test(first.prompt), false, "version pin leaked into adapter");
    }
    if (target === "flux") {
      assert.ok(first.negative_prompt && first.negative_prompt.length > 0);
    }
    if (target === "gemini") {
      assert.ok(first.prompt.includes("Visual intent:"));
      assert.ok(first.prompt.includes("Avoid:"));
    }

    results.push(first);
    compilationCount += 1;
  }

  assert.equal(new Set(results.map((item) => item.semantic_signature)).size, 1);
  assert.equal(
    new Set(
      results.map((item) =>
        JSON.stringify(item.trace.map(({ path, value, polarity }) => ({ path, value, polarity }))),
      ),
    ).size,
    1,
    `${testCase.id} does not preserve one semantic trace across adapters`,
  );
}

assert.equal(compilationCount, 9);

assert.throws(
  () => compilePrompt({ target: "invalid", subject: "x", contract: firstValidContract }),
  /Unsupported target: invalid/,
);
assert.throws(
  () => compilePrompt({ target: "gemini", subject: "   ", contract: firstValidContract }),
  /Subject must not be empty/,
);

process.stdout.write(
  `${JSON.stringify({ status: "passed", cases: caseFiles.length, compilations: compilationCount, checks: ["contract_purity", "determinism", "semantic_trace_preserved", "constraints_preserved", "adapter_syntax", "invalid_target_rejected", "empty_subject_rejected"] }, null, 2)}\n`,
);
