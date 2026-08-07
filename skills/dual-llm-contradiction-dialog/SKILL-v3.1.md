---
name: dual-llm-contradiction-dialog
description: >-
  Orchestration d'un dialogue structuré entre deux LLMs (A et B)
  autour d'un même sujet, avec cadrage d'intention, génération
  d'angles morts, recherche de contradictions, mécanismes de
  révision d'intention, boucle itérative avec consolidation,
  calibration à trois paliers, et juge comme générateur d'angles
  morts.
version: 3.1.0
language: fr
---

# dual-llm-contradiction-dialog (v3.1.0)

## Introduction

Ce document spécifie la skill `dual-llm-contradiction-dialog`.

La version 3.1.0 est une réduction documentaire stricte de la
v3.0.0. Le comportement protocolaire reste strictement équivalent
à la v2.3. Aucun mécanisme n'est ajouté, supprimé ou modifié.
Seule la redondance documentaire a été éliminée : chaque règle
normative n'est définie qu'une seule fois.

## Prérequis et limites

Cette skill suppose des conditions minimales. Les signaler
explicitement si elles ne sont pas remplies.

- **LLM suffisamment capables** : générer des angles non
  génériques, appliquer le filtre anti-slop, détecter les
  contournements silencieux.
- **Orchestrateur humain fiable** : transmettre fidèlement les
  sorties. Un humain biaisé vide la lecture croisée de sa
  substance.
- **Biais humain aux trois points** : à l'entrée (transmission),
  au milieu (arbitrage d'un angle subversif), à la sortie (clôture
  prématurée). Le protocole protège ces trois points.
- **Ce que la skill ne garantit pas** : la validité externe ni la
  faisabilité réelle. Elle teste la cohérence interne des plans.
- **« Validé » ≠ « sans angle mort »** : une validation porte sur
  les failles connues au moment de la validation.
- **Droit à l'incertitude** : tu es autorisé à dire « je ne sais
  pas » ou « cela reste contradictoire » plutôt que de forcer un
  consensus artificiel.

## Rôles

- Tu es soit `LLM_A`, soit `LLM_B`. L'utilisateur précise le rôle
  au lancement. Si non précisé, demande-le avant de commencer.
- Rôle conseillé (adaptable) :
  - `LLM_A` : architecte et interrogateur principal.
  - `LLM_B` : implémenteur et challenger.

## Calibration

Doser selon l'enjeu. Signal d'alarme : si beaucoup de structure
pour peu de substance, raccourcir ou arrêter.

### Palier 1 — Rounds complets

Cas : décisions à fort enjeu, irréversibles.
Appliquer les rounds complets (0 → 1 → 1.5 → 2 → 3, + 4 si
itération). Round 0 et Round 1 écrits explicitement par les deux
LLM.

### Palier 2 — Version raccourcie

Cas : enjeu moyen ou réversible.
Round 0 minimal, Round 1 avec 1 à 3 angles seulement, Round 3
direct. Pas de lecture croisée lourde.

### Palier 3 — Mode compressé / cadrage délégué

Cas : un seul rôle peut cadrer efficacement.
Le cadrage (Round 0) et la position initiale (Round 1) sont
délégués à un rôle. L'autre challenge directement le résultat.
Nommer explicitement ce palier quand il est utilisé.

**Protection anti-ancrage** : avant de lire la position de
l'autre rôle, le challenger génère obligatoirement 2 à 3 angles
morts à l'aveugle à partir du seul brief. Ensuite seulement, il
lit la position adverse et challenge.

## Protocole

### Round 0 — Cadrage

Avant toute prise de position visible :

1. Reformule l'intention en une phrase courte et non ambiguë.
2. Identifie : but final, contraintes explicites, interdictions,
   critères de réussite, critères d'échec, niveau de tolérance à
   l'improvisation.
3. Liste les hypothèses nécessaires pour comprendre le brief.
4. Si une information manquante change le sens, demande-la.
5. Cartographie rapide (style grill-me) : grandes branches,
   dépendances majeures, profondeur approximative de l'arbre.

**Tronc commun + grille différenciée** :

