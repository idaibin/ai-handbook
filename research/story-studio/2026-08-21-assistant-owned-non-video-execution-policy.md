# Story Studio Assistant-Owned Non-Video Execution Policy

状态：`superseded_for_media_execution`  
原生效时间：`2026-08-21`  
替代日期：`2026-09-02`

本文件保留为历史政策入口。助手仍负责非视频工作的设计、准备、验证、证据和同步，但“助手负责”不再解释为允许在 Task 控制 Project 中直接生成或编辑图片。

当前媒体执行权威：

[`2026-09-02-media-asset-generation-isolation-policy.md`](./2026-09-02-media-asset-generation-isolation-policy.md)

当前规则：

```text
Control Project
→ Task / Research / Contract / Review / Evidence / Sync

Isolated Media Context
→ Image Generation / Image Edit / Video Generation
```

以下旧规则已经失效：

```text
同一 Task 控制会话可以直接执行图片生成
separate_chat_required_for_non_video_work: false
control_chat_image_generation_hard_prohibition: removed
```

历史提交中保留本文件完整旧版本；已有 Evidence 和资产状态不因本次替代而删除或自动升级。
