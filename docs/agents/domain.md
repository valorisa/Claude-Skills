# Domain Documentation Layout

Single-context repository.

## Files

- `CONTEXT.md` (root) — Domain glossary and ubiquitous language
- `docs/adr/` — Architecture Decision Records

## When skills read these

- `tdd-hybrid` (FULL workflow): reads CONTEXT.md for test naming vocabulary
- `diagnose`: reads CONTEXT.md + ADRs in area being debugged
- `improve-codebase-architecture`: reads CONTEXT.md + ADRs for refactoring suggestions
- `create-github-issues`: uses CONTEXT.md vocabulary in issue titles/descriptions

## Creating CONTEXT.md

`CONTEXT.md` should contain:

- **Language** section: canonical terms with one-line definitions
- **Relationships** section (optional): how domain entities relate
- **Flagged ambiguities** section (optional): terms that were previously unclear

See `skills/engineering/grill-with-docs/SKILL.md` for the skill that builds CONTEXT.md interactively.

## Creating ADRs

ADRs document hard-to-reverse decisions. Use the format in `skills/engineering/grill-with-docs/ADR-FORMAT.md`.
