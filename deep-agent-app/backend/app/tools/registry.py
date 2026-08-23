"""Assembles the agent's full tool list: native tools + MCP tools."""

from __future__ import annotations

import logging
from typing import Any

from app.config import Settings
from app.tools.files import download_file, read_pdf
from app.tools.mcp import load_mcp_tools
from app.tools.web import fetch_url, make_web_search

logger = logging.getLogger(__name__)


async def build_tools(settings: Settings) -> list[Any]:
    tools: list[Any] = [fetch_url, download_file, read_pdf]

    if settings.tavily_api_key:
        tools.append(make_web_search(settings.tavily_api_key))
    else:
        logger.warning("TAVILY_API_KEY not set — web search tool disabled")

    tools.extend(await load_mcp_tools(settings))

    logger.info("Tool registry ready: %s", [t.name for t in tools])
    return tools
