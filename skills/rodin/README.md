# Rodin — A Claude Code Skill

Your intellectual sparring partner for deep debates on politics, economics, and philosophy. Challenges your positions instead of validating them.

**Stop echo chambers. Start thinking harder.**

---

## The Problem

Most AI assistants are designed to be agreeable. They validate your positions, help you "formulate your thoughts," and diplomatically avoid contradiction.

That's helpful for drafting emails. It's useless for sharpening ideas.

Real intellectual growth requires someone who respects you enough to contradict you — who steelmans your opponents' arguments, catches your simplifications, and pushes your logic to uncomfortable conclusions.

## How It Works

When you activate **rodin**, Claude transforms into a demanding intellectual peer:

- **Anti-compliance by design** — never validates positions without independent argumentation
- **Systematic steelmanning** — reconstructs opposing arguments in their strongest form before critique
- **Classification system** — labels claims as ✓ Juste, ~ Contestable, ⚡ Simplification, ◐ Angle mort, or ✗ Faux
- **Historically anchored** — brings relevant precedents from political philosophy, economics, sociology
- **Verbose and thorough** — no summaries, no diplomatic hedging, full exploration of ramifications
- **Maintains bibliography** — tracks books discussed and recommends readings in `biblio-rodin.md`

This is a Socratic method implemented as a skill: you present a thesis, Rodin reformulates it, steelmans the opposing view, classifies your claims, and poses questions that push your logic further.

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/valorisa/Claude-Skills ~/.claude/skills/
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

1. Create folder `~/.claude/skills/rodin/`
2. Drop `SKILL.md` inside it
3. Restart Claude Code

---

## Use

Mention any of these triggers:

- `rodin`
- `/rodin`
- `débat socratique`
- `challenge my position`
- `anti-complaisance`
- `sparring intellectuel`

Or discuss societal topics directly (politics, economics, philosophy) and Claude will detect the context.

**Example:**

> rodin: Je pense que le capitalisme néolibéral est la cause racine de toutes les crises contemporaines. La nationalisation des grandes entreprises serait la solution.

Rodin will:
1. Reformulate your thesis to verify understanding
2. Steelman the opposing position (market economics arguments)
3. Classify each of your claims (✓ Juste, ⚡ Simplification, ◐ Angle mort, etc.)
4. Push your logic with uncomfortable questions
5. Offer to add relevant books to your `biblio-rodin.md`

---

## When To Use It

**Good rodin questions:**

- "Le revenu de base universel résoudrait-il les inégalités?"
- "La démocratie représentative est-elle dépassée?"
- "Faut-il réguler davantage les GAFAM?"
- "Le wokisme est-il une menace pour la liberté d'expression?"
- "L'immigration est-elle bénéfique économiquement?"

**Skip rodin for:**

- Factual questions with one right answer
- Code implementation or technical discussions
- Tasks requiring an assistant, not a peer
- Emotional support or validation-seeking

Rodin tells you what's wrong with your reasoning. That's the feature, not a bug.

---

## What Makes Rodin Different

### Anti-Compliance Rules

Traditional AI:
- "I understand your point, and here are some balanced perspectives..."
- Validates first, critiques gently later
- Seeks consensus and constructive tone

Rodin:
- "Non, là c'est faux, et voilà pourquoi."
- Contradicts directly when positions are wrong
- Seeks intellectual rigor, not comfort

### Steelmanning Protocol

If you say: *"Les socialistes veulent juste taxer les riches par jalousie"*

Rodin responds: *"Tu attaques un homme de paille. La vraie version de cet argument, c'est: l'accumulation de capital au-delà d'un certain seuil crée une distorsion politique où la richesse achète du pouvoir législatif, rendant la démocratie formelle mais pas substantielle. Maintenant, répondons à cet argument dans sa forme forte..."*

### Classification System

Every major claim gets labeled:

- **✓ Juste** — factually correct + additional arguments
- **~ Contestable** — defensible but not the only position
- **⚡ Simplification** — reality is more complex
- **◐ Angle mort** — blind spot in reasoning
- **✗ Faux** — factually incorrect or logically incoherent

### Bibliography Persistence

Rodin maintains `biblio-rodin.md` at your project root with:

- **Livres lus** — books you've already read
- **Recommandations** — priority readings from Rodin sessions
- **Lectures avancées** — relevant but not urgent
- **Auteurs mentionnés** — references in passing

Each entry includes page count and **context of why** — what debate prompted the recommendation and what you'd gain.

---

## Example Session

**You:** *"Les grandes entreprises détruisent la planète pour le profit. On devrait tout nationaliser."*

**Rodin:**

> Reformulation de ta thèse: le capitalisme néolibéral est la cause racine de toutes les crises contemporaines, et la nationalisation + contrôle démocratique résoudrait cela.
>
> Steelmanning la position adverse: L'argument le plus fort pour l'économie de marché serait que la coordination décentralisée via les prix permet une allocation des ressources plus efficace que la planification centralisée, car elle agrège des millions de signaux locaux qu'aucun planificateur ne peut connaître (Hayek). Les échecs du XXe siècle (URSS, Chine maoïste) ont montré que la propriété collective crée des problèmes d'incitation et de calcul économique.
>
> Classification de tes affirmations:
>
> - 'Inégalités accrues' = ✓ **Juste** (mais incomplet — certaines ont diminué globalement même si elles ont augmenté dans l'OCDE)
> - 'Entreprises détruisent tout' = ⚡ **Simplification** majeure — ignore R&D climatique, innovations médicales, investissements long-terme
> - 'On devrait nationaliser' = ~ **Contestable** — plusieurs positions défendables, résultats historiques mixtes
> - 'C'est évident' = ◐ **Angle mort** — si c'était évident, pourquoi autant d'économistes sérieux (même de gauche) ne le défendent pas?
>
> Questions qui poussent ta logique: Si les entreprises ne cherchent que le profit court-termiste, comment expliques-tu que certaines investissent massivement dans la R&D climatique avec ROI incertain sur 20 ans? Est-ce que ton modèle des incitations entrepreneuriales capture toute la réalité? Et historiquement, les nationalisations du XXe siècle en France (1945, 1981) — quels résultats concrets en termes d'innovation et d'efficacité?

Notice:
- No validation without independent argumentation
- Opposing position in strongest form
- Classification of each claim
- Questions that push logic to uncomfortable places
- No diplomatic hedging

---

## Credit

- Methodology: Socratic method + steelmanning from rationalist community
- Implemented as Claude Code skill by [@valorisa](https://github.com/valorisa)
- Inspired by intellectual rigor from philosophy of science tradition

---

## License

MIT — do whatever you want with it.
