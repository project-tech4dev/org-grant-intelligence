"""Streamlit UI for the Graphiti graph: search it, and add episodes to it.

    docker compose up -d
    streamlit run app.py

Two tabs:
  Search — the same three search approaches as search.py, with a text box
           instead of argv. The search logic is imported, not duplicated.
  Add    — one episode at a time, via add_episodes.add_episode(). Nothing is
           written until you press the button.
"""

import asyncio
import os
import threading
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

# Imported for side effects too: loads .env and pins EMBEDDING_DIM before
# graphiti_core is imported.
from add_episodes import add_episode, make_graphiti
from ingest_markdown import (
    EXTRACTION_INSTRUCTIONS,
    PROMPT_OVERHEAD_TOKENS,
    QuotaExhausted,
    TooLargeForTPM,
    add_with_retry,
    already_ingested,
    build_episodes,
)
from search import RECIPES, answer_from_facts, find_focal_node

from graphiti_core.llm_client.errors import RateLimitError  # noqa: E402
from graphiti_core.nodes import EpisodeType  # noqa: E402
from graphiti_core.utils.content_chunking import estimate_tokens  # noqa: E402

st.set_page_config(page_title="Graphiti", page_icon="🔎")


@st.cache_resource
def get_client():
    """Build Graphiti once per session, not once per keystroke.

    Streamlit re-runs this whole script on every interaction, and
    make_graphiti() loads two sentence-transformers models (~100MB) and opens
    a FalkorDB connection. cache_resource keeps one instance across re-runs.

    The event loop is cached alongside it, because the driver's async
    connections bind to the loop that created them -- a fresh asyncio.run()
    per re-run would close the loop out from under them.

    The loop gets its own thread and is never driven from the script thread.
    Streamlit starts a new script run as soon as you touch a widget, without
    waiting for the previous run to finish, so two runs share this one cached
    loop. Calling loop.run_until_complete() from the second run while the
    first is still inside it raises "RuntimeError: this event loop is already
    running". Owning the loop in a separate thread and submitting work with
    run_coroutine_threadsafe() makes overlapping runs safe.
    """
    loop = asyncio.new_event_loop()
    threading.Thread(
        target=loop.run_forever, daemon=True, name="graphiti-eventloop"
    ).start()
    return loop, make_graphiti()


def run(coro):
    """Run a coroutine on the cached loop from Streamlit's script thread."""
    loop, _ = get_client()
    return asyncio.run_coroutine_threadsafe(coro, loop).result()


loop, graphiti = get_client()

DEFAULT_GRAPH = os.getenv("FALKORDB_DATABASE", "graphiti")


@st.cache_resource
def get_writer(group: str):
    """A client pointed at `group`, for writing.

    Searching takes group_ids, but writing does not: on FalkorDB a group is a
    separate graph, so an episode lands in whichever graph the driver is bound
    to. The cached search client is bound to DEFAULT_GRAPH, so adding to any
    other graph needs its own driver. Cached per graph -- the embedder and
    reranker models are reloaded once per graph, not once per episode.
    """
    if group == DEFAULT_GRAPH:
        return graphiti
    return make_graphiti(group)


@st.cache_data(ttl=30)
def list_graphs() -> list[tuple[str, int]]:
    """(graph name, entity count) for every graph, biggest first.

    On FalkorDB each group_id is its own graph, so this is the list of
    ingested documents plus the default graph.

    The counts are the point: querying a deleted FalkorDB graph recreates it
    as an empty shell, so the list alone will happily offer you a graph with
    nothing in it. Cached briefly so a running ingest shows up.
    """

    async def fetch() -> list[tuple[str, int]]:
        client = graphiti.driver.client
        # default_db is FalkorDB's own bookkeeping graph, not one of ours.
        names = [n for n in await client.list_graphs() if n != "default_db"]
        out = []
        for name in names:
            try:
                result = await client.select_graph(name).query(
                    "MATCH (e:Entity) RETURN count(e)"
                )
                out.append((name, int(result.result_set[0][0])))
            except Exception:
                out.append((name, 0))
        return out

    try:
        graphs = run(fetch())
    except Exception:
        return [(DEFAULT_GRAPH, 0)]

    if not graphs:
        return [(DEFAULT_GRAPH, 0)]
    # Biggest first, so the graph you just filled is at the top.
    return sorted(graphs, key=lambda pair: (-pair[1], pair[0]))


