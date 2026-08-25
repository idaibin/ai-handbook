import { RegistryExplorer } from "@/components/registry-explorer";
import { promptCases, registryRecords, registrySnapshot, styles } from "@/data/registry";

export default function HomePage() {
  const verifiedImages = promptCases.reduce(
    (sum, promptCase) => sum + promptCase.results.filter((result) => result.status === "verified").length,
    0,
  );

  return (
    <>
      <section className="hero">
        <div className="heroCopy">
          <h1>查风格、查 Prompt、查独立结果</h1>
          <p>
            这是 Next.js 只读查询投影。Prompt 文本、图片文件和结果证据分开保存；一个 Prompt 可以关联 N
            张独立图片，但图片本身不包含 Prompt、哈希、表格或界面文字。
          </p>
        </div>
        <dl className="metrics" aria-label="Registry 概览">
          <div>
            <dt>候选风格</dt>
            <dd>{styles.length}</dd>
          </div>
          <div>
            <dt>PromptCase</dt>
            <dd>{promptCases.length}</dd>
          </div>
          <div>
            <dt>有效图片</dt>
            <dd>{verifiedImages}</dd>
          </div>
          <div>
            <dt>关系</dt>
            <dd>1:N</dd>
          </div>
        </dl>
      </section>

      <RegistryExplorer records={registryRecords} />

      <footer className="siteFooter">
        <p>
          权威来源：{registrySnapshot.sourceRepository}@{registrySnapshot.sourceCommit.slice(0, 12)} ·
          {registrySnapshot.sourceExperimentPath}
        </p>
      </footer>
    </>
  );
}
