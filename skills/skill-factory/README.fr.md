# Skill Factory

**Meta-skill production-ready pour créer, valider et optimiser les skills Claude.**

Basé sur le [Guide Complet Anthropic pour Créer des Skills Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) (Février 2026).

## Ce Qu'il Fait

Skill Factory transforme des workflows, processus ou tâches répétitives en skills Claude fiables et portables suivant les meilleures pratiques officielles. Il gère le cycle de vie complet :

**Conception** → **Implémentation** → **Validation** → **Itération** → **Distribution**

## Fonctionnalités Clés

✅ **Suit les Patterns Officiels Anthropic**
- Divulgation progressive à 3 niveaux (frontmatter → SKILL.md → references/)
- Conception par catégorie (Création de Documents, Automatisation de Workflows, Enhancement MCP)
- Structure token-efficiente (<5,000 mots dans le fichier principal)

✅ **Package de Production Complet**
- Frontmatter YAML optimisé avec phrases de déclenchement
- Instructions structurées avec portes de validation
- Fichiers de référence pour divulgation progressive
- Scripts de validation pour cohérence
- Suites de tests (déclenchement, fonctionnel, performance)

✅ **Assurance Qualité**
- Validation automatisée (structure, sécurité, déclenchements)
- Tests de précision des déclenchements (cible >90%)
- Comparaison de performance baseline
- Processus de raffinement itératif

✅ **Prêt pour Distribution**
- Structure adaptée GitHub
- Instructions d'installation
- Templates de workflow CI/CD
- Gestion de versions

## Quand l'Utiliser

Utilisez Skill Factory quand vous devez :

- **Créer des skills production-ready** avec structure et validation appropriées
- **Auditer des skills existants** pour la qualité des déclenchements et meilleures pratiques
- **Générer des packages de skills complets** prêts pour distribution
- **Concevoir des skills par catégorie** : Création de documents, Automatisation de workflows, ou Enhancement MCP
- **Construire des suites de tests** pour tests de déclenchement et fonctionnels
- **Optimiser la performance des skills** (efficacité tokens, précision déclenchements)
- **Préparer des skills pour déploiement équipe** ou publication publique

**Ne pas utiliser pour :**
- Prototypage rapide → Utilisez `/skill-creator` à la place
- Tâches simples ponctuelles sans valeur de réutilisation
- Tâches générales de codage ou documentation

## Complémentaire à skill-creator

**skill-creator** (existant) : Prototypage rapide, skills simples, itération rapide  
**skill-factory** (nouveau) : Production-ready, testé, validé, prêt pour distribution

Pensez à skill-creator comme "mode croquis" et skill-factory comme "mode production".

## Installation

### Pour Claude Code

1. Copiez le dossier `skill-factory/` vers votre répertoire de skills Claude :
   ```bash
   cp -r skill-factory ~/.claude/skills/
   ```

2. Redémarrez Claude Code ou rafraîchissez les skills.

3. Vérifiez l'installation :
   ```bash
   ls ~/.claude/skills/skill-factory/
   # Devrait afficher : SKILL.md, references/, scripts/, tests/
   ```

### Pour Claude.ai

1. Zippez le dossier `skill-factory/` :
   ```bash
   zip -r skill-factory.zip skill-factory/
   ```

2. Uploadez via Paramètres > Capacités > Skills

3. Activez le skill dans le panneau des skills.

## Utilisation

### Créer un Nouveau Skill

```
"Use skill-factory to build a skill for sprint planning"
"Crée un skill production-ready pour configuration workspace Notion"
"Construis un skill pour générer des notes de version depuis git commits"
```

Skill Factory va :
1. Classifier le cas d'usage (Catégorie 1, 2, ou 3)
2. Choisir le pattern architectural
3. Concevoir un frontmatter optimal avec phrases de déclenchement
4. Générer un SKILL.md complet avec instructions
5. Créer des fichiers de référence pour divulgation progressive
6. Fournir un script de validation et des suites de tests
7. Packager pour distribution

### Réviser un Skill Existant