Tronc commun minimal partagé : intention reformulée, contraintes
explicites, interdictions.

Grille différenciée :

- `LLM_A` : risques, contraintes, interdictions, critères d'échec.
- `LLM_B` : opportunités, alternatives, cas d'usage, critères de
  succès.

Tu ne livres pas encore ta position détaillée.

### Round 1 — Position initiale et angles morts

Tu produis ta propre analyse sans lire l'autre LLM. À l'itération
1, l'indépendance est pleine. Aux itérations 2+, elle est
affaiblie mais informée : tu reçois la synthèse consolidée
précédente et tu dois diverger sur les points non résolus.

1. Position initiale : contexte reformulé, branches de décision,
   choix proposés, critères de succès, principaux risques.
2. Génère 3 à 7 angles morts.

Format :

- `[Move]` « Angle reformulé. » `[tag]` → Potentiel brut (15 mots
  max).

**Moves noyau** : inversion de direction, décalage temporel, test
du clou, changement d'échelle, inversion de point de vue.

**Moves d'appoint** (si pertinent) : fusion, soustraction,
transfert analogique.

**Tags** :

- `[à vérifier]` : fait ou chiffre à sourcer.
- `[spéculatif]` : pari de point de vue.
- `[subvertit l'intention]` : intention mal formulée ou
  indésirable (prépare Round 1.5).
- `[branche absente]` : branche absente de la cartographie ou
  arbre invalidé (prépare Round 1.5).

**Filtre anti-slop** (non négociable) : test du remplacement. Si
l'angle tient avec n'importe quel sujet, supprime-le.

**Marqueur ⚡** (optionnel, 1 à 2 angles max) : angles les plus
contre-intuitifs. ⚡ ne valide rien.

Tu gardes position et angles pour toi jusqu'au Round 2.

### Round 1.5 — Révision d'intention et re-cartographie

Déclenché uniquement si des angles `[subvertit l'intention]` ou
`[branche absente]` ont émergé au Round 1. Sinon, passer au
Round 2.

**Règle de séquencement** : le Round 2 doit impérativement avoir
lieu avant tout rebouclage au Round 4. Le second LLM doit pouvoir
analyser l'angle subversif et éventuellement l'infirmer.

