---
id: example-before-after-ai-session
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

# Before/After: Continue Existing Project

This example is fully synthetic. It shows how an agent uses memory as both input and output: first reading relevant notes, then doing the work, then writing only durable updates. The raw transcript is not saved.

## Before: User Request

```text
Use /path/to/vault. Continue work on Project Meridian and finish the notification preferences cleanup for Example App. Read relevant memory first, then update durable memory afterward.
```

## Agent First Reads Existing Memory

Relevant existing project note:

```markdown
[[Project Meridian]]
current_state: Example App has notification preferences split across two settings panels.
next_actions:
  - Consolidate notification preferences into one settings panel.
  - Keep weekly summaries as the default cadence.
```

Relevant decision:

```markdown
[[Decision Weekly Summary Default]]
decision: Weekly summaries are the default notification cadence.
reason: Daily notifications are too noisy for the default experience.
status: active
```

Relevant reference:

```markdown
[[Reference Settings Panel Patterns]]
summary: Group related preferences together and avoid duplicate controls across panels.
source: https://example.org/reference/settings-panel-patterns
```

Relevant open loop:

```markdown
[[Open Loops]]
- Decide whether daily notifications should be offered as an advanced opt-in later.
```

## Work Performed

The agent consolidates notification preferences into one settings panel for Example App, keeps weekly summaries as the default, and removes duplicate preference wording from the draft documentation.

## After: Curated Memory Updates

### Session Closeout

```markdown
---
id: session-2026-01-15-project-meridian-notification-cleanup
type: session
status: complete
created: 2026-01-15
updated: 2026-01-15
confidence: high
source: synthetic-agent-session
tags:
  - memory/session
  - project/project-meridian
summary: Notification preferences were consolidated for Example App.
memory_updates:
  - Example App now has one notification preferences panel.
  - Weekly summaries remain the default notification cadence.
open_loops:
  - Decide whether daily notifications should be offered as an advanced opt-in later.
---

# Project Meridian Notification Cleanup

## Summary

Notification preferences for Example App were consolidated into one settings panel. The active decision to keep weekly summaries as the default cadence remains unchanged.

## Durable Updates

- One notification preferences panel now owns notification cadence settings.
- Duplicate preference wording was removed from draft documentation.
- Weekly summaries remain the default cadence.

## Open Loops

- Decide whether daily notifications should be offered as an advanced opt-in later.

## Links

- [[Project Meridian]]
- [[Decision Weekly Summary Default]]
- [[Reference Settings Panel Patterns]]
```

### Project Note Update

Only durable state is updated:

```markdown
[[Project Meridian]]
current_state: Example App has one consolidated notification preferences panel.
next_actions:
  - Decide whether daily notifications should be offered as an advanced opt-in later.
```

## What Was Not Saved

- The raw user-agent transcript.
- Drafting chatter.
- Temporary implementation notes.
- Duplicate wording that no longer matters.
