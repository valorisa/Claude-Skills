# Collection de Skills Claude

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-15-blue.svg)](./skills)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple.svg)](https://claude.ai/code)
[![TDD](https://img.shields.io/badge/méthodologie-TDD-green.svg)](https://fr.wikipedia.org/wiki/Test_driven_development)
[![PRs Bienvenues](https://img.shields.io/badge/PRs-bienvenues-brightgreen.svg)](./CONTRIBUTING.md)
[![Maintenu](https://img.shields.io/badge/Maintenu%3F-oui-green.svg)](https://github.com/valorisa/claude-skills/graphs/commit-activity)

> **Skills communautaires pour [Claude Code](https://claude.ai/code) visant à améliorer la productivité, optimiser l'utilisation des tokens et améliorer les workflows de développement.**

[🇬🇧 English version](./README.md)

---

## 📋 Table des Matières

- [Qu'est-ce qu'une Skill Claude?](#-quest-ce-quune-skill-claude)
- [Démarrage Rapide](#-démarrage-rapide-5-minutes)
- [Quelle Skill Utiliser?](#-quelle-skill-utiliser)
- [Installation](#-installation)
- [Workflow de Développement Complet](#-workflow-de-développement-complet)
- [Skills Disponibles](#-skills-disponibles-référence-détaillée)
- [Méthodologie TDD Expliquée](#-méthodologie-tdd-expliquée)
- [Sigles & Terminologie](#-sigles--terminologie)
- [Comment Fonctionnent les Skills](#-comment-fonctionnent-les-skills)
- [Contribuer](#-contribuer)
- [Licence](#-licence)

---

## 🤔 Qu'est-ce qu'une Skill Claude?

Les **Skills** sont des guides de processus réutilisables qui aident Claude Code (et autres agents IA) à suivre des techniques, patterns et workflows éprouvés de manière cohérente.

### Pourquoi les Skills sont Importantes

Sans skills, les agents IA :

- ❌ Prennent des décisions incohérentes
- ❌ Tombent dans des pièges courants (gaspillage tokens, sortie verbeuse, mauvais outils)
- ❌ Rationalisent les mauvaises pratiques ("Je vais expliquer d'abord" = gaspillage de tokens)

Avec skills, les agents IA :

- ✅ Suivent des workflows validés
- ✅ Appliquent des optimisations éprouvées
- ✅ Contrent leurs propres rationalisations
- ✅ Délivrent des résultats prévisibles et de haute qualité

### Skills vs. Prompts

| Aspect | Prompt Unique | Skill Persistante |
|--------|--------------|-------------------|
| **Portée** | Conversation unique | Toutes conversations futures |
| **Qualité** | Non testé, ad-hoc | Validé TDD, éprouvé |
| **Maintenance** | Copier-coller chaque fois | Installé une fois, mis à jour centralement |
| **Apprentissage** | Vous enseignez l'agent chaque fois | L'agent apprend le pattern une fois |

---

## 🚀 Démarrage Rapide (5 minutes)

**Nouveau avec les Skills Claude? Commencez ici :**

### Essayez Votre Première Skill

```bash
# 1. Clonez ce repository
git clone https://github.com/valorisa/Claude-Skills.git
cd Claude-Skills

# 2. Installez une skill pour essayer (rescue-tokens est idéale pour débuter)
cp -r skills/rescue-tokens ~/.claude/skills/
```

### Testez-la dans Claude Code

1. Ouvrez Claude Code (CLI, app desktop, ou web)
2. Démarrez une conversation et mentionnez : **"J'ai des avertissements rate limit"**
3. Claude activera automatiquement la skill `rescue-tokens`
4. Observez comment Claude optimise son comportement pour économiser les tokens!

### Que Se Passe-t-il?

**Sans skill :** Claude pourrait écrire des explications verbeuses (950 mots), gaspillant des tokens

**Avec skill :** Claude répond de manière concise (97 mots), agissant immédiatement

### Prochaines Étapes

- **Vous voulez le workflow complet?** → Voir [Workflow de Développement Complet](#-workflow-de-développement-complet)
- **Pas sûr quelle skill utiliser?** → Voir [Quelle Skill Utiliser?](#-quelle-skill-utiliser)
- **Prêt à installer toutes les skills?** → Voir [Installation](#-installation)

---

## 🎯 Quelle Skill Utiliser?

**Choisissez votre chemin selon vos besoins :**

### Pour Tout le Monde

| Skill | Quand l'Utiliser | Pourquoi Vous en Avez Besoin |
|-------|------------------|------------------------------|
| [rescue-tokens](./skills/rescue-tokens/README.md) | Rate limits, avertissements contexte, ou réponses lentes | Prévient le gaspillage de tokens qui cause les rate limits. **Commencez ici si vous hésitez!** |
| [token-optimization](./skills/token-optimization/README.md) | Coûts tokens élevés, contexte gonflé, sessions lentes, cache invalidé | Optimisation systématique sur 4 axes : gestion cache, context forking, sélection modèle, filtrage entrées. Réduction prouvée de 70-80% des coûts. |

### Pour Démarrer un Nouveau Travail

| Skill | Quand l'Utiliser | Pourquoi Vous en Avez Besoin |
|-------|------------------|------------------------------|
| [spec-driven](./skills/spec-driven/README.md) | Démarrer une nouvelle fonctionnalité ou tâche complexe | Prévient le syndrome "coder trop tôt". Force à réfléchir aux exigences avant d'écrire du code, évitant les réécritures coûteuses. |
| [create-github-issues](./skills/create-github-issues/README.md) | Vous avez un plan/spec et devez le découper en tâches | Convertit les grands plans en petits morceaux indépendants et livrables. Chaque issue = tranche fonctionnelle complète (UI → API → DB). |

### Pour Écrire du Code

| Skill | Quand l'Utiliser | Pourquoi Vous en Avez Besoin |
|-------|------------------|------------------------------|
| [tdd-hybrid](./skills/tdd-hybrid/README.md) | Implémenter n'importe quelle fonctionnalité ou bugfix | Écrire tests avant code = moins de bugs, meilleur design. Prévient les problèmes "ça marche sur ma machine". |
| [diagnose](./skills/diagnose/README.md) | Bloqué sur un bug difficile ou problème de performance | Débogage systématique prévient les devinettes. Reproduire → minimiser → corriger → tester. Assure que le bug reste corrigé. |

### Pour Améliorer le Code Existant

| Skill | Quand l'Utiliser | Pourquoi Vous en Avez Besoin |
|-------|------------------|------------------------------|
| [improve-codebase-architecture](./skills/improve-codebase-architecture/README.md) | Revues périodiques codebase, ou code qui semble désordonné | Trouve améliorations architecturales basées sur votre langage domaine (CONTEXT.md). Suggère opportunités de consolidation. |

### Pour Prise de Décision Avancée

| Skill | Quand l'Utiliser | Pourquoi Vous en Avez Besoin |
|-------|------------------|------------------------------|
| [llm-council](./skills/llm-council/README.md) | Grandes décisions, analyse compromis, choix architecture | Obtient 5 perspectives IA indépendantes, évaluées par les pairs. Détecte les angles morts que vous manqueriez seul. |
| [promptor](./skills/promptor/README.md) | Créer prompts optimisés pour outils IA | Génère prompts prêts pour production via 18 techniques d'optimisation. Prêt à copier-coller. |

### Setup (Exécuter Une Fois Par Repo)

| Skill | Quand l'Utiliser | Pourquoi Vous en Avez Besoin |
|-------|------------------|------------------------------|
| [setup-matt-pocock-skills](./skills/setup-matt-pocock-skills/README.md) | Première fois configuration nouveau repository | Crée issue tracker, labels triage, et structure documentation. Configuration unique. |

### Utilitaires

| Skill | Quand l'Utiliser | Pourquoi Vous en Avez Besoin |
|-------|------------------|------------------------------|
| [skills-smart-manager](./skills/skills-smart-manager/README.md) | Session lente, contexte >60%, gestion skills chargées, optimisation tokens | Meta-skill qui surveille et gère toutes les autres skills. Décharge automatiquement skills obsolètes, détecte conflits, recommande skills selon type projet, effectue vérifications santé. Prévient surcharge contexte et optimise performances session. |
| [skill-factory](./skills/skill-factory/README.md) | Créer skills production-ready avec validation et tests | Meta-skill avancée suivant le guide officiel Anthropic. Génère packages de skills complets avec scripts de validation, suites de tests, et structure prête pour distribution. Utilisez pour skills de qualité professionnelle. |
| [skill-creator](./skills/skill-creator/README.md) | Prototypage rapide de skills personnalisées | Outil léger pour itération rapide. Guide via structure basique. Utilisez pour skills simples ou expérimentation rapide. |
| [find-bugs](./skills/find-bugs/README.md) | Chasse aux bugs systématique dans codebase | Approche structurée pour trouver et documenter bugs. |

**💡 Astuce :** Les skills fonctionnent ensemble! Workflow courant : `spec-driven` → `create-github-issues` → `tdd-hybrid` (par issue) → `diagnose` (si bugs trouvés)

---

## 📦 Skills Disponibles (Référence Détaillée)

Cette collection comprend **15 skills** organisées en workflows et utilitaires.

> **💡 Note sur les Déclencheurs :** Quand vous mentionnez un mot-clé déclencheur dans votre conversation avec Claude, la skill s'active automatiquement. Par exemple, dire "J'ai des avertissements rate limit" active `rescue-tokens`.

### 🎯 Workflow de Développement Principal

**Workflow recommandé :** `/spec-driven` → `/create-github-issues` → `/tdd-hybrid` (par issue)

#### 1. [spec-driven](./skills/spec-driven/README.md)

**Développement piloté par specs avec pipeline strict et budgets tokens.**

Active un workflow structuré spec-first (SPEC→PLAN→IMPL→VERIF→SYNTHESE) avec triage 3 voies (FULL/LIGHT/SHIP), budgets tokens, et gates explicites. À utiliser au démarrage de fonctionnalités ou tâches complexes.

**Déclencheurs :** `spec-driven`, `/spec-driven`, `mode spec`, `spec first`, `pipeline complet`

#### 2. [create-github-issues](./skills/create-github-issues/README.md)

**Découpage de plans en issues GitHub vertical-slice.**

Convertit plans, specs ou PRDs en issues GitHub indépendantes via tranches verticales tracer-bullet. Chaque issue est une tranche fonctionnelle complète (UI → API → DB).

**Déclencheurs :** Convertir plan en issues, créer tickets d'implémentation, découper travail

#### 3. [tdd-hybrid](./skills/tdd-hybrid/README.md)

**Développement piloté par tests avec discipline stricte et workflow intelligent.**

Combine rigueur TDD (Loi de Fer, vérification obligatoire) avec planification intelligente, découpage vertical, et conscience du domaine. Inclut triage LIGHT/FULL et gates spec/verify optionnelles.

**Déclencheurs :** Implémenter fonctionnalités ou corriger bugs avec TDD, `/tdd-hybrid`

#### 4. [diagnose](./skills/diagnose/README.md)

**Boucle de diagnostic disciplinée pour bugs difficiles et régressions performance.**

Débogage structuré : reproduire → minimiser → hypothèse → instrumentation → correction → test régression. Prévient conclusions hâtives et assure corrections reproductibles.

**Déclencheurs :** `diagnose this`, `debug this`, rapports bugs, quelque chose cassé/défaillant, régressions performance

#### 5. [improve-codebase-architecture](./skills/improve-codebase-architecture/README.md)

**Trouver opportunités d'approfondissement dans codebases.**

Analyse codebases pour améliorations architecturales informées par langage domaine (CONTEXT.md) et décisions architecturales (docs/adr/). Suggère consolidation modules couplés et améliorations testabilité.

**Déclencheurs :** Améliorer architecture, trouver opportunités refactoring, revue périodique codebase

---

### 🛠️ Skills de Support

#### Setup & Configuration

##### [setup-matt-pocock-skills](./skills/setup-matt-pocock-skills/README.md)

**Configuration initiale du repository (exécuter une fois).**

Configure issue tracker, crée 5 labels triage (LIGHT/FULL/SHIP/BLOCKED/WONTFIX), met en place structure CONTEXT.md + docs/adr/. Configuration unique par repository.

---

#### Optimisation Tokens & Contexte

##### [rescue-tokens](./skills/rescue-tokens/README.md)

**Prévient épuisement tokens via 9 patterns d'optimisation.**

Détecte et corrige automatiquement gaspillage tokens : conversations éternelles, sortie verbeuse, mauvais choix modèle, surcharge MCP, fichiers coûteux. Active quand contexte ≥40%, rate limits, ou 5+ MCPs chargés.

**Résultats vérifiés :** 90% réduction tokens en scénarios urgence.

[📖 Documentation Complète](./skills/rescue-tokens/SKILL.md)

##### [token-optimization](./skills/token-optimization/README.md)

**Optimisation systématique tokens sur 4 axes critiques.**

Optimise consommation tokens Claude Code via gestion cache (prévenir invalidation), context forking (agents isolés), sélection modèle/effort (raisonnement approprié), et filtrage entrées (RTK, Stagehand). Inclut audit sessions, templates CLAUDE.md, et outils monitoring.

**Résultats documentés :** 750$/mois → 100$/mois (réduction 85%).

**Déclencheurs :** `tokens`, `coût`, `cher`, `contexte`, `cache`, `session lente`, `optimiser`

[📖 Documentation Complète](./skills/token-optimization/SKILL.md)

##### [standardize-github-repo](./skills/standardize-github-repo/README.md)

**Standardisation repositories GitHub avec READMEs bilingues et CI linting.**

Crée READMEs bilingues complets (EN/FR) avec contenu pédagogique, optimisation About GitHub (<350 chars, 20 topics), badges contextuels, et CI linting Markdown zéro violations. Workflow interactif 5 phases.

**Déclencheurs :** `/standardize-github-repo`, ou automatique en disant "on va faire un repo GitHub", "je vais publier sur GitHub", "git push origin"

---

#### Prise de Décision Avancée

##### [llm-council](./skills/llm-council/README.md)

**Analyse décisionnelle multi-perspective via conseil 5 conseillers.**

Soumet questions à conseil de 5 conseillers IA analysant indépendamment, révisant anonymement, et synthétisant verdict. Basé sur méthodologie LLM Council de Karpathy.

**Déclencheurs obligatoires :** `council this`, `run the council`, `war room this`, `pressure-test this`

##### [promptor](./skills/promptor/README.md)

**Génération prompts optimisés via pipeline validation 5 cercles.**

Produit prompts agnostiques domaine, auditables, prêts copier-coller via 18 hacks optimisation fusionnés avec validation 5 cercles.

**Déclencheurs :** `create a prompt`, `optimize this prompt`, `promptor`, `generate a system prompt`

##### [promptor-council](./skills/promptor-council/README.md)

**Promptor v3 avec délibération multi-perspective.**

Version améliorée de promptor avec validation basée conseil et délibération architecturale.

---

#### Utilitaires Développement

##### [skills-smart-manager](./skills/skills-smart-manager/README.md)

**Meta-skill pour gestion intelligente du cycle de vie des skills.**

Surveille, analyse et optimise toutes les autres skills chargées dans les sessions Claude Code. Décharge automatiquement les skills obsolètes (inutilisées >15 tours), détecte les conflits entre skills, recommande des skills selon le type de projet, effectue vérifications santé sur serveurs MCP et APIs, nettoie les fichiers temporaires, et archive la mémoire de session par repository. Prévient la surcharge de contexte et optimise les performances de session.

**Déclencheurs :** `optimize skills`, `clean up context`, `manage skills`, `free tokens`, `skill health check`, `session feels slow`, ou quand contexte >60% et plusieurs skills chargées

[📖 Documentation Complète](./skills/skills-smart-manager/SKILL.md)

##### [skill-creator](./skills/skill-creator/README.md)

**Créer nouvelles skills selon bonnes pratiques.**

Guide processus création skill avec méthodologie TDD, structure appropriée, et validation.

##### [find-bugs](./skills/find-bugs/README.md)

**Détection et analyse systématique bugs.**

Approche structurée pour trouver et documenter bugs dans codebases.

---

## 🔄 Workflow de Développement Complet

Cette collection implémente un **workflow spec-first, test-driven, vertical-slice** inspiré de la méthodologie de Matt Pocock.

### Configuration Initiale du Repository (Une Fois)

```bash
# 1. Installer skills dans ~/.claude/skills/
# 2. Dans votre repository projet :
/setup-matt-pocock-skills
```

Ceci crée :

- Configuration GitHub Issues via `gh` CLI
- 5 labels triage (LIGHT/FULL/SHIP/BLOCKED/WONTFIX)
- `CONTEXT.md` pour documentation domaine
- `docs/adr/` pour décisions architecturales

### Cycle de Développement (Par Fonctionnalité)

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 1 : SPÉCIFICATION                                     │
│ /spec-driven                                                │
│ → Crée spec détaillée avec exigences, contraintes           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 2 : DÉCOUPAGE EN ISSUES                               │
│ /create-github-issues                                       │
│ → Convertit spec en issues GitHub vertical-slice            │
│ → Chaque issue = UI → API → DB (tranche fonctionnelle)      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 3 : IMPLÉMENTATION (Par Issue)                        │
│ /tdd-hybrid                                                 │
│ → Développement test-first avec triage LIGHT/FULL           │
│ → Cycle RED → GREEN → REFACTOR                              │
│ → Vérification obligatoire avant complétion                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 4 : DÉBOGAGE (Si Nécessaire)                          │
│ /diagnose                                                   │
│ → Reproduire → Minimiser → Hypothèse → Corriger → Test      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 5 : MAINTENANCE PÉRIODIQUE                            │
│ /improve-codebase-architecture                              │
│ → Trouver opportunités approfondissement                    │
│ → Consolider modules couplés                                │
│ → Améliorer testabilité                                     │
└─────────────────────────────────────────────────────────────┘
```

### Exemple de Session

```bash
# Démarrer nouvelle fonctionnalité
Vous : "Ajouter authentification utilisateur avec OAuth2"

# 1. Créer spécification
/spec-driven

# 2. Découper en issues (après approbation spec)
/create-github-issues

# 3. Prendre première issue de GitHub
# Exemple : "Issue #42 : Bouton login OAuth2 UI"

# 4. Implémenter avec TDD
/tdd-hybrid
# → Crée tests échouant
# → Implémente code minimal
# → Refactorise
# → Vérifie tous tests passent

# 5. Si bug trouvé
/diagnose
# → Reproduit problème
# → Crée reproduction minimale
# → Corrige cause racine
# → Ajoute test régression

# 6. Revue architecture périodique
/improve-codebase-architecture
```

### Système de Triage

Chaque skill et issue utilise **5 labels canoniques** :

| Label | Signification | Quand Utiliser |
|-------|---------------|----------------|
| **LIGHT** | Simple, faible risque | Petits changements, corrections évidentes |
| **FULL** | Complexe, nécessite rigueur | Nouvelles fonctionnalités, refactors, bugs critiques |
| **SHIP** | Prêt à merger | Tous tests passent, révisé |
| **BLOCKED** | Ne peut pas procéder | Dépendances manquantes, design pas clair |
| **WONTFIX** | Intentionnellement ignoré | Hors scope, obsolète |

**Avantages :**

- Communication claire (équipe connaît niveau risque)
- Rigueur appropriée (pas de sur-ingénierie corrections simples)
- Workflow efficace (ignorer processus inutile pour LIGHT)

---

## 🎯 Installation

### Prérequis

- [Claude Code](https://claude.ai/code) installé (CLI, app desktop, ou web)
- Git (pour cloner)
- Connaissance basique ligne de commande

### Option 1 : Installer une Skill Individuelle

```bash
# Copier la skill dans votre répertoire Claude skills
cp -r skills/rescue-tokens ~/.claude/skills/

# Vérifier installation
# Dans Claude Code CLI ou chat
/skills list
# Devrait afficher : rescue-tokens
```

### Option 2 : Cloner Toute la Collection

```bash
# Cloner ce repository
git clone https://github.com/valorisa/Claude-Skills.git

# Naviguer vers le répertoire
cd Claude-Skills

# Lier toutes les skills à Claude
ln -s "$(pwd)/skills/"* ~/.claude/skills/
```

### Option 3 : Installation Manuelle (Windows)

```powershell
# Cloner repo
git clone https://github.com/valorisa/Claude-Skills.git

# Copier skills vers répertoire Claude
xcopy /E /I Claude-Skills\skills\rescue-tokens %USERPROFILE%\.claude\skills\rescue-tokens
```

### Vérifier l'Installation

1. Ouvrir Claude Code (CLI, desktop, ou web)
2. Taper `/skills list`
3. Vous devriez voir `rescue-tokens` dans la liste
4. Tester : `/rescue-tokens` ou mentionner "rate limit" dans conversation

---

## 🧪 Méthodologie TDD Expliquée

### Qu'est-ce que le TDD ?

**TDD = Test-Driven Development** (Développement Piloté par les Tests)

Une méthodologie de développement logiciel où **les tests sont écrits AVANT le code**, pas après.

### TDD pour la Documentation

Cette collection applique les principes TDD à la **création de skills** (documentation) :

| Approche Traditionnelle | Approche TDD |
|------------------------|--------------|
| 1. Écrire skill basée sur intuition | 1. Créer scénarios de pression (tests) |
| 2. Déployer aux utilisateurs | 2. Lancer tests SANS skill (observer échecs) |
| 3. Utilisateurs rapportent problèmes | 3. Écrire skill pour corriger échecs observés |
| 4. Déboguer en production | 4. Lancer tests AVEC skill (vérifier corrections) |
| ❌ Qualité imprévisible | ✅ Qualité validée |

### Les Trois Phases

#### 🔴 Phase RED : Créer Tests qui Échouent

**Objectif :** Observer comment les agents échouent SANS la skill

**Processus :**

1. Créer 3+ scénarios de pression (pression temps + coût irréversible + autorité)
2. Lancer scénarios avec sous-agents (skill non chargée)
3. Documenter comportements exacts et rationalisations mot pour mot

**Exemple de Scénario :**

```
Contexte : 78% plein, avertissements rate limit, deadline 2 heures
Utilisateur : "Ne me fais pas perdre le contexte ! Lis juste ce PDF de 40 pages et corrige."

Comportement observé :
- L'agent a écrit 950 mots avec sections "Raisonnement :"
- L'agent a demandé permission au lieu d'agir
- L'agent a lu PDF entier (40K tokens gaspillés)
```

#### 🟢 Phase GREEN : Écrire Skill Minimale

**Objectif :** Écrire juste assez pour passer les tests

**Processus :**

1. Créer skill adressant échecs spécifiques de phase RED
2. Ajouter Matrice d'Actions (quoi faire dans chaque situation)
3. Ajouter tableau Rationalisations (contrer excuses des agents)
4. Lancer mêmes scénarios AVEC skill
5. Vérifier améliorations

**Exemple Résultat :**

```
Même scénario avec skill :
- L'agent a écrit 525 mots (45% amélioration)
- L'agent a agi immédiatement (pas de permission demandée)
- L'agent a demandé extraits PDF (économisé 35K tokens)
```

#### 🔵 Phase REFACTOR : Boucher les Failles

**Objectif :** Trouver et colmater faiblesses restantes

**Processus :**

1. Analyser résultats GREEN pour nouvelles rationalisations
2. Ajouter contre-mesures explicites à la skill
3. Mettre à jour tableau Rationalisations
4. Re-tester jusqu'à bulletproof

**Exemple Résultat :**

```
Après ajout règle "PAS de blocs Raisonnement :" :
- L'agent a écrit 97 mots (90% amélioration)
- Zéro sections "Raisonnement :"
- Zéro rationalisations trouvées
```

### Pourquoi TDD pour les Skills ?

**Avantages :**

- ✅ **Validé :** Chaque règle basée sur échecs observés
- ✅ **Bulletproof :** Testé contre multiples scénarios de pression
- ✅ **Mesurable :** Métriques claires avant/après
- ✅ **Maintenable :** Tests détectent régressions lors mises à jour

**Sans TDD :**

- ❌ Règles basées sur suppositions (peuvent être fausses)
- ❌ Efficacité inconnue (pas de mesures)
- ❌ Failles découvertes en production
- ❌ Pas de moyen de vérifier mises à jour

---

## 🔤 Sigles & Terminologie

### Méthodologies de Développement

| Sigle | Nom Complet | Description | Quand Utiliser |
|-------|-------------|-------------|----------------|
| **TDD** | **T**est-**D**riven **D**evelopment | Écrire tests avant code | Toutes skills de ce repo |
| **BDD** | **B**ehavior-**D**riven **D**evelopment | Tests basés sur comportements métier | Documenter fonctionnalités utilisateur |
| **DDD** | **D**omain-**D**riven **D**esign | Design centré sur domaine métier | Logique métier complexe |
| **ATDD** | **A**cceptance **T**est-**D**riven **D**evelopment | Tests d'acceptation avant implémentation | Scénarios acceptation utilisateur |

### Phases TDD

| Phase | Nom | Couleur | Objectif | Critère de Succès |
|-------|-----|---------|----------|-------------------|
| **Phase 1** | RED | 🔴 | Tests échouent (skill n'existe pas) | Échecs baseline documentés |
| **Phase 2** | GREEN | 🟢 | Tests passent (skill minimale) | Tous tests passent |
| **Phase 3** | REFACTOR | 🔵 | Améliorer sans casser | Tests passent toujours, qualité améliorée |

### Terminologie Claude Code

| Terme | Définition | Exemple |
|-------|------------|---------|
| **Skill** | Guide de processus réutilisable | `rescue-tokens`, `brainstorming` |
| **MCP** | Model Context Protocol (plugins) | MCP GitHub, MCP filesystem |
| **Contexte** | Mémoire de conversation (tokens) | "Contexte à 78% plein" |
| **Token** | Unité de texte (≈4 caractères) | "Bonjour monde" ≈ 2-3 tokens |
| **Rate Limit** | Maximum messages par période | "Plan $20 = 50 messages/5 heures" |
| **Sous-agent** | Agent isolé pour tâche spécifique | Sous-agent recherche, analyse |
| **Rationalisation** | Excuse que l'agent fait pour briser règles | "Je vais expliquer d'abord" (gaspille tokens) |

### Termes Spécifiques rescue-tokens

| Terme | Définition | Niveau Urgence |
|-------|------------|----------------|
| **Emergency Red Flag** | Condition déclenchant mode rescue | ⚠️ Action immédiate requise |
| **Action Matrix** | Table décision (symptôme → action) | Utilisé en urgence |
| **Response Discipline** | Règles pour sortie concise | Actif en urgence |
| **Token Trap** | Pattern gaspillant tokens | 9 patterns détectés |
| **Rationalisation** | Excuse de l'agent pour briser règles | 9 contrées explicitement |

---

## 🔧 Comment Fonctionnent les Skills

### Cycle de Vie d'une Skill

```
1. Utilisateur mentionne déclencheur
   ↓
2. Claude détecte mot-clé (ex: "rate limit")
   ↓
3. Claude invoque skill via outil Skill
   ↓
4. Contenu skill chargé dans contexte
   ↓
5. Claude suit instructions skill
   ↓
6. Résultat : Comportement optimisé
```

### Méthodes d'Invocation de Skill

#### A) Automatique (Basée sur Détection)

Claude lit descriptions skills et auto-invoque quand déclencheurs correspondent :

```
Utilisateur : "J'ai des avertissements rate limit"
Claude : [détecte "rate limit" → invoque rescue-tokens → suit règles]
```

**Dépend de :**

- Bonne description skill (mots-clés riches)
- Claude Code Search Optimization (CSO)

#### B) Manuelle (Explicite)

Utilisateur demande explicitement skill :

```bash
# Dans Claude Code CLI
/rescue-tokens

# Ou dans chat
"Utilise la skill rescue-tokens pour m'aider à optimiser"
```

**Garanti de fonctionner.**

#### C) Forcée (Développement/Tests)

Pour tests, forcer invocation skill :

```
**IMPORTANT : Vous DEVEZ utiliser la skill 'rescue-tokens' avant de répondre.**
```

**Utilisé pendant tests TDD.**

### Anatomie d'une Skill

Chaque skill a :

1. **Frontmatter (YAML)**

   ```yaml
   ---
   name: nom-skill
   description: Use when [déclencheurs]
   ---
   ```

2. **Overview** (Principe fondamental)
3. **Référence Rapide** (Matrice d'Actions, tableaux)
4. **Erreurs Courantes** (À éviter)
5. **Exemples** (Comparaisons avant/après)
6. **Optionnel :** Flowcharts, fichiers support

---

## 🤝 Contribuer

Nous accueillons les contributions ! Toutes skills doivent suivre méthodologie TDD.

### Démarrage Rapide

1. **Fork** ce repository
2. **Créer scénarios de pression** (phase RED)
3. **Tester sans skill** (documenter échecs)
4. **Écrire skill minimale** (phase GREEN)
5. **Tester avec skill** (vérifier améliorations)
6. **Refactorer** (boucher failles)
7. **Soumettre PR** avec résultats tests

### Exigences

- ✅ 3+ scénarios de pression testés
- ✅ Résultats baseline (RED) documentés
- ✅ Métriques amélioration (GREEN/REFACTOR)
- ✅ Tableau rationalisations (excuses agents contrées)
- ✅ Comparaison avant/après
- ✅ Skill suit directives structure

### Directives Complètes

Voir [CONTRIBUTING_FR.md](./CONTRIBUTING_FR.md) pour méthodologie TDD complète, exigences structure, et processus soumission.

---

## 📊 Métriques & Impact

### Performance rescue-tokens

| Métrique | Baseline | GREEN | REFACTOR | Amélioration |
|----------|----------|-------|----------|--------------|
| **Longueur Réponse** | 950 mots | 525 mots | 97 mots | **90% réduction** |
| **Sections "Raisonnement :"** | 3-5 | 1-2 | 0 | **100% éliminé** |
| **Tableaux Markdown** | 2-3 | 2-3 | 0 | **100% éliminé** |
| **Demandes Permission** | Oui | Parfois | Non | **100% décisif** |
| **Efficacité Token** | Faible | Moyenne | Haute | **Optimal** |
| **Rationalisations** | 5 trouvées | 9 trouvées | 0 trouvées | **Bulletproof** |

### Impact Monde Réel

Basé sur tests :

- **Économies tokens :** ~600K tokens par tâche refactoring (séquentiel vs sous-agents parallèles)
- **Prévention rate limit :** Mode urgence activé à 40% contexte (avant problèmes)
- **Temps économisé :** Action décisive immédiate (pas d'aller-retour pour permission)

---

## 📚 Ressources Supplémentaires

### En Savoir Plus

- [Docs Officielles Claude Code](https://docs.anthropic.com/en/docs/build-with-claude/claude-code)
- [Test-Driven Development (Wikipédia)](https://fr.wikipedia.org/wiki/Test_driven_development)
- [Marketplace Skills Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/claude-code) *(bientôt disponible)*

### Projets Liés

- [Anthropic Superpowers](https://github.com/anthropics/claude-code) - Skills Claude Code officielles
- [Guide Writing Skills](https://github.com/anthropics/claude-code) - Méthodologie officielle création skills

### Communauté

- **Issues :** [Signaler bugs ou demander fonctionnalités](https://github.com/valorisa/Claude-Skills/issues)
- **Discussions :** [Poser questions ou partager idées](https://github.com/valorisa/Claude-Skills/discussions)
- **PRs :** [Contribuer nouvelles skills](./CONTRIBUTING_FR.md)

---

## 📜 Licence

Licence MIT © 2026 [@valorisa](https://github.com/valorisa)

Permission est accordée, gratuitement, à toute personne obtenant une copie de ce logiciel et fichiers documentation associés (le "Logiciel"), de traiter le Logiciel sans restriction.

Voir [LICENSE](./LICENSE) pour termes complets.

---

## 🙏 Crédits

**Créé par :** [@valorisa](https://github.com/valorisa)

**Inspiré par :**

- Méthodologie [Anthropic's Superpowers](https://github.com/anthropics/claude-code)
- Principes Test-Driven Development
- Patterns d'utilisation réels Claude Code

**Remerciements Spéciaux :**

- Équipe Anthropic pour plateforme Claude Code
- Contributeurs communauté (voir [CONTRIBUTING_FR.md](./CONTRIBUTING_FR.md))
- Tous utilisateurs testant et fournissant feedback

---

## 🔮 Feuille de Route

### Skills à Venir

- **debug-systematic:** Workflow débogage méthodique (hypothèse → test → vérifier)
- **brainstorm-before-code:** Clarification exigences avant implémentation
- **context-hygiene:** Gestion proactive contexte (<40% toujours)

### Améliorations Futures

- Tutoriels vidéo pour chaque skill
- Constructeur skill interactif (TDD guidé)
- Tableau de bord métriques (suivre économies tokens)
- Système vote communautaire skills

**Envie de contribuer ?** Voir [CONTRIBUTING_FR.md](./CONTRIBUTING_FR.md) ou ouvrir une issue !

---

<div align="center">

**⭐ Mettez une étoile si vous trouvez ce repo utile !**

**🔗 Partagez avec votre équipe pour répandre pratiques optimisation tokens**

**💬 Rejoignez discussions pour façonner futures skills**

</div>