# Everything under the repo root is offered in the file picker, so a document
# does not have to be copied into Graphiti/ to be ingested.
REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__", "falkordb_data", ".claude"}


@st.cache_data(ttl=60)
def find_markdown_files() -> list[str]:
    """Repo markdown files, as paths relative to the repo root.

    Cached because rglob over the whole repo on every widget interaction is
    wasteful -- Streamlit re-runs this script on each one.
    """
    found = []
    for path in REPO_ROOT.rglob("*.md"):
        if SKIP_DIRS & set(path.parts):
            continue
        found.append(str(path.relative_to(REPO_ROOT)))
    return sorted(found)


st.title("🔎 Graphiti")
caption = st.empty()  # filled in once the graph is chosen, below

with st.sidebar:
    st.header("Options")

    graphs = list_graphs()
    counts = dict(graphs)
    labels = [f"{name}  ({count} entities)" for name, count in graphs]

    # Open on the fullest graph. FALKORDB_DATABASE is not a useful default
    # here: it points at the starter graph from add_episodes.py, so an
    # ingested document would sit unsearched while the app answered from
    # three toy episodes.
    choice = st.selectbox(
        "Graph",
        labels,
        index=0,
        help=(
            "On FalkorDB each group_id is a separate graph, so episodes added "
            "under `kabil` are only searchable here by picking `kabil`. "
            "Searching a different graph finds nothing from it."
        ),
    )
    group = graphs[labels.index(choice)][0]

    if not counts.get(group):
        st.warning(f"`{group}` is empty. Nothing to search in it yet.")
    recipe = st.selectbox(
        "Search mode",
        ["facts", *RECIPES],
        help=(
            "**facts** - graphiti.search(): BM25 + cosine, merged with "
            "Reciprocal Rank Fusion. The only mode that supports node "
            "distance reranking.\n\n"
            "**edges** - same, via the configurable search_().\n\n"
            "**edges_diverse** - MMR reranking: trades relevance for variety, "
            "so it can return fewer results than you asked for.\n\n"
            "**edges_accurate** - cross-encoder reranking. Most accurate, "
            "slowest.\n\n"
            "**edges_popular** - favours facts mentioned in many episodes.\n\n"
            "**nodes** - entities instead of facts.\n\n"
            "**all** - facts, entities and communities together."
        ),
    )
    limit = st.slider("Max results", 1, 25, 10)

    narrate = st.toggle(
        "Answer in natural language",
        value=True,
        help=(
            "Sends the retrieved facts to Claude and shows a written answer, "
            "with the raw facts underneath. Turn off to see only the facts."
        ),
    )

    focus = st.text_input(
        "Focal entity (optional)",
        placeholder="e.g. Arjun",
        help=(
            "Reranks results by graph distance to this entity, pulling its own "
            "facts to the top. Only applies in **facts** mode."
        ),
    )
    if focus and recipe != "facts":
        st.info("Node distance reranking only applies in **facts** mode.")

caption.caption(
    f"Working on the **{group}** graph in FalkorDB "
    f"({counts.get(group, 0)} entities)."
)

# None for the driver's own default graph; a one-element list otherwise.
group_ids = None if group == DEFAULT_GRAPH else [group]

search_tab, add_tab = st.tabs(["Search", "Add node"])


