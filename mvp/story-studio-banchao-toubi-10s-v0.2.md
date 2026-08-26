# Story Studio MVP — 班超《投笔》10 张分镜 / 10 秒

- `mvp_id`: `story-studio/banchao/toubi-10s-v0.2`
- `status`: `ready_as_downstream_video_test_slice`
- `artifact_role`: `downstream_video_chain_test_slice`
- `project_status_ref`: `research/story-studio/banchao-s1-current-status.md`
- `supersedes`: `story-studio/banchao/toubi-30s-v0.2`
- `scope`: Story Studio only; Forgeway and Skills remain frozen

> **状态说明（2026-08-26）**：本文档仅定义一个后续真实视频链路验证切片，不再代表《班超》S1 的当前项目范围，也不覆盖 S1 当前状态。S1 当前已经进入 EP01–EP24 / 194 张候选分镜的 Visual Canon 最终门禁，权威入口见 `research/story-studio/banchao-s1-current-status.md`。

## Smallest Result

保留 10 张关键分镜图，每张对应约 1 秒，组成严格 10 秒的“受辱—停笔—抬眼—决断”时序。不是减少为 2～3 镜。

## Frame Sequence

| 秒 | Frame | 节拍 | Drive |
| --- | --- | --- | --- |
| 0–1 | F01 | 同僚从背景发出嘲讽 | [PNG](https://drive.google.com/file/d/19ue_7L4ka30H08_XSUFE5ybjLujUyezm/view) |
| 1–2 | F02 | 班超继续书写并忍耐 | [PNG](https://drive.google.com/file/d/16HeTzT5uEtPEHbA_OZ055lJqVwWSAjob/view) |
| 2–3 | F03 | 面部近景承受质问 | [PNG](https://drive.google.com/file/d/1UhJ54-OsJ7StGcIQ1zmItMvMsIzOpkjA/view) |
| 3–4 | F04 | 笔锋逐渐停住 | [PNG](https://drive.google.com/file/d/1jpOQ4kZPBM4axrzxfB1GnhpAxr_BlyQi/view) |
| 4–5 | F05 | 视线开始离开案面 | [PNG](https://drive.google.com/file/d/1cNqH3fKHGE4ccjzzqfTPdjGbGiY7nbPe/view) |
| 5–6 | F06 | 抬眼望向画外 | [PNG](https://drive.google.com/file/d/1MmpOtNMAWuKQ0RX6Layq-qPhzPLi0nPW/view) |
| 6–7 | F07 | 手回到毛笔并犹疑 | [PNG](https://drive.google.com/file/d/1Ry_hEi0O7J9EiAA5z3lMPl-mtQVnOcR1/view) |
| 7–8 | F08 | 放下毛笔 | [PNG](https://drive.google.com/file/d/14wN9xQFFQcadj69Q9keUxAzl94ZlNIRA/view) |
| 8–9 | F09 | 手停止、不再落字 | [PNG](https://drive.google.com/file/d/1JTgEjJ76oT7mGG9Ryb0g5Q1a8SBmgDpe/view) |
| 9–10 | F10 | 面部决断并保持 | [PNG](https://drive.google.com/file/d/1yxdKqdHXSQE9MQMDum23-uBsO7mPvRu2/view) |

- [时序与 SHA-256 Manifest](https://drive.google.com/file/d/1y3O1xVH013cuTidQbeHsEuKWULhmwVnL/view)
- [MVP Brief](https://drive.google.com/file/d/1TBsWkH3ArwheSvjo0PW_r7vwczFK7X1a/view)
- [技术证据](https://drive.google.com/file/d/19EFmYc6ebkaMsG1VStGRK2rjTUmswnrn/view)

## Acceptance

1. 10 张独立 `1920x1080` PNG，`F01—F10` 顺序和一秒映射固定；
2. 视频模型据此生成严格 10 秒 MP4；
3. 班超身份、服装和场景无明显漂移；
4. 完成受辱、停笔、抬眼、放下毛笔四个连续节拍；
5. 最多生成 3 次，随后用户决定 `keep / change / stop`。

## Excluded from this test slice

本切片本身不做 30 秒成片、不把 10 张图缩减为 2～3 镜、不做完整季配音字幕、不补齐历史 G07 十单元，也不承担 EP01–EP24 的 Visual Canon 审批。原 30 秒文件与 3 镜 10 秒代理均为历史预览。

这里的排除项只限定本测试切片，不构成对 S1 项目范围的禁止或回退。
