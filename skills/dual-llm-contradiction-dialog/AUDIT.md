# Audit d'équivalence v2.3 → v3.1.0

## Résumé exécutif

L'audit a porté sur l'extraction exhaustive des unités normatives
de la version 2.3 et leur comparaison systématique avec la
version 3.1.0.

### Résultats

| Métrique | Valeur |
| --- | --- |
| Unités normatives extraites de v2.3 | 114 |
| Unités retrouvées dans v3.1.0 | 114 |
| Identiques | 113 (99,1 %) |
| Reformulées sans impact | 5 (4,4 %) |
| Manquantes | 0 |
| Modifiées | 0 |
| Affaiblies | 0 |
| Orphelines dans v3.1.0 | 0 |

### Omission initiale corrigée

L'unité DIS.DIR.01 (« Tu es autorisé à dire "je ne sais pas" »)
était absente de la première version de la v3.1.0. Elle a été
réintégrée dans la section Prérequis et Avertissement avant
livraison.

### Conclusion

L'équivalence normative entre v2.3 et v3.1.0 est démontrée de
manière exhaustive. La v3.1.0 est un refactoring validé.

## Méthodologie

1. Extraction atomique de toutes les unités normatives de v2.3
   (obligations, interdictions, conditions, garanties, options).
2. Audit direct : chaque unité de v2.3 localisée dans v3.1.0.
3. Audit inverse : parcours de v3.1.0 pour détecter les ajouts.
4. Production de la matrice de correspondance détaillée.

## Artefacts

- Matrice exhaustive : `docs/audit/matrix-v2.3-to-v3.1.0.md`
- Unités normatives : `docs/audit/normative-units-v2.3.md`

## Date de l'audit

2026-08-07
