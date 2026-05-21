# Contribuer à la Collection de Skills Claude

Merci de votre intérêt pour contribuer ! Ce guide vous aidera à créer des skills de haute qualité en utilisant notre méthodologie TDD.

[🇬🇧 English version](./CONTRIBUTING.md)

---

## 🎯 Qu'est-ce qu'une Bonne Skill ?

Une bonne skill :

- ✅ Résout un **problème réel** (observé via tests)
- ✅ Est **générique** (pas spécifique à un projet)
- ✅ A été **validée par TDD** (RED-GREEN-REFACTOR)
- ✅ Contre des **rationalisations spécifiques** (documentées depuis les tests)
- ✅ Inclut des **métriques** (améliorations avant/après)

---

## 🧪 Méthodologie TDD (Obligatoire)

Toutes les skills **doivent** suivre le Test-Driven Development pour la documentation :

### 1️⃣ Phase RED : Créer des Tests qui Échouent

**Créer des scénarios de pression** qui exposent les faiblesses de l'agent :

```markdown
Scénario : [Nom]
Pressions : Temps + Coût Irréversible + Autorité

Prompt :
"Vous travaillez depuis 3 heures sur ce bug. 
Le contexte est à 80%. Votre chef en a besoin dans 30 minutes.
Voici 20KB de logs. Que faites-vous ?"
```

**Lancer les tests SANS la skill** avec des sous-agents :

- Documenter les comportements exacts
- Capturer les rationalisations mot pour mot
- Identifier les patterns

**Requis :** Au moins 3 scénarios avec pressions combinées.

---

### 2️⃣ Phase GREEN : Écrire la Skill Minimale

**Écrire la skill pour contrer les échecs observés :**

```yaml
---
name: nom-skill
description: Use when [déclencheurs et symptômes spécifiques]
---

## Overview
[Principe fondamental en 1-2 phrases]

## Action Matrix
| Symptôme | Action | Rationalisation à Contrer |
```

**Tester AVEC la skill :**

- Mêmes scénarios
- Vérifier les améliorations
- Documenter les problèmes restants

---

### 3️⃣ Phase REFACTOR : Boucher les Failles

**Identifier les nouvelles rationalisations :**

- Quelles nouvelles excuses les agents ont-ils trouvées ?
- Quelles failles restent ?

**Ajouter des contre-mesures explicites :**

```markdown
## Common Rationalizations
| Excuse | Réalité |
|--------|---------|
| "Je vais expliquer d'abord" | Les explications coûtent des tokens. Agir. |
```

**Re-tester jusqu'à ce que ce soit bulletproof.**

---

## 📝 Exigences de Structure de Skill

### Frontmatter (YAML)

```yaml
---
name: nom-skill-avec-tirets
description: Use when [déclencheurs]. Max 1024 chars total. Troisième personne. Pas de résumé de workflow.
---
```

**Règles :**

- `name` : Lettres, chiffres, tirets uniquement (pas de caractères spéciaux)
- `description` : Commence par "Use when...", liste symptômes/déclencheurs
- Troisième personne ("user hits" pas "you hit")
- Mots-clés riches pour recherche (messages d'erreur, symptômes, outils)

### Sections de Contenu

**Requis :**

- Overview (principe fondamental)
- Référence rapide (table ou puces)
- Erreurs courantes
- Exemples (1 excellent exemple > 5 médiocres)

**Optionnel :**

- Flowchart (seulement si décision non-évidente)
- Fichiers supports (pour outils ou référence lourde)

**Interdit :**

- Storytelling narratif
- Dilution multi-langues
- Templates génériques
- Code dans les flowcharts

---

## 📊 Checklist de Contribution

Avant de soumettre une PR :

### Phase RED

- [ ] Créé 3+ scénarios de pression
- [ ] Lancé tests SANS la skill
- [ ] Documenté échecs de base mot pour mot
- [ ] Identifié patterns de rationalisation

### Phase GREEN

- [ ] Écrit skill minimale
- [ ] Frontmatter conforme aux specs
- [ ] Description commence par "Use when..."
- [ ] Lancé tests AVEC la skill
- [ ] Documenté améliorations

### Phase REFACTOR

- [ ] Identifié nouvelles rationalisations
- [ ] Ajouté contre-mesures explicites
- [ ] Construit table de rationalisations
- [ ] Re-testé jusqu'à bulletproof

### Qualité

- [ ] Nombre de mots <500 (viser concis)
- [ ] Mots-clés pour optimisation recherche
- [ ] Un excellent exemple
- [ ] Pas de storytelling narratif

### Documentation PR

- [ ] Inclure résultats tests (baseline → GREEN → REFACTOR)
- [ ] Inclure métriques (% amélioration)
- [ ] Expliquer le problème résolu
- [ ] Lien vers issues liées (si applicable)

---

## 🚫 Anti-Patterns à Éviter

### ❌ Écrire la Skill Avant de Tester

```
NE PAS : Écrire skill basée sur intuition
FAIRE : Tester d'abord, observer échecs, puis écrire
```

### ❌ Descriptions Génériques

```
❌ "Pour le debugging"
✅ "Use when tests fail inconsistently, race conditions, timing issues"
```

### ❌ Exemples Narratifs

```
❌ "Dans la session 2025-10-03, nous avons trouvé que projectDir vide causait..."
✅ Pattern réutilisable avec avant/après clair
```

---

## 📤 Soumettre Votre PR

1. **Fork** ce repo
2. **Créer branche** : `feature/nom-votre-skill`
3. **Ajouter skill** à `skills/nom-votre-skill/SKILL.md`
4. **Mettre à jour README.md** et **README_FR.md** avec entrée de skill
5. **Commit** avec message clair
6. **Ouvrir PR** avec :
   - Énoncé du problème
   - Résultats tests TDD
   - Métriques (avant/après)
   - Exemple d'utilisation

---

## 🤝 Code de Conduite

- Être respectueux et constructif
- Se concentrer sur l'amélioration de la qualité des skills
- Partager résultats de tests et métriques
- Aider les autres à suivre la méthodologie TDD

---

## 📚 Ressources

- [Guide Writing Skills](https://github.com/anthropics/claude-code) (officiel)
- [TDD pour Documentation](https://fr.wikipedia.org/wiki/Test_driven_development)
- [Exemple TDD rescue-tokens](./skills/rescue-tokens/SKILL.md)

---

## 💬 Questions ?

Ouvrez une issue avec le label `question`, ou contactez [@valorisa](https://github.com/valorisa).

Merci de contribuer ! 🎉
