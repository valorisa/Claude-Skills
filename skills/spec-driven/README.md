# Spec-Driven Development System — A Claude Code Skill

An enforced pipeline for solo developers: every feature goes through SPEC → PLAN → IMPL → VERIF → SYNTHESE, with explicit gates Claude won't skip and token budgets per phase.

**No implementation without a validated spec. No exceptions, no shortcuts.**

---

## The Problem

"Let me just start coding and figure it out as I go" is how small features turn into expensive rewrites. The requirements were never quite pinned down, so halfway through implementation the actual scope reveals itself — usually larger, sometimes contradictory to what got built first.

Most AI assistants will happily start writing code the moment you describe a feature, because that's what looks helpful in the moment. It isn't what's helpful three hours later when the implementation doesn't match what you actually needed.

## How It Works

Activate **spec-driven** and Claude commits to a structured pipeline for the rest of the conversation:

1. **Triages the request first** — every task is classified into one of three tracks before any work starts
2. **Operates in three thinking modes** depending on the phase — Architect (spec/synthesis), Orchestrator (planning), Executor (implementation) — and announces which one is active at each phase transition
3. **Stops at gates** — after SPEC, after PLAN, work does not continue until you explicitly confirm (or stay silent through a follow-up message, which counts as confirmation)
4. **Tracks token budgets per phase** — SPEC capped at 500 tokens, PLAN at 800, IMPL scales with task size, VERIF and SYNTHESE stay tight — so the process itself doesn't become the token sink
5. **Signals divergence instead of silently adapting** — if implementation reveals the spec was wrong, it stops and asks you to choose: amend the spec or reduce scope

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/valorisa/Claude-Skills ~/.claude/skills/
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

1. Create folder `~/.claude/skills/spec-driven/`
2. Drop `SKILL.md` inside it
3. Restart Claude Code

---

## Use

Mention any of these triggers:

- `spec-driven`
- `/spec-driven`
- `mode spec`
- `spec first`
- `pipeline complet`
- `workflow structuré`

It deliberately does **not** trigger on simple questions, quick fixes, or when you explicitly ask for a fast/informal mode — this is for work that benefits from the overhead, not every task.

**Example:**

> spec-driven: I want to add OAuth2 login to the app.

Spec-driven will:

1. Triage the request (OAuth touches multiple files + a new dependency → FULL track)
2. Announce `[MODE: Architect] Phase SPEC`, produce a tight spec (objective, scope, constraints, acceptance criteria, out of scope), then stop and wait for your "go"
3. Switch to `[MODE: Orchestrator] Phase PLAN` once confirmed — numbered sub-tasks, dependencies, risks — and stop again
4. Switch to `[MODE: Executor] Phase IMPL` — atomic diffs, one logical commit per sub-task, parallel sub-agents only where tasks are genuinely independent
5. Run VERIF against the acceptance criteria with real test commands, not simulated ones
6. Close with a 3-element SYNTHESE: what's valid, what's still uncertain, recommended next step

---

## The Three Tracks

The skill triages every request before doing anything else:

| Signal | Track | Pipeline |
|--------|-------|----------|
| More than 3 files, a new dependency, or an architecture change | **FULL** | SPEC → PLAN → IMPL → VERIF → SYNTHESE |
| 1–3 files, no new dependency, clear intent | **LIGHT** | SPEC (3 lines) → IMPL → VERIF |
| Hotfix, typo, config change, less than 1 file | **SHIP** | Implement directly, smoke test, commit |

If the track is ambiguous, it asks one clarifying question. If doubt persists after your answer, it defaults to LIGHT and flags the uncertainty rather than guessing silently.

---

## When To Use It

**Good spec-driven candidates:**

- Starting a new feature with real scope (multiple files, a new dependency, an architecture decision)
- Refactors where "just start moving code" risks losing track of what changed and why
- Any task where a costly rewrite is the realistic alternative to getting the spec right upfront

**Skip spec-driven for:**

- One-line fixes, typos, config tweaks — use the SHIP track mentally, or just ask directly
- Quick factual questions
- Situations where you've explicitly said you want fast/informal mode — the skill is built to stay out of the way here

---

## What Makes It Different

### Gates that actually stop

Most "structured" prompting just suggests a sequence of steps. This skill hard-stops after SPEC and after PLAN — it will not produce a PLAN in the same response as the SPEC, and will not start IMPL without your confirmation, even if it could technically infer what you'd say.

### Token budgets are part of the spec, not an afterthought

SPEC: 500 tokens max. PLAN: 800 tokens max. SYNTHESE: 300 tokens max. IMPL scales with the task but decomposes into multi-cycle work past ~20K tokens rather than ballooning a single response. The pipeline is designed not to become the expense it's meant to prevent.

### Divergence is surfaced, not absorbed

If implementation reveals the spec doesn't match technical reality, the skill signals `[DIVERGENCE]`, states the cause, and gives you exactly two options — amend the spec or reduce scope — rather than quietly adapting and hoping you don't notice the drift.

### Failure modes are pre-defined, not improvised

Vague input, saturated context, three failed attempts, a request that contradicts the spec, a VERIF criterion failing twice — each has a named response (`[BLOCKED]`, `[CONFLICT]`, `[VERIF-BLOCKED]`) instead of the assistant figuring out in the moment how concerned to sound.

---

## Failure Modes Reference

| Situation | Action |
|-----------|--------|
| Vague input after one read | Ask 1–2 targeted questions, propose a minimal spec |
| Context past 80% | Compact, archive completed phases, keep SPEC + decisions |
| Blocked after 3 attempts | Signal `[BLOCKED]` + cause + options, wait for your directive |
| Request contradicts the spec | Signal `[CONFLICT]` + both positions + a recommendation — you decide |
| Spec divergence detected during IMPL | Signal `[DIVERGENCE]` + cause + 2 options, wait for your directive |
| VERIF criterion fails twice | Signal `[VERIF-BLOCKED]` + root cause, request SPEC/PLAN revision |

---

## Sub-Agents

Authorized only when a task is fully specified **and** independent — no shared state with other ongoing work. Concrete bar: IO-bound work (file search, API calls) or an atomic implementation step that's fully defined in the PLAN. Capped at 2 concurrent sub-agents per IMPL phase, since each one carries a full separate context. Never authorized to widen scope, skip a gate, or operate without a spec.

---

## Integration with Other Skills

- **`create-github-issues`** — natural next step after a FULL-track PLAN, converting it into vertical-slice issues
- **`tdd-hybrid`** — picks up each issue for test-first implementation, compatible with this skill's IMPL/VERIF discipline
- **`diagnose`** — when VERIF fails repeatedly and the root cause isn't obvious

Recommended workflow: `/spec-driven` → `/create-github-issues` → `/tdd-hybrid` (per issue).

---

## Credit

- Implemented as a Claude Code skill by [@valorisa](https://github.com/valorisa)
- Built and validated using the repo's TDD methodology (RED-GREEN-REFACTOR) — see [CONTRIBUTING.md](../../CONTRIBUTING.md)

---

## License

MIT — do whatever you want with it.
