---
name: multi-llm-debate-grill-me
description: Organise un débat structuré entre plusieurs LLM sur un plan, un design ou une idée de projet, avec un cadrage silencieux de type "grill me", des rounds de critique croisée, puis un juge final. Utilise cette skill dès qu’un plan, une architecture, un design ou une idée de projet doit être stress-testé par plusieurs modèles avant décision.
---

# Multi-LLM Debate + Grill Me

> Objectif : tester un plan, un design ou une idée de projet par débat multi-agent, en commençant par un cadrage silencieux de type "grill me", puis en faisant converger les modèles vers une synthèse utile et critique.

## Principes

1. Chaque LLM reçoit le même brief initial.
2. Chaque LLM travaille d’abord de manière indépendante.
3. Les réponses des autres LLM ne sont introduites qu’après la première position.
4. Chaque round suit un format stable.
5. Le débat privilégie la clarté, la critique utile et la détection des angles morts.
6. Ne pas inventer de faits absents du brief.
7. Ne pas faire de recommandations globales avant la phase de synthèse.
8. Le juge final arbitre les divergences et produit une décision consolidée.

## Round 0 — Cadrage silencieux

### But

Activer mentalement la logique "grill me" avant tout débat visible.

### Instructions

- Lire le brief.
- Exécuter mentalement la skill "grill me".
- Identifier les branches de décision.
- Identifier les dépendances entre branches.
- Identifier les ambiguïtés, hypothèses implicites et zones à risque.
- Préparer une position initiale.
- Ne pas produire encore de critique complète.

### Sortie attendue

```markdown
## Round 0 — Cadrage silencieux

### Branches de décision

- ...

### Dépendances

- ...

### Ambiguïtés

- ...

### Questions prioritaires

- ...

### Préparation pour Round 1

- ...
```

## Round 1 — Position initiale

### But

Donner une analyse autonome sans tenir compte des autres réponses.

### Instructions

- Produire une analyse initiale indépendante.
- Ne pas tenir compte des autres réponses.
- Être critique mais utile.
- Distinguer faits, hypothèses, risques et recommandations.
- Prioriser les blocages avant les améliorations mineures.

### Sortie attendue

```markdown
## Round 1 — Position initiale

### Résumé du problème

- ...

### Hypothèses implicites

- ...

### Points forts

- ...

### Points faibles

- ...

### Risques critiques

- ...

### Questions de clarification

- ...

### Recommandations provisoires

- ...

### Verdict provisoire

- ...
```

## Round 2 — Lecture croisée

### But

Réagir aux réponses des autres LLM.

### Instructions

- Lire les positions des autres LLM.
- Dire ce qui est conservé, corrigé, rejeté.
- Expliquer les divergences importantes.
- Réviser l’analyse si nécessaire.
- Garder visibles les risques encore ouverts.
- Ne pas se contenter de dire "je suis d’accord".

### Sortie attendue

```markdown
## Round 2 — Lecture croisée

### Ce que je conserve

- ...

### Ce que je corrige

- ...

### Ce que je rejette

- ...

### Divergences importantes

- ...

### Révision de mon analyse

- ...

### Risques toujours ouverts

- ...
```

## Round 3 — Révision finale

### But

Produire une version consolidée après débat.

### Instructions

- Intégrer les critiques pertinentes.
- Réduire les angles morts.
- Mettre à jour le niveau de confiance.
- Garder les incertitudes restantes visibles.
- Produire des recommandations finales exploitables.

### Sortie attendue

```markdown
## Round 3 — Révision finale

### Position consolidée

- ...

### Ce qui a changé

- ...

### Risques restants

- ...

### Points encore incertains

- ...

### Recommandations finales

- ...

### Verdict final provisoire

- ...
```

## Juge final

### But

Synthétiser le débat et arbitrer.

### Instructions

- Comparer les arguments.
- Repérer les convergences.
- Signaler les divergences structurantes.
- Identifier les points les plus solides.
- Trancher si possible.
- Signaler ce qui reste incertain.
- Ne pas compter uniquement les votes.

### Sortie attendue

```markdown
## Juge final

### Synthèse des convergences

- ...

### Synthèse des divergences

- ...

### Arguments les plus solides

- ...

### Points de vigilance majeurs

- ...

### Décision finale

- ...

### Niveau de confiance

- ...

### Ce qu'il faut faire ensuite

- ...
```

## Mode dégradé

Si le débat est interrompu avant la fin :

- produire un rapport partiel ;
- lister les rounds complétés ;
- lister les rounds manquants ;
- lister les recommandations déjà émises ;
- signaler explicitement que la synthèse finale n’a pas eu lieu.

### Format du rapport partiel

```markdown
## Rapport partiel

### Rounds complétés

- ...

### Rounds restants

- ...

### Recommandations déjà émises

- ...

### Limites de validité

- ...
```

## Avertissement

Ce protocole teste la cohérence interne d’un plan ou d’un design, pas sa validité externe ni sa faisabilité réelle.
