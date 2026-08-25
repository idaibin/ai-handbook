import Link from "next/link";
import type { RegistryRecord } from "@/data/registry";
import { StatusBadge } from "@/components/status-badge";

interface RegistryCardProps {
  readonly record: RegistryRecord;
}

const symbols: Readonly<Record<string, string>> = {
  anthropomorphic_storybook: "CAT",
  transparent_watercolor: "WTR",
  eastern_ink_wash: "INK",
  classical_oil_portrait: "OIL",
  soft_gouache: "GOU",
  clay_3d: "3D",
  paper_cut_collage: "PPR",
  retro_pixel_art: "PXL",
  linocut_print: "LINO",
  risograph_editorial: "RISO",
  colored_pencil_storybook: "PEN",
  mixed_media_collage: "MIX",
  anthropomorphic_watercolor_cat_librarian_v01: "CASE",
};

export function RegistryCard({ record }: RegistryCardProps) {
  const href = record.kind === "style" ? `/styles/${record.id}` : `/prompts/${record.id}`;

  return (
    <article className="registryCard">
      <Link href={href} className="registryCardLink" aria-label={`查看 ${record.name}`}>
        <div className="registryPreview" aria-hidden="true">
          <span className="previewSymbol">{symbols[record.id] ?? "VR"}</span>
          <span className="previewCount">有效图片 {record.resultCount}</span>
        </div>
        <div className="registryCardBody">
          <span className="eyebrow">{record.kind === "style" ? "Style" : "PromptCase"}</span>
          <h2>{record.name}</h2>
          <p>{record.description}</p>
          <div className="tagList" aria-label="标签">
            {record.tags.map((tag) => (
              <span key={tag} className="tag">
                {tag}
              </span>
            ))}
          </div>
          <div className="cardMeta">
            <span>{record.medium}</span>
            <StatusBadge status={record.status} />
          </div>
        </div>
      </Link>
    </article>
  );
}
