# Create GitHub Issues

Break specs/PRDs into independently-grabbable GitHub issues using vertical slices.

## When to use

- After `/spec-driven` validation
- Converting plans into trackable issues
- Breaking down large features

## What it does

1. Reads spec + CONTEXT.md (domain vocabulary)
2. Creates **vertical slices** (end-to-end, not horizontal layers)
3. Labels: AFK (autonomous) or HITL (human-in-the-loop)
4. Manages dependencies (blockers)
5. Publishes to GitHub via `gh` CLI

## Requires

`/setup-matt-pocock-skills` run once per repo.

See [SKILL.md](./SKILL.md) for vertical slice rules.
