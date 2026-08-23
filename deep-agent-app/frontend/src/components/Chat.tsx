import { useEffect, useReducer, useRef, useState } from "react";
import { fetchThread } from "../api/history";
import { streamChat } from "../api/stream";
import type { AssistantMessage, ChatMessage, Segment, Source } from "../types/chat";
import Message from "./Message";

type Action =
  | { type: "hydrate"; messages: ChatMessage[] }
  | { type: "send"; text: string }
  | { type: "token"; text: string }
  | { type: "tool_start"; id: string; name: string; args: Record<string, unknown> }
  | { type: "tool_end"; id: string; result: string; isError: boolean }
  | { type: "source"; source: Source }
  | { type: "stream_error"; message: string }
  | { type: "finalize" };

function closeRunningTools(segments: Segment[], note: string): Segment[] {
  return segments.map((seg): Segment => {
    if (seg.kind === "tool" && seg.status === "running") {
      return { ...seg, status: "done", isError: true, result: seg.result ?? note };
    }
    return seg;
  });
}

function withLastAssistant(
  messages: ChatMessage[],
  update: (m: AssistantMessage) => AssistantMessage,
): ChatMessage[] {
  const last = messages[messages.length - 1];
  if (!last || last.role !== "assistant") return messages;
  return [...messages.slice(0, -1), update(last)];
}

function reducer(messages: ChatMessage[], action: Action): ChatMessage[] {
  switch (action.type) {
    case "hydrate":
      return action.messages;
    case "send":
      return [
        ...messages,
        { role: "user", text: action.text },
        { role: "assistant", segments: [], sources: [] },
      ];
    case "token":
      return withLastAssistant(messages, (m) => {
        const segments = [...m.segments];
        const last = segments[segments.length - 1];
        if (last && last.kind === "text") {
          segments[segments.length - 1] = { kind: "text", text: last.text + action.text };
        } else {
          segments.push({ kind: "text", text: action.text });
        }
        return { ...m, segments };
      });
    case "tool_start":
      return withLastAssistant(messages, (m) => ({
        ...m,
        segments: [
          ...m.segments,
          { kind: "tool", id: action.id, name: action.name, args: action.args, status: "running" },
        ],
      }));
    case "tool_end":
      return withLastAssistant(messages, (m) => ({
        ...m,
        segments: m.segments.map((seg): Segment => {
          if (seg.kind === "tool" && seg.id === action.id) {
            return { ...seg, status: "done", result: action.result, isError: action.isError };
          }
          return seg;
        }),
      }));
    case "source":
      return withLastAssistant(messages, (m) =>
        m.sources.some((s) => s.url === action.source.url)
          ? m
          : { ...m, sources: [...m.sources, action.source] },
      );
    case "stream_error":
      return withLastAssistant(messages, (m) => ({
        ...m,
        error: action.message,
        segments: closeRunningTools(m.segments, "(run aborted before this tool finished)"),
      }));
    case "finalize":
      return withLastAssistant(messages, (m) => ({
        ...m,
        segments: closeRunningTools(m.segments, "(interrupted)"),
      }));
  }
}

export default function Chat({ threadId }: { threadId: string }) {
  const [messages, dispatch] = useReducer(reducer, []);
  const [streaming, setStreaming] = useState(false);
  const [draft, setDraft] = useState("");
  const abortRef = useRef<AbortController | null>(null);
  const bottomRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetchThread(threadId)
      .then((history) => {
        if (!cancelled && history.length > 0) dispatch({ type: "hydrate", messages: history });
      })
      .catch(() => {});
    return () => {
      cancelled = true;
    };
  }, [threadId]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const send = async () => {
    const text = draft.trim();
    if (!text || streaming) return;
    setDraft("");
    setStreaming(true);
    dispatch({ type: "send", text });

    const controller = new AbortController();
    abortRef.current = controller;
    try {
      await streamChat(
        { thread_id: threadId, message: text },
        {
          onToken: (e) => dispatch({ type: "token", text: e.text }),
          onToolStart: (e) =>
            dispatch({ type: "tool_start", id: e.id, name: e.name, args: e.args }),
          onToolEnd: (e) =>
            dispatch({ type: "tool_end", id: e.id, result: e.result_preview, isError: e.is_error }),
          onSource: (e) => dispatch({ type: "source", source: e }),
          onError: (e) => dispatch({ type: "stream_error", message: e.message }),
        },
        controller.signal,
      );
    } catch (err) {
      if ((err as Error).name !== "AbortError") {
        dispatch({ type: "stream_error", message: String(err) });
      }
    } finally {
      dispatch({ type: "finalize" });
      setStreaming(false);
      abortRef.current = null;
    }
  };

  const stop = () => abortRef.current?.abort();

  return (
    <div className="chat">
      <div className="messages">
        {messages.length === 0 && (
          <div className="empty-state">
            Ask a research question, or point me at a GitHub repo to inspect or change.
          </div>
        )}
        {messages.map((message, i) => (
          <Message key={i} message={message} />
        ))}
        <div ref={bottomRef} />
      </div>
      <div className="composer">
        <textarea
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              void send();
            }
          }}
          placeholder="Message the agent… (Enter to send, Shift+Enter for newline)"
          rows={3}
          disabled={streaming}
        />
        {streaming ? (
          <button className="btn stop" onClick={stop}>
            Stop
          </button>
        ) : (
          <button className="btn" onClick={() => void send()} disabled={!draft.trim()}>
            Send
          </button>
        )}
      </div>
    </div>
  );
}
