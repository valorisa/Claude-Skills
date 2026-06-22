# Skill Creator — A Claude Code Skill

A lightweight skill-building assistant: it interviews you in five focused questions, generates a working `SKILL.md`, immediately smoke-tests it, and iterates until the result is what you actually wanted.

**For quick prototyping. If you need production-grade skills with test suites and validation scripts, use `skill-factory` instead.**

---

## The Problem

Writing a skill from scratch means making a lot of small decisions upfront — what exactly should it do, when should it trigger, what's out of scope — and it's easy to get halfway through before realizing the scope was wrong.

Most of those decisions are better made through a short conversation than by staring at a blank file.

## How It Works

Five phases, in order:

### Phase 1 — Interview

Five questions, one at a time — never dumped all at once:

1. **What should this skill do?** (one sentence)
2. **When should it trigger?** (slash command, auto-detect, or both — list trigger phrases)
3. **What does "good output" look like?** (a concrete example or description)
4. **What should it NOT do?** (boundaries, failure modes to avoid)
5. **Does it need tools?** (file read/write, bash, web, agents, etc.)

If your answer is vague, it proposes a concrete interpretation and asks "is this what you mean?" before moving on.

### Phase 2 — First draft

Generates a complete `SKILL.md` based on the interview, structured as:

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

Placed at `~/.claude/skills/[skill-name]/SKILL.md`.

### Phase 3 — Smoke test

Right after generating the draft:

1. Proposes 2–3 realistic prompts that would trigger the new skill
2. Asks you to pick one (or suggest your own)
3. Simulates how the skill would respond to that prompt
4. Asks: "Is this what you wanted? What's wrong?"

### Phase 4 — Iterate

Based on your feedback:

1. Identifies what to change
2. Edits the `SKILL.md` directly
3. Re-runs the same test prompt (or a new one)
4. Asks again: "Better? What's still off?"

Repeats until you say it's good. Doesn't stop after one round.

### Phase 5 — Finalize

Once satisfied:

1. Confirms the skill location and trigger command
2. Suggests 1–2 edge cases to watch for in production
3. Reminds you that `/skill-creator` can be invoked again to improve it later

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/valorisa/Claude-Skills ~/.claude/skills/
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

1. Create folder `~/.claude/skills/skill-creator/`
2. Drop `SKILL.md` plus the `templates/` and `tests/` folders inside it
3. Restart Claude Code

---

## Use

Mention any of these triggers:

- `/skill-creator`
- `create a skill`
- `new skill`
- `skill for X`
- `build me a custom command`
- `improve this skill`

**Example:**

> create a skill for summarizing pull request diffs into plain English

Skill Creator will:

1. Ask the five interview questions one by one
2. Generate a first `SKILL.md` draft based on your answers
3. Propose test prompts like "summarize this diff: [paste]" and simulate the skill's response
4. Iterate based on your feedback until the result is right
5. Confirm the file location and suggest edge cases to watch for

---

## When To Use It

**Use Skill Creator for:**

- Quickly prototyping a new idea — you want something working in minutes, not hours
- Simple to moderately complex skills (fits in ~2 screens of markdown)
- Experimenting with trigger phrases and output formats before committing
- Improving or refactoring an existing skill

**Use `skill-factory` instead for:**

- Production-grade skills that need validation scripts, test suites, and distribution-ready structure
- Skills you'll publish or share with a team
- Anything that doesn't fit on 2 screens — Skill Creator will split the scope; `skill-factory` will architect it properly

---

## What Makes It Different

### Interview-first, not template-first

Most skill-building approaches start from a template you fill in. Skill Creator starts from a conversation that extracts your intent — and only then generates the structure that fits that intent.

### Smoke test is part of the workflow, not optional

Generating a skill and immediately simulating its behavior against a real prompt catches mismatches between "what I described" and "what the skill actually does" before they become embedded in production usage.

### Short is a feature, not a limitation

The skill enforces that generated skills fit on 2 screens. If your scope doesn't fit, it asks you to split it into two skills rather than generating a monolith. A skill that's too long to read is a skill that won't be maintained.

---

## What's Included

Beyond `SKILL.md`, the `skill-creator/` folder ships with:

- **`templates/simple-skill.md`** — bare-bones template for single-step skills
- **`templates/multi-step-skill.md`** — template for multi-phase skills with interview → generate → iterate workflows
- **`tests/test-prompts.md`** — example trigger phrases and expected behavior for smoke-testing new skills

---

## Credit

- Implemented as a Claude Code skill by [@valorisa](https://github.com/valorisa)
- See also `skill-factory` for the production-grade variant with full validation and test infrastructure

---

## License

MIT — do whatever you want with it.
