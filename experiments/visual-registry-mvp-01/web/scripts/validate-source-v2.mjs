import { readdir, readFile, stat } from "node:fs/promises";
import { dirname, extname, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const ignoredDirectories = new Set([
  ".git",
  ".next",
  "node_modules",
  "out",
  "coverage",
  ".vercel",
]);
const forbiddenExtensions = new Set([".html", ".js", ".jsx"]);
const authoredRoots = ["app", "components", "lib", "data"];

async function walk(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    if (entry.isDirectory() && ignoredDirectories.has(entry.name)) continue;

    const absolutePath = resolve(directory, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await walk(absolutePath)));
    } else if (entry.isFile()) {
      files.push(absolutePath);
    }
  }

  return files;
}

async function exists(path) {
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
const missingRequiredFiles = [];
for (const file of requiredFiles) {
  if (!(await exists(resolve(root, file)))) missingRequiredFiles.push(file);
}
if (missingRequiredFiles.length > 0) {
  throw new Error(`Missing required Next.js files: ${missingRequiredFiles.join(", ")}`);
}

const packageJson = JSON.parse(await readFile(resolve(root, "package.json"), "utf8"));
const allDependencies = {
  ...(packageJson.dependencies ?? {}),
  ...(packageJson.devDependencies ?? {}),
};
const missingDependencies = ["next", "react", "react-dom", "typescript"].filter(
  (name) => !allDependencies[name],
);
if (missingDependencies.length > 0) {
  throw new Error(`Missing required dependencies: ${missingDependencies.join(", ")}`);
}

const forbiddenSources = [];
for (const authoredRoot of authoredRoots) {
  const absoluteRoot = resolve(root, authoredRoot);
  try {
    const files = await walk(absoluteRoot);
    for (const file of files) {
      if (forbiddenExtensions.has(extname(file))) {
        forbiddenSources.push(relative(root, file));
      }
    }
  } catch (error) {
    if (error && typeof error === "object" && "code" in error && error.code === "ENOENT") {
      continue;
    }
    throw error;
  }
}

if (forbiddenSources.length > 0) {
  throw new Error(`Forbidden plain source files: ${forbiddenSources.join(", ")}`);
}

const authoredFiles = (
  await Promise.all(
    authoredRoots.map(async (authoredRoot) => {
      try {
        return await walk(resolve(root, authoredRoot));
      } catch (error) {
        if (error && typeof error === "object" && "code" in error && error.code === "ENOENT") {
          return [];
        }
        throw error;
      }
    }),
  )
).flat();

const reactSourceFiles = authoredFiles.filter((file) => [".ts", ".tsx"].includes(extname(file)));
if (reactSourceFiles.length === 0) {
  throw new Error("No TypeScript/TSX application source found");
}

process.stdout.write(
  `${JSON.stringify({
    status: "passed",
    framework: "nextjs-react-typescript",
    checked_authored_files: authoredFiles.length,
    ignored_directories: [...ignoredDirectories],
  })}\n`,
);
