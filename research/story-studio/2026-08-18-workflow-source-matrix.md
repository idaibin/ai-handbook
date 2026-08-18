# Story Studio 班超实验点：外部视频工作流资料验证矩阵 v1

状态：`partial_with_evidence_remote_sync_verified`

生成时间：2026-08-18（Asia/Shanghai）

## 1. 本轮边界

用户提供的两份粘贴资料是研究输入，不是权威仓库或已完成的验证结果。本轮只对其中最关键的四个原始 GitHub 仓库做了只读核验：

- 公开仓库页面、README、目录树可读取；
- 使用 `git ls-remote <repo> HEAD` 记录了现场 HEAD；
- 没有 clone、安装依赖、下载模型、启动 Web UI、提交 Git 或执行第三方 provider；
- 因而“来源可读/目录存在”不等于“本机可复现”，也不等于“已生成视频”。

两份用户粘贴资料的 SHA-256：

| 输入 | SHA-256 |
|---|---|
| `pasted-text.txt`（广泛仓库调查） | `c3748f4f7df38611b0783d78ec08560a38cb343368330bce656eeaa003ec6301` |
| `pasted-text.txt`（重点仓库推荐） | `0be02b88dceac18c27fd7186ca8c0def561b488f3b150ea966e25f8381740d9c` |

## 2. 原始来源矩阵

### 2.1 `liangdabiao/Seedance2-Storyboard-Generator`

