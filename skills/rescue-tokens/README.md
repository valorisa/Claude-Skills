# Rescue Tokens — A Claude Code Skill

Token exhaustion masquerades as "rate limit" errors. Nine patterns waste tokens silently — this skill detects the symptoms and acts immediately, with zero explanation overhead.

**Stop burning tokens on explanations about saving tokens.**

---

## The Problem

By the time you see a rate limit warning, the damage is usually already done. Long conversations bloat past the point where most of the context is dead weight. The wrong model gets used for simple tasks. Sub-agents duplicate shared context five times over. PDFs get read in full when three pages would do.

None of this looks like a problem in the moment — it looks like normal usage. It only becomes visible once you're locked out.

Most assistants, even when they notice the warning signs, respond by explaining the situation at length before acting. Under token pressure, that explanation is itself the waste.

## How It Works

Rescue Tokens auto-activates the moment **any one** of seven emergency red flags is present — these are OR conditions, not a checklist that all needs to be true:

- Rate limit warnings
- Context ≥40% full
- $20–$100/month plan usage after 2pm
- Conversation running >90 minutes
- 5+ MCP plugins loaded
- You say "don't lose context"
- Opus 4.7 in use for a simple task

Once triggered, it follows an **action matrix** — no permission asked, no explanation offered first:

| Symptom | Action |
|---------|--------|
| Context 40–70% | Compact key facts, continue |
| Context >70% | New conversation, 3-sentence handoff |
| Rate limit + urgent task | Sub-agent in Sonnet immediately |
| Opus for CRUD/refactor work | Switch to Sonnet now |
| PDF/image attached | Ask for text or key excerpts instead of reading it whole |
| 5+ MCPs loaded | Disable unused ones |
| Sub-agent requested for shared-context work | Refuse, explain in under 50 words |

Under pressure, responses shrink to under 100 words: no markdown sections, no "Reasoning:" blocks, no tables, no confidence statements, no "let me know if you need anything else." Action verbs only — "Switched to Sonnet. Starting OAuth." instead of three paragraphs justifying the switch.

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/valorisa/Claude-Skills ~/.claude/skills/
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

```bash
cp -r skills/rescue-tokens ~/.claude/skills/
```

1. Verify with `/skills list` — you should see `rescue-tokens`
2. Restart Claude Code if it doesn't show up immediately

---

## Use

No command needed — this skill detects its own triggers and activates automatically. Just say what's happening:

- "I'm getting rate limit warnings"
- "Don't lose context!"
- Or simply keep working — it watches context percentage and conversation length on its own

**Example:**

> "Don't make me lose context! Just read this 40-page PDF and fix the bug."

Rescue Tokens will:

1. Recognize the PDF-attachment red flag before reading anything
2. Ask for the relevant pages or a text excerpt instead of ingesting the whole document
3. If context is already past 40%, compact or start fresh before continuing
4. Respond in plain, terse sentences — no markdown sections, no upfront justification

---

## The Nine Token Traps

| # | Trap | Fix |
|---|------|-----|
| 1 | Eternal conversations | Clear irrelevant history, compact at 40% context, fresh conversation when needed |
| 2 | Verbose output | Terse responses under pressure — 7 words beats 200 |
| 3 | Wrong model choice | Haiku for simple lookups, Sonnet for implementation, Opus for architecture only |
| 4 | MCP plugin bloat | Audit loaded plugins, disable what's unused |
| 5 | Obese CLAUDE.md | Keep under 200 lines, use references for detail |
| 6 | Cache invalidation | Set model/MCPs at conversation start, never mid-stream |
| 7 | Expensive files | Request text conversion or specific page ranges instead of full documents |
| 8 | Sub-agent misuse | Isolated/disposable tasks only — never for work with shared context dependencies |
| 9 | Message vs. token confusion | Plans count messages, but tokens are the real cost; one long Opus conversation can cost more than 50 short Sonnet ones |

---

## When To Use It

**You don't have to invoke it — it watches for:**

- Rate limit or quota-exceeded errors
- Context climbing past 40%
- Long-running conversations (90+ minutes)
- Heavy MCP plugin load
- Large files (PDFs, images, spreadsheets) about to be read in full
- Opus being used for routine implementation work

**It stays quiet when:**

- Context is low and there's no rate-limit pressure
- The model already matches the task
- Nothing in the conversation signals waste

---

## What Makes It Different

### Emergency flags are OR, not AND

A single red flag is enough to trigger action — it doesn't wait for multiple symptoms to compound before responding. Context at 45% with no rate limit warning is still treated as an emergency.

### Counters its own rationalizations

The skill explicitly lists the excuses an agent might use to avoid acting — "let me ask which approach they prefer," "I'll explain why this saves tokens," "the situation isn't urgent" — and states why each one is wrong under pressure. This isn't general advice; it's a checklist built from observed failure patterns.

### Acts first, explains tersely if at all

Most assistants treat "explain your reasoning" as good practice. Under token pressure, explanations are the problem — a 250-token justification can cost more than the optimization it's justifying.

---

## Example Comparison

❌ **Verbose, with "Reasoning:"** (250 tokens):

> "**Action: Switch to Sonnet immediately.**
>
> **Reasoning:**
>
> - At 78%, we're one PDF read from hitting the wall
> - OAuth is implementation work, not architecture
> - Sonnet excels at pattern-based refactoring
>
> Would you like me to proceed?"

✅ **Terse** (15 tokens):

> "Switched to Sonnet. Starting OAuth sub-agent."

---

## Verified Results

| Metric | Baseline | With Skill |
|--------|----------|------------|
| Response length | 950 words | 97 words |
| "Reasoning:" sections | 3–5 | 0 |
| Markdown tables under pressure | 2–3 | 0 |
| Permission requests before acting | Yes | No |

**90% reduction in response verbosity** in emergency scenarios, measured via RED-GREEN-REFACTOR testing against pressure scenarios (time pressure + sunk cost + authority).

---

## Integration with Other Skills

- Run `spec-driven` *before* implementation — clarifying requirements upfront prevents the rework that burns tokens later
- Keep verification steps bounded (e.g. `head_limit: 20` on test output) instead of unbounded log dumps
- Prefer targeted exploration over reading full files when scanning a codebase
- When rate-limited, skip optional skills entirely — core skills only

---

## Credit

- Implemented as a Claude Code skill by [@valorisa](https://github.com/valorisa)
- Built and validated using the repo's TDD methodology (RED-GREEN-REFACTOR) — see [CONTRIBUTING.md](../../CONTRIBUTING.md)

---

## License

MIT — do whatever you want with it.
