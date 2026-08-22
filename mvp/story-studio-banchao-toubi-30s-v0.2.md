# Story Studio MVP — 班超《投笔》30 秒内部样片

- `mvp_id`: `story-studio/banchao/toubi-30s-v0.2`
- `status`: `rendered_pending_user_review`
- `approved_by`: user request on 2026-08-22
- `scope`: Story Studio only; Forgeway and Skills remain frozen

## Problem

EP01 已有 105 秒剧本、27 格分镜和大量候选资产，但没有先提供一个可直接观看、可据此决定是否继续投入的最小结果。

## Smallest Result

只复用既有 `EP01_SHOT_07`—`EP01_SHOT_10`，将“受辱—停笔—决断”裁成严格 30 秒内部样片。未生成新角色、场景、道具或生产镜头。

## Acceptance

- MP4：H.264，1920×1080，24fps，30.000 秒；
- 音频：AAC stereo 48kHz，仅基础 room tone 与一个低频落点；
- 输出 SHA-256：`631ae1c7c7ef08c4868b592112aa65362f2c9f97c78c5f523f0901c8c3cd28e1`；
- 用户看完后只做 `keep / change / stop` 决策。

## Evidence

- [30 秒样片](https://drive.google.com/file/d/1a53of7NQ-176tPlL9qUXd4nGw6t5qzuo/view)
- [MVP Brief](https://drive.google.com/file/d/10roOpEsqjCalXYbqB3OuZ6ZKlhMkK2ge/view)
- [技术证据](https://drive.google.com/file/d/1Yhg8I5TtEP9Y4hc1KTQnSFVnPWQi6HcS/view)

限制：Drive 历史 105 秒代理经连接器内联取回时尾部不完整，未匹配历史全文件哈希；本次使用的 42.00–75.95 秒区间已完整解码，最终输出也通过解码与抽帧检查。因此本结果仅为 `internal_mvp_candidate_not_production_ready`。

## Stop Condition

若用户不能从该片段理解班超由受辱转为决断，停止补资产并只重写本片段。在用户给出 `keep` 前，不恢复 105 秒整集、G07 十单元或 24 集扩展。
