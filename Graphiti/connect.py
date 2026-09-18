"""Step 1: connect to FalkorDB through Graphiti and confirm it works.

    docker compose up -d
    python connect.py

Read-only: it opens a connection, pings, and closes. Nothing is written.
"""

import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # Graphiti/.env
# Falls back to the repo-root .env (does not override the local one)
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# Must be set before importing graphiti_core: it reads EMBEDDING_DIM at import time.
# 384 = sentence-transformers/all-MiniLM-L6-v2
os.environ.setdefault("EMBEDDING_DIM", "384")

from anthropic import AsyncAnthropic  # noqa: E402

from graphiti_core import Graphiti  # noqa: E402
from graphiti_core.driver.falkordb_driver import FalkorDriver  # noqa: E402
from graphiti_core.llm_client.anthropic_client import AnthropicClient  # noqa: E402
from graphiti_core.llm_client.config import LLMConfig  # noqa: E402

FALKOR_HOST = os.getenv("FALKORDB_HOST", "localhost")
FALKOR_PORT = int(os.getenv("FALKORDB_PORT", "6379"))

ANTHROPIC_MODEL = "claude-opus-5"


async def main():
    graphiti = Graphiti(
        # FalkorDB is passed as a driver; uri/user/password are Neo4j-only
        graph_driver=FalkorDriver(
            host=FALKOR_HOST,
            port=FALKOR_PORT,
            database=os.getenv("FALKORDB_DATABASE", "graphiti"),
        ),
        # Without this, Graphiti defaults to OpenAI and fails on a missing OPENAI_API_KEY.
        # A plain AsyncAnthropic is enough here because this file never sends a
        # prompt; graphiti's AnthropicClient passes a `temperature` the
        # anthropic 1.x SDK rejects, so anything that does call the model goes
        # through make_graphiti() in add_episodes.py instead.
        llm_client=AnthropicClient(
            config=LLMConfig(model=os.getenv("ANTHROPIC_MODEL", ANTHROPIC_MODEL)),
            client=AsyncAnthropic(
                api_key=os.environ["ANTHROPIC_API_KEY"], max_retries=1
            ),
        ),
    )

    try:
        await graphiti.driver.health_check()
        print(f"Connected to FalkorDB at {FALKOR_HOST}:{FALKOR_PORT}")
    finally:
        await graphiti.close()


if __name__ == "__main__":
    asyncio.run(main())
