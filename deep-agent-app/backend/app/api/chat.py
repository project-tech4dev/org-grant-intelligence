"""Chat streaming, thread history, and config endpoints."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Request
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from pydantic import BaseModel, Field
from sse_starlette.sse import EventSourceResponse

from app.api.sse import RESULT_PREVIEW_CHARS, agent_event_stream, text_content

router = APIRouter()


class ChatRequest(BaseModel):
    thread_id: str = Field(min_length=1, max_length=128)
    message: str = Field(min_length=1, max_length=32_000)
    model: str | None = None


@router.post("/chat/stream")
async def chat_stream(body: ChatRequest, request: Request):
    try:
        agent = request.app.state.agent_factory.get(body.model)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    settings = request.app.state.settings
    return EventSourceResponse(
        agent_event_stream(
            agent,
            message=body.message,
            thread_id=body.thread_id,
            recursion_limit=settings.recursion_limit,
        )
    )


@router.get("/config")
async def get_config(request: Request) -> dict[str, Any]:
    return {"model": request.app.state.settings.model}


@router.get("/threads/{thread_id}")
async def get_thread(thread_id: str, request: Request) -> dict[str, Any]:
    agent = request.app.state.agent_factory.get(None)
    state = await agent.aget_state({"configurable": {"thread_id": thread_id}})
    messages = (state.values or {}).get("messages", [])
    serialized = [s for m in messages if (s := _serialize_message(m)) is not None]
    return {"thread_id": thread_id, "messages": serialized}


def _serialize_message(message: Any) -> dict[str, Any] | None:
    if isinstance(message, HumanMessage):
        return {"role": "user", "content": text_content(message.content)}
    if isinstance(message, AIMessage):
        return {
            "role": "assistant",
            "content": text_content(message.content),
            "tool_calls": [
                {"id": tc.get("id", ""), "name": tc.get("name", ""), "args": tc.get("args", {})}
                for tc in (message.tool_calls or [])
            ],
        }
    if isinstance(message, ToolMessage):
        return {
            "role": "tool",
            "tool_call_id": message.tool_call_id,
            "name": message.name or "",
            "content": text_content(message.content)[:RESULT_PREVIEW_CHARS],
        }
    return None
