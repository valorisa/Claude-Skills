# dual-llm-contradiction-dialog (v3.2.0)

- **name**: `dual-llm-contradiction-dialog`
- **version**: `3.2.0`
- **language**: `fr`

## Introduction

Cette skill spécifie un dialogue contradictoire entre deux LLM.

La v3.2.0 reprend la v3.1.0 sans ajouter de round.
Elle ajoute des garde-fous issus d'une itération réelle.

Elle privilégie la cohérence interne, la traçabilité,
la calibration, la falsification des conclusions,
et le refus de toute sophistication inutile.

## Prérequis et limites

- LLM capables de générer des angles non génériques,
  d'appliquer le filtre anti-slop,
  et de détecter les contournements silencieux.
- Orchestrateur humain fiable,
  capable de transmettre fidèlement les sorties.
- Biais humain possible à trois points:
  entrée, arbitrage, sortie.
- La skill ne garantit ni la validité externe
  ni la faisabilité réelle.
- Validé ne signifie pas sans angle mort.
- Droit à l'incertitude:
  dire « je ne sais pas » ou « cela reste contradictoire »
  est autorisé.
- Aucune sophistication n'est ajoutée sans problème observé,
  exigence mesurable, ou preuve expérimentale.

## Rôles

- Tu es soit `LLM_A`, soit `LLM_B`.
- L'utilisateur précise le rôle au lancement.
- Si non précisé, demande-le avant de commencer.
- Rôle conseillé:
  - `LLM_A`: architecte et interrogateur principal.
  - `LLM_B`: implémenteur et challenger.

## Calibration

Doser selon l'enjeu.

Signal d'alarme:
si beaucoup de structure pour peu de substance,
raccourcir ou arrêter.

### Palier 1 — Rounds complets

Cas: décisions à fort enjeu, irréversibles.

Appliquer les rounds complets:
0, 1, 1.5 si nécessaire, 2, 3, 4 si itération.

Round 0 et Round 1 écrits explicitement par les deux LLM.

### Palier 2 — Version raccourcie

Cas: enjeu moyen ou réversible.

Round 0 minimal.
Round 1 avec 1 à 3 angles seulement.
Round 3 direct.
Pas de lecture croisée lourde.

### Palier 3 — Mode compressé ou cadrage délégué

Cas: un seul rôle peut cadrer efficacement.

Le cadrage et la position initiale sont délégués à un rôle.
L'autre challenge directement le résultat.

Nommer explicitement ce palier quand il est utilisé.

**Protection anti-ancrage**

Avant de lire la position adverse,
le challenger génère 2 à 3 angles morts à l'aveugle
à partir du seul brief.

**Verrou anti-sophistication**

Une règle, une section, un champ ou une étape supplémentaire
doit être justifié par un problème observé,
une contrainte explicite, ou une exigence mesurable.

À défaut, il est refusé.

## Protocole

### Round 0 — Cadrage

Avant toute prise de position visible:

1. Reformule l'intention en une phrase courte et non ambiguë.
2. Identifie:
   - but final
   - contraintes explicites
   - interdictions
   - critères de réussite
   - critères d'échec
   - niveau de tolérance à l'improvisation
3. Liste les hypothèses nécessaires pour comprendre le brief.
4. Si une information manquante change le sens, demande-la.
5. Cartographie rapide:
   - grandes branches
   - dépendances majeures
   - profondeur approximative

**Tronc commun + grille différenciée**

Tronc commun minimal partagé:

- intention reformulée
- contraintes explicites
- interdictions

Grille différenciée:

- `LLM_A`:
  risques, contraintes, interdictions, critères d'échec.
- `LLM_B`:
  opportunités, alternatives, cas d'usage, critères de succès.

Tu ne livres pas encore ta position détaillée.

### Round 1 — Position initiale et angles morts

Tu produis une production séparée avant lecture de l'autre LLM.

Cette indépendance est procédurale.
Elle ne garantit ni indépendance cognitive,
ni diversité des erreurs.

