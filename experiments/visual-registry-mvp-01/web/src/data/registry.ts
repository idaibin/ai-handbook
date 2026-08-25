export type RegistryKind = "style" | "prompt_case";
export type RegistryStatus = "candidate" | "generation_blocked" | "ready";
export type ResultStatus = "pending" | "generated_unverified" | "verified" | "rejected";

export interface ImageResult {
  readonly resultId: string;
  readonly sequence: number;
  readonly fileName: string;
  readonly status: ResultStatus;
  readonly imageUrl: string | null;
  readonly provider: string | null;
  readonly model: string | null;
  readonly driveFileId: string | null;
  readonly imageSha256: string | null;
  readonly width: number | null;
  readonly height: number | null;
}

interface BaseRegistryRecord {
  readonly id: string;
  readonly kind: RegistryKind;
  readonly name: string;
  readonly description: string;
  readonly medium: string;
  readonly status: RegistryStatus;
  readonly tags: readonly string[];
  readonly resultCount: number;
  readonly sourcePath: string;
}

export interface StyleRecord extends BaseRegistryRecord {
  readonly kind: "style";
}

export interface PromptCaseRecord extends BaseRegistryRecord {
  readonly kind: "prompt_case";
  readonly styleId: string;
  readonly subject: string;
  readonly promptText: string;
  readonly promptSha256: string;
  readonly requestedCount: number;
  readonly aspectRatio: string;
  readonly results: readonly ImageResult[];
}

export type RegistryRecord = StyleRecord | PromptCaseRecord;

const pendingResults: readonly ImageResult[] = [1, 2, 3, 4].map((sequence) => ({
  resultId: `anthropomorphic_watercolor_cat_librarian_v01__r0${sequence}`,
  sequence,
  fileName: `anthropomorphic_watercolor_cat_librarian_v01__r0${sequence}.png`,
  status: "pending" as const,
  imageUrl: null,
  provider: null,
  model: null,
  driveFileId: null,
  imageSha256: null,
  width: null,
  height: null,
}));

export const styles: readonly StyleRecord[] = [
  {
    id: "anthropomorphic_storybook",
    kind: "style",
    name: "拟人绘本",
    description: "动物或物体具有人类姿态与叙事行为，重视角色动作、身份和情绪可读性。",
    medium: "storybook",
    status: "candidate",
    tags: ["anthropomorphic", "character", "narrative"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "transparent_watercolor",
    kind: "style",
    name: "透明水彩",
    description: "清透叠色、纸张纹理和柔和边缘，适合温暖叙事与自然场景。",
    medium: "watercolor",
    status: "candidate",
    tags: ["watercolor", "paper-grain", "soft-light"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "eastern_ink_wash",
    kind: "style",
    name: "东方水墨",
    description: "墨色层次、留白、湿笔扩散与克制构图。",
    medium: "ink-wash",
    status: "candidate",
    tags: ["ink", "eastern", "negative-space"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "classical_oil_portrait",
    kind: "style",
    name: "古典油画肖像",
    description: "厚重笔触、暗部层次和古典人物光线。",
    medium: "oil-painting",
    status: "candidate",
    tags: ["portrait", "oil", "chiaroscuro"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "soft_gouache",
    kind: "style",
    name: "柔和水粉",
    description: "不透明颜料、柔和块面与温和配色。",
    medium: "gouache",
    status: "candidate",
    tags: ["gouache", "matte", "editorial"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "clay_3d",
    kind: "style",
    name: "3D 黏土",
    description: "柔软材质、圆润体积和微缩场景光照。",
    medium: "3d-clay",
    status: "candidate",
    tags: ["3d", "clay", "miniature"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "paper_cut_collage",
    kind: "style",
    name: "剪纸拼贴",
    description: "分层纸张、清晰轮廓和手工材质。",
    medium: "paper-cut",
    status: "candidate",
    tags: ["paper", "collage", "layered"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "retro_pixel_art",
    kind: "style",
    name: "复古像素",
    description: "有限色板、像素边缘和复古游戏画面。",
    medium: "pixel-art",
    status: "candidate",
    tags: ["pixel", "retro", "limited-palette"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "linocut_print",
    kind: "style",
    name: "木刻版画",
    description: "高对比线条、刻痕纹理与强轮廓。",
    medium: "linocut",
    status: "candidate",
    tags: ["print", "engraving", "high-contrast"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "risograph_editorial",
    kind: "style",
    name: "孔版印刷",
    description: "套色偏移、颗粒与编辑插画感。",
    medium: "risograph",
    status: "candidate",
    tags: ["riso", "grain", "editorial"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "colored_pencil_storybook",
    kind: "style",
    name: "彩铅绘本",
    description: "可见笔触、纸面颗粒和细腻童话叙事。",
    medium: "colored-pencil",
    status: "candidate",
    tags: ["pencil", "storybook", "texture"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
  {
    id: "mixed_media_collage",
    kind: "style",
    name: "综合材料拼贴",
    description: "纸张、照片、笔触和纹理的混合构成。",
    medium: "mixed-media",
    status: "candidate",
    tags: ["collage", "mixed-media", "experimental"],
    resultCount: 0,
    sourcePath: "web/src/data/registry.ts",
  },
];

export const promptCases: readonly PromptCaseRecord[] = [
  {
    id: "anthropomorphic_watercolor_cat_librarian_v01",
    kind: "prompt_case",
    name: "拟人橘猫图书管理员 · 透明水彩",
    description: "同一冻结 Prompt 计划生成 4 张独立 4:3 图片；当前没有合格的 Provider 原生独立图片。",
    medium: "watercolor",
    status: "generation_blocked",
    tags: ["anthropomorphic", "watercolor", "storybook", "cat-librarian"],
    resultCount: 0,
    sourcePath: "prompt-cases/anthropomorphic-watercolor-cat-librarian-v01.json",
    styleId: "transparent_watercolor",
    subject: "一只拟人化橘猫图书管理员穿简洁小马甲，坐在窗边木桌前阅读一本打开的书；桌上有一杯茶、一盆小绿植和两三本书。",
    promptText: "一张独立的横向插画：一只拟人化橘猫图书管理员穿简洁小马甲，坐在窗边木桌前阅读一本打开的书；桌上有一杯茶、一盆小绿植和两三本书。透明水彩与温暖儿童绘本风格，柔和自然光，纸张纹理可见，色彩清透克制，主体、动作和桌面物件清晰完整。不要文字、标题、边框、表格、拼版、信息图、UI、水印或多画面组合。",
    promptSha256: "7b9028e383835b574e0a25bcfb97f7e4ab9f34b9047918cdd86c1afe8fbec66f",
    requestedCount: 4,
    aspectRatio: "4:3",
    results: pendingResults,
  },
];

export const registryRecords: readonly RegistryRecord[] = [...styles, ...promptCases];

export const registrySnapshot = {
  sourceRepository: "idaibin/ai-handbook",
  sourceCommit: "27ae1d2045da94a6391ea97099cbbe2cca2f276c",
  sourceExperimentPath: "experiments/visual-registry-mvp-01",
  generatedAt: "2026-08-25T07:30:00+04:00",
  note: "This Next.js app is a read-only projection. GitHub JSON contracts and Google Drive image assets remain authoritative.",
} as const;
