import type { Metadata } from "next";
import { RegistryExplorer } from "@/components/registry-explorer";
import { styles } from "@/data/registry";

export const metadata: Metadata = {
  title: "Styles",
};

export default function StylesPage() {
  return (
    <>
      <section className="pageIntro">
        <span className="eyebrow">Visual Taxonomy</span>
        <h1>图片风格类型</h1>
        <p>浏览 provider-neutral 的风格候选。风格合同与实际 Prompt、图片结果分别维护。</p>
      </section>
      <RegistryExplorer records={styles} initialKind="style" />
    </>
  );
}
