import { readdir, readFile, stat } from "node:fs/promises";
import { dirname, extname, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const authoredRoots = ["app", "components", "lib", "data"];
const ignoredDirectories = new Set([".git", ".next", "node_modules", "out", "coverage", ".vercel"]);
const forbiddenExtensions = new Set([".html", ".js", ".jsx"]);

async function walk(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    if (entry.isDirectory() && ignoredDirectories.has(entry.name)) continue;
    const absolute = resolve(directory, entry.name);
    if (entry.isDirectory()) files.push(...(await walk(absolute)));
    if (entry.isFile()) files.push(absolute);
  }

  return files;
}

async function isFile(path) {
  try {
    return (await stat(path)).isFile();
  } catch {
    return false;
  }
}

const requiredFiles = [
  "package.json",
  "tsconfig.json",
  "next.config.mjs",
  "app/layout.tsx",
  "app/page.tsx",
];
const missingFiles = [];
for (const path of requiredFiles) {
  if (!(await isFile(resolve(root, path)))) missingFiles.push(path);
}
if (missingFiles.length > 0) {
  throw new Error(`Missing required Next.js files: ${missingFiles.join(", ")}`);
}

const packageJson = JSON.parse(await readFile(resolve(root, "package.json"), "utf8"));
const dependencies = {
  ...(packageJson.dependencies ?? {}),
  ...(packageJson.devDependencies ?? {}),
};
const missingDependencies = ["next", "react", "react-dom", "typescript"].filter(
  (name) => dependencies[name] === undefined,
);
if (missingDependencies.length > 0) {
  throw new Error(`Missing required framework dependencies: ${missingDependencies.join(", ")}`);
}

const authoredFiles = [];
for (const authoredRoot of authoredRoots) {
  const directory = resolve(root, authoredRoot);
  try {
    authoredFiles.push(...(await walk(directory)));
  } catch (error) {
    if (error && typeof error === "object" && "code" in error && error.code === "ENOENT") continue;
    throw error;
  }
}

const forbiddenSources = authoredFiles
  .filter((file) => forbiddenExtensions.has(extname(file)))
  .map((file) => relative(root, file));
if (forbiddenSources.length > 0) {
  throw new Error(`Forbidden non-TypeScript application sources: ${forbiddenSources.join(", ")}`);
}

const typedSources = authoredFiles.filter((file) => [".ts", ".tsx"].includes(extname(file)));
if (typedSources.length === 0) throw new Error("No TypeScript or TSX application source found");

process.stdout.write(
  `${JSON.stringify({
    status: "passed",
    framework: "nextjs-react-typescript",
    checked_authored_files: authoredFiles.length,
    ignored_directories: [...ignoredDirectories],
  })}\n`,
);
