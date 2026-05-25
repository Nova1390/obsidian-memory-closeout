# Transcript Processing Workflow

Use this when transforming chat logs, meeting notes, audio transcripts, or exported conversations into durable Obsidian memory.

## Privacy First

Do not store raw transcripts unless the user explicitly asks and accepts the privacy tradeoff. Prefer summaries, decisions, and project updates.

Never store:

- API keys, tokens, credentials, private keys, or seed phrases.
- Full private logs or raw chat dumps.
- Sensitive personal details with no future operational value.
- Unverified sensitive claims.

## Extraction Pass

Read for durable items:

- Decisions made.
- Project state changes.
- New requirements or constraints.
- Resolved open loops.
- New open loops.
- Stable user/team preferences.
- Reusable technical references.
- Corrections to existing memory.

Ignore:

- Back-and-forth drafting noise.
- Failed commands unless the failure teaches a durable environment constraint.
- Long code or log output unless a concise summary is needed.
- Temporary emotions or non-actionable commentary.

## Chunking Long Transcripts

For long transcripts:

1. Split by session, date, topic, or natural milestones.
2. Summarize each chunk into durable candidates.
3. Merge duplicates.
4. Resolve contradictions by preferring the latest verified source.
5. Mark uncertainty explicitly.

## Output Shape

Produce one or more of:

- Session note for "what happened".
- Decision note for "what was decided".
- Project update for "what changed".
- Reference note for reusable external material.
- Proposal note when placement is unclear.

Each output should include source traceability without copying raw transcript content.