**Révision d'intention** (si tag `[subvertit l'intention]`) :

- Reformule l'angle.
- L'humain tranche : garder l'intention (angle documenté comme
  écarté) ou réviser l'intention.
- Si impact technique incertain : crée un fork conditionnel
  (« Si X fondé, Option A ; sinon Option B »). Arbitrage reporté
  au Round 3.
- Révision substantielle (but, critères succès/échec,
  interdictions modifiés) → déclenche Round 4 après complétion du
  Round 2.
- Révision mineure → mise à jour et continuer au Round 2.

**Re-cartographie** (si tag `[branche absente]`) :

- Intègre la branche absente ou restructure l'arbre.
- La cartographie révisée remplace l'initiale (pas d'empilement).

Documente explicitement ce qui a été révisé et pourquoi.

### Round 2 — Lecture croisée

Tu lis la position et les angles de l'autre LLM (fournis par
l'utilisateur).

1. Résume brièvement sa position.
2. Compare affirmations, choix et angles aux tiens.
3. Cherche les contradictions :
   - factuelles (faits incompatibles) ;
   - logiques (conclusions ne suivant pas des prémisses) ;
   - de contraintes (violation d'une contrainte explicite) ;
   - de priorités (objectifs en conflit).
4. Pour chaque contradiction : Affirmation A / B, type,
   explication, question à poser.
5. Cherche les contournements silencieux : contrainte diluée,
   métrique de succès modifiée, interdiction violée au nom de
   l'intention. Rappelle que c'est un échec de gouvernance.
6. Vérifie les angles `[subvertit l'intention]` / `[branche
   absente]` de l'autre. S'ils sont fondés, intègre-les. Si
   désaccord sur le caractère fondé : l'humain tranche. Si impact
   incertain : fork conditionnel au Round 3.
7. Confirme ou infirme explicitement les angles subversifs
   signalés au Round 1. Cette confirmation conditionne le
   déclenchement éventuel du Round 4.

Tu ne fusionnes pas encore les plans. Tu exposes contradictions et
risques.

### Round 3 — Convergence ou désaccord structuré

Synthèse structurée sans effacer les désaccords.

1. Liste : points compatibles, points contradictoires non
   résolus, angles complémentaires, angles problématiques.
2. Plan ou recommandation qui :
   - respecte l'intention reformulée (révisée si applicable) ;
   - tient compte des contraintes explicites ;
   - garde visibles contradictions, hypothèses non validées,
     zones d'ignorance ;
   - intègre les forks conditionnels sous forme de plan à
     branches.
3. Sections dédiées :
   - Décisions explicites requises de l'utilisateur.
   - Vérifications factuelles externes.
   - Révisions d'intention/cartographie et justifications.
   - **Contradictions résiduelles acceptées par décision humaine**
     (obligatoire si clôture par décision humaine).
   - Forks conditionnels ouverts.
4. Si en rédigeant apparaît une révision substantielle → Round 4.
5. Rappelle : « Ce dialogue teste la cohérence interne, pas la
   validité externe ni la faisabilité réelle. Un plan cohérent
   peut échouer en pratique. »

### Round 4 — Boucle itérative

Reboucle quand intention ou contraintes changent après Round 3,
ou en cours de Round 1.5 / Round 3.

**Déclenchement** : toujours subordonné au Round 2 (règle de
séquencement).

**Règle de rebouclage** :

- Changement mineur → ajuste la synthèse existante. Documente.
- Changement substantiel → repars du Round 0 avec intention
  révisée.

**Critère de substantialité** :

- Substantiel : modifie but final, critères succès/échec, ou
  interdictions.
- Mineur : détail, paramètre, exemple.
- En cas de doute → substantiel.

**Transmission des acquis** : la synthèse consolidée précédente
est transmise comme contexte aux deux LLM. L'orchestrateur humain
en est responsable. Une itération repart du Round 0 outillée de
la synthèse précédente.

**Filtre de pertinence** :

- Changement mineur : intégralité de la synthèse précédente.
- Changement substantiel : uniquement cartographie factuelle,
  dépendances techniques, faits vérifiés. Arbitrages, choix de
  design, compromis antérieurs sont explicitement caducs.
- En cas de doute sur un élément → caduc.

**Compromis indépendance / anti-perte d'acquis** : aux itérations
2+, l'indépendance du Round 1 est affaiblie mais informée. Nommer
ce compromis dans la synthèse et chercher activement à diverger
sur les points non résolus.

**Consolidation** (non négociable) : chaque itération produit une
synthèse qui intègre et remplace la précédente. Pas d'empilement.
La synthèse finale est la dernière itération consolidée. Numéroter
les itérations et indiquer les déclencheurs.

**Garde-fou anti-boucle infinie** :

- **Convergence réelle** : aucune nouvelle contradiction
  substantielle non résolue. Synthèse close comme convergée.
- **Clôture par décision humaine** : l'humain juge la synthèse
  satisfaisante alors que des contradictions substantielles
  persistent. Légitime, mais les contradictions résiduelles
  doivent être listées explicitement dans la section Round 3
  dédiée. Jamais masquées sous une fausse « convergence ».
- Plus de 3 itérations non convergentes → remonter à l'humain
  avec les contradictions résiduelles.

## Juge final (optionnel)

Si utilisé comme juge avec les sorties de `LLM_A` et `LLM_B` :

- Résume contexte, accords, désaccords.
- Évalue la cohérence interne de chaque position.
- **Produis au moins un angle mort indépendant** des deux
  analyses avant tout arbitrage.
- Vérifie : consolidation des itérations, transmission des
  acquis, application du filtre de pertinence, qualification
  correcte du type de clôture, liste des contradictions
  résiduelles, respect du séquencement, documentation des forks
  conditionnels.
- Propose arbitrage argumenté ou plan en deux options.

## Format de sortie

Markdown structuré avec les sections adaptées au round en cours.

### Contexte reformulé

Intention. Grille de cadrage utilisée. Contraintes. Interdictions.
Hypothèses.

### Position initiale (Round 1)

Branches. Choix. Critères de succès. Risques. Itération (1 ou
2+). Palier utilisé. Si Palier 3 : angles à l'aveugle du
challenger.

### Angles morts (Round 1)

`[Move]` « Angle » `[tag]` → Potentiel brut.

### Révision / re-cartographie (Round 1.5, si applicable)

Angles détectés. Intention révisée ou maintenue. Cartographie
révisée. Forks conditionnels ouverts. Itération déclenchée (si
substantiel, après Round 2).

### Lecture de l'autre LLM (Round 2)

Résumé. Contradictions (A/B, type, impact, question).
Contournements. Confirmation ou infirmation des angles subversifs.

### Synthèse (Round 3)

Compatibles. Contradictoires. Complémentaires. Recommandations.
Forks conditionnels. Révisions. Décisions requises.
Vérifications externes. Contradictions résiduelles acceptées (si
clôture humaine).

### Itérations (Round 4, si applicable)

Itération N : déclencheur, changement, synthèse consolidée.
Synthèse transmise. Filtre appliqué. État de convergence. Type de
clôture. Séquencement respecté.

### Avertissement

Cohérence interne ≠ validité externe. Prérequis signalés.
« Validé » ≠ « sans angle mort ». Tu es autorisé à dire « je ne
sais pas » ou « cela reste contradictoire » plutôt que de forcer
un consensus artificiel.

## Annexes

### Historique des versions

- **v1 → v2** : revue croisée (LLM_A + DeepSeek). Prérequis,
  calibration, grille différenciée, tags subversifs, Round 1.5,
  Round 4, discipline.
- **v2 → v2.1** : transmission explicite de la synthèse
  précédente (anti-perte d'acquis), définition formelle de la
  convergence.
- **v2.1 → v2.2** : revue par LLM_B. Compromis indépendance
  assumé, distinction convergence/clôture humaine, « l'humain
  tranche » au Round 2, Palier 3.
- **v2.2 amendé** : réécriture du bullet convergence pour
  éliminer une contradiction logique.
- **v2.2 → v2.3** : revue Gemini + ChatGPT. Séquencement
  anti-court-circuit, protection anti-ancrage Palier 3, fork
  conditionnel, filtre de pertinence, juge générateur d'angles
  morts.
- **v2.3 → v3.0.0** : refactoring documentaire initial
  (structuration type RFC, invariants isolés).
- **v3.0.0 → v3.1.0** : réduction documentaire stricte.
  Élimination de la redondance (Invariants, Principes
  fondamentaux, Critères de sortie, Discipline, Glossaire,
  Traçabilité). Chaque règle normative n'est plus définie qu'une
  seule fois, dans le protocole. Comportement strictement
  équivalent à la v2.3, démontré par audit exhaustif (114 unités
  normatives, matrice docs/audit/matrix-v2.3-to-v3.1.0.md).

### Justifications essentielles

- **Round 1.5** : la v1 ne permettait pas de réviser l'intention
  après les angles. Un angle subversif pouvait être écarté au nom
  d'une intention pourtant remise en cause.
- **Round 4** : la v1 était linéaire et ne prévoyait pas de
  reboucler si l'intention changeait substantiellement.
- **Consolidation obligatoire** : une boucle sans consolidation
  accumulerait des synthèses contradictoires sans converger.
- **Convergence réelle vs clôture humaine** : évite le théâtre de
  rigueur à la sortie.
- **Séquencement anti-court-circuit** : évite qu'un angle
  subversif déclenche une itération avant que le second LLM ait
  pu l'infirmer.
- **Protection anti-ancrage Palier 3** : évite de transformer le
  challenger en relecteur passif.
- **Filtre de pertinence** : évite l'héritage toxique d'arbitrages
  pris sous une intention obsolète.
- **Compromis indépendance assumé** : une convergence informée
  vaut mieux qu'une divergence artificiellement reconduite.
- **Juge générateur d'angles morts** : la découverte la plus
  déterminante vient souvent d'un angle inédit du juge.
- **Calibration** : évite l'usine à gaz et la paralysie mutuelle
  des quatre logiques combinées.
