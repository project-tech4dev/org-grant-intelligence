"""Step 2: add episodes (nodes + facts) and let Graphiti build the graph.

    docker compose up -d
    python add_episodes.py                 # the starter episodes below
    python add_episodes.py "some text"     # add one episode of your own

Nothing is written until you actually run this file. Importing it (as search.py
and app.py do) only builds the client.

Re-running adds the episodes again. To start clean:
    docker exec graphiti-falkordb redis-cli GRAPH.DELETE graphiti
"""

import argparse
import asyncio
import os

from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# Must be set before importing graphiti_core: it reads EMBEDDING_DIM at import time.
# 384 = sentence-transformers/all-MiniLM-L6-v2
os.environ.setdefault("EMBEDDING_DIM", "384")

from anthropic import AsyncAnthropic  # noqa: E402

from graphiti_core import Graphiti  # noqa: E402
from graphiti_core.cross_encoder.client import CrossEncoderClient  # noqa: E402
from graphiti_core.driver.falkordb_driver import FalkorDriver  # noqa: E402
from graphiti_core.embedder.client import EmbedderClient, EmbedderConfig  # noqa: E402
from graphiti_core.llm_client.anthropic_client import AnthropicClient  # noqa: E402
from graphiti_core.llm_client.config import LLMConfig  # noqa: E402
from graphiti_core.nodes import EpisodeType  # noqa: E402

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

ANTHROPIC_MODEL = "claude-opus-5"


class LocalEmbedder(EmbedderClient):
    """Graphiti ships only API-backed embedders and Anthropic has no
    embeddings endpoint, so embeddings run locally via sentence-transformers."""

    def __init__(self):
        from sentence_transformers import SentenceTransformer

        self.model = SentenceTransformer(EMBEDDING_MODEL)
        dim = self.model.get_embedding_dimension()
        if dim != int(os.environ["EMBEDDING_DIM"]):
            raise ValueError(f"set EMBEDDING_DIM={dim} to match {EMBEDDING_MODEL}")
        self.config = EmbedderConfig(embedding_dim=dim)

    async def create(self, input_data) -> list[float]:
        text = input_data if isinstance(input_data, str) else str(input_data)
        return (await self.create_batch([text]))[0]

    async def create_batch(self, input_data_list: list[str]) -> list[list[float]]:
        if not input_data_list:
            return []
        loop = asyncio.get_running_loop()
        vectors = await loop.run_in_executor(
            None,
            lambda: self.model.encode(input_data_list, normalize_embeddings=True),
        )
        return [[float(x) for x in v] for v in vectors]


class LocalReranker(CrossEncoderClient):
    """Local reranker so search doesn't fall back to OpenAI either."""

    def __init__(self):
        from sentence_transformers import CrossEncoder

        self.model = CrossEncoder(RERANKER_MODEL)

    async def rank(self, query: str, passages: list[str]) -> list[tuple[str, float]]:
        if not passages:
            return []
        loop = asyncio.get_running_loop()
        scores = await loop.run_in_executor(
            None, self.model.predict, [[query, p] for p in passages]
        )
        return sorted(
            ((p, float(s)) for p, s in zip(passages, scores, strict=False)),
            key=lambda pair: pair[1],
            reverse=True,
        )


class _MessagesCompat:
    """Fixes up every request graphiti sends to the Anthropic API.

    Two things need patching in graphiti-core 0.30.2's AnthropicClient
    against the anthropic 1.x SDK:

    1. It passes `temperature=` on every call (anthropic_client.py). anthropic
       1.x removed that parameter -- Claude 4.6 and later reject sampling
       parameters -- so the call raises TypeError before it reaches the API.
       Dropped here. This is not Opus-specific: without it, AnthropicClient
       fails on every model.
    2. It cannot set output_config, so effort is always the API default
       (high). ANTHROPIC_EFFORT (low|medium|high|xhigh|max) sets it.
       Extraction is several calls per episode, so lowering it is the
       cheapest way to cut the bill on a large ingest.
    """

    def __init__(self, messages):
        self._messages = messages
        effort = os.getenv("ANTHROPIC_EFFORT")
        self._output_config = {"effort": effort} if effort else None

    async def create(self, **kwargs):
        kwargs.pop("temperature", None)
        if self._output_config:
            kwargs.setdefault("output_config", self._output_config)
        return await self._messages.create(**kwargs)


class _AnthropicCompat:
    """Stands in for AsyncAnthropic: AnthropicClient only ever reaches for
    .messages.create()."""

    def __init__(self, client: AsyncAnthropic):
        self.messages = _MessagesCompat(client.messages)


def make_graphiti(database: str | None = None) -> Graphiti:
    """Build the Graphiti client. `database` overrides FALKORDB_DATABASE.

    On FalkorDB a group_id is a separate graph, not a filter, so writing to
    one means pointing the driver at that graph -- otherwise
    build_indices_and_constraints() builds its indices on the wrong graph.
    """
    api_key = os.environ["ANTHROPIC_API_KEY"]
    return Graphiti(
        graph_driver=FalkorDriver(
            host=os.getenv("FALKORDB_HOST", "localhost"),
            port=int(os.getenv("FALKORDB_PORT", "6379")),
            database=database or os.getenv("FALKORDB_DATABASE", "graphiti"),
        ),
        # Without an llm_client, Graphiti defaults to OpenAI and fails on a
        # missing OPENAI_API_KEY. max_tokens comes from LLMConfig's default
        # (16384), shared between thinking and the response.
        llm_client=AnthropicClient(
            config=LLMConfig(model=os.getenv("ANTHROPIC_MODEL", ANTHROPIC_MODEL)),
            # max_retries=1 because graphiti retries on top of this: three
            # attempts inside AnthropicClient.generate_response.
            client=_AnthropicCompat(AsyncAnthropic(api_key=api_key, max_retries=1)),
        ),
        embedder=LocalEmbedder(),
        cross_encoder=LocalReranker(),
    )


async def add_episode(graphiti, text: str, name: str, source_description: str):
    """Add one episode and print the entities and facts Graphiti extracted."""
    result = await graphiti.add_episode(
        name=name,
        episode_body=text,
        source=EpisodeType.text,
        source_description=source_description,
        reference_time=datetime.now(timezone.utc),
    )
    print(f"\n{name}: {text}")
    print(f"  entities ({len(result.nodes)}): {[n.name for n in result.nodes]}")
    print(f"  facts    ({len(result.edges)}):")
    for edge in result.edges:
        print(f"    - {edge.fact}")
    return result


# Small and deliberately connected, so the extracted graph has edges to look at.
EPISODES = [
    "Priya Sharma is a data engineer at Dalgo. She joined in March 2023.",
    "Dalgo is a data platform built by Project Tech4Dev for non-profits.",
    "Priya mentors Arjun Rao, a junior analyst who joined Dalgo in 2024.",
]


async def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "text", nargs="?", help="one episode to add; omit for the starter episodes"
    )
    parser.add_argument("--group-id", help="write to this graph instead of the default")
    args = parser.parse_args()

    graphiti = make_graphiti(args.group_id)
    try:
        # Creates indices and constraints. Safe to run repeatedly.
        await graphiti.build_indices_and_constraints()

        if args.text:
            await add_episode(graphiti, args.text, "episode-cli", "manual entry")
        else:
            for i, text in enumerate(EPISODES, start=1):
                await add_episode(
                    graphiti, text, f"episode-{i}", "step 2 starter episodes"
                )
    finally:
        await graphiti.close()


if __name__ == "__main__":
    asyncio.run(main())
