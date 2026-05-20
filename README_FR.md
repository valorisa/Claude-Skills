# Collection de Skills Claude

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-1-blue.svg)](./skills)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple.svg)](https://claude.ai/code)
[![TDD](https://img.shields.io/badge/méthodologie-TDD-green.svg)](https://fr.wikipedia.org/wiki/Test_driven_development)
[![PRs Bienvenues](https://img.shields.io/badge/PRs-bienvenues-brightgreen.svg)](./CONTRIBUTING.md)
[![Maintenu](https://img.shields.io/badge/Maintenu%3F-oui-green.svg)](https://github.com/valorisa/claude-skills/graphs/commit-activity)

> **Skills communautaires pour [Claude Code](https://claude.ai/code) visant à améliorer la productivité, optimiser l'utilisation des tokens et améliorer les workflows de développement.**

[🇬🇧 English version](./README.md)

---

## 📋 Table des Matières

- [Qu'est-ce qu'une Skill Claude?](#-quest-ce-quune-skill-claude)
- [Skills Disponibles](#-skills-disponibles)
- [Installation](#-installation)
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

## 📦 Skills Disponibles

### 🚀 rescue-tokens

**Prévient l'épuisement des tokens et les rate limits via 9 patterns d'optimisation.**

#### Le Problème

Les utilisateurs rencontrent des erreurs "rate limit" non pas parce qu'ils ont envoyé trop de messages, mais parce qu'ils **brûlent des tokens silencieusement** :
- Conversations éternelles (contexte gonflé)
- Sortie verbeuse (les explications coûtent des tokens)
- Mauvais choix de modèle (Opus 4.7 pour tâches simples = coût 5x)
- Surcharge de plugins MCP (overhead à chaque message)
- Fichiers coûteux (PDF, images = 10-50x tokens)

#### La Solution

`rescue-tokens` détecte et corrige 9 patterns de gaspillage de tokens **automatiquement**.

#### Quand l'Utiliser

**La skill s'active quand UNE OU PLUSIEURS conditions présentes (logique OR) :**
- ⚠️ Avertissements de rate limit
- ⚠️ Contexte ≥40% plein
- ⚠️ Plan à $20-$100/mois après 14h
- ⚠️ Conversation >90 minutes
- ⚠️ 5+ plugins MCP chargés
- ⚠️ Utilisateur dit "ne perds pas le contexte"
- ⚠️ Opus 4.7 pour tâches simples

**Note :** Chaque flag SEUL déclenche le mode urgence. Vous n'avez pas besoin de toutes les conditions.

#### Ce qu'Elle Fait

**Matrice d'Actions** (Pas de confirmation utilisateur) :
- Contexte 40-70% → `/compact` faits clés
- Contexte >70% → Nouvelle conversation, résumé 3 phrases
- Rate limit + urgence → Sous-agent en Sonnet immédiatement
- Opus 4.7 pour CRUD → Changer vers Sonnet
- PDF/image → Demander extraits texte
- 5+ MCPs → Désactiver inutilisés

**Discipline de Réponse Sous Pression :**
- <100 mots total
- PAS de sections markdown
- PAS de blocs "Raisonnement :"
- PAS de tableaux
- Verbes d'action seulement : "Changé vers Sonnet. Démarre OAuth."

**Rationalisations Contrées :**
La skill contre explicitement 9 rationalisations d'agents :
- "Laisse-moi expliquer pourquoi" → Les explications brûlent des tokens
- "Je vais ajouter sections Raisonnement" → Énoncer décision seulement
- "Les tableaux aident à comparer" → Tableaux coûtent 5x tokens
- "L'utilisateur veut le contexte" → 80% est du poids mort
- ...et 5 de plus

#### Résultats Vérifiés

**Résultats tests TDD (7 scénarios) :**
- **Baseline :** 950 mots moyenne (agent sans skill)
- **Phase GREEN :** 525 mots (45% amélioration)
- **Phase REFACTOR :** 97 mots (90% amélioration)
- **Rationalisations :** 0 dans tests finaux

[📖 Documentation Complète](./skills/rescue-tokens/SKILL.md)

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
