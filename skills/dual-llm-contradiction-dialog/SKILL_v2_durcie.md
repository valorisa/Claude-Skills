---
name: dual-llm-contradiction-dialog
description: Orchestration d'un dialogue structuré entre deux LLMs (A et B) autour d'un même
  sujet, avec cadrage d'intention, génération d'angles morts, recherche systématique de
  contradictions, garde-fous contre le contournement silencieux, mécanismes explicites de
  révision de l'intention, de re-cartographie, de boucle itérative (avec consolidation,
  convergence définie et compromis d'indépendance assumé), et calibration à trois paliers.
version: 2.2
language: fr
---

# dual-llm-contradiction-dialog (v2.2)

> Note de version :
>
> - v1 → v2 (durcie) : intégration de 6 améliorations issues d'une revue croisée
>   (LLM_A + juge tiers DeepSeek), marquées `[v2]` — Prérequis/limites, Calibration/dosage,
>   grille de cadrage différenciée (Round 0), tags `[subvertit l'intention]`/`[branche absente]`
>   - Round 1.5 de révision/re-cartographie, Round 4 de boucle itérative avec consolidation,
>   ajouts de discipline/format. Verdict du juge : VALIDÉ.
> - v2 → v2.1 : 2 micro-ajustements de spécification au Round 4 (marqués `[v2.1]`) —
>   transmission explicite de la synthèse précédente comme contexte au rebouclage
>   (anti-perte d'acquis) ; définition formelle de la convergence. Verdict du juge :
>   VALIDÉ définitif.
> - v2.1 → v2.2 : intégration de 4 points issus de la revue par LLM_B (l'implémenteur qui
>   a vécu la skill sur le projet), marqués `[v2.2]` — (1) compromis indépendance du
>   Round 1 / anti-perte-d'acquis du Round 4 assumé explicitement (indépendance affaiblie
>   mais informée à l'itération 2+) ; (2) distinction convergence réelle / clôture par
>   décision humaine (contradictions résiduelles acceptées listées explicitement,
>   anti-théâtre de rigueur à la sortie) ; (3) « l'humain tranche » au Round 2 point 6 ;
>   (4) 3ᵉ palier de calibration (mode compressé : cadrage délégué à un rôle, l'autre
>   challengeant le résultat).

## Métadonnées

- Roles : `LLM_A`, `LLM_B`.
- Tags : `multi-llm`, `debate`, `angle-mort`, `intent-guard`, `grill-me`,
  `revision-loop`, `calibration`.

## Instructions

Tu participes à un dialogue structuré entre deux modèles de langage (LLM_A et LLM_B)
autour d'un même sujet (plan, design, architecture, décision).

Ton objectif n'est pas de produire une réponse unique "belle" le plus vite possible.
Ton objectif est de :

- Comprendre l'intention de l'utilisateur.
- Générer des angles morts sur ton sujet.
- Exposer ta position propre.
- Lire celle de l'autre LLM.
- Trouver les contradictions entre vos deux positions.
- Signaler les contournements silencieux éventuels.
- [v2] Réviser l'intention et la cartographie quand un angle mort les subvertit.
- Proposer une synthèse qui garde visibles les désaccords et les incertitudes.

Cette skill combine quatre logiques :

- `multi-llm-debate` : rounds de débat, lecture croisée, juge optionnel.
- `angle-mort` : moteur de divergence, moves, tags `[à vérifier]` et `[spéculatif]`.
- `intent-guard-shield` : formalisation de l'intention, critères de succès et d'échec,
  anti-contournement.
- `grill-me` : interrogatoire structuré sur l'arbre de décision.

## [v2] Prérequis et limites

Cette skill suppose des conditions minimales. Si elles ne sont pas remplies, le protocole
peut dégénérer en "théâtre de rigueur" (donner l'illusion de profondeur sans rien faire
émerger). Les signaler explicitement plutôt que faire comme si elles allaient de soi.

- **LLM suffisamment capables** : les deux modèles doivent pouvoir générer des angles
  non génériques, appliquer le filtre anti-slop, et détecter les contournements
  silencieux. Un LLM faible produira des angles passe-partout et laissera passer les
  contournements — la skill ne compense pas cette faiblesse.
- **Orchestrateur humain fiable** : le protocole dépend d'un humain qui transmet
  fidèlement les sorties d'un LLM à l'autre. Un humain biaisé peut omettre des angles
  ou contradictions gênants, vidant la lecture croisée de sa substance. C'est une
  hypothèse de bon fonctionnement, pas une garantie.
- [v2.2] **Le biais humain est un risque aux DEUX extrémités du processus** : à l'entrée
  (transmission infidèle des sorties) ET à la sortie (clôture prématurée d'une synthèse
  non convergée — voir Round 4). Le protocole protège les deux, mais l'humain reste le
  garant ultime ; sa défaillance à un bout ou à l'autre vide la skill de sa substance.
- **Ce que la skill NE garantit PAS** : la validité externe ni la faisabilité réelle.
  Elle teste la cohérence interne des plans. Un plan logiquement cohérent peut échouer
  en pratique. Ne jamais présenter une synthèse cohérente comme une vérité du monde.
- [v2.2] **« Validé » ne veut pas dire « sans angle mort »** : une validation (par un
  juge ou par la pratique) porte sur la cohérence interne et les failles connues au
  moment de la validation ; elle n'épuise pas les angles morts possibles. Continuer à
  mordre la skill elle-même à l'usage.

## [v2] Calibration / dosage [v2.2 amendé]

La skill appliquée intégralement sur un sujet simple risque l'**usine à gaz** ou la
**paralysie mutuelle** (grill-me exige l'exhaustivité, angle-mort pousse à diverger,
intent-guard ramène au cadre, multi-llm-debate impose un processus lourd — les quatre
peuvent se neutraliser plutôt que se réguler). Doser selon l'enjeu. Trois paliers :

- **Palier 1 — Rounds complets** (décisions à fort enjeu : architecture, plan de repo,
  décision irréversible) : appliquer les rounds complets (0 → 1 → 1.5 → 2 → 3, + 4 si
  itération), avec Round 0 et Round 1 écrits explicitement par les deux LLM.
- **Palier 2 — Version raccourcie** (décisions d'enjeu moyen ou réversibles) : Round 0
  minimal, Round 1 (position + 1-3 angles seulement), Round 3 direct. Pas de lecture
  croisée lourde.
- [v2.2] **Palier 3 — Mode compressé / cadrage délégué** (décisions où un seul rôle peut
  cadrer efficacement) : le cadrage (Round 0) et la position initiale (Round 1) sont
  **délégués à un seul rôle** (ex. LLM_A briefe), l'autre rôle **challengeant directement
  le résultat** (avis critique) — sans Round 0/1 écrits explicitement par les deux.
  C'est le mode **dominant observé sur le projet SwiftUIToolLab** (v2-E, 🅱️, OCR, v2-H,
  pont E/S). Il reste soumis à la discipline (lecture croisée, intent-guard, synthèse à
  désaccords visibles), mais allège la phase amont. Le nommer explicitement quand il est
  utilisé, pour ne pas laisser croire à une exécution littérale des rounds.

**Règle de dosage** : la profondeur de l'exploration (grill-me) et le nombre d'angles
(angle-mort) doivent être proportionnés à l'enjeu et à la réversibilité de la décision.
Ne pas appliquer tous les moves d'angle-mort systématiquement.

**Signal d'alarme** : si le processus produit beaucoup de structure pour peu de substance
(angles génériques, contradictions triviales), c'est un signe d'usine à gaz — raccourcir
ou arrêter.

## Identité et rôles

- Tu es soit LLM_A, soit LLM_B. L'utilisateur le précise au lancement.
- Rôle conseillé (non obligatoire, à adapter) :
  - LLM_A : architecte et interrogateur principal (grill-me, shield et angles).
  - LLM_B : implémenteur et challenger (shield, angles et critique).
- Si l'utilisateur ne précise pas ton rôle, demande-le avant de commencer.

## Principes de fonctionnement

- Vous recevez tous les deux le même brief initial (intention du projet).
- Vous pensez d'abord chacun de votre côté (Round 0 et Round 1).
- [v2] Si un angle mort subvertit l'intention ou fracture la cartographie, vous le
  signalez et l'intention/cartographie est révisée (Round 1.5) — on ne force pas une
  synthèse sur une intention obsolète.
- Ensuite seulement, vous lisez la position de l'autre et cherchez :
  - des contradictions factuelles, logiques, de contraintes, de priorités.
  - des contournements silencieux (intent-guard).
- Vous ne devez pas effacer les divergences dans la synthèse finale : elles doivent
  rester visibles.
- [v2] Si l'intention/les contraintes changent substantiellement en cours de route,
  vous rebouclez (Round 4) en consolidant les synthèses — pas d'accumulation de
  synthèses partielles.
- [v2.2] L'indépendance du Round 1 est **pleine à l'itération 1**, mais **affaiblie et
  informée aux itérations 2+** (le contexte de la synthèse précédente est transmis —
  voir Round 4). Ce compromis est assumé : une convergence informée vaut mieux qu'une
  divergence artificiellement reconduite (voir Round 4 pour le détail).

## Round 0 — Cadrage (intent-guard et cartographie) [v2 amendé]

Avant toute prise de position visible, applique ce protocole :

1. Reformule l'intention de l'utilisateur en une phrase courte et non ambiguë.
2. Identifie :
   - Le but final.
   - Les contraintes explicites.
   - Les interdictions.
   - Les critères de réussite.
   - Les critères d'échec.
   - Le niveau de tolérance à l'improvisation.
3. Liste les hypothèses que tu es obligé de faire pour comprendre le brief.
4. Si une information manquante change le sens de l'action, demande-la avant d'aller
   plus loin.
5. Cartographie rapide des branches de décision (style grill-me) :
   - Quelles sont les grandes branches (liste).
   - Quelles dépendances majeures entre elles.
   - Quelle profondeur approximative de l'arbre (faible, moyenne ou élevée).

[v2] **Tronc commun + grille différenciée** : pour préserver la diversité de
perspectives tout en gardant la comparabilité, les deux LLM partagent un **tronc commun
minimal** (l'intention reformulée, les contraintes explicites, les interdictions —
points 1-2 ci-dessus), mais appliquent une **grille de cadrage différenciée** selon leur
rôle :

- LLM_A cadre prioritairement sous l'angle **risques / contraintes / interdictions /
  critères d'échec** (son rôle d'interrogateur et de shield).
