---
id: example-ingest-query-lint-workflow
type: reference
status: complete
created: 2026-01-15
updated: 2026-01-15
confidence: high
source: synthetic-example
tags:
  - memory/example
  - workflow/query-ingest-lint
---

# Ingest / Query / Lint Workflow

This synthetic example shows how an agent can use an Obsidian-compatible vault as both input and output. It does not store raw transcripts.

## 1. Query Existing Memory

Input:

```text
Use /path/to/vault. Before working on Project Alpha, query relevant memory notes, decisions, open loops, and references.
```

Relevant existing notes:

```markdown
[[Project Alpha]]
- Current state: Example App has a basic notification settings screen.
- Next action: Decide the default notification cadence.

[[Decision Notification Cadence]]
- Status: active
- Current decision: weekly summaries are preferred over daily summaries.
- Revisit after: 2026-04-15

[[Open Loops]]
- Confirm whether daily alerts should be available as an opt-in.
```

## 2. Do The Work

The agent updates Example App documentation and tests using the retrieved memory. It keeps the weekly-summary decision in scope and does not reintroduce daily summaries as the default.

## 3. Ingest Durable Updates

Curated output:

```markdown
---
id: session-2026-01-15-project-alpha-notifications
type: session
status: complete
created: 2026-01-15
updated: 2026-01-15
confidence: high
source: synthetic-agent-session
tags:
  - memory/session
  - project/project-alpha
summary: Example App notification docs and tests were updated around weekly summaries.
memory_updates:
  - Weekly summaries remain the default notification cadence.
  - Documentation and tests now reflect the active notification cadence decision.
open_loops:
  - Confirm whether daily alerts should be offered as an opt-in.
---

# Project Alpha Notification Update

## Summary

Example App documentation and tests were updated to align with the active decision that weekly summaries are the default notification cadence.

## Memory Updates

- Weekly summaries remain the default.
- Daily alerts are not the default and should only be considered as an opt-in.

## Open Loops

- Confirm whether daily alerts should be offered as an opt-in.

## Links

- [[Project Alpha]]
- [[Decision Notification Cadence]]
```

## 4. Lint Memory Quality

Lint findings:

```text
Schema: session note includes required frontmatter.
Links: related project and decision notes are linked.
Privacy: no raw transcript, credentials, secrets, or unnecessary sensitive details were saved.
Stale decisions: notification cadence decision has a revisit date.
Duplication/noise: no duplicate session note needed.
Coverage gaps: daily alert opt-in remains an open loop.
```

## What Was Not Saved

- The raw AI session transcript.
- Temporary drafting chatter.
- Repeated confirmations.
- Unnecessary implementation noise.