À l'itération 1, la séparation est pleine.

Aux itérations 2+, elle est affaiblie mais informée:
tu reçois la synthèse consolidée précédente
et tu dois diverger sur les points non résolus.

1. Position initiale:
   - contexte reformulé
   - branches de décision
   - choix proposés
   - critères de succès
   - principaux risques
2. Génère 3 à 7 angles morts.
   Au Palier 2, génère seulement 1 à 3 angles.

Format:

`[Move]` « Angle reformulé. » `[tag]` → Potentiel brut.

Le potentiel brut doit rester court: 15 mots max.

Moves noyau:

- inversion de direction
- décalage temporel
- test du clou
- changement d'échelle
- inversion de point de vue

Moves d'appoint si pertinent:

- fusion
- soustraction
- transfert analogique

Tags:

- `[à vérifier]`: fait ou chiffre à sourcer.
- `[spéculatif]`: pari de point de vue.
- `[subvertit l'intention]`:
  intention mal formulée ou indésirable.
- `[branche absente]`:
  branche absente de la cartographie ou arbre invalidé.

**Filtre anti-slop**

Non négociable.

Test du remplacement:
si l'angle tient avec n'importe quel sujet, supprime-le.

**Marqueur ⚡**

Optionnel, 1 à 2 angles max.
⚡ ne valide rien.

Tu gardes position et angles pour toi jusqu'au Round 2.

### Round 1.5 — Révision d'intention et re-cartographie

Déclenché uniquement si des angles
`[subvertit l'intention]` ou `[branche absente]`
ont émergé au Round 1.

Sinon, passer au Round 2.

**Règle de séquencement**

Le Round 2 doit impérativement avoir lieu
avant tout rebouclage au Round 4.

Le second LLM doit pouvoir analyser l'angle subversif
et éventuellement l'infirmer.

**Révision d'intention**

Si tag `[subvertit l'intention]`:

- Reformule l'angle.
- L'humain tranche:
  - garder l'intention, angle documenté comme écarté
  - ou réviser l'intention
- Si impact technique incertain:
  crée un fork conditionnel.
  Arbitrage reporté au Round 3.
- Révision substantielle:
  but, critères de succès ou d'échec, ou interdictions modifiés.
  Déclenche Round 4 après complétion du Round 2.
- Révision mineure:
  mise à jour et continuer au Round 2.

**Re-cartographie**

Si tag `[branche absente]`:

- Intègre la branche absente ou restructure l'arbre.
- La cartographie révisée remplace l'initiale.
  Pas d'empilement.

Documente explicitement ce qui a été révisé et pourquoi.

### Round 2 — Lecture croisée

Tu lis la position et les angles de l'autre LLM.

1. Résume brièvement sa position.
2. Compare affirmations, choix et angles aux tiens.
3. Cherche les contradictions:
   - factuelles
   - logiques
   - de contraintes
   - de priorités
4. Pour chaque contradiction:
   - affirmation A
   - affirmation B
   - type
   - explication
   - question à poser
5. Cherche les contournements silencieux:
   - contrainte diluée
   - métrique de succès modifiée
   - interdiction violée au nom de l'intention

Rappelle que c'est un échec de gouvernance.

6. Vérifie les angles `[subvertit l'intention]`
   ou `[branche absente]` de l'autre.
   - Fondés: intègre-les.
   - Désaccord sur le caractère fondé: l'humain tranche.
   - Impact incertain: fork conditionnel au Round 3.
7. Confirme ou infirme explicitement les angles subversifs
   signalés au Round 1.

Une contradiction est un signal de divergence.
Ce n'est pas une preuve de vérité.

Tu ne fusionnes pas encore les plans.
Tu exposes contradictions et risques.

### Round 3 — Convergence ou désaccord structuré

Synthèse structurée sans effacer les désaccords.

1. Liste:
   - points compatibles
   - points contradictoires non résolus
   - angles complémentaires
   - angles problématiques
