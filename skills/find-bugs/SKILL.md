# Find Bugs

Analyse un fichier pour détecter des bugs et propose des corrections.

## Trigger

Slash command: `/find-bugs`

Auto-détection : "cherche les bugs", "find bugs", "debug ce fichier", "quels bugs dans", "analyse ce fichier pour les erreurs", "bug hunt".

## Process

1. Identifier le fichier cible. Si l'utilisateur ne le précise pas, demander quel fichier analyser.
2. Lire le fichier avec Read.
3. Si pertinent, lancer les outils d'analyse statique disponibles (linter, type-checker, compilateur) via Bash pour collecter des signaux supplémentaires.
4. Analyser le code pour détecter les bugs : erreurs logiques, off-by-one, null/undefined non gérés, race conditions, fuites de ressources, mauvaise gestion d'erreurs, vulnérabilités de sécurité.
5. Présenter les résultats sous forme de liste numérotée. Pour chaque bug :
   - **Ligne(s)** : numéro(s) de ligne concerné(s)
   - **Problème** : description claire du bug
   - **Impact** : ce qui peut mal se passer
   - **Fix proposé** : le correctif sous forme de diff ou snippet
6. Demander à l'utilisateur : "Veux-tu que j'applique ces corrections ? (toutes / certaines / aucune)"
7. Appliquer uniquement les corrections confirmées via Edit.

## Constraints

- Ne jamais modifier le fichier sans confirmation explicite de l'utilisateur.
- Se concentrer sur les vrais bugs — pas de refactoring, pas de suggestions stylistiques, pas d'optimisations de performance sauf si elles causent un bug.
- Un fichier à la fois. Si l'utilisateur demande plusieurs fichiers, traiter séquentiellement en demandant confirmation pour chaque.
- Si aucun bug n'est trouvé, le dire clairement plutôt qu'inventer des problèmes.

## Output

Une liste numérotée des bugs avec explication et fix, suivie d'une proposition d'appliquer les corrections après accord de l'utilisateur.