# A function, not inline script: the early exits below are `return`s. st.stop()
# would end the whole script run and leave the Add tab blank.
def render_search():
    query = st.text_input("Query", placeholder="what do you know about KABIL?")
    go = st.button("Search", type="primary")

    if go or query:
        if not query.strip():
            st.warning("Type a query first.")
            return

        center_uuid = None
        if focus.strip():
            with st.spinner(f'Looking up "{focus}"...'):
                node, by_name = run(find_focal_node(graphiti, focus.strip(), group_ids))
            if node is None:
                st.warning("The graph has no entities. Add an episode first.")
            elif by_name:
                center_uuid = node.uuid
                st.success(f"Focal node: **{node.name}**")
            else:
                # Hybrid search always returns nearest neighbours, so an unknown
                # name yields a loose match rather than nothing. Say so.
                center_uuid = node.uuid
                st.warning(
                    f'No entity named "{focus}" — closest is **{node.name}**, using that.'
                )

        with st.spinner("Searching..."):
            if recipe == "facts":
                edges = run(
                    graphiti.search(
                        query=query,
                        center_node_uuid=center_uuid,
                        num_results=limit,
                        group_ids=group_ids,
                    )
                )
                results = None
            else:
                config = RECIPES[recipe].model_copy(deep=True)
                config.limit = limit
                results = run(
                    graphiti.search_(query=query, config=config, group_ids=group_ids)
                )
                edges = results.edges

        # What the LLM is allowed to use. Node summaries count as context in
        # nodes mode, where the search returns no edges at all.
        # The answer no longer prints [1]/[2] markers -- the facts are listed
        # under it instead -- but the numbering is kept so a reader can still
        # match a claim in the prose to the item it came from.
        context = [edge.fact for edge in edges]
        citation: dict[str, int] = {}
        if results is not None:
            for node in results.nodes:
                summary = (node.summary or "").strip()
                if summary:
                    context.append(f"{node.name}: {summary}")
                    citation[node.uuid] = len(context)

        if not context:
            st.info(
                f"No results in the **{group}** graph. "
                "If your data was added under a different group, pick it above."
            )
            return

        if narrate:
            with st.spinner("Writing an answer..."):
                answer = run(answer_from_facts(query, context))
            st.subheader("Answer")
            st.write(answer)
            st.caption(
                f"Grounded in the {len(context)} retrieved item(s) below — "
                "the model was given nothing else."
            )
            st.divider()

        if edges:
            # Numbered so a claim in the answer above can be traced back.
            st.subheader(f"Facts ({len(edges)})")
            for i, edge in enumerate(edges, start=1):
                st.markdown(f"{i}. {edge.fact}")

        if results is not None:
            if results.nodes:
                st.subheader(f"Entities ({len(results.nodes)})")
                for node in results.nodes:
                    n = citation.get(node.uuid)
                    with st.expander(f"{n}. {node.name}" if n else node.name):
                        st.write((node.summary or "_no summary_").strip())
            if results.communities:
                st.subheader(f"Communities ({len(results.communities)})")
                for community in results.communities:
                    st.markdown(f"- {community.name}")


with search_tab:
    render_search()

