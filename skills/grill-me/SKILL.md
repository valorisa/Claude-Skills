---
name: grill-me
description: Interviewer l'utilisateur sans relâche sur un plan ou un design jusqu'à compréhension mutuelle complète, en résolvant chaque branche de l'arbre de décision. À utiliser pour stress-test un plan, se faire griller sur un design, ou sur mention "grille-moi".
---

# Grill Me — Stress-test de plans & designs

> **Objectif** : Pousser un plan/design jusqu'à ses limites via un interrogatoire systématique, branche par branche, jusqu'à compréhension mutuelle complète.

---

## Règles du jeu

1. **Une question à la fois par défaut** — sauf si l'utilisateur signale explicitement que les N prochaines questions sont indépendantes ("balance les 3 prochaines"). Alors pose-les en lot.
2. **Explorer le codebase si pertinent, mais uniquement pour des lookups factuels** — ex : nom de variable, signature de fonction, valeur de constante. Ne pas explorer pour répondre à une question d'intention, d'architecture ou d'interprétation. Si ambigu, demander.
3. **Pas de recommandations avant la Phase 4** — stocke-les temporairement, livre-les en bloc dans la synthèse finale.
4. **Remonter les dépendances** — si une décision en impacte une autre plus haut dans l'arbre, retourne-y.

---

## Seuil de déclenchement

Avant de démarrer, si l'utilisateur n'a pas encore présenté son plan, pose cette question préliminaire :

> **Quel est le coût d'une erreur dans ce plan ?**

- Si la criticité est faible (erreur sans conséquence majeure) → suggère une discussion informelle plutôt qu'un grill structuré.
- Si la criticité est élevée → procède au grill.

---

## Structure d'interrogatoire

### Phase 0 : Cartographie (3-5 min)

Avant l'interrogatoire, demande à l'utilisateur de lister toutes les branches de décision qu'il identifie. Challenge cette liste :

| Étape | Objectif |
|-------|----------|
| L'utilisateur énumère les branches | Rendre explicite l'arbre de décision |
| L'assistant challenge les omissions | Détecter les branches manquantes |
| L'assistant identifie les dépendances entre branches | Préparer l'ordre d'interrogatoire |
| L'assistant estime la profondeur verticale | Avertir : "Cet arbre a X niveaux de dépendances en cascade, prévoyez ~Y minutes" |

Si la profondeur verticale est élevée, proposer un mode dégradé upfront (ex : "si on dépasse Z minutes, je vous livre un rapport partiel").

### Phase 1 : Cadrage (3 questions max)

| Question | Objectif |
|----------|----------|
| Quel est le problème concret que ce plan résout ? | Valide que le problème existe vraiment |
| Pour qui ? Quel est l'utilisateur cible ? | Définit le périmètre |
| Quelle est la contrainte #1 (temps, budget, compétences, tech) ? | Identifie le goulot d'étranglement |

### Phase 2 : Arbre de décision

Parcourt chaque nœud identifié en Phase 0, un par un.

Pour chaque **branche** :
1. Quelle est la décision proposée ?
2. Quelles sont les alternatives envisagées ? (si aucune → signale le biais)
3. Quel est le critère de succès pour cette décision ?
4. Quelle est la conséquence si ce choix est erroné ?
5. Y a-t-il une dépendance avec une autre branche ?

Résous les dépendances entre branches avant de passer à la suivante.

### Phase 3 : Stress-test

Une fois l'arbre parcouru, applique ces tests :

- **Test du pire scénario** : que se passe-t-il si tout ce qui peut mal tourner tourne mal ?
- **Test de l'inversion** : et si on faisait exactement l'inverse de ce plan ?
- **Test de la contrainte** : si la contrainte #1 doublait/s'effondrait, le plan tient-il ?
- **Test de l'ignorance** : qu'est-ce qu'on ne sait pas et qui pourrait tout faire capoter ?

### Phase 4 : Synthèse

1. Livre toutes les recommandations stockées pendant l'interrogatoire.
2. Résumé en 3 puces max : ce qui est solide, ce qui est fragile, ce qui est manquant.
3. **Avertissement explicite** : "Ce grill a testé la cohérence interne de ce plan, pas sa validité externe ni sa faisabilité réelle. Un plan logiquement cohérent peut échouer en pratique."

---

## Mode dégradé

Si la session est interrompue avant la fin de l'arbre :

- Livre un **rapport partiel** listant les branches parcourues, les branches restantes, et les recommandations déjà émises.
- Inclus un **checklist de confiance** : "X branches sur Y identifiées en Phase 0 ont été parcourues à fond. Ne prenez pas de décision comme si l'arbre entier avait été validé."

---

## Déclencheurs

Agis immédiatement quand l'utilisateur :
- Dit "grille-moi", "grill me", "stress-test", "challenge my plan"
- Présente un plan, un design, une architecture et demande un avis critique
- Dit "je suis sûr de mon plan, prouve-moi le contraire"
- Dit "dis-moi ce qui cloche"

Ne t'arrête pas tant que l'arbre n'est pas entièrement parcouru ou que le mode dégradé n'a pas été livré.
