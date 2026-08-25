"use client";

import { useMemo, useState, type ChangeEvent } from "react";
import { RegistryCard } from "@/components/registry-card";
import type { RegistryKind, RegistryRecord, RegistryStatus } from "@/data/registry";
import { searchText } from "@/lib/registry";

interface RegistryExplorerProps {
  readonly records: readonly RegistryRecord[];
  readonly initialKind?: RegistryKind | "";
}

export function RegistryExplorer({ records, initialKind = "" }: RegistryExplorerProps) {
  const [query, setQuery] = useState("");
  const [kind, setKind] = useState<RegistryKind | "">(initialKind);
  const [medium, setMedium] = useState("");
  const [status, setStatus] = useState<RegistryStatus | "">("");
  const [imageFilter, setImageFilter] = useState<"" | "yes" | "no">("");

  const media = useMemo(
    () => [...new Set(records.map((record) => record.medium))].sort((a, b) => a.localeCompare(b)),
    [records],
  );

  const filteredRecords = useMemo(() => {
    const normalizedQuery = query.trim().toLocaleLowerCase("zh-CN");

    return records.filter((record) => {
      if (normalizedQuery && !searchText(record).includes(normalizedQuery)) return false;
      if (kind && record.kind !== kind) return false;
      if (medium && record.medium !== medium) return false;
      if (status && record.status !== status) return false;
      if (imageFilter === "yes" && record.resultCount === 0) return false;
      if (imageFilter === "no" && record.resultCount > 0) return false;
      return true;
    });
  }, [imageFilter, kind, medium, query, records, status]);

  return (
    <>
      <section className="filterPanel" aria-label="Registry 查询过滤器">
        <label className="field fieldSearch">
          <span>关键词</span>
          <input
            value={query}
            onChange={(event: ChangeEvent<HTMLInputElement>) => setQuery(event.target.value)}
            type="search"
            placeholder="搜索名称、Prompt、主题、标签或 SHA-256"
          />
        </label>
        <label className="field">
          <span>类型</span>
          <select value={kind} onChange={(event: ChangeEvent<HTMLSelectElement>) => setKind(event.target.value as RegistryKind | "")}>
            <option value="">全部</option>
            <option value="style">Style</option>
            <option value="prompt_case">PromptCase</option>
          </select>
        </label>
        <label className="field">
          <span>媒介</span>
          <select value={medium} onChange={(event: ChangeEvent<HTMLSelectElement>) => setMedium(event.target.value)}>
            <option value="">全部</option>
            {media.map((item) => (
              <option key={item} value={item}>
                {item}
              </option>
            ))}
          </select>
        </label>
        <label className="field">
          <span>状态</span>
          <select value={status} onChange={(event: ChangeEvent<HTMLSelectElement>) => setStatus(event.target.value as RegistryStatus | "")}>
            <option value="">全部</option>
            <option value="candidate">candidate</option>
            <option value="generation_blocked">generation_blocked</option>
            <option value="ready">ready</option>
          </select>
        </label>
        <label className="field">
          <span>图片</span>
          <select value={imageFilter} onChange={(event: ChangeEvent<HTMLSelectElement>) => setImageFilter(event.target.value as "" | "yes" | "no")}>
            <option value="">全部</option>
            <option value="yes">已有有效图片</option>
            <option value="no">暂无有效图片</option>
          </select>
        </label>
      </section>

      <div className="resultHeader">
        <h2>查询结果</h2>
        <span>
          {filteredRecords.length} / {records.length} 条
        </span>
      </div>

      {filteredRecords.length > 0 ? (
        <section className="registryGrid" aria-live="polite">
          {filteredRecords.map((record) => (
            <RegistryCard key={`${record.kind}:${record.id}`} record={record} />
          ))}
        </section>
      ) : (
        <section className="emptyState" aria-live="polite">
          <h2>没有匹配结果</h2>
          <p>减少筛选条件，或尝试搜索风格名称、媒介、标签和 Prompt 内容。</p>
        </section>
      )}
    </>
  );
}
