# Visual Registry Web

使用 **Next.js App Router + React + TypeScript** 实现的只读 Registry 查询 MVP。此前的手写 `index.html` 原型已废弃，不再作为源码维护。

## 功能

- `/`：统一搜索与筛选；
- `/styles/`：风格类型列表；
- `/styles/[id]/`：风格详情与关联 PromptCase；
- `/prompts/`：PromptCase 列表；
- `/prompts/[id]/`：Prompt 文本、身份和 1:N 独立 ImageResult；
- 静态导出，可部署到 Vercel 或其他静态托管。

## 资产边界

- Prompt 是文本资产；
- 每个 ImageResult 是独立图片文件；
- Prompt、Hash、Provider、Receipt 不会写入图片；
- Contact Sheet 只能作为 `derived_review_only`；
- 当前有效独立图片仍为 `0/4`，页面显示真实 pending 槽位。

## 本地运行

```bash
npm install
npm run dev
```

完整验证：

```bash
npm run verify
```

`next build` 会将静态站点导出到 `out/`。
