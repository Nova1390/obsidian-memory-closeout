# Graphify Integration

Graphify is optional. The skill works without it.

When available, Graphify can turn the curated Markdown vault into derived graph artifacts for exploration and review. The Markdown notes remain canonical.

## Runtime Behavior

The skill should refresh Graphify only after it has written curated notes and completed a privacy review.

The bundled helper runs:

```bash
python3 skill/obsidian-memory-closeout/scripts/refresh_graphify.py /path/to/vault
```

This calls:

```bash
graphify update . --no-cluster --force
graphify cluster-only . --no-viz
```

To generate the visual HTML graph as well:

```bash
python3 skill/obsidian-memory-closeout/scripts/refresh_graphify.py /path/to/vault --html
```

## Expected Outputs

Graphify outputs are derived artifacts. Exact filenames depend on the installed Graphify version and configuration, but vaults commonly use a `graphify-out/` directory for generated JSON, reports, cache, and optional HTML visualization.

Do not edit generated Graphify files as canonical memory. Update Markdown notes first, then refresh.

## Privacy Guardrails

Before refreshing Graphify, review `.graphifyignore` or create one if the vault does not have it.

Recommended ignores:

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

Do not index raw transcript folders unless the user explicitly accepts that privacy tradeoff. Prefer curated summaries, decisions, and project updates.

## Failure Modes

- If `graphify` is not installed, leave Markdown notes updated and report that the derived index was not refreshed.
- If `.graphifyignore` is missing and the vault contains raw source folders, pause and ask before indexing.
- If Graphify fails, keep the note changes and include the failed command in the handoff without dumping long logs.
