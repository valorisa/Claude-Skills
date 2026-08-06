# Task Observer

Skill de consignation asynchrone et low-cost des frictions et apprentissages.

## Principes de design

- Write fast, clean later : append-only pendant la tâche, consolidation
  mécanique et humaine différée.

- La machine fait la mécanique (timestamp via `date`, dossier via `mkdir -p`),
  le LLM ne fournit que le sens.

- Zéro vérification pré-écriture, zéro numérotation, zéro statut.

## Historique des versions

- V1 (original "Task Observer" de rebelytics) : concept excellent mais 40%
  du prompt dédié à la gestion de concurrence d'écriture. Sur-ingénierie.

- V2 : fire-and-forget mais orchestrateur externe fantôme et skill IA de
  ménage. Fuite vers l'hypothétique.

- V3 : triggers heuristiques internes mais capteurs non groundés (horloge,
  anthropomorphisme, biais négatif).

- V3.1 : trigger différé post-résolution, compteur de tool calls, trigger
  positif WIN, normalisation lexicale.

- Finale : timestamp estampé par le shell, `mkdir -p` inconditionnel,
  préfixes `DO:`/`DONT:`/`PREFER:`, critère de validation télémétrique.

## Crédits

Concept inspiré de "Task Observer" par Eoghan Henn (rebelytics), refondu par
revues d'architecture adversariales itératives (audits LLM_A).

## Limites connues

- Windows PowerShell natif : `date -u` indisponible (WSL/Git Bash ou `[DATE-NA]`).
- `sort -u` est un pré-filtre syntaxique ; la consolidation sémantique reste
  humaine.
