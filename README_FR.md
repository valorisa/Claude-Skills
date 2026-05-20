# Collection de Skills Claude

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-1-blue.svg)](./skills)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple.svg)](https://claude.ai/code)
[![TDD](https://img.shields.io/badge/méthodologie-TDD-green.svg)](https://fr.wikipedia.org/wiki/Test_driven_development)
[![PRs Bienvenues](https://img.shields.io/badge/PRs-bienvenues-brightgreen.svg)](./CONTRIBUTING.md)
[![Maintenu](https://img.shields.io/badge/Maintenu%3F-oui-green.svg)](https://github.com/valorisa/claude-skills/graphs/commit-activity)

[🇬🇧 English version](./README.md)

Skills communautaires pour [Claude Code](https://claude.ai/code) visant à améliorer la productivité, optimiser l'utilisation des tokens et améliorer les workflows de développement.

## 📦 Skills Disponibles

### 🚀 rescue-tokens

**Prévient l'épuisement des tokens et les limitations de débit via 9 patterns d'optimisation.**

**À utiliser quand :**
- Avertissements de rate limit apparaissent
- Le contexte dépasse 40%
- Conversations longues (>90 minutes)
- Mauvais choix de modèle (Opus pour des tâches simples)
- Surcharge de plugins MCP

**Ce que ça fait :**
- Détecte 9 patterns de gaspillage de tokens
- Force des réponses concises sous pression (<100 mots)
- Fournit une Matrice d'Actions pour décisions immédiates
- Contre 9 rationalisations courantes

**Résultats :** 90% de réduction de verbosité, élimine les problèmes de rate limit

[📖 Documentation complète](./skills/rescue-tokens/SKILL.md)

---

## 🎯 Installation

### Option 1 : Installer une Skill Individuelle

```bash
# Copier la skill dans votre répertoire Claude skills
cp -r skills/rescue-tokens ~/.claude/skills/
```

### Option 2 : Cloner Toute la Collection

```bash
# Cloner ce repo
git clone https://github.com/valorisa/claude-skills.git

# Lier les skills à Claude
ln -s "$(pwd)/claude-skills/skills/"* ~/.claude/skills/
```

### Vérifier l'Installation

```bash
# Dans Claude Code CLI
/skills list

# Devrait afficher : rescue-tokens
```

---

## 🧪 Méthodologie de Développement des Skills

Toutes les skills de cette collection suivent le **Test-Driven Development (TDD)** pour la documentation :

1. **Phase RED :** Créer des scénarios de pression, observer les échecs de l'agent sans la skill
2. **Phase GREEN :** Écrire la skill minimale pour contrer les rationalisations observées
3. **Phase REFACTOR :** Identifier les nouvelles failles, ajouter des contre-mesures explicites, re-tester

Voir [le journal de développement de rescue-tokens](./skills/rescue-tokens/SKILL.md) pour un exemple de TDD.

---

## 🤝 Contribuer

Vous voulez contribuer une skill ?

1. **Testez d'abord :** Créez des scénarios de pression, documentez les échecs de base
2. **Suivez le TDD :** Cycle RED → GREEN → REFACTOR
3. **Documentez les rationalisations :** Quelles excuses les agents ont-ils utilisées ?
4. **Soumettez une PR :** Incluez les résultats des tests et les métriques

---

## 📜 Licence

Licence MIT - libre d'utilisation, de modification et de partage.

---

## 🙏 Crédits

Créé par [@valorisa](https://github.com/valorisa)

Inspiré par la méthodologie [Anthropic's Superpowers](https://github.com/anthropics/claude-code).
