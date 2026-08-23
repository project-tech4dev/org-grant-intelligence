# Environment Variables

Copy `.env.example` → `.env` and fill in the values below. `.env` is gitignored — **never commit it**.

```bash
cp .env.example .env
```

## Required

| Variable | Example | Where to get it |
|---|---|---|
| `MODEL` | `anthropic:claude-sonnet-5` | Format is `provider:model_name`. Providers: `anthropic`, `openai`, `google_genai`. Examples: `openai:gpt-5`, `google_genai:gemini-2.5-pro` |
| `ANTHROPIC_API_KEY` | `sk-ant-...` | [console.anthropic.com](https://console.anthropic.com) → API Keys. Required if `MODEL` uses `anthropic:` |
| `OPENAI_API_KEY` | `sk-...` | [platform.openai.com](https://platform.openai.com). Required if `MODEL` uses `openai:` |
| `GOOGLE_API_KEY` | `AIza...` | [aistudio.google.com](https://aistudio.google.com). Required if `MODEL` uses `google_genai:` |

Only the API key for your chosen provider is required; the other two can stay empty.

## Tools

| Variable | Example | Notes |
|---|---|---|
| `TAVILY_API_KEY` | `tvly-...` | [app.tavily.com](https://app.tavily.com) — free tier: 1k searches/month. If empty, the web-search tool is disabled (URL fetching still works). |
| `GITHUB_PAT` | `github_pat_...` | GitHub → Settings → Developer settings → **Fine-grained tokens**. Scope it to ONLY the repos the agent may touch, with **Contents: read/write** and **Pull requests: read/write**. Do NOT grant merge/admin. If empty, the GitHub MCP integration is disabled. |

## Optional

| Variable | Default | Purpose |
|---|---|---|
| `CHECKPOINT_DB` | `checkpoints.sqlite` | Path to the SQLite checkpoint file, or a `postgresql://user:pass@host/db` URL to use Postgres instead |
| `GITHUB_MCP_URL` | `https://api.githubcopilot.com/mcp/` | GitHub's hosted MCP endpoint. Point at a local `github-mcp-server` if you need air-gapped operation |
| `MCP_SERVERS` | `{}` | JSON map of extra MCP servers, merged into the tool registry — see below |
| `GITHUB_TOOL_ALLOWLIST` | (safe built-in list) | Comma-separated GitHub MCP tool names the agent may use. The default excludes merge/delete operations |
| `DOWNLOADS_DIR` | `downloads` | Folder where the `download_file` tool saves files. In Docker this is `/data/downloads`, bind-mounted to `./downloads` on your machine |
| `RECURSION_LIMIT` | `100` | Max agent steps per turn (runaway-loop protection) |
| `ALLOWED_ORIGINS` | `http://localhost:5173,http://localhost:3000` | Comma-separated CORS origins (only relevant in dev; in Docker the nginx proxy makes this moot) |
| `LANGSMITH_TRACING` | `false` | Set `true` (plus `LANGSMITH_API_KEY`) for free tracing at [smith.langchain.com](https://smith.langchain.com) |

## Adding an MCP server without code changes

Set `MCP_SERVERS` to a JSON object keyed by server name, using the
[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) connection format:

```bash
MCP_SERVERS={"linear": {"transport": "streamable_http", "url": "https://mcp.linear.app/mcp", "headers": {"Authorization": "Bearer lin_api_..."}}}
```

All tools from extra servers are exposed to the agent as-is (no allowlist), so
prefer read-scoped credentials for servers you add this way.

## Rotation / safety notes

- The GitHub PAT is the real blast-radius control — prefer a 30–90 day expiry and re-issue it.
- All secrets enter only via env (`env_file` in docker-compose); nothing is baked into images.
- The agent is prompted never to merge PRs, and merge/delete tools are excluded by the default
  allowlist — but the PAT's scopes are what actually enforce this.
