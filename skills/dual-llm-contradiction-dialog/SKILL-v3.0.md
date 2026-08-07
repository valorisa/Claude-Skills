---
name: dual-llm-contradiction-dialog
description: >-
  Orchestration d'un dialogue structuré entre deux LLMs (A et B)
  autour d'un même sujet, avec cadrage d'intention,
  génération d'angles morts, recherche systématique de
  contradictions, garde-fous contre le contournement silencieux,
  mécanismes explicites de révision de l'intention,
  de re-cartographie, de boucle itérative avec consolidation,
  convergence définie, compromis d'indépendance assumé,
  séquencement anti-court-circuit et filtre de pertinence des
  acquis, calibration à trois paliers avec protection
  anti-ancrage, et juge comme générateur d'angles morts.
version: 3.0.0
language: fr
---

# dual-llm-contradiction-dialog (v3.0.0)

## Métadonnées

- Rôles : `LLM_A`, `LLM_B`.
- Tags :
  `multi-llm`, `debate`, `angle-mort`, `intent-guard`,
  `revision-loop`, `calibration`, `grill-me`.

## Introduction

Ce document spécifie la skill
`dual-llm-contradiction-dialog`.

La version 3.0.0 est un refactoring documentaire de la version 2.3.
Le comportement protocolaire reste strictement équivalent à la v2.3.
Aucun mécanisme n'est ajouté, supprimé ou modifié.

Le protocole est normatif.
Les annexes contiennent l'historique, les justifications de
conception, les cas particuliers et le guide utilisateur.

## Objectif

Tu participes à un dialogue structuré entre deux modèles de langage
(`LLM_A` et `LLM_B`) autour d'un même sujet :
plan, design, architecture ou décision.

Ton objectif n'est pas de produire une réponse unique « belle »
le plus vite possible.

Ton objectif est de :

- comprendre l'intention de l'utilisateur ;
- générer des angles morts sur le sujet ;
- exposer ta position propre ;
- lire la position de l'autre LLM ;
- trouver les contradictions entre les deux positions ;
- signaler les contournements silencieux éventuels ;
- réviser l'intention et la cartographie quand un angle mort
  les subvertit ;
- proposer une synthèse qui garde visibles les désaccords et les
  incertitudes.

Cette skill combine quatre logiques :

- `multi-llm-debate` : rounds de débat, lecture croisée,
  juge optionnel ;
- `angle-mort` : moteur de divergence, moves, tags
  `[à vérifier]` et `[spéculatif]` ;
- `intent-guard-shield` : formalisation de l'intention,
  critères de succès et d'échec, anti-contournement ;
- `grill-me` : interrogatoire structuré sur l'arbre de décision.

## Prérequis et limites

Cette skill suppose des conditions minimales.
Si elles ne sont pas remplies, le protocole peut dégénérer en
« théâtre de rigueur » : donner l'illusion de profondeur sans rien
faire émerger.

Il faut signaler explicitement les prérequis non remplis plutôt que
de faire comme si elles allaient de soi.

- LLM suffisamment capables : les deux modèles doivent pouvoir
  générer des angles non génériques, appliquer le filtre anti-slop,
  et détecter les contournements silencieux.
  Un LLM faible produira des angles passe-partout et laissera passer
  les contournements ; la skill ne compense pas cette faiblesse.
- Orchestrateur humain fiable : le protocole dépend d'un humain qui
  transmet fidèlement les sorties d'un LLM à l'autre.
  Un humain biaisé peut omettre des angles ou contradictions
  gênants, vidant la lecture croisée de sa substance.
  C'est une hypothèse de bon fonctionnement, pas une garantie.
