// Converts the backend's serialized thread history into UI chat messages.

import type { AssistantMessage, ChatMessage, ToolSeg } from "../types/chat";

type ApiToolCall = { id: string; name: string; args: Record<string, unknown> };

type ApiMessage = {
  role: "user" | "assistant" | "tool";
  content: string;
  tool_calls?: ApiToolCall[];
  tool_call_id?: string;
  name?: string;
};

export async function fetchThread(threadId: string): Promise<ChatMessage[]> {
  const response = await fetch(`/api/threads/${encodeURIComponent(threadId)}`);
  if (!response.ok) return [];
  const data = (await response.json()) as { messages: ApiMessage[] };
  return messagesFromHistory(data.messages ?? []);
}

export function messagesFromHistory(api: ApiMessage[]): ChatMessage[] {
  // Tool results arrive as separate "tool" messages; index them first.
  const toolResults = new Map<string, string>();
  for (const message of api) {
    if (message.role === "tool" && message.tool_call_id) {
      toolResults.set(message.tool_call_id, message.content);
    }
  }

  const out: ChatMessage[] = [];
  let current: AssistantMessage | null = null;

  for (const message of api) {
    if (message.role === "user") {
      if (current) {
        out.push(current);
        current = null;
      }
      out.push({ role: "user", text: message.content });
    } else if (message.role === "assistant") {
      // Merge consecutive assistant/tool steps into one visual turn.
      current ??= { role: "assistant", segments: [], sources: [] };
      if (message.content) {
        current.segments.push({ kind: "text", text: message.content });
      }
      for (const call of message.tool_calls ?? []) {
        const seg: ToolSeg = {
          kind: "tool",
          id: call.id,
          name: call.name,
          args: call.args,
          status: "done",
          result: toolResults.get(call.id),
        };
        current.segments.push(seg);
      }
    }
  }
  if (current) out.push(current);
  return out;
}
