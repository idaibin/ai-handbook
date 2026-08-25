import type { Metadata } from "next";
import { RegistryExplorer } from "@/components/registry-explorer";
import { promptCases } from "@/data/registry";

export const metadata: Metadata = {
  title: "Prompts",
};

export default function PromptsPage() {
  return (
    <>
      <section className="pageIntro">
        <span className="eyebrow">PromptCase</span>
        <h1>Prompt 与 1:N 独立结果</h1>
        <p>每个 PromptCase 展示 Prompt 文本、身份和独立 ImageResult；不会把文字与图片合成一张报告图。</p>
      </section>
      <RegistryExplorer records={promptCases} initialKind="prompt_case" />
    </>
  );
}
