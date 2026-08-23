"""Builds and caches deep agent graphs per model spec."""

from __future__ import annotations

from typing import Any, Sequence

from deepagents import create_deep_agent
from langgraph.checkpoint.base import BaseCheckpointSaver

from app.agent.models import resolve_model
from app.agent.prompt import SYSTEM_PROMPT
from app.config import Settings


class AgentFactory:
    """Creates deep agents lazily, one per model spec, sharing tools and checkpointer.

    Sharing the checkpointer means a conversation thread survives a mid-thread
    model switch — the new model resumes from the same LangGraph state.
    """

    def __init__(
        self,
        *,
        tools: Sequence[Any],
        checkpointer: BaseCheckpointSaver,
        settings: Settings,
    ) -> None:
        self._tools = list(tools)
        self._checkpointer = checkpointer
        self._settings = settings
        self._agents: dict[str, Any] = {}

    def get(self, model_spec: str | None = None) -> Any:
        spec = model_spec or self._settings.model
        if spec not in self._agents:
            self._agents[spec] = create_deep_agent(
                model=resolve_model(spec),
                tools=self._tools,
                system_prompt=SYSTEM_PROMPT,
                checkpointer=self._checkpointer,
            )
        return self._agents[spec]
