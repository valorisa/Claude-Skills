---
name: github-standardization-process
description: "Automatic GitHub repo standardization at publication checkpoints with bilingual READMEs (EN/FR), CI linting, badges, and About configuration"
metadata: 
  node_type: memory
  type: process
  originSessionId: 40fb3600-9bc1-42ea-a0ef-2ca75a220c56
---

# GitHub Repository Standardization Process

Processus automatique de standardisation des repositories GitHub, déclenché aux checkpoints de publication.

**Why:** L'utilisateur veut une standardisation professionnelle et pédagogique de tous ses repos GitHub sans avoir à répéter les instructions à chaque fois. Ce processus s'applique automatiquement ou via skill manuelle.

**How to apply:** Détecter les triggers et proposer le processus complet si le repo n'est pas déjà standardisé.

## Automatic Triggers

### Phase 1: Pré-création du repo GitHub
Détecter ces phrases et proposer le processus AVANT git init :
- "on va (en) faire un repo GitHub de ce projet"
- "créons un repo GitHub"
- "je veux publier ça sur GitHub"
- "transformons ça en repo GitHub"

### Phase 2: Pré-publication (checkpoint)
Détecter ces phrases et vérifier la checklist de standardisation :
- "je vais publier sur GitHub"
- "push vers GitHub"
- "créer une PR"
- "git push origin"

**Action :** Vérifier automatiquement :
- ✅ README.md existe et suit le template standard ?
- ✅ README.fr.md existe ?
- ✅ `.github/workflows/markdown-lint.yml` existe ?
- ✅ `.markdownlint.json` configuré ?
- ✅ Zéro violations MarkdownLint ?

Si manquant → Proposer : "Ce repo n'est pas encore standardisé. Voulez-vous appliquer le processus de standardisation GitHub maintenant ?"

## Opt-Out Mechanism

Si l'utilisateur dit :
- "pas besoin du processus de standardisation ici"
- "skip la standardisation pour ce repo"
- "nul besoin du processus ici"

**Action :** Enregistrer l'exception en mémoire de **session uniquement** (ne plus proposer dans cette conversation, mais reproposer dans les futures sessions sur ce repo).

## Process Overview

```
Phase 0: Pre-Flight Check (silent)
  ↓
Phase 1: Repository Analysis (automatic)
  ↓
Phase 2: README.md EN (interactive collaboration)
  → Badges proposal & validation
  → About description (3 versions → choice)
  → 20 Topics (proposal → validation)
  → 13 Sections (one-by-one → validation)
  → Visual content (adaptive: CLI/library/app)
  ↓
Phase 3: README.fr.md (translation & validation)
  ↓
Phase 4: CI Markdown Linting
  → .markdownlint.json
  → .github/workflows/markdown-lint.yml
  → Local validation & fixes
  ↓
Phase 5: Finalization
  → Commit READMEs
  → GitHub About instructions
  → Push & verify CI
```

## Phase 0: Pre-Flight Check

**Si trigger détecté, vérifier silencieusement :**
1. Est-ce un repo Git ? (`git rev-parse --git-dir`)
2. README.md existe et suit le standard ?
3. README.fr.md existe ?
4. `.github/workflows/markdown-lint.yml` existe ?
5. `.markdownlint.json` existe ?
6. Violations MarkdownLint présentes ?

**Si tous les checks passent :** Skip (déjà standardisé)  
**Si au moins un check échoue :** Proposer le processus

## Phase 1: Repository Analysis (Automatic, Silent)

Scanner le repo pour détecter :

**Languages :**
- Extensions de fichiers (`.py`, `.go`, `.js`, `.rs`, etc.)
- Manifestes : `package.json`, `go.mod`, `Cargo.toml`, `requirements.txt`

**Frameworks & Dependencies :**
- Node.js : `package.json` → dependencies
- Python : `requirements.txt`, `pyproject.toml`
- Go : `go.mod`
- Rust : `Cargo.toml`