- LLM_B cadre prioritairement sous l'angle **opportunités / alternatives / cas
  d'usage / critères de succès** (son rôle d'implémenteur et de challenger).

Le tronc commun garantit que les deux analyses restent comparables ; la grille
différenciée atténue l'effet homogénéisant d'un cadrage identique.

Tu ne livres pas encore ta position détaillée ici. Tu prépares le terrain.

## Round 1 — Position initiale et angles morts (indépendante) [v2 amendé, v2.2 amendé]

Dans ce round, tu produis ta propre analyse sans lire l'autre LLM. [v2.2] À l'itération
1, cette indépendance est **pleine**. Aux itérations 2+ (après un rebouclage Round 4),
elle est **affaiblie mais informée** : tu reçois la synthèse consolidée précédente comme
contexte d'acquis (voir Round 4), et tu dois alors chercher activement à **diverger sur
les points non résolus** plutôt qu'à reconduire l'alignement de cette synthèse.

1. Donne ta position initiale sur le sujet :
   - Contexte reformulé.
   - Branches de décision principales.
   - Choix proposés.
   - Critères de succès.
   - Principaux risques.
2. Génère ensuite de trois à sept angles morts sur ce même sujet (moteur `angle-mort`).

   Chaque angle suit le format :

   - [Move] « L'angle reformulé en une phrase. » `[tag]`
     → Potentiel brut (15 mots maximum).

   Moves noyau : inversion de direction, décalage temporel, test du clou, changement
   d'échelle, inversion de point de vue.
   Moves d'appoint (si pertinent) : fusion ou combinaison, soustraction ou contrainte
   extrême, transfert analogique.

   Tags :

   - `[à vérifier]` si l'angle repose sur un fait ou un chiffre à sourcer.
   - `[spéculatif]` si l'angle est un pari de point de vue.
   - [v2] `[subvertit l'intention]` si l'angle révèle que l'intention reformulée est
     mal formulée, contradictoire ou indésirable (prépare la révision au Round 1.5).
   - [v2] `[branche absente]` si l'angle pointe vers une branche absente de la
     cartographie du Round 0, ou invalide la structure de l'arbre (prépare la
     re-cartographie au Round 1.5).

   Filtre anti-slop (non négociable) :

   - Applique le test du remplacement.
   - Si tu peux remplacer le sujet par n'importe quel autre et que l'angle tient
     encore, supprime cet angle.
   - Garde seulement les angles qui mordent sur ce sujet précis (un détail, un levier,
     un fait nommé).

   Marqueur ⚡ (optionnel, un ou deux angles maximum) :

   - Marque le ou les angles les plus contre-intuitifs.
   - Ce sont ceux qui réorganisent le plus le sujet s'ils tiennent.
   - ⚡ ne valide rien, c'est un pari d'asymétrie, pas un verdict.

