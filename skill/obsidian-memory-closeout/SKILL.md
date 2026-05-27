---
name: obsidian-memory-closeout
description: Query existing Obsidian memory before work, then ingest curated closeouts, proposals, decisions, project updates, lint findings, and Graphify refreshes afterward. Use when the user asks to use an Obsidian-compatible vault as durable AI memory, summarize sessions or transcripts into notes, maintain project memory, inspect open loops, validate memory quality, or keep Graphify in sync without storing raw logs or secrets.
---

# Obsidian Memory Closeout

## Principle

Memory is both input and output. Query relevant existing notes before acting, then write durable, curated updates into an Obsidian-compatible Markdown vault after useful work happens.

Do not store raw transcripts, secrets, credentials, or noisy command logs. Prefer explicit notes, traceable sources, and small updates over archival dumps.

## Locate The Vault

Use the first available source:

1. A vault path explicitly provided by the user.
2. `OBSIDIAN_VAULT_PATH`, `MEMORY_VAULT_PATH`, or a similar environment variable.
3. The current working directory, if it looks like an Obsidian vault or memory repo.
4. Ask the user for the vault path when none can be inferred safely.

Before querying or writing, inspect local conventions: `AGENTS.md`, `.gitignore`, `.graphifyignore`, templates, and existing note structure.

## Before Work / Query

When a vault is available before a task, read relevant existing memory before acting. Search or inspect:

- Project and area notes for current state, goals, constraints, and next actions.
- Decision notes for active choices, rejected alternatives, and revisit dates.
- Session notes for recent changes and unresolved open loops.
- Reference notes for reusable technical or domain context.
- Reviewed web clip proposals or inbox items, but not raw clipping dumps.
- Proposal notes when canonical memory placement is still unresolved.

Use the smallest useful context set. If no relevant memory exists, continue with the current task and note the coverage gap during linting.

## Operating Model

Follow this loop:

1. **Query existing memory**: read relevant notes, decisions, open loops, and references before work.
2. **Do the work**: use current task context plus retrieved memory.
3. **Ingest durable updates**: convert useful sources into curated notes.
4. **Lint memory quality**: validate that the vault remains useful, private, linked, current, and non-duplicative.

### Query

Query means reading relevant existing memory before acting. Prefer precise notes over broad folder scans. Capture any relevant constraints, decisions, open loops, stale assumptions, or missing coverage in the working context.

### Ingest

Ingest means converting useful sources into curated notes. Identify durable memory candidates: decisions, project state changes, resolved open loops, stable preferences, reusable references, and session summaries.

Exclude raw transcripts, secrets, credentials, private keys, tokens, full logs, and unnecessary sensitive details.

Choose the smallest useful write:

- Session summary.
- Decision note.
- Project or area update.
- Reference note.
- Memory proposal when canonical placement is unclear.

Use Obsidian links between related notes.

### Web Clips

Browser and web clippings are unreviewed source material, not canonical memory. Use this generic inbox convention when the vault has no existing one:

```text
00_Inbox/Web Clips/raw/
```

Raw clips should be ignored by Git and indexing by default. Review them before promotion. Read `references/web-clips.md` for promotion and rejection criteria.

### Lint

Lint means validating memory quality before handoff. Check:

- Schema: required frontmatter exists and matches local templates.
- Links: related notes are connected and broken links are avoided.
- Privacy: no raw transcripts, secrets, credentials, or unnecessary sensitive details.
- Web clips: raw clips are not treated as canonical notes and are excluded from Git/indexing when possible.
- Stale decisions: active decisions with revisit dates or outdated assumptions are called out.
- Duplication/noise: repeated, low-value, or overly broad notes are avoided.
- Coverage gaps: missing project state, open loops, or references are noted.

Run a privacy scan before commit or handoff. Use `scripts/secret_scan.py` if helpful. Refresh Graphify when available. Read `references/graphify.md`, then use `scripts/refresh_graphify.py` if helpful. If the vault is a Git repo, checkpoint meaningful memory changes.

## Transcript Handling

When given a transcript, chat log, meeting notes, audio transcript, or exported conversation:

- Extract durable facts and decisions only.
- Preserve source traceability at the summary level.
- Do not copy long raw passages.
- Split very long transcripts into chunks, then merge only stable outcomes.
- Mark uncertain claims with lower confidence.

Read `references/transcript-processing.md` for the detailed transcript workflow.

## Note Schema

Follow the vault's existing schema first. If none exists, use the generic schema in `references/memory-note-schema.md`.

Every canonical note should have enough metadata to answer:

- What type of memory is this?
- Where did it come from?
- How confident is it?
- When was it last updated?
- What notes does it connect to?

## Graphify

Graphify is a derived index, not the source of truth. Markdown notes remain canonical.

Refresh Graphify only after curated notes are written. Do not index raw transcript folders unless the user explicitly accepts that privacy tradeoff.

Read `references/graphify.md` before setting up or refreshing Graphify.

## Failure Modes

- If the vault path is unknown, ask instead of guessing.
- If the write would require storing sensitive material, summarize at a safer abstraction or refuse that part.
- If Graphify is unavailable, leave notes updated and mention that the derived index was not refreshed.
- If direct canonical writing is risky, create a memory proposal in the inbox or provide the proposal text to the user.