**Project Type :**
- CLI tool : `bin/`, `cmd/`, `main.go`, `__main__.py`, shebangs
- Library : `lib/`, `src/`, `index.js`, `__init__.py`
- Application : `app/`, `public/`, `templates/`
- Documentation : principalement `.md`, répertoire `docs/`

**Testing :**
- Fichiers tests : `*_test.go`, `test_*.py`, `*.spec.js`
- Frameworks : Jest, pytest, Go testing
- Coverage : `coverage/`, `.coverage`, `c.out`

**Containerization :**
- `Dockerfile`, `docker-compose.yml` présents ?

**CI/CD :**
- `.github/workflows/*.yml` présent ?

**License :**
- Détecter depuis `LICENSE`, `LICENSE.md`
- Type : MIT, Apache 2.0, GPL, etc.

**Output :** Base de connaissances interne pour les phases suivantes

## Phase 2: README.md (English) - Interactive

### Step 2.1: Badges Proposal

Générer une liste de badges contextuels basée sur l'analyse Phase 1 :

**Categories :**
- **Mandatory :** License, Primary Language
- **Contextual :** CI Status (si workflows), Docker (si Dockerfile), Tests (si suite détectée)
- **Optional :** Coverage, Platform, Version

**Format Shield.io :**
```markdown
[![Label](https://img.shields.io/badge/Label-Value-Color)](URL)
```

**Présentation :**
```
📛 Badges suggérés pour [Project Name]:
✓ License: MIT
✓ Language: Python 3.12+
✓ CI Status: GitHub Actions
✓ Docker: Ready
✓ Tests: 47 passed
? Coverage: 92%
? Version: v1.0.0

Voulez-vous garder tous ces badges ? Modifications ?
```

**User response :** Valider/ajuster

### Step 2.2: GitHub About Description (<350 chars)

Proposer **3 versions** optimisées :

**Version A - Technical :** Focus sur stack et fonctionnalités précises  
**Version B - Marketing :** Focus sur valeur ajoutée et problème résolu  
**Version C - Pedagogical :** Focus sur apprentissage et accessibilité

**Exemple :**
```
Version A (Technical) - 248 chars:
"High-performance CLI tool for automated Docker container security 
scanning using Trivy and Grype. Supports multi-arch builds, parallel 
scanning, SARIF output, GitHub Actions integration. Written in Go 1.23+."

Version B (Marketing) - 234 chars:
"Secure your Docker containers effortlessly. Automated vulnerability 
scanning with instant reports, CI/CD integration, and zero-config setup. 
Perfect for DevOps teams who value security without complexity."

Version C (Pedagogical) - 285 chars:
"Learn Docker security by doing. Beginner-friendly CLI tool that guides 
you through container vulnerability scanning step-by-step, explains CVEs 
in plain language, and teaches best practices. No prior security knowledge 
required."

Choisissez une version ou mixez des éléments.
```

**User response :** Sélectionner/mixer/custom

**Output :** Description finalisée <350 chars (idéalement 330-349)

### Step 2.3: 20 GitHub Topics

Générer 20 topics groupés par catégorie :

**Categories :**
- Languages (3-4 topics)
- Technologies (4-5 topics)
- Domain (4-5 topics)
- Ecosystem (3-4 topics)
- Audience/Purpose (2-3 topics)

**Exemple :**
```
🏷️ Topics suggérés (20 total):

[Languages] python, bash, powershell
[Technologies] docker, github-actions, cli, automation, security
[Domain] vulnerability-scanning, devops, container-security, trivy, grype
[Ecosystem] docker-security, ci-cd, sarif, sbom
[Audience] beginner-friendly, tutorial, learning

Validez-vous cette liste ? Modifications ?
```

**Rules :**
- Lowercase uniquement
- Hyphens (pas spaces/underscores)
- Max 50 chars par topic
- Aligné avec taxonomie GitHub

**User response :** Valider/modifier

### Step 2.4: README Sections (13 Standard Sections)

**Template standardisé (ordre fixe) :**