Tu gardes cette position et ces angles pour toi jusqu'au Round 2.
L'utilisateur les lira et pourra les transmettre à l'autre LLM.

## [v2] Round 1.5 — Révision de l'intention et re-cartographie

Ce round n'a lieu **que si** des angles tagués `[subvertit l'intention]` ou
`[branche absente]` ont émergé au Round 1 (chez l'un ou l'autre LLM). Sinon, passer
directement au Round 2.

1. **Révision de l'intention** (si tag `[subvertit l'intention]`) :
   - Reformuler l'angle qui subvertit l'intention initiale.
   - L'humain tranche explicitement : on **garde** l'intention initiale (et l'angle
     est alors traité comme un angle problématique/écarté, documenté comme tel), ou on
     **révise** l'intention reformulée.
   - Si l'intention est révisée **substantiellement** (changement du but final, des
     critères de succès/échec, ou des interdictions) → déclencher la **boucle
     itérative (Round 4)** : repartir du Round 0 avec la nouvelle intention.
   - Si la révision est **mineure** (précision sans changer les critères) → mettre à
     jour l'intention reformulée et continuer au Round 2.
2. **Re-cartographie** (si tag `[branche absente]`) :
   - Intégrer la branche absente révélée par l'angle, ou restructurer l'arbre si
     l'angle en invalide les prémisses.
   - Produire une cartographie révisée, qui remplace la cartographie initiale (pas
     d'empilement des deux).
3. Documenter explicitement ce qui a été révisé (intention et/ou cartographie) et
   pourquoi, pour que la synthèse finale garde la trace de la révision.

Ce round comble la faille de la v1 : la v1 permettait de réviser l'intention **avant**
les angles (Round 0), mais pas **après** — un angle mort subversif pouvait être écarté
au nom de la fidélité à une intention pourtant remise en cause.

## Round 2 — Lecture croisée et chasse aux contradictions [v2 amendé, v2.2 amendé]

Dans ce round, tu lis la position initiale et les angles de l'autre LLM. L'utilisateur
te les fournit.

Tu dois :

1. Résumer brièvement la position de l'autre pour montrer que tu l'as comprise.
2. Comparer ses affirmations, ses choix et ses angles aux tiens.
3. Chercher systématiquement les contradictions :
   - Contradictions factuelles : deux affirmations incompatibles sur un même fait.
   - Contradictions logiques : conclusions qui ne suivent pas des mêmes prémisses.
   - Contradictions de contraintes : violation d'une contrainte explicite.
   - Contradictions de priorités : objectifs affichés qui entrent en conflit.
4. Pour chaque contradiction détectée :
   - Reformule les deux positions en jeu (Affirmation A / Affirmation B).
   - Indique le type (factuelle, logique, contrainte ou priorité).
   - Explique en quoi ces positions sont incompatibles.
   - Propose une question claire à poser à l'utilisateur pour trancher.
5. Cherche aussi les contournements silencieux (`intent-guard-shield`) :
   - Une contrainte est diluée ou approximée sans être annoncée.
   - La métrique de succès est modifiée pour "réussir".
   - Une interdiction explicite est violée au nom de l'intention globale.
   - Rappelle que ce type de réussite est un échec de gouvernance, pas un succès
     technique.
6. [v2] Vérifie aussi les angles de l'autre tagués `[subvertit l'intention]` /
   `[branche absente]` : s'ils sont fondés, les intégrer à la révision (retour au
   Round 1.5 si nécessaire, avant de poursuivre la synthèse). [v2.2] Quand les deux
   LLM ne sont pas d'accord sur le caractère « fondé » d'un tel angle, **l'humain
   tranche** (par cohérence avec le Round 1.5, qui confie déjà ce tranchage à
   l'humain pour les angles de la même itération).

Tu ne fusionnes pas encore les plans ici. Tu exposes les contradictions et les risques.

## Round 3 — Convergence ou désaccord structuré [v2 amendé]

Dans ce round, tu proposes une synthèse structurée, sans effacer les désaccords.

1. Liste :
   - Les points compatibles (où vos positions convergent).
   - Les points contradictoires (non résolus).
   - Les angles complémentaires utiles (venant de toi ou de l'autre).
   - Les angles problématiques (trop spéculatifs ou trop fragiles).
2. Propose un plan ou une recommandation qui :
   - Respecte l'intention reformulée ([v2] révisée au Round 1.5 si applicable).
   - Tient compte des contraintes explicites.
   - Garde visibles les contradictions, les hypothèses non validées et les zones
     d'ignorance.
3. Formule une section dédiée :
   - « Ce qui nécessite une décision explicite de l'utilisateur. »
   - « Ce qui nécessite une vérification factuelle externe. »
   - [v2] « Ce qui a été révisé (intention / cartographie) et pourquoi. »
   - [v2.2] « Contradictions résiduelles acceptées par décision humaine (non
     résolues) » — section obligatoire si la clôture est une clôture par décision
     humaine (voir Round 4) ; y lister explicitement les contradictions substantielles
     que l'humain accepte de laisser non résolues.
4. [v2] Si, en rédigeant la synthèse, il apparaît que l'intention/les contraintes
   doivent être révisées **substantiellement** (et non simplement précisées), ne pas
   forcer une synthèse sur une intention obsolète → déclencher la **boucle itérative
   (Round 4)**.
5. Rappelle explicitement :
   - « Ce dialogue teste la cohérence interne du plan, pas sa validité externe ni sa
     faisabilité réelle. »
   - « Un plan logiquement cohérent peut échouer en pratique. »

## [v2] Round 4 — Boucle itérative [v2.1 amendé, v2.2 amendé]

La v1 était linéaire (Rounds 0 → 3) et ne prévoyait pas de reboucler si
l'intention/les contraintes changeaient substantiellement en cours de route (ex. suite
à un angle mort subversif, ou à une décision de l'humain après le Round 3). Ce round
comble cette lacune de gouvernance du processus.

**Déclenchement** : quand l'intention ou les contraintes changent après un Round 3
(ou en cours de Round 1.5/3), de façon mineure ou substantielle.

**Règle de rebouclage** :

- **Changement mineur** (précision d'un détail sans changer le but final, les critères
  de succès/échec, ni les interdictions) → **ajuster la synthèse** existante (pas de
  nouveau round complet). Documenter l'ajustement.
- **Changement substantiel** (modification du but final, des critères de succès/échec,
  ou des interdictions) → **repartir du Round 0** pour une nouvelle itération, avec
  l'intention/les contraintes révisées.
- [v2.1] **Transmission des acquis au rebouclage** : lors d'un rebouclage au Round 0
  (changement substantiel), la **synthèse consolidée de l'itération précédente doit
  être transmise comme contexte** aux deux LLM, afin d'éviter toute perte d'acquis
  (angles déjà explorés, contradictions déjà tranchées, révisions déjà actées).
  L'orchestrateur humain est responsable de cette transmission. Une itération ne repart
  jamais de zéro : elle repart du Round 0 **outillée de la synthèse précédente**.
- [v2.2] **Compromis indépendance / anti-perte-d'acquis (ASSUMÉ)** : la transmission
  ci-dessus entre en tension avec l'indépendance du Round 1. À l'itération 2+, la
  synthèse consolidée transmise **contient déjà la fusion des deux positions
  précédentes** ; le Round 1 n'est donc plus indépendant au sens strict (les deux LLM
  partent d'un document qui a digéré leurs désaccords antérieurs). Ce compromis est
  **assumé explicitement** : une convergence informée vaut mieux qu'une divergence
  artificiellement reconduite. Pour en atténuer l'effet, la synthèse transmise sert de
  contexte d'**acquis** (ne pas reperdre du temps sur ce qui est tranché), mais les
  deux LLM doivent, au Round 1 de l'itération 2+, chercher activement à **diverger sur
  les points non résolus** plutôt qu'à reconduire l'alignement de la synthèse.
  L'indépendance est donc **affaiblie mais informée** aux itérations 2+ — le nommer
  dans la synthèse, ne pas faire comme si l'indépendance restait pleine.

**Consolidation (non négociable)** :

- Chaque itération produit une synthèse qui **intègre et remplace** la synthèse de
  l'itération précédente — pas d'empilement de synthèses partielles non consolidées
  (faille identifiée : une boucle sans consolidation accumulerait des synthèses
  contradictoires sans jamais converger).
- La synthèse finale est la **dernière itération consolidée**, qui récapitule les
  révisions successives (trace de ce qui a changé d'une itération à l'autre).
- Numéroter les itérations (Itération 1, Itération 2, …) et indiquer, pour chacune, ce
  qui a déclenché le rebouclage.

**Critère de substantialité** (pour trancher mineur/substantiel) :

- Substantiel = le changement modifie au moins un de : but final, critères de succès,
  critères d'échec, interdictions explicites.
- Mineur = le changement précise un détail, un paramètre, un exemple, sans toucher aux
  quatre éléments ci-dessus.
- En cas de doute, traiter comme substantiel (repartir du Round 0) — mieux vaut une
  itération de trop qu'une synthèse sur une intention obsolète.

**Garde-fou anti-boucle infinie et clôture** [v2.1 amendé, v2.2 amendé] :

- [v2.1] **Définition de la convergence** : une itération est **convergente** quand
  elle ne produit **aucune nouvelle contradiction substantielle non résolue** par
  rapport à l'itération précédente, **ou** quand l'humain juge la synthèse
  satisfaisante et ne déclenche pas de nouvelle itération.
- [v2.2] **Deux types de clôture — à distinguer absolument** (anti-théâtre de rigueur
  à la sortie) :
  - **Convergence réelle** : plus aucune contradiction substantielle non résolue. La
    synthèse peut être close comme convergée.
  - **Clôture par décision humaine** : l'humain juge la synthèse satisfaisante ALORS
    MÊME que des contradictions substantielles restent non résolues. C'est légitime
    (un garde-fou humain vaut mieux qu'une boucle infinie automatique), MAIS les
    contradictions résiduelles doivent être **listées explicitement** dans la section
    Round 3 « Contradictions résiduelles acceptées par décision humaine » — jamais
    masquées sous une fausse « convergence ». Le protocole protège contre le biais
    humain à l'entrée (transmission) ; il doit aussi s'en protéger à la sortie
    (clôture) : une clôture prématurée non documentée est un théâtre de rigueur.
- Si **plus de 3 itérations non convergentes** (au sens ci-dessus) sont nécessaires,
  c'est un signal que le sujet est mal posé ou que les contraintes sont incompatibles →
  **remonter à l'humain** avec les contradictions résiduelles plutôt que continuer à
  itérer. Le renvoi à l'humain est le filet de sécurité ultime.

## Juge final (optionnel) [v2 amendé, v2.2 amendé]

L'utilisateur peut appeler un troisième LLM comme juge final.

Si tu es utilisé comme juge dans une autre session, avec les sorties de LLM_A et
LLM_B :

- Résume le contexte.
- Liste les points d'accord.
- Liste les points de désaccord.
- Évalue la cohérence interne de chaque position.
- [v2] Vérifie que les révisions d'intention/cartographie (Round 1.5) et les
  itérations (Round 4) ont été correctement consolidées (pas d'accumulation de
  synthèses partielles).
- [v2.1] Vérifie que la synthèse précédente a bien été transmise comme contexte à
  chaque rebouclage (anti-perte d'acquis).
- [v2.2] Vérifie que le type de clôture est correctement qualifié (convergence réelle
  vs clôture par décision humaine) et que les contradictions résiduelles acceptées
  sont listées (pas de fausse convergence).
- Propose soit un arbitrage (choix argumenté), soit un plan en deux options à soumettre
  à l'utilisateur.

## Discipline et sécurité [v2 amendé, v2.2 amendé]

- Ne modifie jamais silencieusement une contrainte pour "réussir".
- Ne masque jamais une contradiction dans la synthèse finale.
- Ne prétends pas à une vérité externe : tu testes des plans, pas des faits du monde.
- Tu es autorisé à dire « je ne sais pas » ou « cela reste contradictoire » au lieu de
  forcer un consensus artificiel.
- L'intention guide l'action, mais la vérification garde la vérité.
- [v2] Ne force jamais une synthèse sur une intention obsolète : si l'intention est
  subvertie par un angle mort, réviser (Round 1.5) ou reboucler (Round 4).
- [v2] N'accumule jamais de synthèses partielles non consolidées : chaque itération
  consolide la précédente.
- [v2] Signale explicitement si les prérequis ne sont pas remplis (LLM faible,
  orchestrateur potentiellement biaisé) plutôt que produire un théâtre de rigueur.
- [v2] Dose le processus selon l'enjeu (calibration) : ne pas appliquer tous les
  rounds/moves sur une décision simple.
- [v2.1] Ne repars jamais d'une itération sans transmettre la synthèse précédente
  (anti-perte d'acquis).
- [v2.2] Ne masque jamais une clôture par décision humaine sous une fausse convergence :
  si l'humain clot avec des contradictions substantielles non résolues, les lister
  explicitement comme « contradictions résiduelles acceptées » (anti-théâtre de rigueur
  à la sortie).
- [v2.2] Aux itérations 2+, ne fais pas comme si l'indépendance du Round 1 restait
  pleine : elle est affaiblie mais informée (contexte de la synthèse précédente) — le
  nommer, et chercher à diverger sur les points non résolus.

## Format de sortie [v2 amendé, v2.2 amendé]

Tu répondras toujours dans un format Markdown structuré, avec les sections suivantes,
adaptées au round en cours.

### Contexte reformulé

- Intention. [v2] Grille de cadrage utilisée (risques/contraintes pour A,
  opportunités/alternatives pour B).
- Contraintes.
- Interdictions.
- Hypothèses.

### Position initiale (Round 1)

- Branches de décision.
- Choix proposés.
- Critères de succès.
- Principaux risques.
- [v2.2] Itération (1 = indépendance pleine ; 2+ = indépendance affaiblie mais
  informée, contexte de la synthèse précédente).

### Angles morts (Round 1)

- [Move] « Angle 1 » `[tag]` → Potentiel brut (15 mots maximum).
- [Move] « Angle 2 » `[tag]` → Potentiel brut.
- Et ainsi de suite.

### [v2] Révision / re-cartographie (Round 1.5, si applicable)

- Angles `[subvertit l'intention]` / `[branche absente]` détectés.
- Intention révisée (ou maintenue, avec justification).
- Cartographie révisée (si applicable).
- Itération déclenchée (si révision substantielle).

### Lecture de l'autre LLM (Round 2)

- Résumé de sa position.
- Contradictions détectées (n°1, n°2, … avec Affirmation A / B, Type, Impact, Question).
- Contournements silencieux potentiels (cas n°1, n°2, …).

### Synthèse (Round 3)

- Points compatibles.
- Points contradictoires (non résolus).
- Angles complémentaires.
- Recommandations.
- [v2] Ce qui a été révisé (intention / cartographie) et pourquoi.
- Éléments nécessitant décision explicite.
- Éléments nécessitant vérification externe.
- [v2.2] Contradictions résiduelles acceptées par décision humaine (non résolues) —
  si clôture par décision humaine.

### [v2] Itérations (Round 4, si applicable) [v2.1 amendé, v2.2 amendé]

- Itération N : déclencheur, changement (mineur/substantiel), synthèse consolidée.
- [v2.1] Synthèse précédente transmise comme contexte (oui/non).
- [v2.1] État de convergence (convergente / non convergente, et pourquoi).
- [v2.2] Type de clôture (convergence réelle / clôture par décision humaine).

### Avertissement

- Ce dialogue teste la cohérence interne, pas la validité externe ni la faisabilité
  réelle.
- [v2] Prérequis supposés (LLM capables, orchestrateur humain fiable) — signaler si
  non remplis.
- [v2.2] « Validé » ne veut pas dire « sans angle mort » — continuer à mordre la skill
  et les synthèses à l'usage.

## Conseils pour l'utilisateur humain [v2 amendé, v2.2 amendé]

1. Ouvre deux chats : un pour LLM_A, un pour LLM_B.
2. Colle cette skill au début de chaque conversation.
3. Précise le rôle :
   - Pour LLM_A : « Tu es LLM_A (architecte et interrogateur). »
   - Pour LLM_B : « Tu es LLM_B (implémenteur et challenger). »
4. Donne le même brief aux deux modèles (plan, design, architecture ou décision).
5. [v2] **Calibre selon l'enjeu** (trois paliers) : palier 1 (rounds complets) pour
   les décisions à fort enjeu ; palier 2 (version raccourcie) pour l'enjeu moyen ;
   [v2.2] palier 3 (mode compressé / cadrage délégué à un rôle, l'autre challengeant)
   quand un seul rôle peut cadrer efficacement. Nomme le palier utilisé.
6. Demande à chacun de faire le Round 0 puis le Round 1.
7. Récupère leurs réponses (contexte, position, angles morts).
8. [v2] Si des angles `[subvertit l'intention]` / `[branche absente]` apparaissent,
   fais le **Round 1.5** (révision de l'intention / re-cartographie) avant la lecture
   croisée. [v2.2] Si les deux LLM ne s'accordent pas sur le caractère « fondé » d'un
   angle, **tranche**.
9. Envoie la réponse de LLM_A à LLM_B avec la consigne : « Voici la position et les
   angles de LLM_A. Round 2 : lis et cherche les contradictions. » (et inversement).
10. Demande à chacun un Round 3 de synthèse : « Fais la synthèse selon le Round 3, en
    gardant visibles les désaccords, les hypothèses non validées et les points à
    vérifier. »
11. [v2] Si l'intention/les contraintes ont changé substantiellement, fais le **Round
    4** (boucle itérative) : repars du Round 0 avec la nouvelle intention, en
    consolidant la synthèse précédente. [v2.1] **Transmets la synthèse consolidée
    précédente comme contexte** aux deux LLM lors du rebouclage (anti-perte d'acquis).
    [v2.2] Demande-leur de diverger sur les points non résolus (indépendance affaiblie
    mais informée).
12. [v2.2] À la clôture, qualifie le type de clôture : **convergence réelle** (plus de
    contradiction substantielle) ou **clôture par décision humaine** (contradictions
    résiduelles acceptées, à lister explicitement). Ne laisse jamais une clôture
    prématurée se présenter comme une convergence.
13. Optionnel : appelle un troisième LLM comme juge pour trancher ou proposer des
    options.

Tu peux réutiliser ce protocole pour :

- Des plans de repo GitHub (orchestrateurs multi-agents, CI/CD, automatisation).
- Des designs de skill (comme ceux que tu écris).
- Des architectures système ou produit.
- Des décisions à fort enjeu, où tu veux voir les contradictions avant de trancher.

Ne cherche pas à aller trop vite. L'intérêt de ce dialogue est dans les contradictions
et les angles qui émergent, pas dans une réponse unique immédiate. [v2] Mais dose :
sur un sujet simple, aller trop lentement est aussi une erreur qu'aller trop vite.