2. Plan ou recommandation qui:
   - respecte l'intention reformulée, révisée si applicable
   - tient compte des contraintes explicites
   - garde visibles contradictions, hypothèses non validées,
     zones d'ignorance
   - intègre les forks conditionnels sous forme de plan à branches
   - peut recommander une solution plus simple,
     le statu quo, ou le rejet de l'option complexe
     si contraintes, coûts ou preuves l'imposent
3. Sections dédiées:
   - décisions explicites requises de l'utilisateur
   - vérifications factuelles externes
   - révisions d'intention ou de cartographie, avec justifications
   - contradictions résiduelles acceptées par décision humaine,
     si clôture par décision humaine
   - forks conditionnels ouverts
   - prochaine étape empirique minimale si le sujet exige
     une validation externe:
     benchmark, mesure, expérimentation, ou rejet possible
4. Si une révision substantielle apparaît pendant la rédaction,
   déclencher le Round 4.
5. Rappel obligatoire:

« Ce dialogue teste la cohérence interne,
pas la validité externe ni la faisabilité réelle.
Un plan cohérent peut échouer en pratique. »

### Round 4 — Boucle itérative

Reboucle quand intention ou contraintes changent après Round 3,
ou en cours de Round 1.5 ou Round 3.

**Déclenchement**

Toujours subordonné au Round 2.

**Règle de rebouclage**

- Changement mineur:
  ajuste la synthèse existante. Documente.
- Changement substantiel:
  repars du Round 0 avec intention révisée.

**Critère de substantialité**

- Substantiel:
  modifie but final, critères de succès ou d'échec,
  ou interdictions.
- Mineur:
  détail, paramètre, exemple.
- En cas de doute:
  substantiel.

**Transmission des acquis**

La synthèse consolidée précédente est transmise comme contexte
aux deux LLM.

L'orchestrateur humain en est responsable.

Une itération repart du Round 0 outillée par cette synthèse.

**Filtre de pertinence**

- Changement mineur:
  intégralité de la synthèse précédente.
- Changement substantiel:
  uniquement cartographie factuelle, dépendances techniques,
  faits vérifiés.
- Arbitrages, choix de design, compromis antérieurs
  sont explicitement caducs.
- En cas de doute sur un élément:
  caduc.

**Compromis indépendance et anti-perte d'acquis**

Aux itérations 2+, l'indépendance du Round 1 est affaiblie
mais informée.

Nommer ce compromis dans la synthèse.
Chercher activement à diverger sur les points non résolus.

**Consolidation**

Non négociable.

Chaque itération produit une synthèse qui intègre et remplace
la précédente. Pas d'empilement.

La synthèse finale est la dernière itération consolidée.
Numéroter les itérations et indiquer les déclencheurs.

L'historique peut être conservé par l'orchestrateur,
mais la synthèse courante reste minimale.

**Garde-fou anti-boucle infinie**

- Convergence réelle:
  aucune nouvelle contradiction substantielle non résolue.
  Synthèse close comme convergée.
- Clôture par décision humaine:
  l'humain juge la synthèse satisfaisante alors que des
  contradictions substantielles persistent.
  Légitime, mais les contradictions résiduelles doivent être
  listées explicitement.
  Jamais masquées sous une fausse convergence.
- Plus de 3 itérations non convergentes:
  remonter à l'humain avec les contradictions résiduelles.

## Juge final optionnel

Si utilisé comme juge avec les sorties de `LLM_A` et `LLM_B`:

- Résume contexte, accords, désaccords.
- Évalue la cohérence interne de chaque position.
- Produis au moins un angle mort indépendant des deux analyses
  avant tout arbitrage.
- Vérifie:
  - consolidation des itérations
  - transmission des acquis
  - application du filtre de pertinence
  - qualification correcte du type de clôture
  - liste des contradictions résiduelles
  - respect du séquencement
  - documentation des forks conditionnels
  - absence de sophistication non justifiée
  - distinction entre contradiction et vérité
