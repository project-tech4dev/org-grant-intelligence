# Deep Agent App

A lightweight, production-ready AI agent built on **LangChain Deep Agents** (LangGraph), with:

- **Provider-agnostic LLM layer** — switch OpenAI / Anthropic / Gemini via one env var
- **Web search** (Tavily) + **URL fetching** with readable-text extraction
- **GitHub MCP** — inspect repos, commit to branches, open PRs (merge/delete excluded by allowlist)
- **SSE streaming** — tokens, tool calls, and sources stream live into the UI
- **Conversation checkpointing** — LangGraph threads persisted in SQLite (Postgres-ready)
- **Config-driven MCP registry** — add more MCP servers with an env var, zero code

```
frontend (React/Vite) ──SSE──▶ FastAPI ──▶ deep agent (LangGraph)
                                              ├─ tavily_search / fetch_url
                                              ├─ GitHub MCP (allowlisted)
                                              └─ checkpointer (SQLite/Postgres)
```

## Quickstart (dev)

Requirements: Python 3.11+, Node 20+.

```bash
cp .env.example .env        # then fill in keys — see ENV.md

# backend
cd backend
python3 -m venv .venv && .venv/bin/pip install -e .   # or: uv venv && uv pip install -e .
.venv/bin/uvicorn app.main:app --reload               # http://localhost:8000

# frontend (second terminal)
cd frontend
npm install
npm run dev                                           # http://localhost:5173 (proxies /api)
```

## Quickstart (Docker)

```bash
cp .env.example .env        # fill in keys
docker compose up --build   # app on http://localhost:3000
```

Only the frontend is exposed; nginx proxies `/api` to the backend with SSE
buffering disabled. Checkpoints live on a named volume.

## Configuration

Everything is env-driven — see **[ENV.md](ENV.md)**. The essentials:

| Variable | Purpose |
|---|---|
| `MODEL` | `anthropic:claude-sonnet-5`, `openai:gpt-5`, `google_genai:gemini-2.5-pro`, … |
| `TAVILY_API_KEY` | enables web search |
| `GITHUB_PAT` | enables GitHub MCP (fine-grained token, scoped repos only) |
| `MCP_SERVERS` | JSON map of additional MCP servers |

## API

| Endpoint | Description |
|---|---|
| `POST /api/chat/stream` | `{thread_id, message, model?}` → SSE stream of `token` / `tool_start` / `tool_end` / `source` / `done` / `error` events |
| `GET /api/threads/{id}` | Replay a thread's history (for page reloads) |
| `GET /api/config` | Active model spec |
| `GET /health` | Liveness (internal; not proxied) |

Smoke-test the stream without the UI:

```bash
curl -N localhost:8000/api/chat/stream \
  -H 'Content-Type: application/json' \
  -d '{"thread_id": "test-1", "message": "What is LangGraph? Search the web and cite sources."}'
```

## Architecture notes

- **SSE contract** (`backend/app/api/sse.py`): raw LangChain events are translated
  server-side into a small stable schema the UI is built against. The frontend never
  parses LangChain internals.
- **Tool registry** (`backend/app/tools/registry.py`): native tools + MCP tools are
  assembled in one place. New MCP servers come from `MCP_SERVERS` config.
- **GitHub safety**: a tool allowlist (`GITHUB_TOOL_ALLOWLIST`) excludes merge/delete
  operations, and the system prompt forbids merging — but the PAT's scopes are the
  real enforcement boundary.
- **Checkpointing** (`backend/app/persistence.py`): each conversation is a LangGraph
  thread. Set `CHECKPOINT_DB` to a `postgresql://` URL (and install
  `pip install -e '.[postgres]'`) to move off SQLite — nothing else changes.
- **Model switching**: `MODEL` env var, or per-request `model` field in the chat body.
  Agents are cached per spec and share the checkpointer, so a thread survives a
  mid-conversation model switch.
