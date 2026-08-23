"""FastAPI application: agent lifecycle, CORS, routes."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.agent.factory import AgentFactory
from app.api.chat import router as chat_router
from app.config import get_settings
from app.persistence import open_checkpointer
from app.tools.registry import build_tools

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    async with open_checkpointer(settings.checkpoint_db) as checkpointer:
        tools = await build_tools(settings)
        app.state.settings = settings
        app.state.agent_factory = AgentFactory(
            tools=tools, checkpointer=checkpointer, settings=settings
        )
        logger.info("Agent ready: model=%s tools=%d", settings.model, len(tools))
        yield


app = FastAPI(title="Deep Agent API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_settings().origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