- 原始来源：[GitHub 仓库](https://github.com/liangdabiao/Seedance2-Storyboard-Generator)
- 现场 HEAD：`17b9ca6dfac3e4a086a2874791ef19ae5aae3932`
- 页面可见结构：`写剧本和分镜/`、`司马光项目/`、`岳阳楼记项目/`、`崖山海战项目/`、`林冲项目/`、`素材/` 等；README 给出剧本、素材清单、逐集分镜的命名约定。
- 可复用内容：README 明确描述“故事创意 → 剧本 → 素材描述 → 图片 → 分镜脚本 → 分集视频”的顺序，并给出时间线提示词、尾帧描述和 15 秒分集示例；这可作为 EP01 前置文本和后续 provider-neutral shot contract 的结构参考。
- 依赖/模型（仓库自述）：Claude Code 负责剧本/分镜，GPT-Image-2、Seedream、Nano Banana Pro 负责素材，Seedance 2.0 负责视频。它们是外部 provider 声明，不是本机已验证依赖。
- 许可证/限制：README 明确写明“本项目内容仅供学习和参考使用”；没有在本轮把它判为可商业再分发素材。标准 SPDX 许可证和商业授权范围 `Not verified`。
- 硬件/运行：仓库页未给出本机可复现的统一硬件门槛；实际视频依赖 Seedance provider，`Not verified`。
- 输入/输出：Markdown 剧本、素材清单、逐集分镜、时间线提示词；未见“本地端到端视频输出”证据。
- 可下载/可复现：网页和目录可读，HEAD 可解析；未 clone/运行，故标记 `source_readable_only`。
- Story Studio 结论：`可用作结构参考；不可直接升级为生产标准或许可证已清晰的资产包`。

### 2.2 `worldwonderer/drama-skills`

- 原始来源：[GitHub 仓库](https://github.com/worldwonderer/drama-skills)；重点样例：[examples/golden-project](https://github.com/worldwonderer/drama-skills/tree/main/examples/golden-project)
- 现场 HEAD：`0d176130fdacf09526793a1dfcfb36b764a6c47f`
- 许可证：GitHub 页面标注 MIT；仓库包含 `LICENSE`。仍需在任何再分发前按当前 HEAD 复核具体文本。
- 可复用内容：`golden-project` 页面可见 `创作者决策/`、`剧集/`、`审查/`、`设定集/`、`输入/`、`项目开发/`、`short-drama.json`；README 将其定义为 8 集样例，覆盖项目开发、剧本、资产提取、图片提示词、分镜覆盖、关键帧、运动提示词和审查结论。
- 关键边界：样例只分发 UTF-8 文本和 JSON，不包含图片、音频、视频或 provider 结果；SHA-256 绑定的是直接上游快照，不是全套全局锁定；候选状态本身不是通过证明，需结合创作者决策哈希。
- 依赖/运行：README 要求 Python 3.10+；技能输出主要是文本，实际生成通过外部 adapter；声明兼容 Claude Code/Codex。没有在本机安装或执行。
- 输入/输出：结构化项目资料、集/剧本、资产与提示词、审查报告、哈希门禁；没有已验证的媒体输出。
- 可下载/可复现：源码页面、样例目录和验证器入口可读；本轮未 clone/执行测试，故 `source_readable_only`，运行结果 `Not verified`。
- Story Studio 结论：`本轮四个候选中最适合做前置文本/合同验证夹具`，尤其适合校验班超 Bible、EP01 剧本、分镜字段和审查哈希，但不能证明视频模型质量。

### 2.3 `HBAI-Ltd/Toonflow-app`

- 原始来源：[GitHub 仓库](https://github.com/HBAI-Ltd/Toonflow-app)；数据目录：[data](https://github.com/HBAI-Ltd/Toonflow-app/tree/master/data)
- 现场 HEAD：`bc61ec7a1b5df31293b286981a5f4ad4635464ee`
- 页面可见结构：仓库包含 `data/`；其目录树可见 `assets/`、`modelPrompt/video/`、`models/all-MiniLM-L6-v2/`、`skills/`、`vendor/`、`web/` 等。
- 可复用内容（仓库自述）：从规划、剧本、分镜到输出的一体化应用；三层 agent、持久记忆、provider system、章节事件图和 skill 配置可作为“流程编排/模型替换”参考。
- 许可证/限制：README 自述 Apache-2.0，同时存在补充商业条款（包括第三方分发和标识等限制）；不能按“纯 Apache-2.0、无附加条件”处理。商业再分发范围 `Not verified`，需单独做法律复核。
- 依赖/运行（仓库自述）：Node 23.11+、TypeScript 5、Express 5、SQLite、Vercel AI SDK、Electron 等；本机未安装/启动，版本和 M2 可运行性 `Not verified`。
- 输入/输出：应用级文本、资产、提示词和流程状态；本轮只验证到目录存在，未证明 `data/skills/` 内有可独立复用的完整班超/中文剧集样例。
- 可下载/可复现：仓库和 `data/` 可读，HEAD 可解析；未 clone/运行，`source_readable_only`。
- Story Studio 结论：`适合作为产品/编排架构邻近案例；不作为当前班超内容金标准，也不直接导入其运行时`。

### 2.4 `HKUDS/ViMax`

- 原始来源：[GitHub 仓库](https://github.com/HKUDS/ViMax)；重点目录：[vimax_benchmark](https://github.com/HKUDS/ViMax/tree/main/vimax_benchmark)
- 现场 HEAD：`05a48943878312d88fe5a016c12a9654940ecc43`
- 许可证：仓库 README/GitHub 页面标注 MIT；具体依赖和 provider 许可仍需按实际模型逐项复核。
- 可复用内容：`vimax_benchmark/` 页面可见 `benchmark_index.json` 及多组 JSON benchmark case（如 artist/weather、athlete、barista 等），适合作为 provider-neutral 评测和回归样例。
- 关键边界：本轮目录证据显示它是 benchmark/评测素材集合，不是完整的中文历史剧集生产包；没有把它当成班超故事 Bible、分集剧本或已完成视频案例。
- 依赖/运行（仓库自述）：`uv sync`，README 提到 Linux/Windows 及 Node 18+ Web UI 路径；未在 Mac Studio M2 或当前 ComfyUI runtime 执行，运行可用性 `Not verified`。
- 输入/输出：脚本/故事到视频的 agent/provider 流程与 JSON benchmark；视频输出和 provider 结果未在本轮取得。
- 可下载/可复现：仓库和 benchmark 目录可读、HEAD 可解析；未 clone/运行，`source_readable_only`。
- Story Studio 结论：`适合作为 provider-neutral benchmark/回归思路；不替代班超内容主稿，也不证明本机视频生成`。

## 3. 采用资料对当前班超流程的验证

| Story Studio 阶段 | 当前本地事实 | 外部资料映射 | 本轮结论 |
|---|---|---|---|
| 全传 Bible、背景、人物与世界规则 | `banchao-first-step-v1-freeze.md`，SHA-256 `fe52a7017eb774413b2c5dbe51aa9dd522e8b624dc567ef95f1ce1a289b766c0` | `drama-skills/examples/golden-project/` 的设定集/项目开发；Seedance 的剧本前置结构 | 文本结构可映射；史实仍以《后汉书》证据链为准，不以仓库样例替代 |
| EP01《佣书》剧本 | `ep01-yongshu-screenplay-v1.md`，SHA-256 `b6fecaf0b2ac681a654a2343c8398904bd18e6a04ee892050c71a35bc43f33fa`，105 秒 | Seedance 的剧本/素材/逐集命名与时间线；drama-skills 的 `剧集/` 与审查字段 | 已通过文本生产检查；未生成图片/视频 |
| EP01 分镜与提示词接口 | 尚无冻结分镜 artifact | Seedance 的时间线/尾帧约定；drama-skills 的关键帧/运动提示词字段 | 可借鉴字段，尚未执行阶段 05 |
| 视频/音频 provider | 当前不依赖 ComfyUI；Wan/其他在线 provider 未运行 | ViMax benchmark 的 provider-neutral 评测思路；Toonflow 的 provider system 思路 | 仅接口设计参考；视频和音频结果 `Not verified` |
| 证据与审查 | `ep01-world-background-validation-v1.md`，SHA-256 `570850874f6b86befd7cfd69a43536b140a48866b74d378d9a6f64dd1e0a10c1`；已有 Gemini/AGY 审查文件 | drama-skills 的创作者决策哈希与审查目录 | 本地文件哈希可回读；第三方仓库测试尚未在本机运行 |

## 4. 本轮未独立验证的候选

两份粘贴资料还提到 `SDSmirnov/AI-Story-To-Movie`、`HKUDS/ViMax` 以外的 Jellyfish、OpenMontage、MoneyPrinterTurbo、Toonflow 的具体 skill 文件、ArcReel、LumenX、LocalMiniDrama、story-systems-template、screenplay-tools，以及 BBC/StudioBinder 等剧本资源。它们在本轮没有完成同等级的原始文件、当前 HEAD、许可证和运行核验，不能写成“已验证可复现”。

## 5. 同步状态与下一步

- GitHub 已写入独立 review branch `agent/story-studio-workflow-source-matrix-20260818`，`main` 未触碰：来源矩阵 commit `0b365883b47dac47572d9bd35adea79a76180359`，生产路线文件 commit `5e26383434836b958b7e616a02d12bfaca8988ae`；两份文件均已通过 branch readback。
- Drive 已写入 `04_Story-Studio/IP/banchao`、`Scripts/banchao` 和 `Evidence/banchao`；Bible、全传轨迹、24 集处理稿、EP01 v1/v1.1、背景验证、provider-neutral 生产路线及 evidence manifest 均已通过 metadata/大小回读，权限为 owner-only/private。
- 本轮只同步来源矩阵、生产路线和证据索引；没有上传第三方仓库代码、模型权重或媒体，也没有启动 ComfyUI Web UI。
- 下一步仍是 EP01 的 `Shot List → Asset Manifest → Continuity Contract`；视频、音频和 provider 运行结果继续保持 `Not verified`。

## 6. 本轮判定

`PASS_FOR_SOURCE_STRUCTURE_AND_CONTRACT_MAPPING`  
`REMOTE_SYNC_AND_READBACK_VERIFIED`  
`NOT_VERIFIED_FOR_LOCAL_REPRODUCTION_OR_MEDIA_OUTPUT`
