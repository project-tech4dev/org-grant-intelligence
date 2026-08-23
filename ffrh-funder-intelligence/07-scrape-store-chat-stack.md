# How People Build Scrape → Store → Chat Pipelines with AI Agents (2025–2026)

Research conducted 13 Aug 2026 via three parallel research agents, to inform the FFRH
funder-intelligence architecture: (1) AI-agent web scraping, (2) storage of scraped data,
(3) using stored data as context for chat / agentic products.

---

## TL;DR — the consensus stack

1. **Scraping**: nobody serious runs "LLM reads every page." The production pattern is
   **fetch → clean to markdown → cheap-LLM extraction against a strict schema** for
   heterogeneous/low-volume sources, and **LLM-writes-scraper-code-once (self-healing on
   breakage)** for high-volume stable sources. Raw HTML is a ~7–50x token tax vs markdown.
2. **Storage**: one **Postgres** database (JSONB + pgvector + full-text, all in one place),
   raw HTML snapshots in cheap object storage (Cloudflare R2), and — the big 2025–26 shift —
   a **markdown knowledge base** (one file per entity) that agents grep/read directly,
   Claude-Code-style. Change tracking via `content_hash` + `first_seen`/`last_seen` +
   SCD2 version history.
3. **Consumption**: one-shot RAG is no longer the default. The mainstream pattern is an
   **agent with typed tools** (SQL query, doc search, fetch) **exposed as an MCP server** —
   exactly what Benevity and Candid shipped under Claude for Nonprofits. Nobody has built
   the Indian equivalent. Recurring value lives in **scheduled agents** (nightly diff →
   LLM fit-scoring → digest), not chat; chat is the front door.

Total infra cost for our scale: **$0–6/month** (Neon/Supabase free tier + R2 free tier, or
one small VPS).

---

## 1. Pulling data with AI agents

### The four approaches, by cost/reliability regime

| Regime | Approach | Marginal cost |
|---|---|---|
| Few sources, changing layouts (foundation sites, RFP pages) | markdown → cheap-LLM schema extraction per page | <$0.01/page |
| Same source, high volume, stable layout (registries) | LLM-generated deterministic code, or hand-found JSON API; zero LLM at runtime | ~$0 |
| Interactive JS flows re-run on schedule | **Stagehand** (Browserbase) with action caching — AI resolves the flow once, replays deterministically | first run $0.01–0.10 → ~$0 |
| Unknown navigation, one-offs | Browser Use / Firecrawl FIRE-1 / computer use | $0.02–0.50/task |
| Hostile/visual UIs | Skyvern (vision-based) | $0.10–0.50/task, last resort |

### Key tools

- **Firecrawl** — API workhorse: URL → markdown or schema'd JSON; `/crawl`, `/map`, `/monitor`
  (change detection). Free 500 credits, ~$16/mo hobby. Watch multipliers: AI extraction ≈ 5x credits.
- **Crawl4AI** (OSS, ~50k stars) — best free self-hosted core. CSS-schema extraction (free,
  deterministic) *and* LLM extraction with Pydantic schemas; adaptive crawling (LLM decides
  which links to follow, stops when it has enough).
- **Jina Reader** (`r.jina.ai/<url>`) — cheapest URL→markdown (~$0.10/1k requests); no anti-bot bypass.
- **llm-scraper** (TS) / **Instructor** (Python) — canonical schema-first extraction (Zod/Pydantic
  + structured outputs; validation failure → retry).
- **Browser agents**: Browser Use (~108k stars, LLM call per step), **Stagehand** (action caching —
  best fit for recurring portal crawls), Skyvern (vision, survives redesigns).
- **Managed**: Apify (actor marketplace + official MCP server), Zyte, Bright Data (biggest proxy
  network incl. Indian IPs + dataset marketplace), Kadoa/Reworkd (self-healing scraper-as-a-service).
- **Self-healing OSS**: `mdowis/anansi` (confidence-scored selectors, 4 healing strategies, ships
  an MCP server); `dgtlmoon/changedetection.io` (scheduled monitoring, now with LLM change rules —
  "alert only when a new RFP appears").

### Production patterns

- **Schema-first extraction is the contract**: Pydantic/Zod schema + structured outputs; freeform
  prompts are a prototyping smell. Validate → retry → dedupe → upsert with provenance.
- **Only LLM-process changed content**: hash/diff cleaned markdown; unchanged pages skip the LLM.
  Combined with prompt-caching the schema prefix, cuts recurring cost ~10x.
