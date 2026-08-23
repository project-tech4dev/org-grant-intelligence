export type Source = { url: string; title: string | null };

export type ToolSeg = {
  kind: "tool";
  id: string;
  name: string;
  args: Record<string, unknown>;
  status: "running" | "done";
  result?: string;
  isError?: boolean;
};

export type TextSeg = { kind: "text"; text: string };

export type Segment = TextSeg | ToolSeg;

export type UserMessage = { role: "user"; text: string };

export type AssistantMessage = {
  role: "assistant";
  segments: Segment[];
  sources: Source[];
  error?: string;
};

export type ChatMessage = UserMessage | AssistantMessage;
