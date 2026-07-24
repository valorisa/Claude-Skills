# Repo Audit

Repo Audit est une skill Claude Code qui réalise un audit technique approfondi d’un dépôt Git (local ou GitHub). Elle détecte bugs, problèmes de performance, failles de sécurité, gaps de couverture de tests et incohérences de documentation, puis peut créer des issues GitHub structurées pour les findings prioritaires.

## Description

Cette skill est pensée pour les développeurs, mainteneurs et équipes DevSecOps qui veulent obtenir une vue claire de la santé d’un repository. Elle combine exploration structurée du code, analyse qualitative et génération optionnelle d’issues GitHub, afin de transformer les observations en backlog exploitable.

Repo Audit ne modifie jamais le code sans confirmation explicite de l’utilisateur ; elle se concentre sur la détection, la priorisation et la création d’issues, pas sur l’auto‑fix en aveugle.

## Fonctionnalités

- Audit complet du dépôt : structure, code source, tests, scripts CI/CD et fichiers de configuration.
- Détection de bugs logiques, problèmes de performance et faiblesses de conception d’API.
- Analyse des risques de sécurité (secrets, exécution dynamique, permissions de fichiers, sérialisation de données non fiables).
- Identification des gaps de couverture de tests et des fonctionnalités non vérifiées.
- Repérage des gaps de documentation (README incomplet, comportement non documenté, exemples manquants).
- Génération optionnelle d’issues GitHub pour les findings Critiques et Haute priorité.

## Quand utiliser Repo Audit

Tu peux utiliser cette skill dans plusieurs situations typiques.

- Avant une release importante, pour vérifier que le repo ne présente pas de risques majeurs.
- Lors de la reprise d’un projet legacy ou d’un dépôt externe que tu dois désormais maintenir.
- Pour réaliser un health check régulier d’un monorepo ou d’un service central à ton architecture.
- Après une phase de développement intense pour transformer la dette technique en backlog d’issues priorisées.

## Installation

Repo Audit est une skill Claude Code installée côté client. Elle se déclare dans le répertoire des skills de Claude.

### macOS et Linux

```bash
mkdir -p ~/.claude/skills/repo-audit
curl -L https://example.com/skills/repo-audit/SKILL.md \
  -o ~/.claude/skills/repo-audit/SKILL.md
```

Les skills sont chargées automatiquement au démarrage de Claude Code depuis `~/.claude/skills/<skill-name>/SKILL.md`.

### Windows

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills\repo-audit"
Invoke-WebRequest `
  -Uri "https://example.com/skills/repo-audit/SKILL.md" `
  -OutFile "$env:USERPROFILE\.claude\skills\repo-audit\SKILL.md"
```

Sur Windows, les skills résident dans `%USERPROFILE%\.claude\skills\<skill-name>\SKILL.md` et sont détectées lors du prochain démarrage de Claude Code.

## Mode de fonctionnement

Repo Audit suit un workflow en plusieurs étapes pour structurer l’analyse.

### 1. Détermination de la cible

La skill commence par identifier le dépôt cible.

- Si l’utilisateur fournit une URL GitHub (`https://github.com/owner/repo`), la skill en déduit `owner/repo`.
- Si un chemin local est fourni, celui‑ci est utilisé directement.
- Si rien n’est précisé, la skill considère le répertoire de travail courant comme cible.

La skill demande ensuite si elle doit créer des issues GitHub pour les findings de haute priorité avant de poursuivre.

### 2. Exploration de la structure du repo

L’objectif est de comprendre ce que fait le projet et comment il est organisé.

- Lecture du `README.md` pour les objectifs, la description et les fonctionnalités annoncées.
- Inspection des fichiers de dépendances (`pyproject.toml`, `package.json`, `go.mod`, `Cargo.toml`, etc.) pour identifier langages et bibliothèques utilisées.
- Listing des fichiers de code source et des fichiers de tests pour estimer la couverture logique.
- Lecture du point d’entrée principal et des modules cœur (services, API, CLI, etc.).

La skill construit ainsi un modèle mental du projet : objectifs, stack, architecture, modes d’exécution et organisation des tests.

### 3. Analyse détaillée du code

La skill passe ensuite en revue les modules pour détecter différents types de problèmes.

- Bugs logiques dans les conditions, setters et accesseurs.
- Mauvais usage de la bibliothèque standard ou des API de runtime.
- Ordre d’arguments incorrect dans certaines fonctions.
- Mauvaise gestion de la concurrence (threads, async, race conditions).
- Off‑by‑one et erreurs d’indexation.
- Boucles intensives sans pause (busy‑wait), recomputations inutiles, absence de cache ou de pooling.
- Fuites potentielles de mémoire via des structures de données non bornées.

### 4. Sécurité, API et tests

La skill examine ensuite les risques plus globaux.

- Patterns d’exécution dynamique (`exec`, `eval`) sans validation d’entrée.
- Gestion des fichiers et répertoires avec des permissions trop permissives.
- Sérialisation et désérialisation de données non fiables (pickle, JSON, etc.).
- Secrets et credentials hardcodés ou loggés.
- Incohérences dans la conception des API (types de retour, conventions de nommage, validation des arguments).
- Gaps de tests : fonctionnalités documentées mais non testées, logique de retry/timeout sans vérification, chemins spécifiques à une plateforme jamais exercés.

