# 🧮 Maths Olympiad Skill

Ce skill implémente un workflow multi-agents rigoureux pour résoudre et vérifier des problèmes de mathématiques de niveau compétition. Il est conçu pour maximiser la précision conditionnelle, en s'assurant que chaque solution fournie est mathématiquement solide, correctement interprétée et élégamment présentée.

## 🌟 Fonctionnalités Clés

- **Résolution Parallèle Multi-Agents** : Lancement de 8 à 12 agents "solveurs" en parallèle avec des angles d'attaque variés (invariants, cas extrêmes, induction, etc.) pour explorer l'espace du problème de manière exhaustive.
- **Politique d'Outils Stricte (No-Web)** : Privilégie le raisonnement pur. L'accès au web est strictement interdit pour éviter toute "triche" ou fuite de la solution. Le calcul est limité à un "Mode Profond" avec des bornes strictes (arithmétique modulaire, petits cas).
- **Vérification Adversariale** : Utilisation d'agents "vérificateurs" à contexte vierge, aveugles aux traces de réflexion du solveur et aux opinions des autres vérificateurs. Emploie des vérifications en 5 passes avec des critères spécifiques (ex: détection de problèmes ouverts célèbres, tautologies, ou lemmes généraux faux).
- **Vote Asymétrique et Sortie Précoce** : Nécessite 4 votes `HOLDS` (Valide) pour confirmer une preuve, mais seulement 2 votes `HOLE FOUND` (Faille trouvée) pour la réfuter. Le processus s'arrête dès que l'issue est décidée pour économiser les ressources de calcul.
- **Abstention Calibrée** : Préfère honnêtement répondre "pas de solution confiante" avec des résultats partiels plutôt que de deviner et fournir une réponse fausse avec assurance.
- **Passe de Présentation** : Sépare la correction de l'élégance. Un agent dédié réécrit la preuve vérifiée dans le format LaTeX le plus simple et le plus beau possible, en fusionnant ou extrayant les lemmes si nécessaire.

## 🔄 Vue d'Ensemble du Workflow

1. **Vérification de l'Interprétation** : Identifie la lecture attendue du problème pour éviter les pièges des interprétations "trop faciles" (spécification-gaming).
2. **Phase de Résolution** : Les agents parallèles itèrent (résoudre → s'améliorer → se vérifier → corriger) en utilisant un raisonnement pur.
3. **Nettoyage du Contexte** : Les traces de réflexion, les doutes et les faux départs sont supprimés pour éviter que le vérificateur ne soit biaisé par la longueur du raisonnement (biais d'acquiescement).
4. **Vérification Adversariale** : De nouveaux agents attaquent les preuves nettoyées en utilisant des vérifications mathématiques ciblées.
5. **Révision / Mode Profond** : Si des failles sont trouvées, des agents "réviseurs" tentent de les corriger. Si les solveurs standards s'abstiennent, un agent en "Mode Profond" utilise le calcul local borné pour débloquer la situation.
6. **Présentation** : La preuve finale vérifiée est formatée en LaTeX propre et compilée en PDF.

## 📂 Structure des Références

Le skill s'appuie sur plusieurs fichiers de référence pour ses invites (prompts) adversariales et de présentation :
- `references/solver_heuristics.md` — Angles d'attaque initiaux pour les solveurs.
- `references/verifier_patterns.md` — Les 12 vérifications adversariales (ex: Pattern #40 pour les lemmes d'une ligne).
- `references/adversarial_prompts.md` — Invites prêtes à l'emploi pour les vérificateurs.
- `references/presentation_prompts.md` — Invites d'embellissement et modèles LaTeX.
- `references/model_tier_defaults.md` — Configuration par modèle (Haiku, Sonnet, Opus).

## ⚠️ Contraintes d'Utilisation

- **Aucun Accès Web** : Les outils `WebSearch`, `WebFetch` ou tout accès réseau sont strictement prohibés pour maintenir l'intégrité du processus de résolution.
- **Calcul Borné** : Les récursions doublement exponentielles ou les forces brutes non bornées (ex: $n > 30$) sont interrompues. Le travail symbolique ou modulo $2^m$ doit être privilégié.
- **Isolation de Contexte** : Un solveur ne peut jamais vérifier sa propre solution. Chaque vérificateur pense être le premier à évaluer la preuve.
