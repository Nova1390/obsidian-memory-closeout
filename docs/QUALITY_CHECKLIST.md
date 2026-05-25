# Quality Checklist

Use this checklist when reviewing the repository or preparing a release.

## Skill Quality

- `SKILL.md` frontmatter contains only `name` and `description`.
- Description explains both what the skill does and when to use it.
- Runtime instructions are concise and action-oriented.
- Longer optional workflows live in `references/`.
- Every referenced file exists.
- Scripts are deterministic and have been run locally.

## Repository Quality

- README has install, validate, package, usage, privacy, and license sections.
- `AGENTS.md` tells future agents how to avoid privacy mistakes.
- `CONTRIBUTING.md` and `SECURITY.md` exist.
- CI runs validation, secret scan, and packaging checks.
- Release documentation explains how to build and attach the package.

## Privacy Quality

- No private vault content.
- No raw transcripts.
- No credentials or tokens.
- No personal absolute paths.
- Examples are synthetic.
