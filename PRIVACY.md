# Privacy

This project is designed for curated memory, not raw archival storage.

## Public Repository Boundary

The repository may contain:

- The generic Codex skill.
- Sanitized examples.
- Validation, packaging, and installation helpers.
- Documentation about privacy-safe workflows.

The repository must not contain:

- Private Obsidian vault notes.
- Raw transcripts, exported chats, or full meeting logs.
- API keys, tokens, credentials, seed phrases, private keys, or secrets.
- Sensitive personal details that are not necessary for operating the skill.
- Machine-specific absolute paths from a private environment.

## Runtime Boundary

When the skill is used, Codex should:

- Prefer summaries, decisions, project updates, and proposals over raw logs.
- Preserve source traceability at a high level.
- Use the vault's existing conventions before creating new note shapes.
- Ask for a vault path when it cannot be inferred safely.
- Run a secret scan before commits or handoff when files were written.
- Treat Graphify output as derived data, not as the canonical memory source.
- Review `.graphifyignore` before refreshing Graphify so raw transcripts, caches, exports, and other sensitive folders stay out of the derived graph.

## Review Checklist

Before publishing changes:

1. Run `python3 skill/obsidian-memory-closeout/scripts/secret_scan.py .`.
2. Search for private paths, vault names, usernames, emails, and organization-specific details.
3. Confirm examples are synthetic.
4. Confirm packaged artifacts contain only the installable skill.
5. Confirm no raw transcript or generated cache was added.
