import { useEffect, useState } from "react";
import Chat from "./components/Chat";

const THREAD_KEY = "deep-agent-thread-id";

export default function App() {
  const [threadId, setThreadId] = useState<string>(
    () => localStorage.getItem(THREAD_KEY) ?? crypto.randomUUID(),
  );
  const [model, setModel] = useState<string>("");

  useEffect(() => {
    localStorage.setItem(THREAD_KEY, threadId);
  }, [threadId]);

  useEffect(() => {
    fetch("/api/config")
      .then((r) => r.json())
      .then((d: { model: string }) => setModel(d.model))
      .catch(() => {});
  }, []);

  return (
    <div className="app">
      <header className="header">
        <div className="header-title">
          <h1>Deep Agent</h1>
          {model && <span className="model-badge">{model}</span>}
        </div>
        <button className="btn ghost" onClick={() => setThreadId(crypto.randomUUID())}>
          New conversation
        </button>
      </header>
      {/* key remounts Chat with a clean slate when the thread changes */}
      <Chat key={threadId} threadId={threadId} />
    </div>
  );
}