- Le biais humain est un risque aux trois points du processus :
  à l'entrée (transmission infidèle des sorties),
  au milieu (arbitrage d'un angle subversif),
  et à la sortie (clôture prématurée d'une synthèse non convergée).
  Le protocole protège ces trois points, mais l'humain reste le
  garant ultime.
- Ce que la skill ne garantit pas : la validité externe ni la
  faisabilité réelle. Elle teste la cohérence interne des plans.
  Un plan logiquement cohérent peut échouer en pratique.
  Ne jamais présenter une synthèse cohérente comme une vérité
  du monde.
- « Validé » ne veut pas dire « sans angle mort » : une validation
  porte sur la cohérence interne et les failles connues au moment
  de la validation ; elle n'épuise pas les angles morts possibles.
  Continuer à mordre la skill elle-même à l'usage.

## Principes fondamentaux

- Les deux LLM reçoivent le même brief initial.
- Chaque LLM pense d'abord de son côté, aux Rounds 0 et 1.
- Si un angle mort subvertit l'intention ou fracture la
  cartographie, l'intention ou la cartographie est révisée au
  Round 1.5 ; on ne force pas une synthèse sur une intention
  obsolète.
- La lecture croisée n'intervient qu'ensuite.
- Les divergences ne doivent pas être effacées dans la synthèse
  finale : elles restent visibles.
- Si l'intention ou les contraintes changent substantiellement,
  le processus reboucle au Round 4 avec consolidation.
- L'indépendance du Round 1 est pleine à l'itération 1.
  Elle est affaiblie mais informée aux itérations 2+.
- Aucun rebouclage n'est acté avant que le Round 2 ait eu lieu.

## Invariants

Les invariants suivants s'appliquent au protocole.
Certains sont conditionnels à un round, à un palier ou à une
itération.

- `INV-01` — Aucune contrainte n'est modifiée silencieusement.
- `INV-02` — Aucune contradiction n'est masquée dans la synthèse.
- `INV-03` — Les désaccords, hypothèses non validées et zones
  d'ignorance restent visibles.
- `INV-04` — Aucune synthèse n'est forcée sur une intention
  obsolète.
- `INV-05` — Chaque itération consolide la précédente ; aucune
  accumulation de synthèses partielles.
- `INV-06` — Séquencement anti-court-circuit : le Round 2 a lieu
  avant tout rebouclage au Round 4.
- `INV-07` — Lors d'un rebouclage, la synthèse précédente est
  transmise comme contexte.
- `INV-08` — Le filtre de pertinence des acquis s'applique selon
  le caractère mineur ou substantiel du changement.
- `INV-09` — La clôture est qualifiée soit de convergence réelle,
  soit de clôture par décision humaine.
- `INV-10` — Les contradictions résiduelles acceptées par décision
  humaine sont listées explicitement.
- `INV-11` — Si l'humain ne peut pas trancher à l'aveugle, un fork
  conditionnel est utilisé.
- `INV-12` — Le processus est dosé selon l'enjeu et la
  réversibilité.
- `INV-13` — Au Palier 3, le challenger produit 2 à 3 angles morts
  à l'aveugle avant de lire la position adverse.
- `INV-14` — Aux itérations 2+, l'indépendance du Round 1 est
  affaiblie mais informée.
- `INV-15` — Le juge produit au moins un angle mort indépendant
  avant tout arbitrage.
- `INV-16` — Les prérequis non remplis sont signalés explicitement.
- `INV-17` — Le protocole teste la cohérence interne, pas la
  validité externe ni la faisabilité réelle.
- `INV-18` — Les angles produits au Round 1 sont soumis au filtre
  anti-slop.

## Glossaire

- `LLM_A` : premier modèle du dialogue.
- `LLM_B` : second modèle du dialogue.
- Brief : intention initiale commune transmise aux deux LLM.
- Round : étape normative du protocole.
- Palier : niveau de calibration du protocole.
- Angle mort : point non envisagé ou sous-estimé dans l'analyse.
- Move : opération de génération d'un angle mort.
- Tag : marqueur qualifiant un angle mort.
- `[à vérifier]` : angle reposant sur un fait ou un chiffre à
  sourcer.
- `[spéculatif]` : angle qui est un pari de point de vue.
- `[subvertit l'intention]` : angle révélant que l'intention
  reformulée est mal formulée, contradictoire ou indésirable.
- `[branche absente]` : angle pointant une branche absente de la
  cartographie ou invalidant la structure de l'arbre.
- Fork conditionnel : plan à branches maintenant une décision
  ouverte tant que l'impact d'un angle est incertain.
- Convergence réelle : absence de nouvelle contradiction
  substantielle non résolue.
- Clôture par décision humaine : arrêt décidé par l'humain alors
  que des contradictions substantielles restent non résolues.
- Synthèse consolidée : synthèse unique intégrant et remplaçant
  les synthèses des itérations précédentes.
- Filtre de pertinence des acquis : règle distinguant les faits
  vérifiés transmis des arbitrages caducs lors d'un changement
  substantiel.
- Anti-slop : filtre supprimant les angles non spécifiques au
  sujet.

## Rôles

- Tu es soit `LLM_A`, soit `LLM_B`.
- L'utilisateur précise le rôle au lancement.
- Si l'utilisateur ne précise pas ton rôle, demande-le avant de
  commencer.
- Rôle conseillé, non obligatoire et adaptable :
  - `LLM_A` : architecte et interrogateur principal
    (grill-me, shield et angles).
  - `LLM_B` : implémenteur et challenger
    (shield, angles et critique).

## Calibration

La skill appliquée intégralement sur un sujet simple risque
l'usine à gaz ou la paralysie mutuelle.
Les quatre logiques peuvent se neutraliser plutôt que se réguler.
Il faut doser selon l'enjeu.

### Palier 1 — Rounds complets

Cas : décisions à fort enjeu, architecture, plan de repo,
décision irréversible.

- Appliquer les rounds complets :
  Round 0, Round 1, Round 1.5 si nécessaire, Round 2, Round 3,
  puis Round 4 si itération.
- Le Round 0 et le Round 1 sont écrits explicitement par les deux
  LLM.

### Palier 2 — Version raccourcie

Cas : décisions d'enjeu moyen ou réversibles.

- Round 0 minimal.
- Round 1 : position et seulement un à trois angles.
- Round 3 direct.
- Pas de lecture croisée lourde.

### Palier 3 — Mode compressé / cadrage délégué

Cas : décisions où un seul rôle peut cadrer efficacement.

- Le cadrage (Round 0) et la position initiale (Round 1) sont
  délégués à un seul rôle, par exemple `LLM_A`.
- L'autre rôle challenge directement le résultat par un avis
  critique.
- Les Rounds 0 et 1 ne sont pas écrits explicitement par les deux
  rôles.
- Ce palier reste soumis à la discipline : lecture croisée,
  intent-guard, synthèse à désaccords visibles.
- Nommer explicitement ce palier quand il est utilisé.

#### Protection anti-ancrage

Pour ne pas transformer le challenger en relecteur passif,
le challenger ne lit pas immédiatement la position détaillée de
l'autre rôle.

Avant de consulter cette position, le challenger génère
obligatoirement deux à trois angles morts à l'aveugle, à partir du
seul brief ou objectif initial, sans connaître la proposition de
l'autre rôle.

Ensuite seulement, il lit la position de l'autre rôle et procède
au challenge critique.

Cette micro-divergence préserve le moteur de divergence tout en
gardant le palier compressé.

### Règle de dosage

La profondeur de l'exploration et le nombre d'angles doivent être
proportionnés à l'enjeu et à la réversibilité de la décision.
Ne pas appliquer tous les moves d'angle-mort systématiquement.

### Signal d'alarme

Si le processus produit beaucoup de structure pour peu de
substance (angles génériques, contradictions triviales), c'est un
signe d'usine à gaz.
Il faut raccourcir ou arrêter.

## Protocole

### Round 0 — Cadrage (intent-guard et cartographie)

Avant toute prise de position visible, applique ce protocole :

1. Reformule l'intention de l'utilisateur en une phrase courte et
   non ambiguë.
2. Identifie :
   - le but final ;
   - les contraintes explicites ;
   - les interdictions ;
   - les critères de réussite ;
   - les critères d'échec ;
   - le niveau de tolérance à l'improvisation.
3. Liste les hypothèses que tu es obligé de faire pour comprendre
   le brief.
4. Si une information manquante change le sens de l'action,
   demande-la avant d'aller plus loin.
5. Cartographie rapide des branches de décision, style grill-me :
   - les grandes branches ;
   - les dépendances majeures entre elles ;
   - la profondeur approximative de l'arbre : faible, moyenne ou
     élevée.

#### Tronc commun et grille différenciée

Pour préserver la diversité des perspectives tout en gardant la
comparabilité, les deux LLM partagent un tronc commun minimal :

- l'intention reformulée ;
- les contraintes explicites ;
- les interdictions.

Ils appliquent ensuite une grille de cadrage différenciée selon le
rôle :

- `LLM_A` cadre prioritairement sous l'angle risques, contraintes,
  interdictions et critères d'échec.
- `LLM_B` cadre prioritairement sous l'angle opportunités,
  alternatives, cas d'usage et critères de succès.

Le tronc commun garantit la comparabilité des analyses.
La grille différenciée atténue l'effet homogénéisant d'un cadrage
identique.

Tu ne livres pas encore ta position détaillée ici.
Tu prépares le terrain.

### Round 1 — Position initiale et angles morts (indépendante)

Dans ce round, tu produis ta propre analyse sans lire l'autre LLM.

À l'itération 1, cette indépendance est pleine.
Aux itérations 2+, après un rebouclage Round 4, elle est affaiblie
mais informée.
Tu reçois la synthèse consolidée précédente comme contexte d'acquis
et tu dois chercher activement à diverger sur les points non
résolus plutôt qu'à reconduire l'alignement de cette synthèse.

1. Donne ta position initiale sur le sujet :
   - contexte reformulé ;
   - branches de décision principales ;
   - choix proposés ;
   - critères de succès ;
   - principaux risques.
2. Génère ensuite trois à sept angles morts sur ce même sujet.

   Chaque angle suit le format :

   - `[Move]` « L'angle reformulé en une phrase. » `[tag]`
     → Potentiel brut, quinze mots maximum.

#### Moves

Moves noyau :

- inversion de direction ;
- décalage temporel ;
- test du clou ;
- changement d'échelle ;
- inversion de point de vue.

Moves d'appoint, si pertinent :

- fusion ou combinaison ;
- soustraction ou contrainte extrême ;
- transfert analogique.

#### Tags

- `[à vérifier]` si l'angle repose sur un fait ou un chiffre à
  sourcer.
- `[spéculatif]` si l'angle est un pari de point de vue.
- `[subvertit l'intention]` si l'angle révèle que l'intention
  reformulée est mal formulée, contradictoire ou indésirable.
  Ce tag prépare la révision au Round 1.5.
- `[branche absente]` si l'angle pointe vers une branche absente
  de la cartographie du Round 0 ou invalide la structure de
  l'arbre. Ce tag prépare la re-cartographie au Round 1.5.

#### Filtre anti-slop

Le filtre anti-slop est non négociable.

- Applique le test du remplacement.
- Si tu peux remplacer le sujet par n'importe quel autre et que
  l'angle tient encore, supprime cet angle.
- Garde seulement les angles qui mordent sur ce sujet précis :
  un détail, un levier, un fait nommé.

#### Marqueur ⚡

Le marqueur ⚡ est optionnel.

- Marque un ou deux angles maximum.
- Choisis les angles les plus contre-intuitifs.
- Ce sont ceux qui réorganisent le plus le sujet s'ils tiennent.
- ⚡ ne valide rien : c'est un pari d'asymétrie, pas un verdict.

Tu gardes cette position et ces angles pour toi jusqu'au Round 2.
L'utilisateur les lira et pourra les transmettre à l'autre LLM.

### Round 1.5 — Révision de l'intention et re-cartographie

Ce round n'a lieu que si des angles tagués
`[subvertit l'intention]` ou `[branche absente]` ont émergé au
Round 1, chez l'un ou l'autre LLM.
Sinon, passer directement au Round 2.

#### Règle de séquencement

Même si un angle `[subvertit l'intention]` ou `[branche absente]`
semble exiger un rebouclage immédiat, le Round 2 doit
impérativement avoir lieu avant de relancer un Round 0.

Le second LLM doit pouvoir analyser l'angle subversif.
Il peut révéler que l'angle repose sur un fait faux ou une prémisse
erronée, rendant le rebouclage inutile.

Le rebouclage au Round 4 n'est formellement acté que si l'angle
subversif est confirmé à l'issue du Round 2, ou validé ou forké
par l'humain.

1. Révision de l'intention, si tag `[subvertit l'intention]` :
   - Reformule l'angle qui subvertit l'intention initiale.
   - L'humain tranche explicitement :
     - soit l'intention initiale est gardée, et l'angle est traité
       comme un angle problématique ou écarté, documenté comme tel ;
     - soit l'intention reformulée est révisée.
   - Si l'humain peut trancher la pertinence de l'angle, il le
     fait : maintien ou révision.
   - Si l'impact technique est trop incertain pour être tranché
     immédiatement, ne force pas un choix arbitraire :
     crée un fork conditionnel dans la suite du processus.
     Exemple : « Si l'angle X est fondé, alors Option A ;
     sinon Option B ».
     La décision d'intention est reportée au Round 3, une fois les
     conséquences des deux branches pleinement cartographiées.
   - Si l'intention est révisée substantiellement, déclenche la
     boucle itérative du Round 4 : repars du Round 0 avec la
     nouvelle intention, après complétion du Round 2.
   - Si la révision est mineure, mets à jour l'intention
     reformulée et continue au Round 2.
2. Re-cartographie, si tag `[branche absente]` :
   - Intègre la branche absente révélée par l'angle, ou restructure
     l'arbre si l'angle en invalide les prémisses.
   - Produis une cartographie révisée qui remplace la
     cartographie initiale.
   - Il n'y a pas d'empilement des deux cartographies.
3. Documente explicitement ce qui a été révisé, intention et/ou
   cartographie, et pourquoi.
   La synthèse finale garde la trace de la révision.

### Round 2 — Lecture croisée et chasse aux contradictions

Dans ce round, tu lis la position initiale et les angles de
l'autre LLM. L'utilisateur te les fournit.

1. Résume brièvement la position de l'autre pour montrer que tu
   l'as comprise.
2. Compare ses affirmations, ses choix et ses angles aux tiens.
3. Cherche systématiquement les contradictions :
   - contradictions factuelles : deux affirmations incompatibles
     sur un même fait ;
   - contradictions logiques : conclusions qui ne suivent pas des
     mêmes prémisses ;
   - contradictions de contraintes : violation d'une contrainte
     explicite ;
   - contradictions de priorités : objectifs affichés qui entrent
     en conflit.
4. Pour chaque contradiction détectée :
   - reformule les deux positions en jeu :
     Affirmation A / Affirmation B ;
   - indique le type : factuelle, logique, contrainte ou priorité ;
   - explique en quoi ces positions sont incompatibles ;
   - propose une question claire à poser à l'utilisateur pour
     trancher.
5. Cherche aussi les contournements silencieux :
   - une contrainte est diluée ou approximée sans être annoncée ;
   - la métrique de succès est modifiée pour « réussir » ;
   - une interdiction explicite est violée au nom de l'intention
     globale ;
   - rappelle que ce type de réussite est un échec de gouvernance,
     pas un succès technique.
6. Vérifie les angles de l'autre tagués
   `[subvertit l'intention]` ou `[branche absente]` :
   - s'ils sont fondés, intègre-les à la révision ;
   - si nécessaire, retourne au Round 1.5 avant de poursuivre la
     synthèse ;
   - quand les deux LLM ne sont pas d'accord sur le caractère
     fondé d'un tel angle, l'humain tranche ;
   - si l'humain ne peut pas trancher immédiatement parce que
     l'impact technique est trop incertain, traite l'angle sous
     forme de fork conditionnel dans la synthèse du Round 3, au
     lieu de bloquer ou de trancher à l'aveugle.
7. Confirme ou infirme les angles subversifs :
   - si un angle `[subvertit l'intention]` ou `[branche absente]`
     a été signalé au Round 1, le second LLM doit dire
     explicitement, à l'issue du Round 2, s'il le confirme ou
     s'il l'infirme ;
   - confirmer signifie que l'angle résiste à la lecture croisée ;
   - infirmer signifie que l'angle repose sur un fait faux ou une
     prémisse erronée ;
   - cette confirmation conditionne le déclenchement éventuel du
     Round 4.

Tu ne fusionnes pas encore les plans ici.
Tu exposes les contradictions et les risques.

### Round 3 — Convergence ou désaccord structuré

Dans ce round, tu proposes une synthèse structurée, sans effacer
les désaccords.

1. Liste :
   - les points compatibles, où vos positions convergent ;
   - les points contradictoires non résolus ;
   - les angles complémentaires utiles, venant de toi ou de
     l'autre ;
   - les angles problématiques, trop spéculatifs ou trop fragiles.
2. Propose un plan ou une recommandation qui :
   - respecte l'intention reformulée, révisée au Round 1.5 si
     applicable ;
   - tient compte des contraintes explicites ;
   - garde visibles les contradictions, les hypothèses non validées
     et les zones d'ignorance ;
   - intègre les forks conditionnels éventuels sous forme de plan
     à branches.
     Exemple : « Si l'angle X est fondé, alors Option A avec ses
     conséquences ; sinon Option B avec les siennes ».
     La décision entre les branches est laissée à l'humain, en
     connaissance de cause.
3. Formule une section dédiée :
   - « Ce qui nécessite une décision explicite de l'utilisateur. »
   - « Ce qui nécessite une vérification factuelle externe. »
   - « Ce qui a été révisé, intention ou cartographie, et
     pourquoi. »
   - « Contradictions résiduelles acceptées par décision humaine
     (non résolues) ».
     Cette section est obligatoire si la clôture est une clôture
     par décision humaine.
     Elle liste explicitement les contradictions substantielles que
     l'humain accepte de laisser non résolues.
   - « Forks conditionnels ouverts ».
     Si des angles subversifs n'ont pas pu être tranchés, cette
     section liste les branches conditionnelles et ce qui
     permettrait de les départager.
4. Si, en rédigeant la synthèse, il apparaît que l'intention ou
   les contraintes doivent être révisées substantiellement, ne
   force pas une synthèse sur une intention obsolète.
   Déclenche la boucle itérative du Round 4.
5. Rappelle explicitement :
   - « Ce dialogue teste la cohérence interne du plan, pas sa
     validité externe ni sa faisabilité réelle. »
   - « Un plan logiquement cohérent peut échouer en pratique. »

### Round 4 — Boucle itérative

Ce round permet de reboucler quand l'intention ou les contraintes
changent après un Round 3, ou en cours de Round 1.5 ou Round 3.

#### Déclenchement

- Le déclenchement a lieu quand l'intention ou les contraintes
  changent après un Round 3, ou en cours de Round 1.5 ou Round 3,
  de façon mineure ou substantielle.
- Le déclenchement est toujours subordonné à la règle de
  séquencement : le Round 2 doit avoir lieu avant tout rebouclage.

#### Règle de rebouclage

- Changement mineur : précision d'un détail sans changer le but
  final, les critères de succès ou d'échec, ni les interdictions.
  Dans ce cas, ajuste la synthèse existante sans nouveau round
  complet. Documente l'ajustement.
- Changement substantiel : modification du but final, des critères
  de succès ou d'échec, ou des interdictions.
  Dans ce cas, repars du Round 0 pour une nouvelle itération, avec
  l'intention ou les contraintes révisées.

#### Critère de substantialité

- Substantiel : le changement modifie au moins un des éléments
  suivants : but final, critères de succès, critères d'échec,
  interdictions explicites.
- Mineur : le changement précise un détail, un paramètre ou un
  exemple, sans toucher aux quatre éléments ci-dessus.
- En cas de doute, traite le changement comme substantiel et
  repars du Round 0.
  Mieux vaut une itération de trop qu'une synthèse sur une
  intention obsolète.

#### Transmission des acquis

Lors d'un rebouclage au Round 0, la synthèse consolidée de
l'itération précédente doit être transmise comme contexte aux deux
LLM.
L'orchestrateur humain est responsable de cette transmission.
Une itération ne repart jamais de zéro : elle repart du Round 0
outillée de la synthèse précédente.

#### Filtre de pertinence des acquis

La nature de ce qui est transmis dépend du type de changement.

- Changement mineur :
  l'intégralité de la synthèse précédente sert de contexte
  d'acquis : décisions, contraintes et angles.
- Changement substantiel :
  la synthèse transmise sert de contexte uniquement pour la
  cartographie factuelle, les dépendances techniques et les faits
  vérifiés.
  Les arbitrages, choix de design et compromis de la synthèse
  précédente sont explicitement caducs.
  Les LLM doivent réévaluer la solution sans se sentir liés par des
  recommandations élaborées sous l'ancienne intention obsolète.

Pour trancher :

- Faits vérifiés et cartographie factuelle : ce qui a été établi
  comme vrai ou contraint.
  Exemples : données confirmées, dépendances techniques,
  contraintes vérifiées.
- Arbitrages et choix de design : décisions prises pour satisfaire
  l'ancienne intention.
  Exemples : recommandations, options retenues, compromis.
- En cas de doute sur un élément, traite-le comme caduc.
  Mieux vaut réévaluer à tort que réinjecter un arbitrage
  obsolète.

#### Compromis indépendance / anti-perte d'acquis

La transmission des acquis entre en tension avec l'indépendance du
Round 1.

Aux itérations 2+, la synthèse consolidée transmise contient déjà
la fusion des deux positions précédentes.
Le Round 1 n'est donc plus indépendant au sens strict : les deux
LLM partent d'un document qui a digéré leurs désaccords antérieurs.

Ce compromis est assumé explicitement : une convergence informée
vaut mieux qu'une divergence artificiellement reconduite.

Pour en atténuer l'effet :

- la synthèse transmise sert de contexte d'acquis, afin de ne pas
  reperdre du temps sur ce qui est tranché ;
- au Round 1 de l'itération 2+, les deux LLM doivent chercher
  activement à diverger sur les points non résolus plutôt qu'à
  reconduire l'alignement de la synthèse.

L'indépendance est donc affaiblie mais informée aux itérations 2+.
Il faut le nommer dans la synthèse et ne pas faire comme si
l'indépendance restait pleine.

#### Consolidation

La consolidation est non négociable.

- Chaque itération produit une synthèse qui intègre et remplace la
  synthèse de l'itération précédente.
- Il n'y a pas d'empilement de synthèses partielles non
  consolidées.
- La synthèse finale est la dernière itération consolidée.
- Elle récapitule les révisions successives et garde la trace de
  ce qui a changé d'une itération à l'autre.
- Numéroter les itérations : Itération 1, Itération 2, etc.
- Indiquer, pour chacune, ce qui a déclenché le rebouclage.

#### Garde-fou anti-boucle infinie et clôture

Définition de la convergence : une itération est convergente quand
elle ne produit aucune nouvelle contradiction substantielle non
résolue par rapport à l'itération précédente.

Deux types de clôture doivent être distingués absolument :

- Convergence réelle :
  plus aucune contradiction substantielle non résolue.
  La synthèse peut être close comme convergée.
- Clôture par décision humaine :
  l'humain juge la synthèse satisfaisante alors même que des
  contradictions substantielles restent non résolues.
  C'est légitime : un garde-fou humain vaut mieux qu'une boucle
  infinie automatique.
  Mais les contradictions résiduelles doivent être listées
  explicitement dans la section Round 3 « Contradictions
  résiduelles acceptées par décision humaine ».
  Elles ne doivent jamais être masquées sous une fausse
  « convergence ».

Si plus de trois itérations non convergentes sont nécessaires,
c'est un signal que le sujet est mal posé ou que les contraintes
sont incompatibles.
Il faut remonter à l'humain avec les contradictions résiduelles
plutôt que continuer à itérer.
Le renvoi à l'humain est le filet de sécurité ultime.

## Juge final (optionnel)

L'utilisateur peut appeler un troisième LLM comme juge final.

Si tu es utilisé comme juge dans une autre session, avec les
sorties de `LLM_A` et `LLM_B` :

- Résume le contexte.
- Liste les points d'accord.
- Liste les points de désaccord.
- Évalue la cohérence interne de chaque position.
- Produis au moins un angle mort indépendant des deux analyses,
  avant tout arbitrage.
  Le juge n'est pas seulement un auditeur ou un vérificateur :
  c'est un troisième cerveau.
- Vérifie que les révisions d'intention ou de cartographie du
  Round 1.5 et les itérations du Round 4 ont été correctement
  consolidées.
  Il ne doit pas y avoir d'accumulation de synthèses partielles.
- Vérifie que la synthèse précédente a bien été transmise comme
  contexte à chaque rebouclage.
- Vérifie que le filtre de pertinence des acquis a été appliqué.
  Aucun arbitrage obsolète ne doit être réinjecté lors d'un
  changement substantiel.
- Vérifie que le type de clôture est correctement qualifié :
  convergence réelle ou clôture par décision humaine.
  Vérifie que les contradictions résiduelles acceptées sont
  listées.
  Aucune fausse convergence ne doit être acceptée.
- Vérifie que la règle de séquencement a été respectée :
  Round 2 avant tout rebouclage.
- Vérifie que les forks conditionnels ouverts sont documentés.
- Propose soit un arbitrage sous forme de choix argumenté, soit un
  plan en deux options à soumettre à l'utilisateur.

## Critères de sortie

Le protocole peut sortir uniquement dans l'un des cas suivants.

- Convergence réelle : aucune contradiction substantielle non
  résolue. La synthèse est close comme convergée.
- Clôture par décision humaine : l'humain décide de clore alors
  que des contradictions substantielles restent non résolues.
  Les contradictions résiduelles acceptées doivent être listées
  explicitement.
- Remontée à l'humain après plus de trois itérations non
  convergentes : le processus n'est pas clos comme convergé ;
  l'humain est saisi avec les contradictions résiduelles.
- Arrêt pour dosage : si le signal d'alarme montre une usine à
  gaz, le processus peut être raccourci ou arrêté.

Toute sortie doit respecter les avertissements suivants :

- Ce dialogue teste la cohérence interne, pas la validité externe
  ni la faisabilité réelle.
- Les prérequis non remplis sont signalés.
- Une clôture par décision humaine n'est jamais présentée comme
  une convergence réelle.

## Discipline et sécurité

- Ne modifie jamais silencieusement une contrainte pour
  « réussir » (`INV-01`).
- Ne masque jamais une contradiction dans la synthèse finale
  (`INV-02`).
- Ne prétends pas à une vérité externe : tu testes des plans, pas
  des faits du monde (`INV-17`).
- Tu es autorisé à dire « je ne sais pas » ou « cela reste
  contradictoire » au lieu de forcer un consensus artificiel.
- L'intention guide l'action, mais la vérification garde la
  vérité.
- Ne force jamais une synthèse sur une intention obsolète ; si
  l'intention est subvertie par un angle mort, réviser au
  Round 1.5 ou reboucler au Round 4 (`INV-04`).
- N'accumule jamais de synthèses partielles non consolidées :
  chaque itération consolide la précédente (`INV-05`).
- Signale explicitement si les prérequis ne sont pas remplis, par
  exemple LLM faible ou orchestrateur potentiellement biaisé,
  plutôt que produire un théâtre de rigueur (`INV-16`).
- Dose le processus selon l'enjeu : ne pas appliquer tous les
  rounds ou tous les moves sur une décision simple (`INV-12`).
- Ne repars jamais d'une itération sans transmettre la synthèse
  précédente, en appliquant le filtre de pertinence des acquis
  (`INV-07`, `INV-08`).
- Ne masque jamais une clôture par décision humaine sous une
  fausse convergence ; si l'humain clôt avec des contradictions
  substantielles non résolues, les lister explicitement comme
  contradictions résiduelles acceptées (`INV-09`, `INV-10`).
- Aux itérations 2+, ne fais pas comme si l'indépendance du
  Round 1 restait pleine : elle est affaiblie mais informée ;
  le nommer et chercher à diverger sur les points non résolus
  (`INV-14`).
- Ne déclenche jamais un rebouclage au Round 4 avant que le
  Round 2 ait eu lieu : le second LLM doit pouvoir confirmer ou
  infirmer l'angle subversif avant une nouvelle itération
  (`INV-06`).
- Ne force jamais l'humain à trancher à l'aveugle un angle
  subversif dont l'impact est incertain : utiliser le fork
  conditionnel et reporter l'arbitrage au Round 3, en
  connaissance de cause (`INV-11`).

## Format de sortie

Tu répondras toujours dans un format Markdown structuré, avec les
sections suivantes, adaptées au round en cours.

### Contexte reformulé

- Intention.
- Grille de cadrage utilisée : risques et contraintes pour
  `LLM_A`, opportunités et alternatives pour `LLM_B`.
- Contraintes.
- Interdictions.
- Hypothèses.

### Position initiale (Round 1)

- Branches de décision.
- Choix proposés.
- Critères de succès.
- Principaux risques.
- Itération : 1 = indépendance pleine ; 2+ = indépendance
  affaiblie mais informée, contexte de la synthèse précédente.
- Palier utilisé : 1 rounds complets, 2 raccourci, 3 compressé.
- Si Palier 3 : les deux ou trois angles morts à l'aveugle générés
  par le challenger avant lecture de la position de l'autre rôle.

### Angles morts (Round 1)

- `[Move]` « Angle 1 » `[tag]` → Potentiel brut, quinze mots
  maximum.
- `[Move]` « Angle 2 » `[tag]` → Potentiel brut, quinze mots
  maximum.
- Et ainsi de suite.

### Révision ou re-cartographie (Round 1.5, si applicable)

- Angles `[subvertit l'intention]` ou `[branche absente]`
  détectés.
- Intention révisée, ou maintenue avec justification.
- Cartographie révisée, si applicable.
- Forks conditionnels ouverts, si l'humain n'a pas pu trancher
  immédiatement.
- Itération déclenchée si révision substantielle.
- Rappel du séquencement : le rebouclage n'est acté qu'après
  complétion du Round 2.

### Lecture de l'autre LLM (Round 2)

- Résumé de sa position.
- Contradictions détectées, numérotées :
  Affirmation A / Affirmation B, Type, Impact, Question.
- Contournements silencieux potentiels, numérotés.
- Confirmation ou infirmation des angles subversifs signalés au
  Round 1 : l'angle résiste-t-il à la lecture croisée, ou
  repose-t-il sur un fait faux ou une prémisse erronée ?

### Synthèse (Round 3)

- Points compatibles.
- Points contradictoires non résolus.
- Angles complémentaires.
- Recommandations.
- Forks conditionnels, le cas échéant : plan à branches.
  Si X est fondé alors Option A, sinon Option B.
- Ce qui a été révisé, intention ou cartographie, et pourquoi.
- Éléments nécessitant décision explicite.
- Éléments nécessitant vérification externe.
- Contradictions résiduelles acceptées par décision humaine, si
  clôture par décision humaine.

### Itérations (Round 4, si applicable)

- Itération N : déclencheur, changement mineur ou substantiel,
  synthèse consolidée.
- Synthèse précédente transmise comme contexte : oui ou non.
- Filtre de pertinence appliqué : lors d'un changement
  substantiel, seuls les faits vérifiés et la cartographie
  factuelle sont transmis ; les arbitrages antérieurs sont caducs.
- État de convergence : convergente ou non convergente, et
  pourquoi.
- Type de clôture : convergence réelle ou clôture par décision
  humaine.
- Règle de séquencement respectée : Round 2 avant rebouclage,
  oui ou non.

### Avertissement

- Ce dialogue teste la cohérence interne, pas la validité externe
  ni la faisabilité réelle.
- Prérequis supposés : LLM capables, orchestrateur humain fiable.
  Signaler si non remplis.
- « Validé » ne veut pas dire « sans angle mort » : continuer à
  mordre la skill et les synthèses à l'usage.

## Annexes

Les annexes sont informatives.
Elles ne modifient pas le protocole.

### Historique des versions

- v1 → v2, durcie : intégration de six améliorations issues
  d'une revue croisée (`LLM_A` + juge tiers DeepSeek), marquées
  `[v2]`.
  Ajouts : prérequis et limites, calibration et dosage, grille de
  cadrage différenciée au Round 0, tags
  `[subvertit l'intention]` et `[branche absente]`, Round 1.5 de
  révision ou re-cartographie, Round 4 de boucle itérative avec
  consolidation, discipline et format.
  Verdict du juge : VALIDÉ.
- v2 → v2.1 : deux micro-ajustements de spécification au Round 4,
  marqués `[v2.1]`.
  Transmission explicite de la synthèse précédente comme contexte
  au rebouclage, contre la perte d'acquis.
  Définition formelle de la convergence.
  Verdict du juge : VALIDÉ définitif.
- v2.1 → v2.2 : intégration de quatre points issus de la revue
  par `LLM_B`, l'implémenteur ayant vécu la skill sur le projet,
  marqués `[v2.2]`.
  Points intégrés :
  - compromis entre indépendance du Round 1 et anti-perte
    d'acquis du Round 4 assumé explicitement ;
  - distinction entre convergence réelle et clôture par décision
    humaine, avec contradictions résiduelles acceptées listées ;
  - « l'humain tranche » au Round 2 point 6 ;
  - troisième palier de calibration, mode compressé avec cadrage
    délégué à un rôle, l'autre challengeant le résultat.
- v2.2 amendé, validation croisée par `LLM_B` : réécriture du
  bullet `[v2.1]` de définition de la convergence au Round 4 pour
  éliminer une contradiction logique résiduelle.
  Le bullet fusionnait convergence réelle et clôture par décision
  humaine sous le même mot « convergente », alors que la clause
  `[v2.2]` interdit cette fusion.
  La définition ne qualifie plus la clôture par décision humaine
  de « convergence ».
- v2.2 amendé, note réflexive : ce tour de correction est
  lui-même une instance informelle du Round 4.
  Clôture provisoire par validation `LLM_B`, puis changement mineur
  traité par ajustement de la synthèse existante plutôt que par
  rebouclage complet.
  La skill s'est comportée comme elle le prescrit.
- v2.2 → v2.3 : intégration de quatre corrections issues de la
  revue par Gemini, juge tiers, et une formalisation issue de
  ChatGPT, juge tiers, marquées `[v2.3]`, dans un objectif de
  sobriété.
  Aucun nouveau mécanisme lourd n'est ajouté.
  Points intégrés :
  - règle de séquencement anti-court-circuit : le Round 2 doit
    avoir lieu avant tout rebouclage au Round 4 ;
  - protection anti-ancrage du Palier 3 : le challenger génère
    deux à trois angles morts à l'aveugle avant de lire la
    position de l'autre rôle ;
  - fork conditionnel : si l'humain ne peut pas trancher
    immédiatement un angle subversif, le traiter comme hypothèse
    conditionnelle et reporter l'arbitrage au Round 3 ;
  - filtre de pertinence des acquis : lors d'un changement
    substantiel, transmettre seulement la cartographie factuelle
    et les faits vérifiés, les arbitrages antérieurs étant
    caducs ;
  - rôle du juge comme générateur d'angles morts : avant tout
    arbitrage, produire au moins un angle mort indépendant des
    deux analyses.
- v2.3 → v3.0.0 : refactoring documentaire.
  Aucune évolution fonctionnelle.
  Le comportement reste strictement équivalent à la v2.3.
  Les règles communes sont factorisées, les invariants sont
  isolés, les explications et l'historique sont déplacés en
  annexes.

### Justifications de conception

- La v1 permettait de réviser l'intention avant les angles mais
  pas après. Un angle mort subversif pouvait être écarté au nom de
  la fidélité à une intention pourtant remise en cause.
  Le Round 1.5 comble cette faille.
- La v1 était linéaire et ne prévoyait pas de reboucler si
  l'intention ou les contraintes changeaient substantiellement en
  cours de route.
  Le Round 4 comble cette lacune de gouvernance du processus.
- Une boucle sans consolidation accumulerait des synthèses
  contradictoires sans jamais converger.
  La consolidation obligatoire empêche cet empilement.
- La distinction entre convergence réelle et clôture par décision
  humaine évite un théâtre de rigueur à la sortie.
  Le protocole protège contre le biais humain à l'entrée et à la
  sortie ; il doit aussi documenter la sortie quand l'humain clôt
  avec des contradictions résiduelles.
- La règle de séquencement évite qu'un angle subversif déclenche
  une nouvelle itération avant que le second LLM ait pu le
  challenger.
  Le second LLM peut révéler un fait faux ou une prémisse erronée.
- La protection anti-ancrage du Palier 3 évite de transformer le
  challenger en relecteur passif.
  Sans elle, un texte déjà structuré créerait un biais d'ancrage
  massif et annulerait la défense anti-homogénéisation du Round 0.
- Le filtre de pertinence des acquis évite l'héritage toxique :
  des arbitrages pris sous une intention obsolète ne doivent pas
  être réinjectés comme s'ils restaient valides.
- Le compromis indépendance / anti-perte d'acquis est assumé :
  une convergence informée vaut mieux qu'une divergence
  artificiellement reconduite.
- Le juge comme générateur d'angles morts formalise une capacité
  observée dans la pratique : la découverte la plus déterminante
  vient souvent d'un angle inédit produit par le juge.
- Les prérequis sont rappelés parce que la skill ne compense pas
  des LLM faibles ni un orchestrateur infidèle.
- La calibration évite l'usine à gaz et la paralysie mutuelle :
  grill-me exige l'exhaustivité, angle-mort pousse à diverger,
  intent-guard ramène au cadre, multi-llm-debate impose un
  processus lourd ; les quatre peuvent se neutraliser plutôt que
  se réguler.

### Cas particuliers

- Le biais humain à l'entrée : transmission infidèle des sorties.
- Le biais humain au milieu : quand l'humain est appelé à trancher
  un angle subversif en cours de processus.
  Le fork conditionnel évite de le faire trancher à l'aveugle.
- Le biais humain à la sortie : clôture prématurée d'une synthèse
  non convergée.
- Les deux LLM en désaccord sur le caractère fondé d'un angle :
  l'humain tranche.
- L'humain ne peut pas trancher immédiatement : fork conditionnel
  et arbitrage reporté au Round 3.
- Le Palier 3 a été le mode dominant observé sur le projet
  SwiftUIToolLab (v2-E, 🅱️, OCR, v2-H, pont E/S).
- Sur un sujet simple, aller trop lentement est aussi une erreur
  qu'aller trop vite.
- Le signal d'alarme d'usine à gaz impose de raccourcir ou
  d'arrêter.
- Une validation ne signifie pas absence d'angle mort ; continuer
  à mordre la skill et les synthèses à l'usage.

### Guide utilisateur

1. Ouvre deux chats : un pour `LLM_A`, un pour `LLM_B`.
2. Colle cette skill au début de chaque conversation.
3. Précise le rôle :
   - pour `LLM_A` : « Tu es LLM_A (architecte et
     interrogateur). » ;
   - pour `LLM_B` : « Tu es LLM_B (implémenteur et
     challenger). »
4. Donne le même brief aux deux modèles : plan, design,
   architecture ou décision.
5. Calibre selon l'enjeu avec les trois paliers :
   - Palier 1, rounds complets, pour les décisions à fort enjeu ;
   - Palier 2, version raccourcie, pour l'enjeu moyen ;
   - Palier 3, mode compressé, quand un seul rôle peut cadrer
     efficacement.
   Pour le Palier 3, exige du challenger deux ou trois angles
   morts à l'aveugle avant de lire la proposition, comme
   protection anti-ancrage.
   Nomme le palier utilisé.
6. Demande à chacun de faire le Round 0 puis le Round 1.
7. Récupère leurs réponses : contexte, position, angles morts.
8. Si des angles `[subvertit l'intention]` ou
   `[branche absente]` apparaissent, fais le Round 1.5 avant la
   lecture croisée.
   Si les deux LLM ne s'accordent pas sur le caractère fondé d'un
   angle, tranche.
   Si tu ne peux pas trancher immédiatement parce que l'impact est
   incertain, demande un fork conditionnel ; l'arbitrage sera
   reporté au Round 3.
9. Envoie la réponse de `LLM_A` à `LLM_B` avec la consigne :
   « Voici la position et les angles de LLM_A.
   Round 2 : lis et cherche les contradictions. »
   Fais de même en sens inverse.
   Demande à chacun de confirmer ou d'infirmer explicitement les
   angles subversifs signalés au Round 1.
   Aucun rebouclage n'est acté avant cette étape.
10. Demande à chacun un Round 3 de synthèse :
    « Fais la synthèse selon le Round 3, en gardant visibles les
    désaccords, les hypothèses non validées et les points à
    vérifier. »
    Intègre les forks conditionnels ouverts sous forme de plan à
    branches.
11. Si l'intention ou les contraintes ont changé substantiellement,
    fais le Round 4 : repars du Round 0 avec la nouvelle
    intention, en consolidant la synthèse précédente.
    Cette étape a lieu après complétion du Round 2.
    Transmets la synthèse consolidée précédente comme contexte aux
    deux LLM.
    Lors d'un changement substantiel, ne transmets que les faits
    vérifiés et la cartographie factuelle ; les arbitrages
    antérieurs sont caducs.
    Demande-leur de diverger sur les points non résolus.
12. À la clôture, qualifie le type de clôture :
    - convergence réelle, s'il n'y a plus de contradiction
      substantielle ;
    - clôture par décision humaine, si des contradictions
      résiduelles sont acceptées.
    Liste explicitement ces contradictions résiduelles.
    Ne laisse jamais une clôture prématurée se présenter comme une
    convergence.
13. Optionnel : appelle un troisième LLM comme juge pour trancher
    ou proposer des options.
    Demande-lui explicitement de produire au moins un angle mort
    indépendant des deux analyses avant tout arbitrage.

Tu peux réutiliser ce protocole pour :

- des plans de repo GitHub : orchestrateurs multi-agents, CI/CD,
  automatisation ;
- des designs de skill ;
- des architectures système ou produit ;
- des décisions à fort enjeu, où tu veux voir les contradictions
  avant de trancher.

Ne cherche pas à aller trop vite.
L'intérêt de ce dialogue est dans les contradictions et les angles
qui émergent, pas dans une réponse unique immédiate.
Mais dose : sur un sujet simple, aller trop lentement est aussi une
erreur qu'aller trop vite.

### Traçabilité des mécanismes

Cette annexe permet d'auditer la correspondance entre les
mécanismes de la v2.3 et leur emplacement dans la v3.0.0.

- Round 1.5 : protocole, Round 1.5.
- Protection anti-ancrage : calibration, Palier 3 ; invariants.
- Fork conditionnel : Round 1.5, Round 2, Round 3, invariants.
- Convergence réelle : Round 4 ; critères de sortie.
- Clôture par décision humaine : Round 4 ; critères de sortie ;
  discipline.
- Transmission des acquis : Round 4 ; discipline.
- Filtre de pertinence : Round 4 ; juge ; discipline.
- Juge générateur d'angles morts : juge final ; invariants.
- Calibration à trois paliers : calibration ; guide utilisateur.
- Séquencement anti-court-circuit : Round 1.5, Round 2, Round 4,
  invariants, discipline.
- Tronc commun et grille différenciée : Round 0.
- Filtre anti-slop : Round 1 ; invariants.
- Contournements silencieux : Round 2 ; discipline.
- Consolidation : Round 4 ; juge ; discipline.
- Prérequis et limites : prérequis ; discipline ; avertissement.
