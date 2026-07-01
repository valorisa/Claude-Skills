# Multi-LLM Debate + Grill Me

## Vue d’ensemble

Ce dépôt contient une skill destinée à organiser un débat structuré entre plusieurs LLM autour d’une idée, d’un plan, d’un design ou d’un choix d’architecture.

Le but n’est pas d’obtenir plusieurs réponses indépendantes sans coordination. Le but est de créer un processus de débat contrôlé, où chaque modèle :

- commence par analyser le problème de manière autonome,
- exécute mentalement une phase de stress-test de type "grill me",
- lit ensuite les réponses des autres modèles,
- ajuste sa position si nécessaire,
- puis contribue à une synthèse finale.

Cette approche est utile pour :

- tester la cohérence d’un plan ;
- identifier les dépendances cachées ;
- révéler les ambiguïtés ;
- forcer un vrai stress-test intellectuel ;
- obtenir une synthèse plus robuste qu’un avis isolé.

## Pourquoi cette skill existe

Quand on soumet une idée à un seul modèle, on obtient souvent une réponse rapide, mais pas forcément assez challengée.

Quand on fait simplement passer la réponse d’un modèle à un autre, on peut au contraire créer un effet de dérive :

- les erreurs se propagent ;
- les hypothèses implicites se renforcent ;
- le débat devient une simple chaîne de répétition.

Cette skill évite ces deux pièges.

Elle impose :

1. un cadrage silencieux initial ;
2. une position initiale indépendante ;
3. une lecture croisée structurée ;
4. une révision finale ;
5. un juge final séparé.

## Structure de la skill

La skill est organisée en cinq blocs :

- **Round 0** — cadrage silencieux.
- **Round 1** — position initiale.
- **Round 2** — lecture croisée.
- **Round 3** — révision finale.
- **Juge final** — synthèse et arbitrage.

Le round 0 est essentiel : il sert à activer mentalement la logique de stress-test avant tout débat visible. Il permet d’identifier les branches de décision, les dépendances, les ambiguïtés et les questions critiques.

## Quand l’utiliser

Utilise cette skill quand tu veux :

- challenger un plan ;
- valider une architecture ;
- comparer plusieurs options ;
- préparer un projet GitHub ;
- tester la solidité d’une idée avant d’investir du temps ;
- organiser un débat entre plusieurs LLM sur un même sujet.

Cette skill est particulièrement adaptée à des sujets techniques, produit, architecture, CI/CD, workflow GitHub, design système, ou décisions de création de repo.

## Quand ne pas l’utiliser

Cette skill n’est pas adaptée si :

- tu veux une réponse courte et immédiate ;
- tu n’as pas besoin d’un débat ;
- tu cherches seulement une reformulation ;
- le sujet ne justifie pas plusieurs étapes de confrontation.

Elle n’a pas vocation à remplacer :

- un benchmark réel ;
- des tests ;
- une revue de sécurité approfondie ;
- une validation terrain ;
- un retour utilisateur concret.

## Principe de fonctionnement

### 1. Brief commun

Tous les LLM reçoivent le même brief initial.

### 2. Round 0

Chaque LLM effectue un cadrage silencieux :

- lecture du brief ;
- identification des branches de décision ;
- identification des dépendances ;
- identification des ambiguïtés ;
- préparation de la position initiale.

### 3. Round 1

Chaque LLM donne une analyse indépendante sans tenir compte des autres.

### 4. Round 2

Chaque LLM lit les autres réponses et réagit :

- ce qu’il conserve ;
- ce qu’il corrige ;
- ce qu’il rejette ;
- ce qui diverge ;
- ce qui reste incertain.

### 5. Round 3

Chaque LLM produit une version consolidée.

### 6. Juge final

Un arbitre final lit tout et produit une synthèse unique.

## Rôles possibles

Tu peux attribuer des rôles différents selon les modèles :

- **Planner** : structure, architecture, séquencement.
- **Builder** : implémentation, structure de repo, faisabilité.
- **Critic** : failles, risques, angles morts.
- **Judge** : arbitrage final, synthèse, décision.

Tu peux utiliser les mêmes rôles avec DeepSeek, GLM, Claude, Qwen, ou tout autre LLM chat web.

## Bonnes pratiques

### Garder un format stable

Le format de sortie doit rester identique d’un LLM à l’autre.

### Limiter le nombre de rounds

Trois rounds plus un juge final suffisent dans la plupart des cas.

### Séparer critique et décision

Une critique utile ne remplace pas une décision. Le juge final sert à trancher.

### Garder les incertitudes visibles

Si un point reste flou, il doit rester flou dans la sortie.

### Préserver les désaccords

Les divergences importantes sont souvent les informations les plus utiles.

## Cas d’usage recommandé

Exemple typique :

- tu as une idée de repo GitHub ;
- tu écris un brief clair ;
- tu l’envoies à trois LLM ;
- tu récupères leurs analyses ;
- tu les fais débattre ;
- tu fais conclure un juge final.

Ce workflow est particulièrement pertinent pour un projet de création de repo, une architecture d’outil, ou une réflexion sur une CI/CD ou une automatisation GitHub.

## Remarque importante

Cette skill teste la cohérence interne d’un plan ou d’un design, pas sa validité externe ni sa faisabilité réelle.

Un plan peut être logiquement cohérent et pourtant échouer en pratique.

## Fichiers du dépôt

- `skill.md` : la skill canonique.
- `PROMPT-ENTREE.md` : le prompt d’entrée à copier dans les LLM.
- `README.md` : documentation d’usage.

## Utilisation rapide

1. Lis `skill.md`.
2. Prépare ton brief.
3. Copie le contenu de `PROMPT-ENTREE.md`.
4. Lance le débat sur 3 LLM ou plus.
5. Récupère les réponses.
6. Fais exécuter la lecture croisée.
7. Demande la synthèse du juge final.

## Licence

À adapter selon ton projet.

## Avertissement final

Ce système aide à mieux penser un problème. Il ne garantit pas qu’une idée soit bonne, seulement qu’elle a été davantage challengée.
