# Skill Creator

Create new skills for Claude Code. A skill is just a markdown file — nothing more.

## Trigger

Use when the user says "create a skill", "new skill", "skill for X", `/skill-creator`, or asks to build/improve a custom command.

## Process

### Phase 1 — Interview (extract intent)

Ask these questions one by one. Don't dump them all at once.

1. **What should this skill do?** (one sentence)
2. **When should it trigger?** (slash command, auto-detect, or both — list trigger phrases)
3. **What does "good output" look like?** (ask for a concrete example or description)
4. **What should it NOT do?** (boundaries, failure modes to avoid)
5. **Does it need tools?** (file read/write, bash, web, agents, etc.)

If the user is vague, propose a concrete interpretation and ask "is this what you mean?"

### Phase 2 — Generate first draft

Write a complete SKILL.md based on the interview. Structure it as:

```markdown
# [Skill Name]

[One-line description]

## Trigger

[When this skill activates — command name + auto-trigger phrases]

## Process

[Numbered steps — what Claude does when this skill runs]

## Constraints

[What NOT to do, boundaries, edge cases]

## Output

[What the user gets at the end — format, location, style]
```

Place it in `~/.claude/skills/[skill-name]/SKILL.md`.

### Phase 3 — Smoke test

Immediately after generating:

1. Propose 2-3 realistic test prompts that would trigger the new skill
2. Ask the user to pick one (or suggest their own)
3. Simulate how the skill would respond to that prompt
4. Show the result and ask: "Is this what you wanted? What's wrong?"

### Phase 4 — Iterate

Based on user feedback:

1. Identify what to change
2. Edit the SKILL.md directly
3. Re-run the same test prompt (or a new one)
4. Ask again: "Better? What's still off?"

Repeat until the user says it's good. Don't stop after one round.

### Phase 5 — Finalize

Once satisfied:

1. Confirm the skill location and trigger command
2. Suggest 1-2 edge cases to watch for
3. Remind the user they can invoke `/skill-creator` again to improve it later

## Constraints

- Never over-engineer. A skill is a markdown file, not a codebase.
- Keep generated skills short — if it doesn't fit on 2 screens, it's too complex. Split it.
- Don't add folders, scripts, or infrastructure unless the user explicitly asks.
- Don't generate evaluation frameworks or rubrics. The user is the evaluator.
- Respect the user's existing skill naming conventions if they have any.

## Output

A working skill in `~/.claude/skills/[skill-name]/SKILL.md`, tested and iterated to the user's satisfaction.
