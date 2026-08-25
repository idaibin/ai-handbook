import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { RegistryCard } from "@/components/registry-card";
import { StatusBadge } from "@/components/status-badge";
import { getPromptCasesForStyle, getStyle, styles } from "@/lib/registry";

interface StylePageProps {
  readonly params: Promise<{ id: string }>;
}

export function generateStaticParams() {
  return styles.map((style) => ({ id: style.id }));
}

export async function generateMetadata({ params }: StylePageProps): Promise<Metadata> {
  const { id } = await params;
  const style = getStyle(id);
  return style ? { title: style.name, description: style.description } : {};
}

export default async function StyleDetailPage({ params }: StylePageProps) {
  const { id } = await params;
  const style = getStyle(id);
  if (!style) notFound();

  const relatedPromptCases = getPromptCasesForStyle(style.id);

  return (
    <>
      <Link href="/styles/" className="backLink">
        返回 Styles
      </Link>
      <section className="detailHero">
        <div>
          <span className="eyebrow">Style</span>
          <h1>{style.name}</h1>
          <p>{style.description}</p>
        </div>
        <StatusBadge status={style.status} />
      </section>

      <section className="detailGrid">
        <article className="detailPanel">
          <h2>风格身份</h2>
          <dl className="detailList">
            <div>
              <dt>style_id</dt>
              <dd>{style.id}</dd>
            </div>
            <div>
              <dt>medium</dt>
              <dd>{style.medium}</dd>
            </div>
            <div>
              <dt>有效图片</dt>
              <dd>{style.resultCount}</dd>
            </div>
            <div>
              <dt>source</dt>
              <dd>{style.sourcePath}</dd>
            </div>
          </dl>
        </article>
        <article className="detailPanel">
          <h2>标签</h2>
          <div className="tagList largeTags">
            {style.tags.map((tag) => (
              <span className="tag" key={tag}>
                {tag}
              </span>
            ))}
          </div>
        </article>
      </section>

      <section className="relatedSection">
        <div className="resultHeader">
          <h2>关联 PromptCase</h2>
          <span>{relatedPromptCases.length} 条</span>
        </div>
        {relatedPromptCases.length > 0 ? (
          <div className="registryGrid">
            {relatedPromptCases.map((promptCase) => (
              <RegistryCard key={promptCase.id} record={promptCase} />
            ))}
          </div>
        ) : (
          <div className="emptyState">
            <h2>暂无关联 PromptCase</h2>
            <p>此风格目前只有候选合同，还没有完成 Prompt 1:N 案例。</p>
          </div>
        )}
      </section>
    </>
  );
}
