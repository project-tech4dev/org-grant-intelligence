import type { Source } from "../types/chat";

function hostname(url: string): string {
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return url;
  }
}

export default function SourcesPanel({ sources }: { sources: Source[] }) {
  if (sources.length === 0) return null;
  return (
    <div className="sources">
      <span className="sources-label">Sources</span>
      {sources.map((source) => (
        <a
          key={source.url}
          className="source-chip"
          href={source.url}
          target="_blank"
          rel="noreferrer"
          title={source.title ?? source.url}
        >
          {source.title ? `${source.title} · ${hostname(source.url)}` : hostname(source.url)}
        </a>
      ))}
    </div>
  );
}
