// Minimal SSE-over-fetch reader. Native EventSource can't POST a body,
// and this is ~50 lines, so we parse the stream by hand.

import type {
  DoneEvent,
  SourceEvent,
  StreamErrorEvent,
  StreamHandlers,
  TokenEvent,
  ToolEndEvent,
  ToolStartEvent,
} from "../types/events";

export type ChatRequestBody = {
  thread_id: string;
  message: string;
  model?: string;
};

export async function streamChat(
  body: ChatRequestBody,
  handlers: StreamHandlers,
  signal?: AbortSignal,
): Promise<void> {
  const response = await fetch("/api/chat/stream", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
    signal,
  });
  if (!response.ok || !response.body) {
    throw new Error(`Chat request failed with status ${response.status}`);
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  // Aborting the fetch doesn't reliably reject a pending reader.read() in all
  // browsers (Safari, notably). Cancelling the reader resolves the pending
  // read with {done: true} everywhere, and closes the connection so the
  // backend cancels the agent run.
  const onAbort = () => {
    void reader.cancel().catch(() => {});
  };
  if (signal) {
    if (signal.aborted) {
      onAbort();
      return;
    }
    signal.addEventListener("abort", onAbort, { once: true });
  }

  const dispatch = (rawEvent: string) => {
    let eventName = "message";
    const dataLines: string[] = [];
    for (const line of rawEvent.split("\n")) {
      if (line.startsWith("event:")) eventName = line.slice(6).trim();
      else if (line.startsWith("data:")) dataLines.push(line.slice(5).trimStart());
    }
    if (dataLines.length === 0) return; // comment/ping frames
    let data: unknown;
    try {
      data = JSON.parse(dataLines.join("\n"));
    } catch {
      return;
    }
    switch (eventName) {
      case "token":
        handlers.onToken?.(data as TokenEvent);
        break;
      case "tool_start":
        handlers.onToolStart?.(data as ToolStartEvent);
        break;
      case "tool_end":
        handlers.onToolEnd?.(data as ToolEndEvent);
        break;
      case "source":
        handlers.onSource?.(data as SourceEvent);
        break;
      case "done":
        handlers.onDone?.(data as DoneEvent);
        break;
      case "error":
        handlers.onError?.(data as StreamErrorEvent);
        break;
    }
  };

  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done || signal?.aborted) break;
      // Normalize CRLF (sse-starlette emits \r\n); re-normalizing the whole
      // buffer is idempotent and handles \r\n split across chunk boundaries.
      buffer = (buffer + decoder.decode(value, { stream: true })).replace(/\r\n/g, "\n");
      let separatorIndex: number;
      while ((separatorIndex = buffer.indexOf("\n\n")) !== -1) {
        dispatch(buffer.slice(0, separatorIndex));
        buffer = buffer.slice(separatorIndex + 2);
      }
    }
  } finally {
    signal?.removeEventListener("abort", onAbort);
  }
}
