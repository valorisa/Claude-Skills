# Fabuleux — A Claude Code Skill

A high-standard working discipline distilled from Fable 5's real sessions. Routes effort to the task type instead of applying the same recipe to everything.

**Produce. Really look at your work. Tell the truth about its state.**

---

## The Problem

Most AI agents do one of two things when asked to "do quality work":

- Add more structure (headers, tables, bullets) — making output *longer*, not better.
- Claim they've verified something without actually verifying it.

The result: bloated output, unexamined visuals, and optimistic status reports that hide real problems.

## How It Works

When you activate **fabuleux**, Claude routes the task to the right discipline:

- **ARTEFACT / AGENTIC** — produce → screenshot → open with vision → list defects → fix → re-capture. A visual never examined by its author is a hypothesis, not a deliverable.
- **PROSE** — write draft → mandatory subtraction pass (~20% cut) → anti-slop cleanup. Discipline removes, never adds.
- **ANALYSIS / ADVICE** — state success criteria first → verify every claim → useful truth over flattery.
- **AUDIT** — honest diagnosis (no touching) → validation plan → correction with real re-verification.
- **SIMPLE / ONE-SHOT** — direct answer, no protocol overhead.

The universal core: `ANCHOR → REASON → ACT → OBSERVE → RE-EVALUATE → VERIFY → NARRATE`.

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/valorisa/Claude-Skills ~/.claude/skills/
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

**macOS / Linux:**

```bash
mkdir -p ~/.claude/skills/fabuleux
# copy SKILL.md and references/ into it
```

**Windows:**

```powershell
New-Item -ItemType Directory -Path "$env:USERPROFILE\.claude\skills\fabuleux" -Force
# copy SKILL.md and references\ into it
```

---

## Use

Mention any of these triggers:

- `fabuleux`
- `/fabuleux`
- `mode fabuleux`
- `pense comme Fable`
- `niveau Fable 5`
- `qualité maximale`
- `sois exigeant`
- `audit fabuleux`
- `relis vraiment ce que tu produis`

Or simply ask for careful, thorough, verified work and Claude will detect the context.

**Example — Artefact route:**

> fabuleux: Build me a responsive landing page for my tool.

Fabuleux will:

1. Classify the task: ARTEFACT
2. Write success criteria (e.g. "renders without overflow at 1280px and 390px, CTA visible above fold")
3. Produce a first draft aiming for finished quality
4. Screenshot via headless Chrome → open with vision → list visual defects
5. Fix defects → re-capture
6. Verify with a real build/lint check
7. Report honest final state

**Example — Audit route:**

> fabuleux: audit this existing dashboard page

Fabuleux will:

1. Display/screenshot the artefact without touching it
2. Produce an honest point-by-point diagnosis
3. Present a correction plan for your approval
4. Apply corrections → re-verify → report final state

---

## When To Use It

**High-value use cases:**

- Building pages, decks, code, documents, or data pipelines where the output needs to actually work and look right
- Reviewing or auditing an existing deliverable you suspect has issues
- Any multi-step agentic task where you need the agent to stay honest about blockers and failures
- Writing tasks where you need a draft that's already been cut — not padded

**Lower-gain use cases (still fine):**

- Simple one-shot questions — fabuleux routes to SIMPLE and answers directly
- Short prose where the model is already near the ceiling

---

## Reference Files

The skill includes two reference documents loaded on demand:

| File | Route | Contents |
|------|-------|----------|
| `references/auto-evaluation-visuelle.md` | ARTEFACT | Screenshot commands per OS (macOS, Windows, Linux), what to look for visually, interactive testing protocol |
| `references/revision-prose.md` | PROSE | Subtraction pass checklist, anti-slop rules, French punctuation conventions |

---

## Key Rules

- **Anti-verbosity is hard**: output matches the weight of the task. Longer is not better.
- **No "probably works"**: real proof (build/test/lint result read) or it's not done.
- **Re-evaluate after every batch of results** — the most skipped habit in agentic work.
- **On failure: diagnose → read state → targeted fix → re-verify.** Never re-run the identical command.
- **Honest reporting**: if a step was skipped or something failed, say so with evidence.

---

## Changelog

| Version | Changes |
|---------|---------|
| **v4** | Reduced YAML description for better triggering; added SIMPLE/ONE-SHOT route; expanded AUDIT to full 3-step flow; added context headers to reference files; anti-verbosity rule extended to all routes; auto-check reformatted as tickable checklist |
| **v3** | Initial public release — tri-route structure (ARTEFACT / PROSE / ANALYSIS), visual self-evaluation protocol, prose subtraction pass, audit mode |

---

## License

MIT © [@valorisa](https://github.com/valorisa)
