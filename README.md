# Obsidian Memory Closeout

[![Validate](https://github.com/Nova1390/Obsidian-memory-closeout/actions/workflows/validate.yml/badge.svg)](https://github.com/Nova1390/Obsidian-memory-closeout/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

`obsidian-memory-closeout` is a Codex skill for turning meaningful work sessions, transcripts, decisions, and project updates into curated Markdown notes for an Obsidian-compatible vault.

The skill is intentionally privacy-first: it guides Codex to write durable memory, not raw transcripts, secrets, credentials, or noisy command logs.

## What It Does

- Finds or asks for the target Obsidian vault.
- Extracts durable memory from a session or transcript.
- Writes concise session summaries, decisions, project updates, references, or inbox proposals.
- Uses the vault's existing conventions first, with a generic fallback schema.
- Runs a local secret scan before committing or handing off.
- Refreshes Graphify-derived indexes when `graphify` is available.

## Repository Layout

```text
.
├── skill/obsidian-memory-closeout/   # Installable Codex skill package
├── examples/                         # Sanitized example outputs
├── scripts/                          # Repo validation and packaging helpers
├── .github/workflows/validate.yml     # CI validation
├── PRIVACY.md                        # Privacy model and public repo boundaries
└── README.md
```

## Install

### Option A: Codex Skill Installer

Ask Codex to install the skill from this GitHub directory:

```text
$skill-installer install https://github.com/Nova1390/Obsidian-memory-closeout/tree/main/skill/obsidian-memory-closeout
```

Restart Codex after installation so the skill is discovered.

### Option B: Local Clone

Clone the repository, then install the skill into your local Codex skills directory:

```bash
git clone https://github.com/Nova1390/Obsidian-memory-closeout.git
cd Obsidian-memory-closeout
./scripts/install_local.sh
```

By default, the installer copies the skill to:

```text
~/.codex/skills/obsidian-memory-closeout
```

To install somewhere else:

```bash
CODEX_HOME=/path/to/codex ./scripts/install_local.sh
```

### Option C: Manual Copy

Copy the installable skill folder to your Codex skills directory:

```bash
cp -R skill/obsidian-memory-closeout ~/.codex/skills/obsidian-memory-closeout
```

Restart Codex after copying.

## Package

Create a distributable zip in `dist/`:

```bash
python3 scripts/package_skill.py
```

The package contains only the installable skill folder, not the repository docs or examples.

## Validate

Run the same checks used by CI:

```bash
python3 scripts/validate_skill.py --root .
python3 skill/obsidian-memory-closeout/scripts/secret_scan.py .
python3 scripts/package_skill.py --root . --check
```

The validation checks that:

- `SKILL.md` has valid frontmatter.
- `agents/openai.yaml` exists and matches the skill metadata shape.
- Referenced files exist.
- Sanitized examples contain expected frontmatter.
- Packaging produces a zip with the expected skill files.
- The repository does not contain common secret-like patterns.

## Usage Prompt

After installing, ask Codex something like:

```text
Create a curated memory closeout for this session in my Obsidian vault.
```

You can also provide a vault path explicitly:

```text
Use /path/to/my/vault and create a memory closeout for this transcript.
```

## Privacy

This repository does not include private vault content. The included examples are synthetic and sanitized. See [PRIVACY.md](PRIVACY.md) for the intended privacy boundaries and review checklist.

## Contributing

Issues and pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and keep all examples synthetic. Security or privacy concerns should follow [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
