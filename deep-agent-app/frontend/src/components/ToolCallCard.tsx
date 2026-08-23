import type { ToolSeg } from "../types/chat";

const PR_URL_RE = /https:\/\/github\.com\/[^\s"']+\/pull\/\d+/;

function argPreview(args: Record<string, unknown>): string {
  const json = JSON.stringify(args);
  if (!json || json === "{}") return "";
  return json.length > 80 ? json.slice(0, 80) + "…" : json;
}

export default function ToolCallCard({ seg }: { seg: ToolSeg }) {
  const prUrl =
    seg.name === "create_pull_request" && seg.result ? seg.result.match(PR_URL_RE)?.[0] : null;

  const statusClass =
    seg.status === "running" ? "running" : seg.isError ? "error" : "done";

  return (
    <details className="tool-card">
      <summary>
        <span className={`tool-status ${statusClass}`} aria-hidden="true" />
        <code className="tool-name">{seg.name}</code>
        <span className="tool-args-preview">{argPreview(seg.args)}</span>
        {seg.status === "running" && <span className="tool-running-label">running…</span>}
      </summary>
      <div className="tool-body">
        <div className="tool-label">Arguments</div>
        <pre>{JSON.stringify(seg.args, null, 2)}</pre>
        {seg.result !== undefined && (
          <>
            <div className="tool-label">{seg.isError ? "Error" : "Result"}</div>
            <pre>{seg.result}</pre>
          </>
        )}
        {prUrl && (
          <a className="pr-link" href={prUrl} target="_blank" rel="noreferrer">
            View pull request ↗
          </a>
        )}
      </div>
    </details>
  );
}
