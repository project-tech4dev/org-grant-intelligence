"""Typed application settings loaded from environment / .env."""

from __future__ import annotations

from functools import lru_cache
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict

# GitHub MCP tools the agent may use when no explicit allowlist is configured.
# Deliberately excludes merge_pull_request, delete_file, and other destructive ops:
# the agent can inspect repos and propose PRs, but a human merges them.
DEFAULT_GITHUB_TOOL_ALLOWLIST = [
    "get_me",
    "search_repositories",
    "search_code",
    "search_issues",
    "search_pull_requests",
    "get_file_contents",
    "list_branches",
    "list_commits",
    "get_commit",
    "list_issues",
    "issue_read",
    "add_issue_comment",
    "list_pull_requests",
    "pull_request_read",
    "create_branch",
    "create_or_update_file",
    "push_files",
    "create_pull_request",
    "update_pull_request",
]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # "provider:model_name", resolved via langchain init_chat_model.
    model: str = "anthropic:claude-sonnet-5"

    # SQLite file path, or a postgresql:// URL (requires the [postgres] extra).
    checkpoint_db: str = "checkpoints.sqlite"

    tavily_api_key: str = ""
    github_pat: str = ""
    github_mcp_url: str = "https://api.githubcopilot.com/mcp/"

    # Extra MCP servers as a JSON object in the langchain-mcp-adapters
    # connection format, e.g. {"linear": {"transport": "streamable_http", ...}}
    mcp_servers: dict[str, Any] = {}

    # Comma-separated override of DEFAULT_GITHUB_TOOL_ALLOWLIST.
    github_tool_allowlist: str = ""

    # Where download_file saves files; mounted to ./downloads on the host in Docker.
    downloads_dir: str = "downloads"

    recursion_limit: int = 50
    allowed_origins: str = "http://localhost:5173,http://localhost:3000"

    @property
    def github_allowlist(self) -> list[str]:
        if self.github_tool_allowlist.strip():
            return [t.strip() for t in self.github_tool_allowlist.split(",") if t.strip()]
        return DEFAULT_GITHUB_TOOL_ALLOWLIST

    @property
    def origins(self) -> list[str]:
        return [o.strip() for o in self.allowed_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