```
"Review this skill for trigger quality"
"Audite mon skill sprint-planning pour les meilleures pratiques"
"Vérifie pourquoi mon skill ne se déclenche pas de manière fiable"
```

Skill Factory va :
1. Valider la structure et la sécurité
2. Analyser la couverture des phrases de déclenchement
3. Vérifier la qualité des instructions
4. Identifier les problèmes d'efficacité tokens
5. Suggérer des améliorations spécifiques
6. Fournir une version révisée si demandé

### Optimiser un Skill

```
"Mon skill se déclenche trop souvent, corrige la description"
"Optimise ce skill pour l'efficacité tokens"
"Ajoute des suites de tests pour valider mon skill"
```

## Structure des Fichiers

```
skill-factory/
├── SKILL.md                          # Instructions principales du skill
├── README.md                         # Ce fichier (version anglaise)
├── README.fr.md                      # Ce fichier (version française)
├── references/                       # Niveau 3 de divulgation progressive
│   ├── skill-template.md            # Template réutilisable
│   ├── review-checklist.md          # Checklist d'audit qualité
│   ├── test-cases.md                # Guide de test & templates
│   ├── design-principles.md         # Patterns core d'Anthropic
│   ├── troubleshooting.md           # Problèmes courants & solutions
│   └── examples.md                  # Exemples de skills réels
├── scripts/                         # Validation & helpers
│   └── validate_skill.py            # Validateur de structure
└── tests/                           # Suites de tests (optionnel)
    ├── trigger-tests.md
    ├── functional-tests.md
    └── performance-baseline.md
```

## Démarrage Rapide

### Exemple 1 : Créer un Skill Simple

```
User: "Construis un skill pour convertir CSV en JSON"

Skill Factory:
1. "Ceci correspond à Catégorie 2 (Automatisation de Workflow). 
   Quelles phrases de déclenchement les utilisateurs diraient-ils ?"

User: "convertir CSV", "transformer CSV en JSON", "parser CSV"

Skill Factory:
2. [Génère un skill complet avec] :
   - Frontmatter avec phrases de déclenchement
   - Workflow étape par étape
   - Portes de validation
   - Gestion d'erreurs
   - Suite de tests

3. "Voici votre skill complet. Lancez la validation :"
   python scripts/validate_skill.py csv-to-json/
```

### Exemple 2 : Réviser un Skill Existant

```
User: "Mon skill ne se déclenche pas. Voici le frontmatter :"
---
name: project-helper
description: Aide avec les projets.
---

Skill Factory:
"❌ Problèmes trouvés :

1. Description trop vague (pas de phrases de déclenchement)
2. Portée trop large (quel type de projets ?)
3. Clause WHEN manquante

Correction suggérée :
---
name: agile-sprint-planner
description: Automatise la planification de sprint Agile incluant analyse 
de vélocité, création de tâches et assignation d'équipe. Utilisez quand 
l'utilisateur dit "planifier sprint", "sprint planning", "organiser 
itération", ou demande de "configurer le prochain sprint".
---
```

## Validation

Lancez le script de validation pour vérifier la qualité du skill :

```bash
cd votre-dossier-skill
python ../skill-factory/scripts/validate_skill.py .
```

Sortie attendue :
```
✅ Validation du skill RÉUSSIE
   ✅ SKILL.md trouvé
   ✅ Structure frontmatter valide
   ✅ Nom 'votre-skill' est en kebab-case valide
   ✅ Longueur description OK (287 chars)
   ✅ Description inclut langage de déclenchement
   ✅ Longueur contenu raisonnable (2,143 mots)
   ✅ Utilise divulgation progressive (liens vers references/)
   ✅ Nom dossier correspond au nom du skill
```

## Tests

### Tests de Déclenchement

Testez si votre skill se charge quand il le devrait :

```bash
# Cas positifs (devrait se déclencher)
"Construis un skill pour sprint planning"  → Devrait charger ✅
"Crée un skill Claude Code"                → Devrait charger ✅

# Cas négatifs (ne devrait PAS se déclencher)
"Quel temps fait-il ?"                     → Ne devrait PAS charger ✅
"Écris une fonction Python"                → Ne devrait PAS charger ✅
```

