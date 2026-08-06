---
name: task-observer
description: Consigne frictions et apprentissages en cours de tâche.
  Triggers heuristiques internes, écriture append-only, zéro vérification,
  timestamp estampé par la machine.
---

# Task Observer (Version finale)

## Règle d'or

L'observation ne doit JAMAIS interrompre la tâche.
Tu écris APRÈS la résolution de l'événement, jamais pendant.
La machine estampe le temps ; tu ne fournis que le sens.

## Déclencheurs (quand observer)

### 1. CORRECTION (trigger différé)

Après avoir fourni avec succès une réponse corrigée (suite à une correction
utilisateur ou à ta propre erreur), consigne une ligne.
Pas pendant l'excuse. Après le fix.

### 2. RETRY

Si tu as eu besoin de 3 appels d'outils ou tentatives pour une étape qui
aurait dû en prendre un, consigne une ligne quand elle aboutit enfin.

### 3. WIN (trigger positif)

Si tu découvres une solution élégante, non-standard, ou un raccourci qui
évite une étape complexe, consigne une ligne.

### 4. PIVOT

Si tu abandonnes ta stratégie initiale pour une raison justifiée, consigne
une ligne quand la nouvelle stratégie a prouvé sa valeur.

## Quand NE PAS observer

- Typos, formatage, clarifications triviales
- Événements résolus du premier coup sans apprentissage

## Écriture (comment observer)

Utilise cette commande exacte. Elle est auto-portante : `mkdir -p` crée le
dossier si besoin (idempotent, aucun check préalable) et le shell estampe
l'heure :

    mkdir -p .task-observer && echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [TYPE] Contexte | Friction | REGLE" >> .task-observer/log.md

Les champs ne doivent contenir ni backticks ni `$`.

Si pas d'accès shell : utilise la date EXPLICITEMENT fournie dans ton
contexte système (date seule, sans heure).
Si ni l'un ni l'autre : écris `[DATE-NA]`.
Inventer une heure est interdit.

Zéro lecture préalable. Zéro déduplication. Zéro numérotation.

`TYPE` est exactement : `CORRECTION` | `RETRY` | `WIN` | `PIVOT`

Le champ `REGLE` commence EXACTEMENT par l'un de ces trois préfixes, suivi
d'une phrase impérative courte en anglais. Aucun autre mot avant :

    DO: ...
    DONT: ...
    PREFER: ...

## Exemples

L'utilisateur dit "non, je voulais dire ripgrep". Tu corriges, tu livres la
réponse corrigée, PUIS :

    mkdir -p .task-observer && echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [CORRECTION] file search | grep too slow | DO: use rg by default" >> .task-observer/log.md

Une commande docker échoue deux fois avant de trouver `--rm` :

    mkdir -p .task-observer && echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [RETRY] docker deploy | orphan containers | DO: always add --rm" >> .task-observer/log.md

Un seul `awk` remplace ton pipeline de 3 commandes :

    mkdir -p .task-observer && echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [WIN] log parsing | 3-cmd pipeline | PREFER: one targeted awk" >> .task-observer/log.md

## Maintenance (PAS une skill IA)

- Pré-filtre mécanique : `sort -u .task-observer/log.md`
- Les préfixes `DO:`/`DONT:`/`PREFER:` groupent les règles par catégorie au tri,
  ce qui rend la revue humaine triviale.

- Consolidation sémantique vraie : revue humaine hebdomadaire, ou sur
  demande ("synthétise mon log").

## Notes de portabilité et validation

- Le timestamp exige un shell POSIX/GNU (macOS, Linux, WSL, Git Bash).
  Sous Windows natif PowerShell : utiliser WSL/Git Bash ou `[DATE-NA]`.

- Critère d'acceptation : après 10 sessions, au moins 1 entrée par session
  en moyenne et au moins 50% des entrées jugées utiles en revue hebdo.
  Sinon : ajuster les déclencheurs. Jamais la mécanique d'écriture.
