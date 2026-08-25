import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ResultGrid } from "@/components/result-grid";
import { StatusBadge } from "@/components/status-badge";
import { getPromptCase, getStyle, promptCases } from "@/lib/registry";

interface PromptPageProps {
  readonly params: Promise<{ id: string }>;
}

export function generateStaticParams() {
  return promptCases.map((promptCase) => ({ id: promptCase.id }));
}

export async function generateMetadata({ params }: PromptPageProps): Promise<Metadata> {
  const { id } = await params;
  const promptCase = getPromptCase(id);
  return promptCase ? { title: promptCase.name, description: promptCase.description } : {};
}

export default async function PromptDetailPage({ params }: PromptPageProps) {
  const { id } = await params;
  const promptCase = getPromptCase(id);
  if (!promptCase) notFound();
  const style = getStyle(promptCase.styleId);

  return (
    <>
      <Link href="/prompts/" className="backLink">
        返回 Prompts
      </Link>
      <section className="detailHero">
        <div>
          <span className="eyebrow">PromptCase</span>
          <h1>{promptCase.name}</h1>
          <p>{promptCase.description}</p>
        </div>
        <StatusBadge status={promptCase.status} />
      </section>

      <section className="promptContentGrid">
        <article className="detailPanel promptPanel">
          <h2>Prompt 文本</h2>
          <p className="promptText">{promptCase.promptText}</p>
        </article>
        <article className="detailPanel">
          <h2>Prompt 身份</h2>
          <dl className="detailList">
            <div>
              <dt>prompt_id</dt>
              <dd>{promptCase.id}</dd>
            </div>
            <div>
              <dt>style_id</dt>
              <dd>
                {style ? <Link href={`/styles/${style.id}/`}>{style.id}</Link> : promptCase.styleId}
              </dd>
            </div>
            <div>
              <dt>prompt_sha256</dt>
              <dd className="hashValue">{promptCase.promptSha256}</dd>
            </div>
            <div>
              <dt>aspect_ratio</dt>
              <dd>{promptCase.aspectRatio}</dd>
            </div>
            <div>
              <dt>requested_count</dt>
              <dd>{promptCase.requestedCount}</dd>
            </div>
          </dl>
        </article>
      </section>

      <article className="detailPanel subjectPanel">
        <h2>Subject</h2>
        <p>{promptCase.subject}</p>
      </article>

      <div className="resultHeader resultSectionHeader">
        <h2>独立图片结果</h2>
        <span>
          {promptCase.resultCount} / {promptCase.requestedCount} 有效
        </span>
      </div>
      <ResultGrid results={promptCase.results} />

      <aside className="separationNotice">
        <strong>资产分离规则</strong>
        <p>本页把 Prompt 作为文本显示，把每张 ImageResult 作为独立文件显示。二者不会合成一张信息图。</p>
      </aside>
    </>
  );
}