La documentation est également comparée au comportement réel pour repérer les divergences et les fonctionnalités non documentées.

### 5. Classification des findings

Pour rendre les résultats actionnables, chaque finding est classé par sévérité.

- Critique : bugs runtime, pertes de données, failles de sécurité importantes.
- Haute priorité : comportement incorrect courant, problèmes de performance significatifs, casse d’API.
- Moyenne priorité : fonctionnalités manquantes, gaps de tests et problèmes d’UX.
- Faible / nice‑to‑have : style, documentation et petites améliorations de maintenabilité.

Les findings critiques incluent systématiquement le chemin de fichier, la ligne approximative, la description, la raison du problème et une suggestion de fix.

### 6. Synthèse et interaction avec l’utilisateur

La skill produit un rapport synthétique pour l’utilisateur.

- Résumé des bugs critiques et des problèmes de haute priorité.
- Liste des gaps de couverture de tests et des risques de sécurité.
- Vue d’ensemble des zones du code qui méritent une attention immédiate.

La skill demande ensuite à l’utilisateur pour quelles sévérités elle doit créer des issues GitHub (par défaut : Critique + Haute priorité).

### 7. Création d’issues GitHub

Si l’utilisateur confirme, Repo Audit crée des issues GitHub pour chaque finding sélectionné.

Chaque issue suit un format structuré :

- Description du problème.
- Localisation (fichier, module, ligne approximative).
- Comportement actuel et code concerné.
- Comportement attendu.
- Suggestion de correctif.
- Impact et sévérité.

Les issues sont rédigées en anglais, avec un titre court, spécifique et actionnable, et ne mentionnent pas explicitement l’intervention d’une IA ou d’un outil automatisé.

### 8. Rapport final

À la fin de l’audit, la skill fournit un récapitulatif des issues créées et de leurs sévérités.

- Tableau synthétique des numéros d’issues, titres et niveaux de criticité.
- Suggestions d’ordre de traitement (par exemple quels bugs critiques traiter en premier).
- Indications sur la maturité globale du repo (par exemple : prêt ou non pour une release majeure).

## Exemples de scénarios d’utilisation

Tu peux déclencher Repo Audit avec différents objectifs selon le contexte.

- Health check avant release : “Audite ce repo avant la release et signale les bugs critiques, les problèmes de sécurité et les gaps de tests.”
- Reprise d’un projet legacy : “Analyse ce dépôt hérité, donne‑moi une vue des principaux risques et crée des issues pour les problèmes les plus graves.”
- Audits réguliers : “Fais un audit de ce monorepo, concentre‑toi sur la sécurité et la couverture de tests, et propose des issues pour les findings de haute priorité.”

## Bonnes pratiques

Pour obtenir des résultats utiles et éviter le bruit, quelques bonnes pratiques sont recommandées.

- Commencer par un audit sans création d’issues pour découvrir le paysage de risques et ajuster la portée.
- Limiter l’analyse à certains sous‑répertoires si le monorepo est très volumineux.
- Combiner Repo Audit avec des outils spécialisés (analyse de dépendances, scans de secrets, SAST) pour une couverture maximale.
- Intégrer cette skill dans ton workflow de revue ou dans des audits ponctuels, plutôt que l’exécuter sur chaque commit.

## Licence

Repo Audit est proposée sous licence MIT. Tu peux l’adapter, la redistribuer et l’intégrer à tes propres workflows, sous réserve de conserver la mention de licence appropriée.

## Citations

```text
[1] Repo Audit — Deep analysis of Git history | ClaudSkills https://claudskills.com/skills/repo-audit/
[2] README Doctor — Claude Skill, Tested (8.4/10) https://skillproof.dev/skills/readme-doctor
[3] Auditing Readme · AgentStack https://agentstack.voostack.com/l/skill-qte77-claude-code-plugins-auditing-readme
[4] 345 Claude Code skills & agent skills & plugins (30 ... https://github.com/alirezarezvani/claude-skills
[5] I built a skill that roasts your README against 116 top- ... https://www.reddit.com/r/ClaudeCode/comments/1s7myt3/i_built_a_skill_that_roasts_your_readme_against/
[6] readme-doctor • claude-skills • livlign • Skills • Registry - Tessl https://tessl.io/registry/skills/github/livlign/claude-skills/readme-doctor/security
[7] CLAUDE.md https://github.com/alirezarezvani/claude-skills/blob/main/CLAUDE.md
[8] repo-analyzer - Claude Skills https://claude-plugins.dev/skills/@jmagly/ai-writing-guide/repo-analyzer
[9] skill-system-auditor - Online Tools https://tool.lu/en_US/skill/s/3py
[10] agent-skills/docs/claude-agent-setup.md at main - GitHub https://github.com/fluxcd/agent-skills/blob/main/docs/claude-agent-setup.md
```
