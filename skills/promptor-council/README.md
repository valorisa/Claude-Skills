# Promptor v3 Council Edition — A Claude Code Skill

Everything `promptor` does, plus an optional second opinion: when a generated prompt's self-critique isn't confident enough — or the domain is too critical to trust a single pass — this skill routes it through a 5-advisor council with blind peer review before you ship it.

**Don't just self-critique a production prompt. Get it audited.**

---

## The Problem

Promptor's base pipeline ends with a self-critique score. That's useful, but a model critiquing its own output has a structural blind spot: it tends to miss exactly the kind of thing it would also miss while generating the prompt in the first place.

For a throwaway prompt, that's a non-issue. For a prompt moderating production content, scoring credit risk, or routing legal escalations, a single self-assessment isn't enough of a check — and most workflows don't have a second pass built in at all.

## How It Works

Promptor Council runs the same 5-circle validation and 18-hack pipeline as `promptor`, then adds:

### Compliance-aware circles

- **C2 RESEARCH** now checks for **correlated proxy variables** when the domain touches compliance, legal, or security — e.g. flagging that "zip code" can carry forbidden "origin" signal even when origin itself isn't used
- **C3 GRID** adds a mandatory criterion whenever the prompt includes human escalation: the workflow must specify *who* processes it, *under what timeline*, *with what context*, and *how the decision gets recorded* — partial credit doesn't pass

### The council proposal

If self-critique scores below 4/5, or the domain is flagged as production-critical, Phase 3 ends with an explicit offer:

> 💡 Want an external audit by the LLM Council? ~11x cost, +2–3 minutes, recommended for critical production or high-risk domains.

You can also force it directly by adding `[COUNCIL]` to your request.

### Phase 4 — Council deliberation (when activated)

1. **Context framing** — collects the generated prompt, its self-critique, the C1–C5 traces, and scans your workspace (`CLAUDE.md`, `memory/`, referenced files) for relevant context
2. **5 advisors convened in parallel**, each with a distinct thinking style:
   - **The Contrarian** — assumes a critical defect exists and hunts for it
   - **The First Principles Thinker** — checks whether you're even asking the right question
   - **The Expansionist** — looks for missed opportunities and underexploited leverage
   - **The Outsider** — reacts with zero prior context, catching curse-of-knowledge jargon
   - **The Executor** — only cares whether someone could actually use this prompt Monday morning
3. **Blind peer review** — responses get anonymized as A–E, and each advisor reviews the other four without knowing who said what
4. **Chairman synthesis** — produces a final verdict: where the council converges, where it diverges, blind spots that only surfaced via peer review, a clear recommendation, and one concrete next action
5. **Artifacts generated** — a visual HTML report (opened automatically) and a full markdown transcript, both timestamped

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/valorisa/Claude-Skills ~/.claude/skills/
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

1. Create folder `~/.claude/skills/promptor-council/`
2. Drop `SKILL.md` inside it
3. Restart Claude Code

---

## Use

Same triggers as `promptor`:

- `create a prompt`
- `optimize this prompt`
- `promptor`
- `/promptor`
- `generate a system prompt`

Plus the council-specific flag:

- `[COUNCIL]` — forces the Phase 4 audit regardless of self-critique score

**Example:**

> Create a prompt for moderating user content in production [COUNCIL]

Promptor Council will:

1. Run the standard 5-circle pipeline — detects a security-adjacent domain, flags ambiguity around borderline content
2. Generate the prompt and a self-critique (e.g. 3/5: "no guidelines for gray-area cases")
3. See `[COUNCIL]` and convene the 5 advisors in parallel
4. Run blind peer review, then chairman synthesis
5. Deliver an HTML report and markdown transcript, plus a 2–3 sentence verdict summary and an offer to integrate the recommendations into a v2

---

## When To Use It

**Use the council when:**

- You explicitly add `[COUNCIL]`
- Self-critique scores below 4/5 **and** the domain is critical (security, compliance, production, legal)
- The prompt feeds a production system with real business impact
- It's the first prompt you've written for a domain you haven't explored before

**Skip the council when:**

- The prompt is experimental, internal, or throwaway
- You're doing rapid A/B iteration
- Self-critique already scored 4/5+ on a non-critical domain
- You've already declined the proposal once for this prompt
- Time or budget is explicitly tight — the council costs roughly 11x a standard pass

The skill won't activate the council on its own without your confirmation, except by proposing it — the golden rule baked into the skill is to respect your time and budget rather than treat the council as a default step.

---

## What Makes It Different From `promptor`

| | `promptor` | `promptor-council` |
|---|---|---|
| Self-critique | 0–5 score | 0–5 score + council proposal if under 4 |
| External validation | None | Optional 5-advisor council with blind peer review |
| Compliance checks | Standard | Adds correlated-proxy-variable detection (C2) and mandatory escalation-workflow criteria (C3) |
| Architecture questions | Not asked | Mandatory system-architecture and testability questions for production-critical prompts |
| Artifacts | Prompt only | Prompt + HTML report + markdown transcript (if council runs) |
| Relative cost | Baseline | Baseline, or ~11x if council activates |

---

## Example Session

**You:** "Create a prompt for moderating user content in production [COUNCIL]"

**Claude** runs the standard pipeline, then:

> 🏛️ **COUNCIL DELIBERATION ACTIVATED**
>
> Convening 5 advisors...
>
> **The Contrarian:** "This prompt lets through indirect toxic content — sarcasm, dogwhistles. No handling of context-dependent violations."
>
> **The Outsider:** "I don't understand what 'borderline content' means. If I don't understand it, a junior moderator won't either."
>
> **The Executor:** "Missing a decision matrix with concrete examples. Nobody can apply this Monday morning without examples."
>
> *(blind peer review and chairman synthesis follow)*
>
> ✅ Council verdict available
> 📄 `council-report-20260512-170230.html`
> 📋 `council-transcript-20260512-170230.md`
>
> **Verdict:** All advisors converge on a lack of guidance for ambiguous cases. The biggest blind spot — caught only in peer review — is that "borderline content" itself is undefined jargon. Immediate action: build a 10-row scenario/decision/justification table before shipping.

---

## Credit

- Implemented as a Claude Code skill by [@valorisa](https://github.com/valorisa), building on `promptor`
- Council methodology: [Andrej Karpathy's LLM Council](https://x.com/karpathy/status/1962263486196867115), adapted for Claude Code sub-agents
- See also `llm-council` for the standalone, prompt-agnostic version of the same council mechanism

---

## License

MIT — do whatever you want with it.
