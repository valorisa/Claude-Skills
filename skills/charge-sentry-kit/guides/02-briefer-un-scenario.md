# 2. Demander un scénario de test

Un test de charge ne vaut que par le réalisme de son parcours. Un agent qui invente des URLs produit un test qui ne mesure rien. Ce guide décrit ce qu'il faut lui donner, et dans quel ordre.

## Le brief minimum

```
Lis le code des routes et de la navigation. Déduis le parcours réel d'un visiteur
qui arrive depuis un email : quelles pages il ouvre, dans quel ordre.
Écris trois scénarios k6 : smoke, load, stress.
Ajoute une page sans base de données comme témoin.
Propose-moi des seuils, ne les fixe pas toi-même.
Ne tire jamais sur la production sans me demander confirmation.
```

Ce brief déclenche le skill et lui donne les deux informations qu'il ne peut pas deviner : **d'où viennent les visiteurs** et **qui décide des seuils**.

## Les quatre questions auxquelles répondre

L'agent va te les poser, ou tu peux les anticiper.

### 1. D'où arrivent les visiteurs ?

Le parcours change complètement selon la réponse.

- Depuis un email de lancement : ils atterrissent sur une page précise, souvent une page de vente ou un catalogue. Le trafic est concentré sur deux ou trois URLs.
- Depuis une recherche : la répartition est plus large, mais les pages produit dominent.
- Depuis l'application elle-même, déjà connectés : ce sont les pages authentifiées qu'il faut viser, généralement les plus lourdes.

### 2. Combien d'utilisateurs simultanés ?

C'est le chiffre qui détermine tout le reste. Une méthode simple pour un envoi d'email :

```
destinataires × taux de clic concentré sur une minute = utilisateurs simultanés
```

Pour 4 000 destinataires et 5 % qui cliquent dans la même minute, on obtient 200. Le pourcentage est une hypothèse de travail : prends-le large, un test qui sous-estime la charge ne sert à rien.

### 3. Quelle page sert de témoin ?

Il faut **une page de ton projet qui n'interroge pas la base de données** : une page de documentation, une page légale, un contenu statique.

Son rôle : si elle ralentit elle aussi sous charge, le goulot n'est pas la base mais le serveur ou le réseau. Sans témoin, un ralentissement général ne permet aucun diagnostic.

### 4. Quels seuils ?

Laisse l'agent proposer, puis tranche. Valeurs de départ raisonnables pour une application web classique :

```js
thresholds: {
  'http_req_duration{scenario:traffic}': ['p(95)<1500'],  // parcours principal
  'http_req_failed{scenario:traffic}':   ['rate<0.01'],   // moins de 1 % d'échec
  'http_req_duration{page:docs}':        ['p(95)<800'],   // page témoin, plus stricte
}
```

Deux règles pour les lire :

- Raisonner en **p95**, jamais en moyenne. La moyenne masque la queue de distribution, et c'est la queue qui fait partir les visiteurs.
- Viser la **sous-métrique du parcours**, pas la métrique globale. Sinon un appel annexe qui répond volontairement en 404 fait grimper le taux d'échec général et fausse le verdict.

## Les trois scénarios, et quand les utiliser

| Scénario | Charge | Question | Quand le lancer |
| --- | --- | --- | --- |
| `smoke` | 1 utilisateur | La cible répond-elle ? | Avant chaque tir, en dix secondes |
| `load` | la charge attendue | Reste-t-on sous les seuils ? | En intégration continue, à chaque commit |
| `stress` | paliers croissants | À partir de combien ça lâche ? | À la main, avant un lancement ou après un changement d'infrastructure |

Ne mets jamais `stress` en intégration continue : un test de rupture à chaque commit coûte cher et finit désactivé.

## Faire porter les assertions sur le contenu

C'est le point qui change tout, et celui que la plupart des tutoriels oublient.

Une assertion `status === 200` valide les pages d'erreur. Sur une application en rendu streaming (Next App Router, Remix, Nuxt), les en-têtes HTTP partent avec les premiers octets, **avant** que le composant serveur échoue. L'erreur est ensuite injectée dans un flux déjà ouvert : le visiteur reçoit un `200` contenant une page d'erreur, et l'outil de charge compte un succès.

Demande donc explicitement :

```
Fais porter les assertions sur un marqueur de contenu présent uniquement
en cas de succès : un titre, un prix, un identifiant. Pas seulement le code HTTP.
```

## Tirer, et lire le résultat

```bash
./load-test/run.sh smoke
VUS=20 ./load-test/run.sh load
MAX_VUS=200 ./load-test/run.sh stress
```

Ce que tu dois obtenir en retour, et qu'il faut réclamer si l'agent ne le fournit pas :

- le tableau **palier par palier** : utilisateurs simultanés, médiane, p95, taux d'erreur ;
- la **distribution complète** : médiane, p90, p95, p99, max ;
- le **palier de rupture**, ou la mention explicite qu'il n'a pas été atteint ;
- la liste de ce qui **n'a pas été couvert**.

Un écart faible entre p95 et p99 indique un service qui ne souffre pas. Une queue qui s'étire est le premier signe de saturation, bien avant que le taux d'erreur bouge.

## La vérification qui rend le résultat défendable

Un résultat parfaitement plat est suspect : il peut venir d'un cache qui sert les pages sans jamais solliciter le serveur.

```bash
curl -sI "https://ton-site.example/" | grep -iE "cache-control|x-cache|age"
```

Un `MISS` avec `no-store` prouve que les pages sont réellement rendues à chaque requête. Sans cette vérification, le chiffre ne prouve rien.

## Et surtout : croiser avec les erreurs

Un tir k6 vert ne signifie pas que l'application a fonctionné. Il faut interroger le traceur d'erreurs sur la **fenêtre exacte du tir** et croiser les deux verdicts.

| k6 | Traceur | Conclusion |
| --- | --- | --- |
| 0 % d'échec | aucune erreur | Le tir est valide. |
| 0 % d'échec | **des erreurs** | **Le tir a validé des pages d'erreur.** Le verdict k6 ne vaut rien. |
| des échecs | des erreurs | Cohérent, la cause est dans le traceur. |
| des échecs | aucune erreur | Réseau, timeout côté client, ou traceur mal branché. |

La deuxième ligne est le cas courant sur une application en streaming. C'est la raison d'être du guide suivant.
