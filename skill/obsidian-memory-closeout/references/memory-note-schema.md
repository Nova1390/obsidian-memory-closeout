# Generic Memory Note Schema

Use the vault's existing templates first. If no template exists, this generic schema is safe for Obsidian and agent use.

## Required Frontmatter

```yaml
id: stable-kebab-case-id
type: project|area|person|decision|session|reference|proposal
status: draft|active|complete|superseded|archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: low|medium|high
source: short-source-label
tags:
  - tag
```

## Project Notes

Add:

```yaml
goal:
current_state:
next_actions:
  - item
```

Recommended sections:

- Context
- Current State
- Durable Decisions
- Next Actions
- Coverage Note
- Links

## Decision Notes

Add:

```yaml
decision:
alternatives:
  - option
reason:
revisit_after: YYYY-MM-DD
```

Recommended sections:

- Decision
- Reason
- Consequences
- Links

## Session Notes

Add:

```yaml
summary:
memory_updates:
  - item
open_loops:
  - item
```

Recommended sections:

- Summary
- Memory Updates
- Open Loops

## Proposal Notes

Use proposals when the agent cannot safely decide canonical placement.

Recommended sections:

- Source Context
- Proposed Memory Updates
- Suggested Target Notes
- Privacy Review
- Open Questions
