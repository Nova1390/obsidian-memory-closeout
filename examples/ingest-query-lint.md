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

User request:

```text
Use /path/to/vault. Continue work on Project Alpha. Before changing Example App notification settings, query relevant project notes, decisions, open loops, and references.
```

Relevant existing project note:

```markdown
[[Project Alpha]]
current_state: Example App has a basic notification settings screen.
next_actions:
  - Align documentation and tests with the active notification cadence decision.
  - Keep unresolved daily alert opt-in work visible.
```

Relevant decision:

```markdown
[[Decision Notification Cadence]]
status: active
decision: Weekly summaries are preferred over daily summaries.
revisit_after: 2026-04-15
```

Relevant reference:

```markdown
[[Reference Notification Patterns]]
summary: Notification defaults should be predictable and easy to override.
source: https://example.org/reference/notification-patterns
```

Relevant open loop:

```markdown
[[Open Loops]]
- Confirm whether daily alerts should be available as an opt-in.
```

## 2. Do The Work

The agent updates Example App documentation and tests using the retrieved memory. It keeps the weekly-summary decision in scope, references the notification pattern note, and does not reintroduce daily summaries as the default.

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
- [[Reference Notification Patterns]]
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
