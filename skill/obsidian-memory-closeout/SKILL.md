---
name: obsidian-memory-closeout
description: Create curated Obsidian memory closeouts, proposals, decisions, project updates, and Graphify refreshes from meaningful conversations or transcripts. Use when the user asks to save durable memory, update an Obsidian vault, summarize a session into notes, process transcripts into memory, maintain a personal/team knowledge vault, or keep Graphify in sync without storing raw logs or secrets.
---

# Obsidian Memory Closeout

## Principle

Write durable, curated memory into an Obsidian-compatible Markdown vault. Do not store raw transcripts, secrets, credentials, or noisy command logs. Prefer explicit notes, traceable sources, and small updates over archival dumps.

## Locate The Vault

Use the first available source:

1. A vault path explicitly provided by the user.
2. `OBSIDIAN_VAULT_PATH`, `MEMORY_VAULT_PATH`, or a similar environment variable.
3. The current working directory, if it looks like an Obsidian vault or memory repo.
4. Ask the user for the vault path when none can be inferred safely.

Before writing, inspect local conventions: `AGENTS.md`, `.gitignore`, `.graphifyignore`, templates, and existing note structure.

## Closeout Workflow

1. Identify durable memory candidates: decisions, project state changes, resolved open loops, stable preferences, reusable references, and session summaries.
2. Exclude raw transcripts, secrets, credentials, private keys, tokens, full logs, and unnecessary sensitive details.
3. Choose the smallest useful write:
   - Session summary.
   - Decision note.
   - Project or area update.
   - Reference note.
   - Memory proposal when canonical placement is unclear.
4. Use Obsidian links between related notes.
5. Run a privacy scan before commit or handoff. Use `scripts/secret_scan.py` if helpful.
6. Refresh Graphify when available. Use `scripts/refresh_graphify.py` if helpful.
7. If the vault is a Git repo, checkpoint meaningful memory changes.

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

## Failure Modes

- If the vault path is unknown, ask instead of guessing.
- If the write would require storing sensitive material, summarize at a safer abstraction or refuse that part.
- If Graphify is unavailable, leave notes updated and mention that the derived index was not refreshed.
- If direct canonical writing is risky, create a memory proposal in the inbox or provide the proposal text to the user.
