# Story Studio 工作流来源矩阵（待复核）

状态：`local_sync_ready_for_review`  
本文件只同步来源索引和验证结论，不包含第三方仓库代码、模型权重或生成媒体。创建于 2026-08-18（Asia/Shanghai）。

完整证据、输入文件哈希和执行边界保存在本地任务包，未随本索引上传；本文件只保留可公开版本化的来源、结构结论和状态。

## 已读取的原始来源

| 来源 | 现场 HEAD | 已观察内容 | 许可证/限制 | 用途结论 |
|---|---|---|---|---|
| [Seedance2-Storyboard-Generator](https://github.com/liangdabiao/Seedance2-Storyboard-Generator) | `17b9ca6dfac3e4a086a2874791ef19ae5aae3932` | `写剧本和分镜/`、多个中文项目目录、素材和逐集分镜命名/时间线约定 | README 标注仅供学习和参考；商业复用未核实 | 作为剧本→素材→分镜结构参考 |
| [drama-skills](https://github.com/worldwonderer/drama-skills) / [golden-project](https://github.com/worldwonderer/drama-skills/tree/main/examples/golden-project) | `0d176130fdacf09526793a1dfcfb36b764a6c47f` | 设定集、剧集、审查、创作者决策、`short-drama.json`；样例为文本/JSON | GitHub 标注 MIT；样例不含媒体或 provider 结果 | 作为班超 Bible/EP01 文本合同与哈希门禁夹具 |
| [Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) / [data](https://github.com/HBAI-Ltd/Toonflow-app/tree/master/data) | `bc61ec7a1b5df31293b286981a5f4ad4635464ee` | `data/skills/`、`modelPrompt/video/`、模型和资产目录存在 | Apache-2.0 之外有 README 补充商业条款 | 作为流程编排/provider 抽象邻近案例；不作为内容金标准 |
| [ViMax](https://github.com/HKUDS/ViMax) / [vimax_benchmark](https://github.com/HKUDS/ViMax/tree/main/vimax_benchmark) | `05a48943878312d88fe5a016c12a9654940ecc43` | 多个 JSON benchmark case 和索引 | GitHub 标注 MIT；模型/provider 条款需逐项复核 | 作为 provider-neutral benchmark 参考；不是班超完整剧集 |

## 与当前班超实验点的验证

- 全传 Bible/背景与 `drama-skills` 的设定集、项目开发结构可映射；当前主稿仍以可追溯史料和本地审查文件为权威。
- EP01《佣书》105 秒剧本可映射 Seedance 的剧本/逐集/时间线约定和 `drama-skills` 的剧集/审查字段；当前仅完成文字验证。
- 分镜、关键帧、图生视频和音频尚未执行；上述仓库没有被写成已运行的 provider 或已生成媒体。
- 四个来源本轮均未 clone、安装、运行或下载模型，因此复现状态统一为 `Not verified`，不等同于视频生成成功。

## 班超 EP01 修订与项目隔离

- EP01《佣书》保留 105 秒时长和原有剧情接口；“大丈夫当立功异域，安能久事笔砚间”在 v1.1 中标为 `[F+A]`，表示基于史料原意的戏剧压缩，不再称为《后汉书》逐字原句。
- 班超资产使用独立的 `project_id: banchao`；与既有赛博朋克实验的 `neural-echo` 资产不混用。媒体、分镜和 provider 仍未开始生产。

## 外部同步边界

这份索引已写入本地 `ai-handbook` 工作树。远程 GitHub 采用独立 review branch，Drive 只保存项目原始资料；不把本地路径、私有 Drive ID、第三方仓库代码或模型权重写入公开索引。
