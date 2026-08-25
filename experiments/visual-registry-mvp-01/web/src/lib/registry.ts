import {
  promptCases,
  registryRecords,
  styles,
  type PromptCaseRecord,
  type RegistryRecord,
  type StyleRecord,
} from "@/data/registry";

export function getStyle(id: string): StyleRecord | undefined {
  return styles.find((style) => style.id === id);
}

export function getPromptCase(id: string): PromptCaseRecord | undefined {
  return promptCases.find((promptCase) => promptCase.id === id);
}

export function getPromptCasesForStyle(styleId: string): readonly PromptCaseRecord[] {
  return promptCases.filter((promptCase) => promptCase.styleId === styleId);
}

export function searchText(record: RegistryRecord): string {
  const promptFields =
    record.kind === "prompt_case"
      ? [record.subject, record.promptText, record.promptSha256, record.styleId]
      : [];

  return [
    record.id,
    record.name,
    record.description,
    record.medium,
    record.status,
    ...record.tags,
    ...promptFields,
  ]
    .join(" ")
    .toLocaleLowerCase("zh-CN");
}

export { promptCases, registryRecords, styles };
