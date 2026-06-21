# Promptor v3 — A Claude Code Skill

A prompt architect, not a prompt suggestion box. Promptor runs every prompt request through a 5-circle validation pipeline fused with 18 optimization hacks, and delivers an auditable, copy-paste-ready result.

**Stop hand-writing prompts by feel. Start generating them with a trace.**

---

## The Problem

Most "write me a prompt" requests get answered with something plausible-sounding but unverified — no domain risks identified, no success criteria defined, no check that the result actually does what you needed.

That's fine for a one-off. It's expensive when the prompt is going into production, gets reused across a team, or needs to survive contact with edge cases you haven't thought of yet.

## How It Works

Ask Promptor to build, optimize, or audit a prompt and it runs a 3-phase pipeline:

### Phase 1 — Five Circles (validation, with a structured trace)

Each circle emits a JSON trace block (`{"circle": "C1", "status": "pass|fail", "evidence": "...", "hacks_applied": [...]}`) before moving to the next:

| Circle | Name | What it does |
|--------|------|---------------|
| C1 | STOP | Validates the request, auto-detects domain and your experience level, identifies 3 domain-specific risks |
| C2 | RESEARCH | Cites 2–3 recognized patterns per risk — facts only, marked `[UNVERIFIED]` if unsourced |
| C3 | GRID | Generates a binary pass/fail success checklist — no subjective terms like "good" or "modern" |
| C4 | TRIBUNAL | Applies the grid strictly to your request — pass/fail table, zero free commentary, zero global score |
| C5 | FIX | Targeted corrections for every FAIL, up to 3 iterations, then delivers best-effort with an explicit `[BLOCKED: reason]` if still unresolved |

### Phase 2 — 18-Hack Filter

A library of 18 named optimization techniques (covering token cost, context hygiene, model routing, sub-agent limits, and more) gets prioritized based on what you're optimizing for — tokens, quality, speed, security, or collaboration — and woven into the generated prompt's instructions.

### Phase 3 — Delivery (A-B-C-D)

- **A — Calibration**: 3 bullets max on what was detected and applied
- **B — The prompt itself**: copy-paste ready, with `{{VARIABLE}}` placeholders for reuse across contexts
- **C — Self-critique**: a 0–5 score with one concrete improvement if it's not a 5
- **D — Follow-up**: 2–3 questions to iterate further

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/valorisa/Claude-Skills ~/.claude/skills/
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

1. Create folder `~/.claude/skills/promptor/`
2. Drop `SKILL.md` inside it
3. Restart Claude Code

---

## Use

Mention any of these triggers:

- `create a prompt`
- `optimize this prompt`
- `promptor`
- `/promptor`
- `generate a system prompt`
- `prompt engineering`
- `build me a prompt for...`
- `reverse prompt engineer this`
- `improve this prompt`
- `prompt audit`

**Example:**

> promptor: I need a prompt for summarizing legal contracts into plain-language bullet points.

Promptor will:

1. Ask two questions — what the prompt should do, and which AI tool it's for
2. Run C1–C5: detect domain (legal/contracts), flag risks (e.g. liability language being oversimplified), research relevant summarization standards, build a pass/fail grid, evaluate against it, fix any failures
3. Filter through the 18 hacks relevant to your focus area
4. Deliver calibration notes, the finished copy-paste prompt, a self-critique score, and follow-up questions to refine further

---

## Special Modes

**`[MODE:API]`** — add this to your request for strict JSON output (no markdown, no conversational delivery), useful for programmatic integration.

**`[?word]`** — drop this anywhere in your request to get an immediate inline explanation of that term before Promptor resumes the pipeline.

**`[COLLAB:MODE]`** — co-construct the prompt step by step instead of receiving it all at once.

---

## When To Use It

**Good Promptor candidates:**

- Building a reusable system prompt for a specific AI tool or workflow
- Auditing an existing prompt that isn't performing as expected
- Reverse-engineering what a prompt is actually doing so you can improve it
- Any prompt going into production or shared across a team — where "looks about right" isn't enough

**Skip Promptor for:**

- A single throwaway question you're about to ask directly
- Quick one-off phrasing tweaks where the validation overhead isn't worth it

---

## What Makes It Different

### Every claim has a trace

The five circles don't just produce a prompt — they produce a JSON audit trail showing what was checked, what passed, what failed, and which hacks were applied at each stage. You can see *why* the prompt looks the way it does, not just the final text.

### No subjective success criteria

Phase 1's grid (C3) explicitly bans vague terms like "good" or "modern" as pass/fail criteria. Every criterion has to be checkable, which forces the evaluation in C4 to be a real test rather than a vibe check.

### Self-critique is mandatory, not optional

Every delivery includes a 0–5 self-assessment. A score under 5 comes with a named, concrete improvement — not a vague "could be better."

### Built-in instruction-injection sanitization

Before processing your request, Promptor checks it (and any supplied context) for injection patterns and flags them rather than executing blindly.

---

## Credit

- Implemented as a Claude Code skill by [@valorisa](https://github.com/valorisa)
- See also `promptor-council` for a multi-perspective deliberation variant of this same methodology

---

## License

MIT — do whatever you want with it.
