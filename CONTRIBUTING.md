# Contributing

Thanks for improving `obsidian-memory-closeout`.

## Quality Bar

- Keep the skill generic and reusable.
- Prefer concise workflow instructions over long prose.
- Keep `SKILL.md` focused on core behavior and triggers.
- Move optional detail into `references/`.
- Test scripts by running them locally.
- Keep examples synthetic and privacy-safe.

## Maintainer Privacy Note

Before opening a pull request or publishing a release, run a public safety audit. Examples and docs must remain synthetic and privacy-safe.

Do not include:

- Personal names, private repo names, private vault names, or private filesystem paths.
- Real secrets, tokens, credentials, private keys, or account data.
- Raw transcript-like content, full chat logs, full article dumps, or noisy source archives.
- Examples that imply committing sensitive memory to Git or indexing raw private material.

Use neutral placeholders such as `/path/to/vault`, `Project Alpha`, and `Example App`.

## Local Checks

Run:

```bash
python3 scripts/validate_skill.py --root .
python3 skill/obsidian-memory-closeout/scripts/secret_scan.py .
python3 scripts/package_skill.py --root . --check
```

## Pull Requests

Please include:

- What changed.
- Why it improves the skill.
- Which validation commands passed.
- Any privacy considerations.

## Community

Be kind, assume good intent, and keep feedback specific enough to act on.