1. **Badges** (validés en 2.1)
2. **Description courte + contexte** (2-3 paragraphes)
3. **Table des matières** (auto-générée)
4. **Pourquoi ce projet ?** (Problem statement + motivation)
5. **Fonctionnalités** (Feature list avec descriptions)
6. **Prérequis** (System requirements, dependencies, versions)
7. **Installation** (Instructions step-by-step)
8. **Usage/Exemples** (Cas d'usage communs avec code)
9. **Configuration** (Variables d'environnement, fichiers config)
10. **Tests** (Comment lancer la suite de tests)
11. **Contribution** (Comment contribuer, standards)
12. **License** (Type + lien vers LICENSE file)
13. **Auteur** (valorisa + lien GitHub)

**Workflow collaboratif :**
Pour chaque section :
1. Claude propose un draft basé sur l'analyse Phase 1
2. User valide/ajuste
3. Claude passe à la section suivante

**Questions clés :**
- Section 4 : "Quel problème résout ce projet ?"
- Section 5 : "Fonctionnalités manquantes dans l'analyse ?"
- Section 7 : "Étapes spéciales d'installation ?"
- Section 8 : "3 cas d'usage les plus courants ?"
- Section 9 : "Variables d'environnement importantes ?"
- Section 10 : "Comment lancer les tests ?"

### Step 2.5: Visual Content (Mix Adaptatif)

**Basé sur le type de projet détecté :**

**CLI Tool :**
- Screenshots de terminal (commandes + résultats)
- Optionnel : Asciinema recordings

**Library :**
- Exemples de code exhaustifs avec commentaires ligne par ligne
- API documentation (signatures, paramètres)

**Application :**
- Screenshots UI (écrans clés, workflows)
- Exemples de code (intégration)
- Optionnel : Diagrammes d'architecture

**Action :** Demander assets visuels si applicable

**Organisation images :**
- Stockage : `docs/images/` ou `assets/images/`
- Noms descriptifs : `installation-output.png`, `scan-results.png`
- Références : `![Alt](docs/images/file.png)`

### Step 2.6: Finalization README.md

1. Compiler toutes les sections validées
2. Générer table des matières avec anchor links
3. Valider liens internes
4. Ajouter language switcher en haut :
   ```markdown
   🇺🇸 [English](README.md) | 🇫🇷 [Français](README.fr.md)
   ```
5. Présenter README.md complet pour revue finale

**User response :** Approuver ou ajuster

## Phase 3: README.fr.md (French) - Translation

### Step 3.1: Full Translation

Traduire README.md en français en préservant :
- Structure (mêmes sections, même ordre)
- Formatting (headers, listes, code blocks, liens)
- Termes techniques en anglais (code, commandes, noms d'outils)

**Keep in English :**
- Code snippets, commands, variable names
- URLs, GitHub usernames
- Acronymes techniques (CLI, API, CI/CD)
- Noms d'outils (Docker, npm, pip)

**Translate to French :**
- Prose, descriptions, explications
- Headers de sections
- Items de listes (sauf code)
- Alt text d'images

**Tone :** Maintenir le ton pédagogique en français

### Step 3.2: French README Review

Présenter README.fr.md complet avec highlights sur sections ambiguës

**User response :** Valider ou ajuster

### Step 3.3: Cross-Language Links

Ajouter switcher dans les deux fichiers :

```markdown
🇺🇸 [English](README.md) | 🇫🇷 [Français](README.fr.md)
```

## Phase 4: CI Markdown Linting

### Step 4.1: Create `.markdownlint.json`

**Configuration stricte + exceptions courantes :**

```json
{
  "default": true,
  "MD013": false,
  "MD033": false
}
```

**Rationale :**
- `MD013`: Disable line length (URLs longues, code blocks)
- `MD033`: Allow inline HTML (badges Shield.io, image sizing)

### Step 4.2: Create GitHub Actions Workflow

**File :** `.github/workflows/markdown-lint.yml`

```yaml
name: Markdown Lint

on:
  push:
    paths:
      - '**.md'
  pull_request:
    paths:
      - '**.md'

jobs:
  markdown-lint:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run MarkdownLint
        uses: DavidAnson/markdownlint-cli2-action@v16
        with:
          globs: '**/*.md'
```

**Behavior :**
- Triggers : push/PR sur `*.md`
- Scope : Tous les `*.md` du repo
- Failure : Pipeline fail si violations
- Success : Green checkmark si zéro violations

### Step 4.3: Local Validation & Correction

**Action :**
1. Lancer MarkdownLint localement sur tous `*.md`
2. Reporter les violations catégorisées

**Classification :**

**Simple (Auto-Fix) :**
- MD009: Trailing spaces → Strip
- MD010: Hard tabs → Convert to spaces
- MD012: Multiple blank lines → Reduce to 1
- MD022: Header spacing → Add blank lines
- MD032: List spacing → Add blank lines

**Delicate (Consult User) :**
- MD001: Header level skip → Structural issue ?
- MD025: Multiple H1 → Quel H1 garder ?
- MD033: Inline HTML in prose → Rewrite as Markdown ?

**Process :**
1. Auto-fix simple violations
2. Présenter delicate violations avec options
3. User choisit action
4. Re-run linter
5. Répéter jusqu'à zéro violations

### Step 4.4: Commit Linting Config

```bash
git add .markdownlint.json .github/workflows/markdown-lint.yml
git commit -m "Add Markdown linting CI with strict rules

- Configure MarkdownLint with exceptions for MD013/MD033
- Add GitHub Actions workflow for automated validation
- Validate on push/PR for any *.md file changes

Co-Authored-By: Claude Sonnet 4.5 (1M context) <noreply@anthropic.com>"
```

## Phase 5: Finalization

### Step 5.1: Commit README Files

```bash
git add README.md README.fr.md
git commit -m "Add comprehensive bilingual README (EN/FR)

- Pedagogical documentation for novice users
- 13 standard sections (badges, installation, usage, etc.)
- Visual content adapted to project type
- Cross-language navigation links
- Zero MarkdownLint violations

Co-Authored-By: Claude Sonnet 4.5 (1M context) <noreply@anthropic.com>"
```

### Step 5.2: GitHub About Configuration Instructions

Fournir instructions step-by-step pour configurer About section :

```
📝 GitHub About Section Configuration:

1. Navigate to: https://github.com/valorisa/[repo-name]

2. Click ⚙️ icon next to "About"

3. Fill in:
   Description (XXX/350 chars): [texte optimisé]
   Website: [URL du repo]
   Topics (20): [liste comma-separated]

4. Check boxes: ☑ Releases ☑ Packages

5. Save changes

✅ GitHub About configured!
```

### Step 5.3: Push & Verify CI

```bash
git push origin main
```

Vérifier workflow CI passe :
```bash
gh run list --workflow=markdown-lint.yml --limit 1
```

**Expected :** ✓ Markdown Lint (green checkmark)

**Si CI fail :** Investiguer et corriger

**User notification :**
```
✅ Standardization Complete!

Files committed:
  - README.md (English)
  - README.fr.md (French)
  - .markdownlint.json
  - .github/workflows/markdown-lint.yml

Pushed to: https://github.com/valorisa/[repo-name]
CI Status: ✅ Passing

Next steps:
  1. Configure GitHub About section (instructions above)
  2. Review README rendering on GitHub
```

## Manual Invocation via Skill

L'utilisateur peut aussi invoquer manuellement : `/standardize-github-repo`

**Action :** Lancer immédiatement le processus complet (Phases 0-5) sur le repo courant, sans attendre les triggers.

## Related Memory

Lié à [[feedback_github_repo_standards]] qui définit les standards obligatoires.

## Implementation Notes

- Process documentation complète : [[../../docs/superpowers/specs/2026-05-27-github-standardization-process-design.md]]
- Skill Claude Code disponible : valorisa/Claude-Skills/skills/standardize-github-repo/
