---
name: agentic-loop-github
description: Structure any multi-step, iterative task on a GitHub repo (fixing CI, resolving lint violations, iterating on a PR, debugging a failing workflow) as an observe-decide-execute-verify loop with explicit stop conditions and guardrails. Use this whenever a task could require more than one attempt to succeed — CI is failing and the fix isn't obvious on the first try, a task says "keep trying until X passes", or you're about to loop on the same file/branch multiple times. Do NOT use for single-shot tasks (one clear edit, one commit, no verification loop needed).
---

# Agentic Loop for GitHub Workflows

Une tâche itérative sur un repo (CI cassée, lint à corriger, PR à faire passer) n'est pas juste "corriger et réessayer" — c'est une boucle avec un objectif vérifiable et des limites explicites. Cette skill structure la boucle pour éviter deux échecs classiques : (1) tourner indéfiniment sans savoir si on avance, (2) déclarer "terminé" sur un critère flou.

## La boucle

1. **Observer** — lire l'état réel avant d'agir : `gh pr checks`, logs CI, diff courant, fichiers concernés. Ne jamais supposer l'état ; le vérifier.
2. **Décider** — une action ciblée, pas une réécriture large. Préférer le fix minimal qui adresse la cause identifiée dans les logs.
3. **Exécuter** — appliquer l'action (edit, commit).
4. **Vérifier** — contrôler contre le critère d'arrêt (voir ci-dessous), pas contre une impression.
5. **Décider la suite** — continuer, corriger différemment, rollback, ou stop.
6. **Stop** — dès que le critère vérifiable est atteint. Ne pas continuer "pour être sûr".

## Vérification objective vs subjective

C'est le point qui détermine si la boucle peut tourner seule ou doit impliquer l'humain :

- **Objectif** (l'agent peut juger seul) : CI verte, tests passants, `markdownlint` sans erreur, build qui compile, PR mergeable sans conflit. → boucler jusqu'au critère.
- **Subjectif** (l'agent ne peut pas juger seul) : qualité d'une doc bilingue, pertinence d'un roadmap, ton d'un README. → ne pas boucler sans critère ; demander à l'utilisateur quel test appliquer ("est-ce que la structure en 3 phases te convient ?"), ou proposer un critère proxy vérifiable (ex. "présence des sections X, Y, Z" plutôt que "qualité perçue").

Si la tâche mélange les deux (ex. fix CI + réécriture de doc), traiter chaque partie séparément avec son propre critère.

## Cadrage d'itération (garde-fou anti-dérive)

Avant de lancer une boucle de correction :

- Fixer un nombre max de tentatives (3–5 pour un fix CI ciblé ; ne pas dépasser sans repasser par l'utilisateur).
- Détecter la stagnation : si la même erreur réapparaît après 2 tentatives différentes, ce n'est probablement pas un problème de syntaxe mais de compréhension — s'arrêter et exposer le blocage plutôt que de continuer à deviner.
- Ne jamais silencieusement dépasser la limite convenue ; si elle est atteinte, rapporter l'état et demander comment procéder.

## Rollback

Si une tentative aggrave l'état (nouvelle erreur CI, conflit introduit) :

- Revenir à l'état stable connu avant de retenter (`git checkout -- <fichier>`, ou reset de la branche de travail si plusieurs commits sont impliqués).
- Ne jamais empiler des correctifs sur un état déjà cassé sans comprendre pourquoi il l'est.

## Mémoire à deux niveaux

- **Mémoire de tâche** (le fil de la PR/session en cours) : ce qui a déjà été tenté et pourquoi ça a échoué — évite de retenter la même chose.
- **Mémoire long terme** (patterns réutilisables entre repos) : les erreurs récurrentes déjà connues (ex. `MD013`/`MD033` à désactiver systématiquement, `actions/checkout@v5` requis avant la dépréciation Node 20 de septembre 2026, ordre `git operation` correct pour éviter les conflits d'encodage) devraient être consignées une fois résolues, pas redécouvertes à chaque repo.

## Exemple appliqué

Tâche : "CI markdownlint échoue sur ce repo, corrige-la."

- Critère d'arrêt objectif : `gh pr checks` passe au vert.
- Boucle : lire l'erreur exacte → corriger la ligne concernée → push → re-vérifier CI → si échec différent, recommencer ; si échec identique après 2 essais, arrêter et signaler.
- Pas de rollback nécessaire si chaque commit est un fix isolé et vérifié avant le suivant.