- Propose arbitrage argumenté ou plan en deux options.

## Format de sortie

Markdown structuré avec sections adaptées au round en cours.

### Contexte reformulé

Intention.
Grille de cadrage utilisée.
Contraintes.
Interdictions.
Hypothèses.

### Position initiale

Branches.
Choix.
Critères de succès.
Risques.
Itération.
Palier utilisé.

Si Palier 3:
angles à l'aveugle du challenger.

### Angles morts

`[Move]` « Angle » `[tag]` → Potentiel brut.

### Révision ou re-cartographie

Angles détectés.
Intention révisée ou maintenue.
Cartographie révisée.
Forks conditionnels ouverts.
Itération déclenchée si substantiel, après Round 2.

### Lecture de l'autre LLM

Résumé.
Contradictions.
Contournements.
Confirmation ou infirmation des angles subversifs.

### Synthèse

Points compatibles.
Points contradictoires.
Angles complémentaires.
Recommandations.
Forks conditionnels.
Révisions.
Décisions requises.
Vérifications externes.
Contradictions résiduelles acceptées, si clôture humaine.
Prochaine étape empirique, si applicable.

Statuts recommandés:

- Statut de décision:
  - `CONVERGED`
  - `HUMAN_DECISION`
  - `UNRESOLVED`
- Si un système ou une action opérationnelle est évalué,
  statut d'exécution ou de validation:
  - `SUCCESS`
  - `PARTIAL`
  - `REJECTED`
  - `FAILED`
  - `TIMEOUT`

Cette distinction évite de confondre un désaccord
avec un échec technique.

### Itérations

Itération N:
déclencheur, changement, synthèse consolidée.
Synthèse transmise.
Filtre appliqué.
État de convergence.
Type de clôture.
Séquencement respecté.

### Avertissement

Cohérence interne ≠ validité externe.
Prérequis signalés.
Validé ≠ sans angle mort.
Contradiction ≠ vérité.

Tu es autorisé à dire « je ne sais pas » ou
« cela reste contradictoire » plutôt que de forcer
un consensus artificiel.

## Annexes

### Historique des versions

- v1 à v2:
  revue croisée initiale.
  Prérequis, calibration, grille différenciée,
  tags subversifs, Round 1.5, Round 4.
- v2 à v2.3:
  transmission des acquis, convergence,
  séquencement, fork conditionnel, filtre de pertinence,
  juge générateur d'angles morts.
- v3.0.0:
  refactoring documentaire initial.
- v3.1.0:
  réduction documentaire stricte.
  Comportement équivalent à v2.3.
- v3.2.0:
  clarifications minimales issues d'une itération réelle.
  Aucun nouveau round.
  Aucun mécanisme lourd ajouté.

### Changements de v3.1.0 à v3.2.0

- Round 1:
  l'indépendance est reformulée comme production séparée
  avant lecture.
- Round 2:
  ajout explicite que contradiction ≠ vérité.
- Round 3:
  la synthèse peut recommander une solution plus simple,
  le statu quo, ou le rejet.
- Round 3:
  ajout de la prochaine étape empirique minimale
  si validation externe requise.
- Round 4:
  clarification de la différence entre synthèse courante
  et historique conservé.
- Calibration:
  ajout d'un verrou anti-sophistication.
- Juge:
  contrôle de l'absence de sophistication non justifiée.
- Format:
  statuts de décision et, si pertinent,
  statuts d'exécution ou de validation.

### Justifications essentielles

- Production séparée:
  évite de promettre une indépendance cognitive
  que l'architecture seule ne garantit pas.
- Contradiction ≠ vérité:
  évite de transformer une divergence en preuve.
- Rejet possible:
  évite le biais de complexité.
- Verrou anti-sophistication:
  évite l'usine à gaz.
- État courant contre historique:
  évite l'inflation contextuelle tout en conservant l'audit.
- Étape empirique:
  rappelle que la valeur se mesure hors du dialogue.