- **Prefer the hidden API**: for AJAX sites (NGO Darpan), find the XHR JSON endpoint in DevTools
  and hit it with httpx — no browser, no LLM. Prior art: `pallavmahamana/ngosearch`.
- **Geo-blocking (csr.gov.in)**: cheapest and cleanest fix is running the scraper on an
  **India-region VPS** (AWS ap-south-1 / DO Bangalore); Indian residential proxies (Bright Data,
  Infatica) only if datacenter ranges get blocked.
- **Anti-bot climate hardened in 2025**: Cloudflare now blocks AI crawlers by default (~20% of the
  web) and launched pay-per-crawl. Gov portals rarely run sophisticated anti-bot — politeness suffices.

### Legal notes

- **LinkedIn is a no-go.** Proxycurl (the #1 LinkedIn data API) was sued Jan 2025 and **shut down
  July 2025**; hiQ "won" the CFAA argument and still ended with a $500k settlement + permanent ban.
  Build narrative intelligence from news, press releases, MCA filings, annual reports, foundation
  newsletters instead. This directly affects the proposal's narrative-intelligence differentiator —
  it survives, but LinkedIn-free.
- Public Indian government data scraped politely from an Indian IP carries minimal risk. 2025 case
  law concentrates risk on: fake/authenticated accounts, continuing after cease-and-desist,
  circumventing blocks on ToS-protected content.

---

## 2. Storing scraped data

### The layer model (bronze/silver/gold applied to scraped data)

| Layer | Contents | Store |
|---|---|---|
| Bronze (raw) | Every fetch: gzip'd HTML/JSON + headers, keyed `raw/{source}/{urlhash}/{ts}` | Cloudflare R2 (10GB free, $0 egress — re-parsing the archive is free) |
| Silver | Cleaned markdown per page; extracted typed records, validated, deduped | Postgres: typed columns + JSONB long-tail + `content_md` |
| Gold | Entity-resolved funder profiles, enrichment, embeddings, markdown KB | Postgres + pgvector; `.md` files in git |

**Never parse-and-discard**: extractors are the most-changed component; keeping raw bytes means
improving the parser = re-run over storage, not re-crawl. Also provides "this deadline was on their
page on this date" evidence.

### Where people put it

- **"Just use pgvector" is the overwhelming consensus** at small/medium scale: documents, metadata,
  embeddings, and full-text in one DB, one transaction; SQL joins for filtering ("open education
  grants in Assam, ranked by similarity") — the thing standalone vector DBs (Pinecone/Qdrant) can't
  do without a painful sync layer. Vector search is 5–50ms vs 500ms–3s LLM generation, so dedicated
  vector-DB speed is a rounding error. Real proof point: 30M HN posts on one NVMe Postgres box,
  sub-4ms queries. Firecrawl itself migrated from Pinecone to Supabase pgvector.
- **Supabase** (Postgres + pgvector + storage + auth, free tier; pauses after 7 idle days — a
  nightly cron scrape incidentally prevents this) or **Neon** (scale-to-zero, no pause-death) or
  a $5–12/mo Hetzner/DO VPS.
- **Markdown-files-in-git as a first-class layer** — the emerging pattern: Anthropic dropped vector
  search from Claude Code for grep/glob/read agentic search ("outperformed everything, by a lot");
  Karpathy popularized agent-maintained markdown wikis. Rule of thumb: hundreds of docs → markdown
  + grep + an index file; many thousands → add embeddings. Bonus: **git diff of the nightly
  regenerated KB is a free human-readable change report on funder websites.**
- **dlt (dlthub)** handles incremental loading, merge upserts, and SCD2 declaratively if we don't
  want to hand-roll.

### The canonical change-tracking schema

Current table upserted on a stable `natural_key`, with `content_hash`, `first_seen`, `last_seen`,
`status` (open/closed/removed), plus an SCD2 `*_versions` history table (`valid_from`/`valid_to`).
Hash unchanged → bump `last_seen`; changed → close old version, insert new; absent from full
re-crawl → mark removed. This answers "when did this RFP appear/close." Firecrawl's changeTracking
returns exactly these states (`new/same/changed/removed`).

Provenance minimum on every row: `source_url`, `source_name`, `fetched_at`, `raw_object_key`,
`content_hash`, and `extractor_version` (the one people forget — tells you which rows to
regenerate after a parser fix).

**Entity resolution**: India gives unusually good deterministic keys — CIN, PAN, FCRA number,
12A/80G, normalized domain — before falling back to fuzzy name matching. `funder_aliases` table
mapping each source's ID to one immutable canonical `funder_id`.

---

## 3. Using the data: chat, matching, alerts

### The 2025–26 shift: retrieval split by data shape

- **Structured rows** (funders, grants, CSR spend) → **text-to-SQL / typed query tools**.
  Embeddings are the wrong tool for "which corporates spent >₹5cr on education CSR in Maharashtra
  in FY24" — that's a filter/aggregate. For funder intelligence, ~70% of expected questions are
  SQL-shaped. At our schema size (~5–15 tables), full DDL + 10–20 example queries in a cached
  system prompt performs close to dedicated tools (Vanna.ai, WrenAI).
- **Unstructured docs** (RFP PDFs, annual reports, news) → hybrid RAG: **contextual retrieval**
  (Anthropic — prepend an LLM-generated context blurb per chunk; −49% retrieval failures, −67%
  with reranking), BM25 + vector hybrid, Cohere/Jina reranker, and **metadata pre-filtering**
  (`status='open' AND deadline >= today` is a filter, not a hope).
- **Both in one product (our case)** → **an agent with tools** (`find_funders(sector, geography,
  min_grant_size)`, `get_rfps(status, deadline_before)`, `funder_history(id)`,
  `search_documents(query, filters)`, `web_fetch(url)`) that decides per question — exposed as
  an **MCP server**.

### Prior art in exactly our space

- **Benevity nonprofit MCP server** (Giving Tuesday 2025): 2.5M-nonprofit database exposed to
  Claude — search by cause/location, full profiles, no login, free on paid Claude plans.
- **Candid MCP connector**: funder profiles + sector research; example queries are literally
  funder-matching-via-chat.
- **Nobody has built the Indian equivalent** (MCA CSR spend + Indian foundations + govt schemes +
  RFPs). An MCP server over our Postgres is simultaneously: internal chat backend, distribution
  channel (any NGO with a Claude subscription connects with zero UI built by us), and the tool
  layer our own scheduled agents use.
- Purpose-built typed tools beat raw SQL passthrough for external users (less hallucination, safer).
  Plumbing options: crystaldba/postgres-mcp, pgEdge Postgres MCP.

### Skip-list (evidence-based)

- **GraphRAG/knowledge graphs**: funder→grantee→sector relations are *already relational* from
  scraping — SQL joins give 80% of GraphRAG for free. Revisit LightRAG only if users demand
  ecosystem-network questions joins can't answer.
- **Heavy frameworks**: for one DB + one doc index + one model, a plain-SDK ~400-line pipeline
  beats LangChain/LlamaIndex overhead. Claude Agent SDK + MCP tools is the lowest-friction
  agentic path.
- **Standalone vector DBs**: see §2.

### Beyond chat — where recurring value lives

- **Scheduled digests**: nightly scrape-diff → LLM classifies new RFPs → match against subscribed
  NGO profiles → email/WhatsApp digest. Working precedents: GovMatch, Jorpex, and India-specific
  **Minaions** (monitors 200+ Indian tender portals: GeM, CPPP, state eProcurement). Semantic
  tender discovery finds 40–60% more relevant opportunities than keyword portal search.
- **Matching/scoring**: LLM-as-judge with a rubric + structured output — score each NGO↔RFP pair
  on explicit dimensions (sector, geography, budget band, eligibility incl. FCRA/CSR-1, track
  record); embeddings/SQL pre-filter, LLM-score only the shortlist, batch nightly. Open-source
  job-search agents prove the exact shape (anandanair/job-scraper, MadsLorentzen/ai-job-search,
  BjornMelin/ai-job-scraper — the last has a schema detail worth copying: re-scrapes update
  provider fields without clobbering user notes).
- **Enrichment loops**: agent researches each funder and writes/updates its profile — Exa
  (semantic discovery) + Firecrawl (extraction) + LLM synthesis; Firecrawl's **Fire Enrich** is
  an open-source reference. This generates the per-funder markdown that chat and matching consume.
- **Grounded proposal drafting**: retrieval-first generation with per-claim citations to record
  IDs. Commercial proof: Instrumentl Apply (drafts from its 450k-funder DB), Grantable.

### Quality bar (day one, not later)

- **Citations to record IDs**: require `[funder:123]`-style references; Claude API's native
  Citations feature does span-level attribution. Plus an abstention policy ("answer only from
  retrieved records").
- **Freshness surfaced**: expose `fetched_at` in tool results; model says "as of the funder's site
  on 2 Aug 2026." Grant deadlines make staleness the #1 credibility risk.
- **Evals**: ~50-question golden set (SQL-shaped, doc-shaped, matching); Ragas/DeepEval for
  faithfulness + programmatic checks (cited IDs exist? SQL runs?). Unevaluated RAG hallucinates
  in up to ~40% of responses even with correct context retrieved. Spot-check LLM fit-scores
  against a program officer's rankings before trusting digests.

---

## 4. Proposed FFRH architecture (synthesis)

```
[Scrapers — nightly cron on an India-region VPS]
  csr.gov.in ........ Playwright/Stagehand (cached flow), check for JSON endpoints first
  NGO Darpan ........ direct XHR JSON endpoints via httpx (no browser, no LLM)
  NGOBox RFPs ....... changedetection.io/hash-diff → on change: markdown → LLM → Pydantic RFP schema
  Foundation sites .. Crawl4AI adaptive crawl → markdown → cheap-LLM extract, monthly + diff
  News/narrative .... Serper/Tavily/Exa search + Jina Reader → LLM classification (no LinkedIn)
       │ raw bytes ────────────────► R2  raw/{source}/{urlhash}/{ts}.html.gz     (bronze)
       ▼
[Extract — versioned extractors, schema-first, validate/retry]
       ▼
Postgres (Neon/Supabase/VPS)                                                     (silver/gold)
  funders, grants, rfps, csr_spend  (typed cols + JSONB + provenance + first/last_seen)
  *_versions (SCD2), funder_aliases (CIN/PAN/FCRA/domain keys)
  chunks (tsvector + pgvector) — embed only changed rows
       ▼
[Markdown KB]  funders/{slug}.md, rfps/{slug}.md, index.md — committed to git    (agent layer)
       ▼
[Consumption]
  MCP server w/ typed tools (find_funders, get_rfps, funder_history, search_docs)
  Scheduled agents: nightly diff → fit-scoring → WhatsApp/email digests
  Chat: Claude (via MCP) or thin web UI; citations to record IDs + fetched_at
```

**Sequencing**: (1) prototype this week with a Claude Project over exported markdown-per-funder
files — zero build; (2) markdown KB + git first (immediately useful, free); (3) Postgres + change
tracking; (4) MCP server + digests; (5) embeddings only when the corpus outgrows grep.

**Cost posture**: cheap model (Haiku-class) on cleaned markdown everywhere; frontier model only on
validation failure; prompt-cache schemas; LLM-process only diffs. Infra $0–6/mo.

---

## Sources

Scraping: Kadoa "How AI is changing web scraping" · Scrapfly AI browser agents roundup ·
dev.to "Framework Wars" (Browser Use vs Stagehand vs Skyvern) · Firecrawl job-boards tutorial ·
Crawl4AI docs · mishushakov/llm-scraper · mdowis/anansi · dgtlmoon/changedetection.io ·
reworkd/harambe · Apify MCP server · token-tax measurement (Medium/@spinov001) · Proxycurl
shutdown post-mortem (nubela.co) · Cloudflare pay-per-crawl (MIT Tech Review) · captnemo GoI
geo-fencing · pallavmahamana/ngosearch · Bright Data India proxies.

Storage: Encore "You probably don't need a vector database" · Qdrant pgvector-tradeoffs rebuttal ·
30M HN posts in pgvector (dev.to/geekyfox90) · Supabase × Firecrawl case study · Firecrawl change
tracking · ScrapingAnt data-quality layer · dlt SCD2 docs · Bright Data medallion architecture ·
vadim.blog Claude Code no-indexing · Milvus grep-only counterpoint · MindStudio wiki-vs-RAG ·
Neon vs Supabase free tiers · R2 pricing · scrapy-webarchive/WACZ · Zack Proser scraping-for-RAG.

Consumption: Anthropic Contextual Retrieval · Benevity nonprofit MCP server docs + press release ·
Candid MCP connector blog · Claude for Nonprofits · Vanna.ai / WrenAI comparisons · GraphRAG cost
history (Medium/graph-praxis) + LightRAG · Algolia agentic-retrieval explainer · Instrumentl /
Grantable · Minaions/GovMatch/Jorpex tender-AI landscape · anandanair/job-scraper ·
MadsLorentzen/ai-job-search · BjornMelin/ai-job-scraper · Firecrawl Fire Enrich · DeepEval/Ragas
LLM-as-judge guides · crystaldba/postgres-mcp · pgEdge Postgres MCP · shadcn inline-citation ·
NotebookLM vs Claude Projects comparisons.