def render_ingest():
    """Ingest a markdown file, one episode per section.

    Same pipeline as ingest_markdown.py -- its build_episodes() and
    add_with_retry() are imported rather than reimplemented, so the split and
    the retry behaviour cannot drift from the CLI.
    """
    files = find_markdown_files()
    if not files:
        st.warning("No markdown files found under the repo root.")
        return

    choice = st.selectbox(
        "Markdown file",
        files,
        help="Any .md file in the repo. Nothing is read until you preview or ingest.",
    )
    path = REPO_ROOT / choice

    col_a, col_b = st.columns(2)
    with col_a:
        level = st.number_input(
            "Split on heading level",
            min_value=1,
            max_value=4,
            value=2,
            help=(
                "One episode per heading at this level. A section is the unit "
                "that holds a complete thought: the whole file as one episode "
                "makes the LLM extract in a single pass and it returns a "
                "shallow set."
            ),
        )
        max_ep_tokens = st.number_input(
            "Max tokens per episode",
            min_value=200,
            max_value=8000,
            value=1200,
            step=100,
            help=(
                "Sections bigger than this are split further. Do not lower it "
                f"to 'be safe': the ~{PROMPT_OVERHEAD_TOKENS} tokens of prompt "
                "overhead are charged per call, so smaller episodes mean more "
                "calls and a bigger total bill."
            ),
        )
    with col_b:
        ep_limit = st.number_input(
            "Ingest at most N episodes",
            min_value=1,
            max_value=200,
            value=1,
            help=(
                "Defaults to 1 so you can inspect what one section extracts "
                "before paying for the whole document. Counted after the "
                "resume filter, so it means N *more* episodes."
            ),
        )
        skip_existing = st.toggle(
            "Skip episodes already in the graph",
            value=True,
            help="Lets an interrupted run resume without paying for it twice.",
        )
        strip_code = st.toggle("Strip fenced code blocks", value=True)
        tpm = st.number_input(
            "Tokens-per-minute limit",
            min_value=1000,
            max_value=200000,
            value=8000,
            step=1000,
            help=(
                "Only used to flag oversized sections in the preview; it sends "
                "nothing. Defaults to 8000 to match ingest_markdown.py's --tpm, "
                "so the UI and the CLI agree on what counts as oversized. "
                "Anthropic's usage tier 1 is well above this, so raise it to "
                "your real limit to stop the preview over-warning."
            ),
        )

    use_instructions = st.toggle(
        "Use the built-in extraction instructions",
        value=True,
        help=(
            "Tells the extractor to capture dates, numbers, amounts, counts "
            "and generic demographic categories as facts. Without it, "
            "attribute data such as `| Established | 2012 |` is dropped. "
            f"Costs ~{estimate_tokens(EXTRACTION_INSTRUCTIONS)} tokens per call."
        ),
    )

    preview, ingest = st.columns(2)
    do_preview = preview.button("Preview the split (free)", width="stretch")
    do_ingest = ingest.button(
        f"Ingest {ep_limit} episode(s)", type="primary", width="stretch"
    )

    if not (do_preview or do_ingest):
        st.caption(
            "**Preview** reads the file and shows how it splits — no LLM calls, "
            "no writes, no cost. **Ingest** runs the real pipeline."
        )
        return

    text = path.read_text(encoding="utf-8")
    plan = build_episodes(
        text,
        int(max_ep_tokens),
        strip_code=strip_code,
        level=int(level),
        fallback=path.stem,
    )

    rows = []
    risky = 0
    for i, (ep_name, body) in enumerate(plan, start=1):
        body_tokens = estimate_tokens(body)
        request = body_tokens + PROMPT_OVERHEAD_TOKENS
        too_big = request > int(tpm)
        risky += too_big
        rows.append(
            {
                "#": i,
                "section": ep_name,
                "body tokens": body_tokens,
                "est. request": request,
                "oversized": "⚠️" if too_big else "",
            }
        )

    st.caption(
        f"`{choice}` — ~{estimate_tokens(text)} tokens → **{len(plan)} episode(s)**, "
        f"split on H{int(level)}"
    )
    st.dataframe(rows, hide_index=True, width="stretch")
    if risky:
        st.warning(
            f"{risky} episode(s) build a request bigger than the {int(tpm)} "
            "tokens-per-minute limit set beside the file picker. Lower the max "
            "tokens per episode, or raise the limit if 8000 is not yours."
        )

    if do_preview:
        st.info("Preview only — nothing was sent to the LLM or written.")
        return

    # ---- the real thing -------------------------------------------------
    writer = get_writer(group)
    run(writer.build_indices_and_constraints())

    todo = plan
    if skip_existing:
        existing = run(already_ingested(writer))
        before = len(todo)
        todo = [(n, b) for n, b in todo if n not in existing]
        if before != len(todo):
            st.info(f"{before - len(todo)} episode(s) already in the graph, skipped.")

    todo = todo[: int(ep_limit)]
    if not todo:
        st.success("Nothing left to ingest — every episode is already in the graph.")
        return

    # One timestamp for the whole document: graphiti uses reference_time for
    # temporal edge invalidation, so a per-episode now() would make it treat
    # later sections as superseding earlier ones.
    reference_time = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    instructions = EXTRACTION_INSTRUCTIONS if use_instructions else None

    progress = st.progress(0.0, text="starting...")
    nodes = edges = 0
    failed = []

    for i, (ep_name, body) in enumerate(todo, start=1):
        progress.progress((i - 1) / len(todo), text=f"[{i}/{len(todo)}] {ep_name}")
        try:
            result = run(
                add_with_retry(
                    writer,
                    name=ep_name,
                    episode_body=body,
                    source=EpisodeType.text,
                    source_description=f"{path.name} (markdown section)",
                    reference_time=reference_time,
                    group_id=group_ids[0] if group_ids else None,
                    custom_extraction_instructions=instructions,
                    previous_episode_uuids=None,
                )
            )
        except TooLargeForTPM:
            st.warning(f"**{ep_name}** — too large for the per-minute token limit.")
            failed.append(ep_name)
            continue
        except QuotaExhausted as exc:
            st.error(f"Out of API credit — stopping. {exc}"[:300])
            break
        except RateLimitError:
            st.warning(f"**{ep_name}** — still rate limited after all retries.")
            failed.append(ep_name)
            continue

        nodes += len(result.nodes)
        edges += len(result.edges)
        with st.expander(
            f"[{i}/{len(todo)}] {ep_name} — {len(result.nodes)} entities, "
            f"{len(result.edges)} facts"
        ):
            st.write("**Entities:** " + ", ".join(n.name for n in result.nodes))
            for edge in result.edges:
                st.markdown(f"- {edge.fact}")

    progress.progress(1.0, text="done")
    list_graphs.clear()  # the sidebar counts are cached for 30s

    st.success(
        f"Ingested {len(todo) - len(failed)} episode(s) into **{group}** — "
        f"{nodes} entities, {edges} facts extracted."
    )
    if len(plan) > len(todo):
        st.caption(
            f"{len(plan) - len(todo)} section(s) of this file are still "
            "un-ingested. Raise the limit and run again — "
            "'skip already in the graph' means you will not pay twice."
        )


