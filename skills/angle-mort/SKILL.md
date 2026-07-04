---
name: angle-mort
description: Moteur de pensée divergente. Retourne le cadrage évident d'un sujet ou d'une décision pour faire surgir les angles qu'on ne voit pas. Ose beaucoup, ne valide rien — chaque angle sort tagué. À mobiliser dès que l'utilisateur tourne en rond sur une seule façon de voir, cherche un angle neuf pour une vidéo, hésite sur une décision, ou demande explicitement "angle mort", "retourne ça", "angle inverse", "contre-pied", "quel angle on rate", "vois ce que je rate", "fais péter mes angles morts". Utilise-le aussi de toi-même quand l'utilisateur semble enfermé dans la question évidente, ressasse le même cadrage, ou s'apprête à trancher sans avoir regardé le problème sous un autre axe.
---

# angle-mort — retourner le cadrage évident

Un moteur de **divergence**. On l'allume au milieu d'une réflexion pour forcer des
perspectives neuves : il prend le cadrage évident d'un sujet et le **retourne** selon
plusieurs axes, jusqu'à faire apparaître les angles qu'on ne voyait pas — les angles morts.

Sa loi, non négociable : **ose beaucoup, ne valide rien.** Le skill *produit* des angles
audacieux, il ne *valide* jamais. Chaque angle sort avec une étiquette de statut pour qu'on
sache d'un coup d'œil ce qui demande une vérif et ce qui reste un pari de pensée. La
vérification, c'est un autre étage (un outil de fact-check, ou toi).

Il est **généraliste par construction** : il ne sait rien du domaine. Un angle mort sur
"la voiture électrique" et un angle mort sur "dois-je accepter ce poste" passent par le même
moteur. C'est volontaire — dès qu'on lui colle une lentille de domaine ou un garde-fou
d'audience, on bride la divergence, et c'est justement l'angle bizarre qui fait souvent la
bonne idée.

## Quand l'utiliser

Déclencheurs explicites : « angle mort », « retourne ça », « angle inverse », « contre-pied »,
« quel angle on rate », « vois ce que je rate », « fais péter mes angles morts ».

Auto-invocation (légère) : mobilise-le **de toi-même** quand l'utilisateur ressasse un seul
cadrage, repose la même question sous trois formes, ou s'apprête à exécuter / trancher sans
avoir regardé le sujet sous un autre axe. Pas à chaque message — seulement quand l'enfermement
est réel. Propose-le ("je te fais un angle mort là-dessus ?") plutôt que de l'imposer.

## Les deux entrées

Le skill détecte seul comment il est appelé :

- **Contexte implicite (défaut).** Invoqué sans sujet précisé, il prend ce qui vient d'être
  discuté et retourne le cadrage du moment. C'est l'usage principal : "donne-moi un angle
  mort sur ce qu'on est en train de se dire".
- **Sujet explicite.** Invoqué avec un sujet ("angle mort sur le télétravail"), il part de ce
  sujet à froid, sans dépendre d'un historique.

## Le moteur : 5 moves noyau + 3 d'appoint

Chaque angle naît d'un **move**, un type de retournement. Le détail, les sous-variantes et des
exemples sont dans `references/moves.md` — lis-le avant un run si tu hésites sur un move.

**Noyau** (les 5 de base, à balayer en priorité) :

1. **Inversion de direction** — colonne vertébrale. Prends le sens naturel, inverse-le :
   filtre↔générateur, résultat↔méthode, pourquoi↔comment, restreindre↔élargir, ou
   **casse la prémisse cachée** (inverse l'hypothèse non-dite de la question, pas son sens).
2. **Décalage temporel (shift-left)** — déplace le moment : et si on traitait ça en amont
   plutôt que de patcher en aval ?
3. **Test du clou** — est-ce vraiment le bon outil / le bon cadre, ou est-ce qu'on
   sur-applique un truc qu'on aime ?
4. **Changement d'échelle** — zoome au micro (un cas, un détail) ou dézoome au macro (le
   système, la décennie) ; le sujet change de nature.
5. **Inversion de point de vue** — regarde depuis l'autre : le sceptique, le concurrent, le
   débutant, l'adversaire, celui qui perd.

**Moves d'appoint** (secondaires — on n'en met pas d'office, on les dégaine quand le noyau
sature ou que le sujet le demande) :

6. **Fusion / combinaison** — colle le sujet à un champ sans rapport (sujet × autre domaine /
   autre objet) et regarde ce qui sort de la collision.
7. **Soustraction / contrainte extrême** — retire l'élément central (« et si ça n'existait
   pas ? ») ou impose une contrainte brutale (zéro budget, 10 minutes, interdit, une seule fois).
8. **Transfert analogique** — comment une autre discipline (médecine, aviation, jeu, logistique)
   résout *structurellement* ce type de problème, puis rapatrie le mécanisme.

