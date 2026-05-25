---
id: decision-search-empty-query
type: decision
status: active
created: 2026-01-15
updated: 2026-01-15
confidence: high
source: codex-session-summary
tags:
  - memory/decision
  - project/search
decision: Empty search queries return no results.
alternatives:
  - Return all published notes.
  - Reuse the previous query.
reason: Returning no results is predictable and avoids accidental broad disclosure.
revisit_after: 2026-04-15
---

# Empty Search Query Behavior

## Decision

Empty search queries return no results.

## Reason

This behavior is explicit, easy to test, and avoids exposing unrelated notes when a query field is cleared.

## Consequences

- UI states should show an empty-state message.
- Tests should cover empty and whitespace-only queries.

## Links

- [[Search]]
