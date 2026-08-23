import ReactMarkdown from "react-markdown";
import type { ChatMessage } from "../types/chat";
import SourcesPanel from "./SourcesPanel";
import ToolCallCard from "./ToolCallCard";

export default function Message({ message }: { message: ChatMessage }) {
  if (message.role === "user") {
    return <div className="message user">{message.text}</div>;
  }
  return (
    <div className="message assistant">
      {message.segments.map((seg, i) =>
        seg.kind === "text" ? (
          <div key={i} className="markdown">
            <ReactMarkdown>{seg.text}</ReactMarkdown>
          </div>
        ) : (
          <ToolCallCard key={seg.id || i} seg={seg} />
        ),
      )}
      {message.error && <div className="message-error">⚠ {message.error}</div>}
      <SourcesPanel sources={message.sources} />
    </div>
  );
}
