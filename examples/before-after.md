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
  - privacy/transcripts
---

# Before/After: AI Session Closeout

This example is fully synthetic. It shows the intended transformation from a short, noisy AI session into curated Obsidian memory. The raw transcript is not saved.

## Before: Session Input

```text
User: We changed the notification settings plan. Let's default to weekly summaries.
Assistant: Got it. I can update the docs and tests.
User: Also, ignore my earlier idea about daily summaries. Too noisy.
Assistant: Should the old rollout note be updated?
User: Yes. Add a follow-up to check whether users can opt into daily alerts later.
```

## After: Curated Obsidian Notes

### Session Summary

```markdown
---
id: session-2026-01-15-notification-settings
type: session
status: complete
created: 2026-01-15
updated: 2026-01-15
confidence: high
source: synthetic-ai-session
tags:
  - memory/session
  - project/notifications
summary: Notification settings were clarified around weekly summaries.
memory_updates:
  - Weekly summaries are the default notification cadence.
  - Daily summaries are no longer the default direction.
open_loops:
  - Evaluate whether users should be able to opt into daily alerts later.
---

# Notification Settings Session

## Summary

The notification settings plan now defaults to weekly summaries. A previous daily-summary direction was rejected because it would create too much noise.

## Memory Updates

- Weekly summaries are the default cadence.
- Daily summaries may be reconsidered only as an optional user opt-in.

## Open Loops

- Check whether daily alerts should be exposed as an opt-in setting.
```

### Decision Note

```markdown
---
id: decision-weekly-notification-summary-default
type: decision
status: active
created: 2026-01-15
updated: 2026-01-15
confidence: high
source: synthetic-ai-session
tags:
  - memory/decision
  - project/notifications
decision: Default notification summaries to weekly.
alternatives:
  - Daily summaries by default.
reason: Weekly summaries reduce notification noise while preserving useful updates.
---

# Weekly Notification Summary Default

## Decision

Notification summaries default to weekly.

## Reason

Daily summaries were considered too noisy for the default experience.

## Consequences

- Documentation should describe weekly summaries as the default.
- Daily alerts remain a possible future opt-in.
```

## What Was Not Saved

- The raw back-and-forth transcript.
- Drafting chatter.
- Repeated confirmations.
- Any unnecessary session noise.
