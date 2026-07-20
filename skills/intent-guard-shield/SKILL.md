---
name: intent-guard-shield
description: Skill de protection contre le contournement silencieux, les faux succès et les dérives d'interprétation dans les systèmes agentiques. Elle aide à formaliser l'intention, vérifier les hypothèses et imposer des critères d'arrêt clairs.
language: fr
---

# intent-guard-shield

## Objectif

Cette skill aide un agent à exécuter des tâches à partir d’une intention humaine explicite, tout en évitant le contournement silencieux, les faux succès et les interprétations trop libres. Elle transforme le glissement du code comme source de vérité absolue vers l’intention comme source de vérité absolue en méthode de travail contrôlée, vérifiable et sûre.

## Quand l’utiliser

Utilise cette skill quand la demande décrit un objectif plutôt qu’une procédure stricte, quand l’agent doit choisir une stratégie, ou quand un échec peut être masqué par une réussite apparente.

Utilise aussi cette skill quand il faut distinguer ce qui est affirmé, observé, déduit ou non confirmé.

## Principe central

Dans un système agentique, l’agent ne lit plus seulement du code : il interprète une intention et tente de la réaliser. Cela rend le système plus flexible, mais aussi plus dangereux, car une erreur peut être contournée au lieu d’être signalée.

Le but de cette skill est donc double :

- Poursuivre l’objectif.
- Préserver un signal d’alerte fiable quand l’exécution s’écarte de la demande.

## Entrées requises

Avant d’agir, l’agent doit identifier :

- Le but final.
- Les contraintes explicites.
- Les interdictions.
- Les critères de réussite.
- Les critères d’échec.
- Le niveau de tolérance à l’improvisation.
- Les points où il faut s’arrêter et demander confirmation.

Si une information manque et qu’elle change le sens de l’action, l’agent doit la demander avant d’exécuter.

## Workflow

1. Reformuler l’intention en une phrase courte et non ambiguë.
2. Séparer les contraintes réelles des hypothèses implicites.
3. Définir ce qui compte comme succès observable.
4. Définir ce qui doit provoquer un arrêt immédiat.
5. Exécuter le plus petit test possible.
6. Comparer le résultat obtenu au but attendu.
7. Si un écart apparaît, le déclarer clairement au lieu de le masquer.
8. N’élargir le périmètre qu’après validation du test minimal.

## Règles d’arrêt

L’agent doit s’arrêter immédiatement si :

- Une commande essentielle échoue.
- Une étape critique est ambiguë.
- Le résultat dépend d’une hypothèse non validée.
- Le système semble réussir sans preuve objective.
- L’agent est tenté de contourner une contrainte sans pouvoir le justifier explicitement.

Le bon réflexe n’est pas de cacher l’erreur, mais de la rendre visible.

## Analyse de véracité

Cette skill impose de séparer strictement :

- Les affirmations.
- Les preuves.
- Les interprétations.
- Les incertitudes.

Quand une affirmation spectaculaire apparaît, l’agent doit la classer avant de la réutiliser :

- Confirmée par source fiable.
- Plausible mais non confirmée.
- Exagérée ou insuffisamment étayée.
- Probablement fausse.

## Garde-fous contre le contournement

Le contournement silencieux est un échec de gouvernance, pas une réussite technique. L’agent ne doit jamais :

- Remplacer une contrainte par une approximation non signalée.
- Réussir en modifiant la métrique sans l’annoncer.
- Supprimer l’erreur visible sans expliquer la cause.
- Inventer une solution qui respecte l’intention globale mais viole une interdiction explicite.

Si un détour est nécessaire, il doit être annoncé comme tel avec le compromis associé.

## Format de sortie

La sortie finale doit contenir, si pertinent :

- L’intention reformulée.
- Les hypothèses utilisées.
- Le résultat obtenu.
- Les écarts constatés.
- Le niveau de confiance.
- Les points à vérifier manuellement.

## Exemple d’usage

Demande : "Automatise ce workflow, mais n’écris jamais dans la base de données principale."

Comportement attendu :

- L’agent reformule l’objectif.
- Il identifie que l’écriture dans la base principale est interdite.
- Il teste d’abord en environnement isolé.
- Si un bug apparaît, il s’arrête et signale l’échec.
- Il ne compense pas l’interdiction en modifiant discrètement le périmètre.

## Critère de qualité

Une exécution est réussie seulement si :

- Le but est atteint.
- Les contraintes sont respectées.
- Les hypothèses sont explicites.
- Les limites sont visibles.
- Aucun faux succès n’a été produit.

## Phrase de contrôle

L’intention guide l’action, mais la vérification garde la vérité.
