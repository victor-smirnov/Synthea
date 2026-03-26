# Dolt: operational brief for the memory subsystem (Synthea)

Sources: local clone `dolt/` → `README.md`, `go/libraries/doltcore/doltdb/AGENT.md`; full reference: [docs.dolthub.com](https://docs.dolthub.com/introduction/what-is-dolt).

## What it is

- **Dolt** is a SQL database with Git-style versioning: branches, merge, diff, push/pull, clone.
- Connect **as to MySQL** (compatible protocol; logs may show a Vitess-based server).
- Versioning in SQL: **system tables** (read) + **`dolt_*` stored procedures** (write), analogous to `git` commands.

## CLI and server

| Task | Notes |
|------|-------|
| `dolt init` | Database repo in the current directory |
| `dolt sql-server` | Server defaults to `localhost:3306` |
| `dolt sql` / `mysql -h 127.0.0.1 -P 3306 -u root` | Client; for the MySQL client, prefer TCP |
| `dolt --branch <name> sql` | Session starts on the given branch |

Recommended MySQL client: **8.4 LTS** (9.x may need separate auth configuration).

## Critical for automation: branches and sessions

- **`dolt checkout` in the CLI** only affects the shell process where it runs.
- With **`dolt sql-server`**, each connection keeps **its own** active branch until you switch explicitly.
- At the start of a session/script: `CALL dolt_checkout('<branch>');` — do not assume a checkout in another connection applies here.
- Current branch: `SELECT active_branch();`

## SQL: versioning

**Procedures (examples):**

- `CALL dolt_add('t1', 't2')` / `CALL dolt_add('.')`
- `CALL dolt_commit('-m', 'message')` / `CALL dolt_commit('-am', 'message')`
- `CALL dolt_checkout('branch')` / `CALL dolt_checkout('-b', 'newbranch')`
- `CALL dolt_merge('branch')` → result includes a conflicts flag
- `CALL dolt_reset('--hard')` — reset working tree
- `dolt_revert`, `dolt_undrop` — see [procedure docs](https://docs.dolthub.com/sql-reference/version-control/dolt-sql-procedures)

**System tables / functions:**

| Object | Purpose |
|--------|---------|
| `dolt_log`, `dolt_commits` | Commit history |
| `dolt_status` | staged / modified |
| `dolt_branches` | Branches and HEAD |
| `dolt_diff` (unscoped) | Which tables changed in commits |
| `dolt_diff_<table>` | Row-level diff for a table |
| `dolt_diff('main', 'branch', 'table')` | Diff between branches (table function) |
| `dolt_schema_diff` | Schema changes |
| `dolt_conflicts`, `dolt_conflicts_<table>` | Merge conflicts |
| `dolt_history_<table>` | Row state per commit (audit / lineage) |
| `dolt_remotes`, `dolt_ignore`, `dolt_statistics` | Remotes, ignore, statistics |

**Time travel and comparison:**

```sql
SELECT * FROM employees AS OF 'modifications';
-- also AS OF by commit hash — see official AS OF documentation
```

## SQL transactions vs Dolt commit

- A normal SQL `COMMIT` (InnoDB/autocommit) is **not** the same as a **Dolt commit**.
- **`@@dolt_transaction_commit`**: optionally create a Dolt commit for every SQL transaction — see [sysvars](https://docs.dolthub.com/sql-reference/version-control/dolt-sysvars#dolt_transaction_commit).

## Schema and merge

- **From AGENT.md:** prefer primary keys as **`varchar(36) DEFAULT (uuid())`**, not `AUTO_INCREMENT`, to reduce merge conflicts across branches and clones.
- FKs, indexes, triggers, checks, stored procedures are supported (full-featured SQL database).

## Conflicts

- Inspect: `dolt_conflicts_<table>` or CLI `dolt conflicts cat`; resolve with `dolt conflicts resolve --ours|--theirs <table>`.

## Data testing (`dolt_tests`)

- Insert tests into `dolt_tests`; run: `SELECT * FROM dolt_test_run();` / `dolt_test_run('name')`.
- Useful for schema invariants and business rules before merging to `main`.

## Remotes and ecosystem

- `dolt remote`, `dolt push`, `dolt pull`, `dolt clone` — same idea as Git.
- DoltHub / DoltLab / Hosted Dolt — optional hosting and collaboration.

## Dolt vs vanilla MySQL

Understanding where Dolt matches MySQL and where it does not avoids mixing **portable SQL expectations** with **versioned-memory expectations**.

### Role in the stack

- **MySQL** is a standalone server (InnoDB, etc.), Oracle’s replication/clustering story, and its own binary protocol and versioning.
- **Dolt** is a **different engine**: its own storage and versioning on top of a SQL layer that speaks the **MySQL dialect** over the wire. Clients may report something like **Vitess** or a non-standard `version` string — that is expected; it is not the same binary as Oracle MySQL.

### Dolt-only surface (not in MySQL)

- **Branches, commits, merge, tags, remotes** at the **data and schema** level (Git-style “tables, not files”).
- **`dolt_*` system tables** (`dolt_log`, `dolt_status`, `dolt_branches`, `dolt_diff_*`, `dolt_history_*`, …) — **do not exist** in MySQL.
- **`CALL dolt_*` procedures** (`dolt_commit`, `dolt_checkout`, `dolt_merge`, …) — **do not exist** in MySQL.
- SQL extensions: **`AS OF`** (branch or commit), table functions **`dolt_diff(...)`**, **`active_branch()`**, row **`blame`**, etc.
- A separate axis: **SQL transaction** vs **Dolt commit**, plus Dolt-specific variables such as **`@@dolt_transaction_commit`**.

Anything you rely on for branches, history, diffs, or audit-by-commit is **Dolt-only**, not portable MySQL.

### Dialect compatibility (do not assume parity)

Official goal: behave like **MySQL 8.x** for the language; deviations should be documented under [SQL Language Support](https://docs.dolthub.com/sql-reference/sql-support); unexpected differences may be treated as bugs.

In practice:

- Large real-world dumps (e.g. **Sakila**) may need edits: Dolt’s own tests comment out syntax that is **not supported yet** (search for `UNSUPPORTED SYNTAX` in their Sakila fixture).
- **Do not assume** every production MySQL script runs unchanged; validate critical features against the docs (data description, statements, functions, etc.).

### Operational differences

- **Git-like config** (`user.name`, `user.email`) for meaningful commits — not a MySQL concept.
- **Repository format** migrations (**`dolt migrate`**) — about Dolt storage, not `mysql_upgrade`.
- **Active branch is per session** under `sql-server` — MySQL has no “database branch” in this sense.

### Ecosystem

- **MySQL → Dolt** replication (binlog) is a Dolt scenario; it is not the same as standard MySQL-to-MySQL replication.
- DoltHub / Hosted Dolt / DoltLab sit **beside** the Oracle MySQL ecosystem.

### Design split for this project

| Treat as MySQL-like | Treat as Dolt-only |
|----------------------|--------------------|
| Ordinary `CREATE TABLE`, FKs, indexes, most DML/SELECT | Branches, merge, conflicts, `dolt_*`, `AS OF`, commit-granular audit |
| MySQL drivers and clients | Version semantics and Dolt-specific sysvars |

## Vector search and `VECTOR` operations

Dolt is **not** only a metadata store for chunk IDs: it has **native approximate nearest-neighbor (ANN)** support, with syntax aligned to **MariaDB** / **MySQL 9.x** vector work. Details below; behavior evolves quickly — verify against your installed version and [DoltHub blog / docs](https://www.dolthub.com/blog).

### Vector indexes

- Declared with **`VECTOR INDEX`** on a column (e.g. `CREATE TABLE ... ( v JSON, VECTOR INDEX idx(v) );` or `ALTER TABLE ... ADD VECTOR INDEX ...`).
- Query pattern: **`ORDER BY VEC_DISTANCE(...)`** (and related distance APIs) with **`LIMIT k`** — ANN search; the planner may use the vector index (check with **`DESCRIBE PLAN`** / `EXPLAIN`).
- **ANN semantics:** a small rate of **false negatives** is accepted; **no false positives** (distant points should not rank ahead).
- Indexes are designed to be **history-independent** relative to Dolt’s versioning (indexes can track evolving data across branches/commits without forcing a full rebuild model like some external vector DBs). Still, for static data, bulk load then index build is often faster.

### `VECTOR(N)` vs JSON

- Early path: vectors stored as **JSON arrays of floats** under a **`VECTOR INDEX`** (simple, but deserialization cost made large index builds slow).
- **Dedicated `VECTOR(N)`** columns (fixed **N** float32 dimensions, MySQL/MariaDB-style) reduce overhead and are the **preferred** direction for new work once available in your build; conversion helpers follow MySQL/MariaDB naming (e.g. **`STRING_TO_VECTOR` / `TO_VECTOR`**, **`VECTOR_TO_STRING` / `FROM_VECTOR`**, MariaDB-style **`VEC_FromText` / `VEC_ToText`** as aliases — see release notes).

### Distance functions

- Distance naming overlaps **MySQL** (`DISTANCE`, `VECTOR_DISTANCE`, metric string) and **MariaDB** (`VEC_DISTANCE_EUCLIDEAN`, `VEC_DISTANCE_COSINE`, bare `VEC_DISTANCE` tied to index metadata). Dolt aims to accept **both** styles where documented.
- Under the hood, planner paths reference metrics such as **L2 squared** for indexed lookup; additional metrics and index options (e.g. cosine as default per index) are evolving — read errors/docs if a metric is unsupported.

### Status and limitations (check before production)

- Vector indexing has shipped as **alpha**: index bugs could skew ANN results; **table data** is not corrupted by index issues, but **accuracy/perf** are not yet on par with mature vector DBs.
- Older constraints (e.g. **JSON-only** indexed column in early releases) may differ from current `VECTOR(N)` rules — confirm in release notes.
- **`dolt import`** / Parquet: practical for many embedding dumps; exotic Parquet shapes may need preprocessing.

### RAG / memory subsystem

- Embeddings can live **in-Dolt** (`VECTOR(N)` or JSON + index) with **versioned rows** and branch merges, or **hybrid**: pointers + metadata in Dolt, optional duplicate vectors elsewhere for redundancy.

## What matters for long-term memory on top of Dolt

1. **Explicit `dolt_checkout` on every working connection** — draft vs canonical memory maps to branches.
2. **`AS OF` + `dolt_history_*`** — what was known at a point in time / on a branch.
3. **UUID PKs** — stable identities when merging experience from different sessions.
4. **`dolt_diff` / `dolt_commits`** — diffs and metadata for explainable record-keeping (audit-log-like).
5. **Vector side** — prefer **`VECTOR(N)` + `VECTOR INDEX`** where supported; validate **distance APIs and ANN accuracy** on your version. A **hybrid** design (IDs + optional external embeddings) remains valid if you need portability or a specialized vector engine.

---

*Written for the Synthea project; when upgrading Dolt, cross-check the official release notes and documentation.*
