"""MCP tool loading via langchain-mcp-adapters.

GitHub is configured from GITHUB_PAT; arbitrary extra servers come from the
MCP_SERVERS setting so new integrations need zero code changes.
"""

from __future__ import annotations

import logging
from typing import Any

from langchain_mcp_adapters.client import MultiServerMCPClient

from app.config import Settings

logger = logging.getLogger(__name__)


def build_server_config(settings: Settings) -> dict[str, dict[str, Any]]:
    servers: dict[str, dict[str, Any]] = {}
    if settings.github_pat:
        servers["github"] = {
            "transport": "streamable_http",
            "url": settings.github_mcp_url,
            "headers": {"Authorization": f"Bearer {settings.github_pat}"},
        }
    servers.update(settings.mcp_servers)
    return servers


async def load_mcp_tools(settings: Settings) -> list[Any]:
    servers = build_server_config(settings)
    if not servers:
        return []

    client = MultiServerMCPClient(servers)
    tools: list[Any] = []
    github_allowlist = set(settings.github_allowlist)

    for name in servers:
        try:
            server_tools = await client.get_tools(server_name=name)
        except Exception:
            logger.exception("Failed to load MCP tools from server %r; skipping", name)
            continue
        if name == "github":
            skipped = [t.name for t in server_tools if t.name not in github_allowlist]
            server_tools = [t for t in server_tools if t.name in github_allowlist]
            if skipped:
                logger.info("GitHub MCP: %d tools excluded by allowlist", len(skipped))
        tools.extend(server_tools)
        logger.info("MCP server %r: loaded %d tools", name, len(server_tools))

    return tools
