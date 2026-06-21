# Grill Me — A Claude Code Skill

Stress-test any plan or design before you commit to it. Claude interviews you relentlessly, branch by branch through the decision tree, until every blind spot is on the table.

**Stop shipping plans nobody pressure-tested. Start getting grilled.**

---

## The Problem

Ask most AI assistants to review your plan and they'll skim it, nod along, and hand back three bullet points of generic praise with a token "consider edge cases" at the end.

That's fine for a sanity check. It's useless for a plan where being wrong is expensive.

A real stress-test means someone systematically working through every decision you made, asking what you considered and rejected, what happens if each choice is wrong, and whether your decisions secretly depend on each other in ways you haven't noticed.

## How It Works

When you activate **grill-me**, Claude becomes a structured interviewer:

- **Maps the decision tree first** — before asking anything, has you list every branch of the plan, then challenges the list for omissions and estimates how deep the questioning will go
- **One question at a time by default** — won't dump 15 questions on you at once, unless you explicitly say the next few are independent
- **Walks every branch systematically** — for each decision: what's proposed, what alternatives were considered, what's the success criterion, what happens if it's wrong, does it depend on another branch
- **Holds recommendations until the end** — no advice mid-interview; everything is stored and delivered together in the synthesis
- **Runs four stress tests** once the tree is covered: worst-case, inversion, constraint failure, and "what don't we know"
- **Delivers a synthesis** — what's solid, what's fragile, what's missing, plus an explicit reminder that internal consistency isn't the same as real-world viability

If the session gets interrupted, it hands you a partial report instead of pretending the whole tree was covered.

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/valorisa/Claude-Skills ~/.claude/skills/
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

1. Create folder `~/.claude/skills/grill-me/`
2. Drop `SKILL.md` inside it
3. Restart Claude Code

---

## Use

Mention any of these triggers:

- `grille-moi`
- `grill me`
- `stress-test this`
- `challenge my plan`
- `dis-moi ce qui cloche`

Or present a plan, design, or architecture and ask for critical review directly — Claude will detect the context.

**Example:**

> grille-moi : je veux migrer notre monolithe vers des microservices en 3 mois, équipe de 4 devs, zéro downtime exigé par le client.

Grill Me will:

1. Ask what an error in this plan would actually cost (skips the full grill if the stakes are low)
2. Have you map out every decision branch (service boundaries, data migration, rollback strategy, team allocation, timeline buffers…)
3. Challenge that list for branches you didn't think of
4. Walk each branch: alternatives considered, success criteria, failure consequences, cross-branch dependencies
5. Run the four stress tests against the whole plan
6. Hand you a synthesis: what's solid, what's fragile, what's missing

---

## When To Use It

**Good grill-me candidates:**

- "Should we migrate to microservices in 3 months with a 4-person team?"
- "Here's my data migration plan — find the holes"
- "I want to launch this pricing model, stress-test it"
- "Review this system design before I present it to the architecture board"
- "I'm confident in this rollout plan, prove me wrong"

**Skip grill-me for:**

- Low-stakes decisions where being wrong costs little (the skill itself will suggest this)
- Quick factual questions
- Plans that aren't actually written down yet (write it down first)
- Wanting validation rather than scrutiny

Grill Me is built to find what's wrong with your plan, not to reassure you about it. That's the feature, not a bug.

---

## What Makes Grill Me Different

### Decision-Tree Mapping First

Most review skills jump straight into questions. Grill Me makes you enumerate the full decision tree before the interview starts, then challenges that list — catching branches you forgot to even mention, not just branches you answered poorly.

### One Question at a Time

No question dumps. Branch by branch, with explicit dependency tracking: if answering branch 7 changes the right answer to branch 2, Grill Me goes back to branch 2 before moving forward.

### Recommendations Held to the End

No advice leaks out mid-interview. Everything Claude would tell you is stored and delivered as a single synthesis in Phase 4 — so the interview stays focused on understanding, not persuading.

### Four-Test Stress Pass

Once the tree is mapped, every plan goes through the same four lenses:

- **Worst case** — everything that can go wrong, does
- **Inversion** — what if you did the exact opposite?
- **Constraint failure** — what if your #1 constraint doubled or collapsed?
- **Ignorance** — what don't you know that could sink this?

### Honest About Its Own Limits

The synthesis always closes with an explicit warning: a grill tests internal coherence, not external validity. A logically consistent plan can still fail in the real world — Grill Me says so out loud instead of implying its approval means the plan will work.

---

## Example Session

**You:** *"grille-moi : on veut passer notre API REST en GraphQL d'ici la fin du trimestre."*

**Grill Me:**

> Avant de commencer : quel est le coût d'une erreur dans ce plan ? Une mauvaise migration GraphQL casse-t-elle des clients en prod, ou est-ce réversible facilement ?
>
> *(you answer: "ça casse des clients en prod, pas de rollback simple")*
>
> OK, on grille sérieusement. D'abord, liste-moi toutes les branches de décision que tu identifies dans ce plan — schéma GraphQL, stratégie de migration des clients existants, gestion du versioning, formation équipe, etc.
>
> *(you list 5 branches)*
>
> Je vois 5 branches, mais tu n'as pas mentionné la stratégie de cache — GraphQL casse les patterns de cache HTTP classiques. Ça fait une 6ème branche critique. On a aussi 2 niveaux de dépendance en cascade ici (le schéma dépend du choix de versioning, qui dépend de la stratégie client). Prévoyez environ 20-25 minutes.
>
> Phase 1 — cadrage : quel est le problème concret que cette migration résout ? Pas "GraphQL c'est mieux", le problème réel.

Notice:

- No advice before the decision tree is fully mapped
- Catches a missing branch (caching) before the interview even starts
- Flags dependency depth and sets time expectations upfront
- Refuses vague justifications ("c'est mieux") and pushes for the real problem

---

## Credit

- Implemented as a Claude Code skill by [@valorisa](https://github.com/valorisa)
- Decision-tree interview structure inspired by Socratic questioning and pre-mortem analysis methodology

---

## License

MIT — do whatever you want with it.
