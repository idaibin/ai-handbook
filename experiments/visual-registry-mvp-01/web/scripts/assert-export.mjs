import { access, readdir } from "node:fs/promises";
import { join } from "node:path";

const root = new URL("../out/", import.meta.url);
const expected = [
  "index.html",
  "styles/index.html",
  "prompts/index.html",
  "styles/transparent_watercolor/index.html",
  "prompts/anthropomorphic_watercolor_cat_librarian_v01/index.html",
];

for (const relativePath of expected) {
  await access(new URL(relativePath, root));
}

async function collectHtml(directoryUrl, prefix = "") {
  const entries = await readdir(directoryUrl, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const relative = join(prefix, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await collectHtml(new URL(`${entry.name}/`, directoryUrl), relative)));
    } else if (entry.name.endsWith(".html")) {
      files.push(relative);
    }
  }
  return files;
}

const htmlFiles = await collectHtml(root);
if (htmlFiles.length < 17) {
  throw new Error(`Expected at least 17 exported HTML routes, received ${htmlFiles.length}`);
}

console.log(JSON.stringify({ status: "passed", htmlRoutes: htmlFiles.length, expected }, null, 2));
