# Graphify Workflow

Use this when the user asks to refresh Graphify, inspect a memory graph, or keep a derived vault graph in sync.

## Principle

Markdown notes are canonical. Graphify output is derived and can be regenerated.

## Before Refreshing

1. Write curated memory notes first.
2. Confirm the vault has a `.graphifyignore` or equivalent ignore policy.
3. Exclude raw transcripts, exported chats, secrets, private dumps, caches, and generated folders.
4. Run `scripts/secret_scan.py` on changed notes when practical.

Recommended `.graphifyignore` entries:

```gitignore
.git/
.obsidian/
graphify-out/cache/
raw/
transcripts/
exports/
private/
secrets/
*.env
*.key
*.pem
```

## Refresh

Use the helper:

```bash
scripts/refresh_graphify.py /path/to/vault
```

Use `--html` only when the user wants a visual graph artifact:

```bash
scripts/refresh_graphify.py /path/to/vault --html
```

## Reporting

- If refresh succeeds, mention that Graphify was refreshed after curated notes were written.
- If Graphify is missing, say the derived index was skipped.
- If refresh fails, summarize the failing command and keep the canonical Markdown changes.
