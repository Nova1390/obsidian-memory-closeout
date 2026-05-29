# Checked Memory Edits

Use this when a memory update has a clear canonical target but direct writing may be risky, concurrent, stale-prone, or review-worthy.

## Principle

Obsidian Markdown remains the canonical source of truth.

Prefer direct edits only for small, obvious, low-risk canonical updates. Use a patch proposal when the target note is clear but the update needs validation or review before apply.

## Patch Proposal Shape

A patch proposal should include:

```yaml
type: patch-proposal
status: proposed
target_note: /path/to/vault/Project Alpha.md
target_content_hash: sha256:examplehash
operation: append_to_section|update_frontmatter_field|add_wikilink
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: short-source-label
```

Include the proposed change in Markdown after the frontmatter.

## Allowed v1 Operations

- Append to an existing section.
- Update one existing frontmatter field.
- Add one wikilink to `Links`.

## Excluded Operations

- Delete.
- Rename.
- Multi-file rewrite.
- Whole-note replacement.

## Validation

Before applying, validate:

- Target note exists.
- Target content hash is fresh.
- Required section or frontmatter field exists.
- Proposed change has no secrets, credentials, private keys, tokens, raw transcripts, or unnecessary sensitive details.
- Operation is one of the allowed v1 operations.

## Safe Apply

Apply only validated small patches. After apply:

- Mark the proposal `applied` or `closed`.
- Link the proposal to the target note when useful.
- Run local quality checks.
- Inspect Git status before staging.

Example CLI names such as `memory-patch validate` or `memory-patch apply` are placeholders, not required implementations.
