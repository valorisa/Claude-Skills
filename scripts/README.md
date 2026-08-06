# Scripts de maintenance du dépôt

Ce dossier contient des utilitaires pour maintenir la qualité de la documentation du dépôt Claude-Skills.

## fix_markdownlint.py

### À quoi ça sert ?

Lors de l'importation de nouvelles skills depuis des dépôts externes, leurs fichiers *.md contiennent souvent des erreurs de formatage qui font échouer notre pipeline CI (markdownlint-cli2).

Bien que markdownlint possède une option --fix, celle-ci ne corrige qu'une partie des règles. Ce script Python corrige automatiquement les règles non auto-fixables les plus courantes :

- MD026 : ponctuation finale dans les titres (ex. « # Titre. » devient « # Titre »).
- MD032 : lignes vides manquantes autour des listes.
- MD034 : URLs nues, encapsulées entre chevrons.

### Prérequis

Python 3.6 ou plus récent (bibliothèque standard uniquement, rien à installer).

### Utilisation

Depuis la racine du dépôt, corriger un dossier entier (ex. une skill fraîchement clonée) :

    python3 scripts/fix_markdownlint.py skills/ma-nouvelle-skill/

Corriger un fichier unique :

    python3 scripts/fix_markdownlint.py skills/ma-skill/README.md

Corriger tout le dépôt :

    python3 scripts/fix_markdownlint.py .

### Workflow type après import d'une skill

1. Cloner la skill dans skills/ puis supprimer son .git imbriqué.
2. Lancer le script : python3 scripts/fix_markdownlint.py skills/nouvelle-skill/
3. Vérifier : npx -y markdownlint-cli2 "**/*.md"
4. Commiter et pousser.