**Cible : >90% de précision**

### Tests Fonctionnels

Vérifiez que le skill produit des sorties correctes :

```bash
# Chemin heureux
Given: Utilisateur demande de créer un skill pour X
When: Skill exécute le workflow
Then: Package de skill complet généré
      Toutes les vérifications de validation passent
      Suites de tests créées
```

### Tests de Performance

Comparez avec la baseline (sans le skill) :

| Métrique | Baseline | Avec Skill | Amélioration |
|----------|----------|------------|--------------|
| Messages | 15-20 | 3-5 | -70% ✅ |
| Tokens | 12k-15k | 5k-7k | -55% ✅ |
| Temps | 8-12 min | 2-4 min | -70% ✅ |
| Erreurs | 2-4 | 0-1 | -80% ✅ |

## Exemples

Voir `references/examples.md` pour des exemples réels complets :

- **Catégorie 1 :** frontend-design, docx-creator
- **Catégorie 2 :** sprint-planning, release-notes-generator
- **Catégorie 3 :** sentry-code-review, notion-workspace-setup

## Dépannage

### Skill Factory ne se déclenche pas

**Problème :** Skill Factory ne se charge pas quand vous demandez de créer un skill

**Correction :** Essayez des phrases plus spécifiques :
- "Use skill-factory pour créer un skill pour X"
- "Construis un skill production-ready pour Y"
- "Génère un package de skill Claude complet"

### Le skill créé ne se déclenche pas

**Problème :** Le skill que vous avez créé ne se déclenche pas de manière fiable

**Correction :** Passez par le mode révision de Skill Factory :
```
"Review this skill for trigger quality"
```

Skill Factory auditera les phrases de déclenchement et suggérera des améliorations.

### Le script de validation échoue

**Problème :** `python scripts/validate_skill.py .` rapporte des erreurs

**Problèmes courants :**
1. Fichier pas nommé exactement `SKILL.md` (sensible à la casse)
2. Frontmatter manque des délimiteurs `---`
3. Nom pas en kebab-case (utiliser tirets, pas espaces/underscores)

Voir `references/troubleshooting.md` pour solutions détaillées.

## Ressources

### Documentation Incluse

- `references/skill-template.md` — Template réutilisable
- `references/review-checklist.md` — Guide d'audit qualité
- `references/test-cases.md` — Templates de tests
- `references/design-principles.md` — Patterns d'Anthropic
- `references/troubleshooting.md` — Problèmes courants
- `references/examples.md` — Exemples réels

### Ressources Externes

- [Guide Anthropic Skills (PDF)](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) — Guide officiel 33 pages
- [Documentation Anthropic Skills](https://docs.anthropic.com/skills) — Docs API
- [Dépôt d'Exemples de Skills](https://github.com/anthropics/skills) — Exemples publics

## Contribuer

Vous avez trouvé un problème ou avez une suggestion ?

1. Testez d'abord avec le script de validation : `python scripts/validate_skill.py .`
2. Vérifiez `references/troubleshooting.md` pour problèmes connus
3. Ouvrez une issue dans le dépôt avec :
   - Frontmatter du skill
   - Message d'erreur ou comportement inattendu
   - Étapes pour reproduire

## Licence

Licence MIT

## Auteur

Bertrand Brodeau ([@valorisa](https://github.com/valorisa))

Basé sur le Guide Complet Anthropic pour Créer des Skills Claude (Février 2026)

---

## Historique des Versions

- **v1.0.0** (2026-05-27)
  - Version initiale
  - Implémentation complète des patterns officiels d'Anthropic
  - Support des 3 catégories de skills
  - Suite complète de validation et tests
  - Package de distribution production-ready

---

**Besoin d'aide ?** Ouvrez une issue ou consultez le [guide de dépannage](references/troubleshooting.md).

🇺🇸 [English](README.md) | 🇫🇷 [Français](README.fr.md)
