# Contributing

Thanks for improving `obsidian-memory-closeout`.

## Quality Bar

- Keep the skill generic and reusable.
- Prefer concise workflow instructions over long prose.
- Keep `SKILL.md` focused on core behavior and triggers.
- Move optional detail into `references/`.
- Test scripts by running them locally.
- Keep examples synthetic and privacy-safe.

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
