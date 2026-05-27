# Web Clips Workflow

Use this when the user asks to save, review, import, or process browser/web clippings.

## Principle

Browser and web clips are unreviewed source material, not canonical memory. Do not treat raw clips as durable notes until they pass review and are summarized into a destination note.

## Inbox Convention

If the vault has no existing convention, use:

```text
00_Inbox/Web Clips/raw/
```

Raw clips should be ignored by Git and indexing by default.

Recommended `.gitignore` and `.graphifyignore` entry:

```gitignore
00_Inbox/Web Clips/raw/
```

## Promotion Criteria

Promote a clip only when it:

- Is durable beyond the moment.
- Has a clear source URL and context.
- Is privacy-safe.
- Can be summarized without storing the full raw content.
- Has a clear destination note.

## Rejection Criteria

Reject a clip when it is:

- One-off reading.
- A full article dump.
- Private or account data.
- Secrets, credentials, tokens, or keys.
- Low-quality or duplicate source material.

## Promotion Output

Use one of:

- Reference note for reusable external material.
- Project update when the clip changes project context.
- Decision note when the clip supports a decision.
- Proposal note when placement is unclear.

Include source URL/context, confidence, and links. Do not copy the full raw content.
