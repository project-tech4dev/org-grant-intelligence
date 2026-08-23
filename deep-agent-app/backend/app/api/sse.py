"""Translates LangGraph/LangChain streaming events into the UI's SSE contract.

The frontend is built against this small, stable event schema — never forward
raw LangChain events to the browser:

  token       {"text": str}
  tool_start  {"id": str, "name": str, "args": object}
  tool_end    {"id": str, "name": str, "result_preview": str, "is_error": bool}
  source      {"url": str, "title": str | null}
  done        {"thread_id": str}
  error       {"message": str}
"""

from __future__ import annotations

import json
import logging
import re
from typing import Any, AsyncIterator

from langchain_core.messages import ToolMessage

logger = logging.getLogger(__name__)

RESULT_PREVIEW_CHARS = 1_500
GITHUB_HTML_URL_RE = re.compile(r'"html_url"\s*:\s*"([^"]+)"')
SEARCH_TOOL_NAMES = {"tavily_search", "web_search"}


def _sse(event: str, payload: dict[str, Any]) -> dict[str, str]:
    return {"event": event, "data": json.dumps(payload, default=str)}


def text_content(content: Any) -> str:
    """Extract plain text from message content (a string or content-block list)."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and block.get("type", "text") == "text":
                parts.append(block.get("text") or "")
        return "".join(parts)
    return ""


def _tool_output_text(output: Any) -> str:
    if isinstance(output, ToolMessage):
        output = output.content
    if isinstance(output, str):
        return output
    if isinstance(output, list):
        text = text_content(output)
        if text:
            return text
    try:
        return json.dumps(output, default=str)
    except (TypeError, ValueError):
        return str(output)


def _extract_sources(tool_name: str, tool_input: Any, output_text: str) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []
    if tool_name in SEARCH_TOOL_NAMES:
        try:
            data = json.loads(output_text)
            for result in data.get("results", []):
                if isinstance(result, dict) and result.get("url"):
                    sources.append({"url": result["url"], "title": result.get("title")})
        except (ValueError, AttributeError):
            pass
    elif tool_name == "fetch_url":
        url = (tool_input or {}).get("url") if isinstance(tool_input, dict) else None
        if url:
            sources.append({"url": url, "title": None})
    else:
        # GitHub (and similar) tools: surface human-facing html_url values.
        for url in GITHUB_HTML_URL_RE.findall(output_text)[:5]:
            sources.append({"url": url, "title": None})
    return sources[:10]


async def agent_event_stream(
    agent: Any,
    *,
    message: str,
    thread_id: str,
    recursion_limit: int,
) -> AsyncIterator[dict[str, str]]:
    config = {"configurable": {"thread_id": thread_id}, "recursion_limit": recursion_limit}
    payload = {"messages": [{"role": "user", "content": message}]}
    seen_urls: set[str] = set()

    try:
        async for event in agent.astream_events(payload, config=config, version="v2"):
            kind = event["event"]

            if kind == "on_chat_model_stream":
                text = text_content(event["data"]["chunk"].content)
                if text:
                    yield _sse("token", {"text": text})

            elif kind == "on_tool_start":
                yield _sse(
                    "tool_start",
                    {
                        "id": event["run_id"],
                        "name": event["name"],
                        "args": event["data"].get("input") or {},
                    },
                )

            elif kind == "on_tool_end":
                output = event["data"].get("output")
                output_text = _tool_output_text(output)
                is_error = getattr(output, "status", None) == "error"
                yield _sse(
                    "tool_end",
                    {
                        "id": event["run_id"],
                        "name": event["name"],
                        "result_preview": output_text[:RESULT_PREVIEW_CHARS],
                        "is_error": is_error,
                    },
                )
                if not is_error:
                    for source in _extract_sources(
                        event["name"], event["data"].get("input"), output_text
                    ):
                        if source["url"] not in seen_urls:
                            seen_urls.add(source["url"])
                            yield _sse("source", source)

            elif kind == "on_tool_error":
                yield _sse(
                    "tool_end",
                    {
                        "id": event["run_id"],
                        "name": event["name"],
                        "result_preview": str(event["data"].get("error"))[:RESULT_PREVIEW_CHARS],
                        "is_error": True,
                    },
                )

        yield _sse("done", {"thread_id": thread_id})
    except Exception as exc:
        logger.exception("Agent stream failed (thread %s)", thread_id)
        yield _sse("error", {"message": f"{type(exc).__name__}: {exc}"})
