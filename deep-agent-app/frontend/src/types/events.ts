// Mirrors the backend SSE contract in backend/app/api/sse.py.

export type TokenEvent = { text: string };
export type ToolStartEvent = { id: string; name: string; args: Record<string, unknown> };
export type ToolEndEvent = { id: string; name: string; result_preview: string; is_error: boolean };
export type SourceEvent = { url: string; title: string | null };
export type DoneEvent = { thread_id: string };
export type StreamErrorEvent = { message: string };

export type StreamHandlers = {
  onToken?: (e: TokenEvent) => void;
  onToolStart?: (e: ToolStartEvent) => void;
  onToolEnd?: (e: ToolEndEvent) => void;
  onSource?: (e: SourceEvent) => void;
  onDone?: (e: DoneEvent) => void;
  onError?: (e: StreamErrorEvent) => void;
};