with add_tab:
    st.caption(
        f"Writes to the **{group}** graph. Graphiti runs the LLM over the text "
        "to extract entities and facts — this tab is the only thing in the app "
        "that writes to the database."
    )
    paste_sub, file_sub = st.tabs(["Paste text", "Markdown file"])

    with file_sub:
        render_ingest()

with paste_sub:

    with st.form("add_episode"):
        text = st.text_area(
            "Episode text",
            height=140,
            placeholder="Priya Sharma is a data engineer at Dalgo. She joined in March 2023.",
        )
        name = st.text_input("Episode name", value="episode-ui")
        source_description = st.text_input("Source description", value="added via app.py")
        submitted = st.form_submit_button("Add to graph", type="primary")

    if submitted:
        if not text.strip():
            st.warning("Type some text first.")
        else:
            writer = get_writer(group)
            with st.spinner("Extracting entities and facts..."):
                # Indices are per-graph on FalkorDB and this is cheap to repeat.
                run(writer.build_indices_and_constraints())
                result = run(
                    add_episode(
                        writer, text.strip(), name.strip() or "episode-ui",
                        source_description.strip() or "added via app.py",
                    )
                )
            # The graph list is cached for 30s; drop it so the new counts show.
            list_graphs.clear()

            st.success(
                f"Added **{name}** — {len(result.nodes)} entities, "
                f"{len(result.edges)} facts."
            )
            if result.nodes:
                st.subheader("Entities")
                for node in result.nodes:
                    with st.expander(node.name):
                        st.write((node.summary or "_no summary_").strip())
            if result.edges:
                st.subheader("Facts")
                for i, edge in enumerate(result.edges, start=1):
                    st.markdown(f"{i}. {edge.fact}")
