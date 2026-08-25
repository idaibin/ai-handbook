import type { ImageResult } from "@/data/registry";
import { StatusBadge } from "@/components/status-badge";

interface ResultGridProps {
  readonly results: readonly ImageResult[];
}

export function ResultGrid({ results }: ResultGridProps) {
  return (
    <section className="resultGrid" aria-label="独立图片结果">
      {results.map((result) => (
        <article key={result.resultId} className="resultCard">
          <div className="resultImageArea">
            {result.imageUrl ? (
              // eslint-disable-next-line @next/next/no-img-element
              <img src={result.imageUrl} alt={`${result.resultId} 独立生成结果`} />
            ) : (
              <div className="resultPlaceholder">
                <strong>r{String(result.sequence).padStart(2, "0")}</strong>
                <span>独立图片尚未生成</span>
              </div>
            )}
          </div>
          <div className="resultDetails">
            <div>
              <span className="eyebrow">ImageResult</span>
              <h3>{result.resultId}</h3>
            </div>
            <StatusBadge status={result.status} />
            <dl>
              <div>
                <dt>文件名</dt>
                <dd>{result.fileName}</dd>
              </div>
              <div>
                <dt>Provider</dt>
                <dd>{result.provider ?? "未记录"}</dd>
              </div>
              <div>
                <dt>图片 SHA-256</dt>
                <dd>{result.imageSha256 ?? "未记录"}</dd>
              </div>
            </dl>
          </div>
        </article>
      ))}
    </section>
  );
}
