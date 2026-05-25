# AGENTS.md

Guidance for AI agents working on this public repository.

## Repository Goal

Maintain a generic, public Codex skill for curated Obsidian memory closeouts. Keep the installable skill small, privacy-safe, and easy to validate.

## Privacy Boundary

Do not add:

- Private vault notes.
- Raw transcripts or exported chats.
- Secrets, credentials, tokens, private keys, or seed phrases.
- Machine-specific personal paths.
- Personal names, emails, or organization-specific examples unless they are already public and intentionally documented.

Examples must be synthetic.

## Edit Rules

- Keep behavioral instructions inside `skill/obsidian-memory-closeout/SKILL.md`.
- Put longer guidance in `skill/obsidian-memory-closeout/references/` and link it from `SKILL.md`.
- Put deterministic helper code in `skill/obsidian-memory-closeout/scripts/`.
- Keep repo documentation outside the installable skill folder unless Codex needs it at runtime.
- Avoid adding generated artifacts to git; `dist/` is ignored.

## Validation

Run before commits:

```bash
python3 scripts/validate_skill.py --root .
python3 skill/obsidian-memory-closeout/scripts/secret_scan.py .
python3 scripts/package_skill.py --root . --check
```

If validation fails, fix the cause rather than loosening checks.