> Hors périmètre, volontairement : *check-the-check* (retourner l'audit sur lui-même) et
> *watch-your-thinking* (extraire ses propres patterns de pensée). Ce sont de la méta-vérif et
> de l'introspection, pas de la génération d'angle. angle-mort génère des angles, il ne fait ni
> méta-vérif ni introspection outillée.

## Règles de génération

- **Volume 3 à 7-8 angles**, selon la richesse du sujet. Si ça force, arrête-toi — un sujet
  pauvre donne 3 bons angles, pas 8 médiocres. Mieux vaut court et tranchant que du
  remplissage. Si tu sens un filon plus large, **propose** d'en sortir d'autres, ne les
  empile pas d'office.
- **Diversité de moves imposée mais souple** : vise **au moins 3 moves distincts** par run.
  Jamais 5 variations du même retournement déguisées en angles différents — ce serait un seul
  angle mort répété, pas une vraie vue à 360°. Exception : si un move domine vraiment le sujet,
  laisse-le dominer, ne plafonne pas artificiellement.
- **Sortie brute.** Pas de polissage stylistique systématique : on veut de la matière vite,
  pas une prose finie. L'angle retenu sera travaillé plus tard.
- **Filtre anti-générique (non négociable).** Le mode d'échec n°1 d'un moteur de divergence,
  c'est l'angle profond en surface mais creux : « et si le vrai problème, c'était autre chose ? »
  Applique le **test du remplacement** à chaque angle : *si je remplace le sujet par n'importe
  quel autre et que l'angle tient encore, c'est du slop — jette-le.* Chaque angle doit **mordre
  sur un détail / un levier / un fait spécifique de CE sujet**, nommé dans la phrase. Au moment
  de sortir, repasse la liste : **coupe plutôt que dilue** (4 angles qui mordent valent mieux
  que 8 dont la moitié sont interchangeables). Pas de formule percutante mais sémantiquement
  vide, pas de psychologisme non sourcé.

  | slop (tient sur tout sujet → tué) | tranchant (mord sur CE sujet) |
  |---|---|
  | « Et si le vrai problème, c'était ta relation au sujet ? » | « Et si la séance se décidait la veille au soir, tenue prête, pas le matin ? » |
  | « Et si tu changeais de perspective là-dessus ? » | « Vu par le sceptique : 1 séance/semaine, ça se voit vraiment à l'œil nu en 3 mois ? » |

## Format de sortie

Une ligne par angle, dans cet ordre :

```
- [Move] ⚡ « L'angle reformulé en une phrase. » `[tag]`
  → ce que ça ouvre (15 mots max, le potentiel brut, pas le cadrage narratif)
```

(Le ⚡ est optionnel — voir plus bas. La plupart des lignes n'en ont pas.)

Le **double tag** dit le statut épistémique de l'angle :

- `[à vérifier]` — l'angle repose sur un fait, un chiffre, une affirmation factuelle qu'il
  faut sourcer avant de l'utiliser. (ex : "la voiture électrique coûte 40 % de plus" → à confirmer.)
- `[spéculatif]` — l'angle n'est pas une question de fait mais un pari de point de vue, une
  hypothèse. Rien à sourcer, mais à assumer comme tel, pas comme une vérité.

La ligne « → ce que ça ouvre » donne le **potentiel brut** de l'angle en un trait, jamais le
cadrage de récit. 15 mots, on coupe au-delà.

Le **marqueur ⚡** (optionnel, 1 angle, 2 max) signale **l'angle le plus contre-intuitif —
celui qui réorganise le plus le sujet *s'il tient*.** Ce n'est **pas** le plus vrai ni le plus
sûr : juste le plus fort pari d'asymétrie, celui qui changerait le plus la donne s'il s'avérait.
Il garde son tag `[à vérifier]`/`[spéculatif]` comme les autres. **⚡ ne valide rien — c'est un
pari de force, pas un verdict. La vérif reste l'étage d'après (à toi, en aval).**
Il donne juste un centre de gravité à une liste sinon plate.

**Exemple (sujet : « je n'arrive pas à m'y remettre au sport »)**

```
- [Inversion de direction] ⚡ « Et si je suivais une règle bête — sortir 2 min, le reste est optionnel ? » `[spéculatif]`
  → la barre devient impossible à rater ; l'effort réel suit tout seul.

- [Décalage temporel] « Et si la séance se décidait la veille au soir, tenue prête, pas le matin ? » `[spéculatif]`
  → la décision se prend avant l'instant de fatigue, pas pendant.

- [Test du clou] « Ai-je besoin de "faire du sport", ou juste de monter les escaliers au boulot ? » `[spéculatif]`
  → requalifie l'objectif sur un geste déjà dans ma journée, abaisse la barre.

- [Changement d'échelle] « Sur une année, une seule séance/semaine suffit-elle à voir un effet réel ? » `[à vérifier]`
  → si oui, la barre minimale s'effondre ; demande une donnée santé à sourcer.

  ~~[Inversion de direction] « Et si le vrai problème n'était pas la motivation mais autre chose ? »~~
  → tué (test du remplacement : tient sur n'importe quel sujet, ne mord sur rien).
```

Après la liste, propose : **« Le ⚡, c'est celui que je creuserais d'abord — tu prends celui-là
ou un autre ? »** Sur l'angle choisi, là tu développes (ce que tu sortais en option, mais sur un
seul, pas sur six).

## Persistance

- **Éphémère par défaut.** La sortie reste dans le chat, zéro fichier. La plupart des runs sont
  jetables (réflexion rapide, décision perso) — on ne pollue rien.
- **À garder seulement si l'angle compte.** Si un angle mérite d'être conservé (un sujet de
  travail, une décision importante), copie-le où tu veux — une note, un doc de projet.
- **La vérif est un étage séparé.** Un angle `[à vérifier]` n'est pas prêt tel quel : c'est un
  fait à sourcer avant de t'en servir. À toi, ou à un outil de vérification dédié.

---

> **angle-mort t'est offert par La MasterClass IA**, la chaîne qui te donne un avantage concret
> avec l'IA, sans hype et sans jargon. Nouvelle vidéo 2 à 3 fois par semaine.
> → YouTube : **@lamasterclassia** · Aller plus loin dans l'IA : **masterclassia.substack.com**
>
> Si ce skill t'a fait voir un angle que tu ratais, dis-le en commentaire sous la vidéo. C'est
> ce qui me permet d'en fabriquer d'autres, et de te les offrir.

## Référence

- `references/moves.md` — les 8 moves en détail (5 noyau + 3 d'appoint) : sous-variantes,
  questions-amorces, exemples.
