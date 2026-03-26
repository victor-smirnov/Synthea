# infra0: Synthea MCP + embedded Dolt

## What we are building and how it works

### Role in the larger Synthea picture

The repository defines **identity and ontology** (bootstrap, `kb/`), while **`mcp-server`** is a separate **executable bridge**: LLM clients (primarily Cursor via MCP) get **tools** that talk to **embedded Dolt** — a SQL database with Git-like branches, commits, and diffs (see [docs/dolt-operational-brief.md](docs/dolt-operational-brief.md)).

This is not “loading a persona from markdown”; it is an **operational memory subsystem**: structured storage, queries, and extension via Go stored procedures.

### Data flow (simplified)

```mermaid
flowchart LR
  Cursor[Cursor_or_other_MCP_client]
  HTTP[HTTP_8787]
  MCP[MCP_streamable_/mcp]
  Tools[MCP_tools]
  SE[SqlEngine_embedded_Dolt]
  Disk[SYNTHEA_MCP_DATA_memory_home]

  Cursor --> HTTP
  HTTP --> MCP
  MCP --> Tools
  Tools --> SE
  SE --> Disk
```

- The **client** invokes MCP tools (service name in code: `synthea-mcp`, version `0.0.1`).
- **Transport**: default is **stdio**; **HTTP** (`SYNTHEA_MCP_TRANSPORT=http`) suits Docker and Cursor — streamable handler, **`/mcp`** endpoint, plus **`GET /health`** (see `runHTTP` in [mcp-server/main.go](mcp-server/main.go)).
- **Engine**: one process runs **`engine.SqlEngine`** over a local Dolt repo; if the repo is missing, it initializes as in `openEmbeddedEngine` in the same file.

### Where data lives

| Variable | Purpose |
|----------|---------|
| `SYNTHEA_MCP_DATA` | Data root (default locally `./mcp-data`; in Compose **`/data`** on the volume) |
| Subdirs | `memory/` — Dolt DB, `home/` — Dolt config/home |

The named Docker volume **`synthea_mcp_data`** in [docker-compose.yml](docker-compose.yml) persists data across container restarts.

### Current capabilities (tools)

In `newMCPServer` in [mcp-server/main.go](mcp-server/main.go):

1. **`synthea_echo_proc`** — demo of the **Go stored procedure** `synthea_echo`, registered in the Dolt catalog (`CALL synthea_echo(...)`).
2. **`dolt_sql`** — arbitrary SQL through the same engine; the description says “read-only explore”, but **there is no strict enforcement yet** — room to tighten policy later.

The model also assumes **arbitrary SQL + Dolt versioning** (`CALL dolt_*`, system tables, etc. per the [operational brief](docs/dolt-operational-brief.md)).

### How this connects to the “thinking” layer

- **Mindware / bootstrap / `kb/`** remain the source of meaning and protocols for the agent’s *session* in Cursor.
- **MCP + Dolt** is what can **live on disk** for a long time, be versioned, and align with automation (branches, commits, merge) while chat is ephemeral.

Natural next steps from the brief: explicit branches per session, schemas for episodic memory, tighter limits on `dolt_sql`, MCP resources (files/snapshots), not only tools.

### One-sentence summary

**An MCP server on top of embedded Dolt**: Cursor (and other MCP clients) get a stable HTTP/stdio API to **versioned SQL memory** and **Go extensions**; Docker provides a persistent volume and healthcheck.

### Quick start (Docker)

```bash
cd infra0
cp env.docker.example env.docker   # optional
docker compose --env-file env.docker up -d --build
```

Check: `curl -fsS http://127.0.0.1:8787/health`. MCP URL for Cursor: `http://127.0.0.1:8787/mcp` (see `SYNTHEA_MCP_PUBLISH` in `env.docker` for the host port).
