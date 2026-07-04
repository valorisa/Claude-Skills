# angle-mort

Un moteur de **pensée divergente** transversal. On l'allume au milieu d'une réflexion pour
retourner le cadrage évident d'un sujet ou d'une décision, et faire surgir les angles qu'on
ne voyait pas. Idéation de contenu, choix stratégique, décision perso : même moteur, le skill
ne sait rien du domaine.

Sa loi : **ose beaucoup, ne valide rien.** Il produit des angles audacieux, il ne valide
jamais. Un **filtre anti-générique** s'applique d'abord (le test du remplacement : un angle qui
tient sur n'importe quel sujet est du slop, on le jette) ; ce qui survit sort tagué `[à vérifier]`
(fait à sourcer) ou `[spéculatif]` (pari de point de vue). La vérification, c'est l'étage d'après
(un outil de fact-check, ou toi).

## Comment ça marche

- **Deux entrées.** Sans sujet précisé, il retourne ce qu'on est en train de discuter
  (défaut). Avec un sujet, il part de zéro dessus.
- **5 moves noyau + 3 d'appoint.** Noyau : inversion de direction, décalage temporel
  (shift-left), test du clou, changement d'échelle, inversion de point de vue. Appoint (quand le
  noyau sature) : fusion/combinaison, soustraction/contrainte extrême, transfert analogique.
  Détail dans `references/moves.md`.
- **Sortie.** 3 à 7-8 angles, au moins 3 moves distincts, chacun avec sa ligne « ce que ça
  ouvre ». Brut, rapide, à trier. Un marqueur **⚡** (1-2 max) pointe l'angle le plus
  contre-intuitif — un centre de gravité, **jamais une validation**. On creuse ensuite l'angle
  retenu.
- **Éphémère** par défaut ; garde un angle sur disque seulement s'il compte vraiment.

## Installation

1. Dézippe le dossier `angle-mort/`.
2. Ajoute-le à Claude comme skill (dépose le dossier là où Claude lit tes skills, ou
   importe-le depuis l'interface Skills).
3. Déclenche-le dans une conversation : « fais-moi un angle mort là-dessus », « retourne ce
   cadrage », ou laisse Claude le proposer quand tu tournes en rond.

## Fichiers

- `SKILL.md` — instructions complètes.
- `references/moves.md` — les 8 moves en détail, 5 noyau + 3 d'appoint (mécanique, amorces, exemples).

---

**angle-mort t'est offert par La MasterClass IA** — la chaîne qui te donne un avantage concret
avec l'IA, sans hype et sans jargon.
→ YouTube : **@lamasterclassia** · Aller plus loin dans l'IA : **masterclassia.substack.com**
