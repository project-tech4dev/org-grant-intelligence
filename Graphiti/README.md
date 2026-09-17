# Graphiti + FalkorDB

A temporal knowledge graph over FalkorDB, driven by [Graphiti](https://github.com/getzep/graphiti).
Ported from [apekshagangurde/Langchain/graphiti](https://github.com/apekshagangurde/Langchain/tree/main/graphiti).

Groq does the LLM work (entity/fact extraction, and the written answer).
Embeddings and reranking run locally via `sentence-transformers`, so nothing
reaches OpenAI.

## Files

| File | What it does |
| --- | --- |
| `docker-compose.yml` | FalkorDB — the graph database. Port 6379, browser UI on :3000. |
| `connect.py` | Health check. Opens a connection, pings, closes. Writes nothing. |
| `add_episodes.py` | Adds episodes (nodes + facts). Also holds `make_graphiti()`, the local embedder and the local reranker that everything else imports. |
| `search.py` | CLI search — hybrid, node-distance reranked, and the configurable recipes. |
| `app.py` | Streamlit UI: a **Search** tab and an **Add node** tab. |

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env    # then fill in GROQ_API_KEY
```

Nothing here runs against a database until you start one.

## Running

```bash
docker compose up -d    # start FalkorDB
python connect.py       # confirm the connection

python add_episodes.py                  # the three starter episodes
python add_episodes.py "Priya works at Dalgo."   # one episode of your own

python search.py                        # interactive prompt
python search.py "who works at Dalgo?"  # one-shot
python search.py "Dalgo" --nodes        # entities instead of facts

streamlit run app.py                    # the UI
```

## Groups are separate graphs

On FalkorDB a `group_id` is a whole separate graph, not a filter on one graph.
`add_episodes.py --group-id kabil` writes to a graph named `kabil`, and it is
only searchable by picking `kabil` in the sidebar. The sidebar lists every
graph with its entity count, so an empty one is visible as empty — querying a
deleted FalkorDB graph silently recreates it as an empty shell.

## Starting clean

```bash
docker exec graphiti-falkordb redis-cli GRAPH.DELETE graphiti
```
