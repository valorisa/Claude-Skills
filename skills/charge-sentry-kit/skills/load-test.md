---
name: load-test
description: Construire et exécuter des tests de charge k6 sur une application web. Produit trois scénarios (smoke, load, stress), des seuils bloquants, un rapport lisible corrélé aux erreurs du traceur, et l'analyse du palier de rupture. Utiliser quand on demande "est-ce que ça tient ?", "test de charge", "combien d'utilisateurs simultanés", "on va prendre un pic de trafic", "load test", "stress test", "k6", ou avant un envoi massif d'emails / un lancement produit. NE PAS utiliser pour du profilage front (voir Chrome DevTools MCP) ni pour du monitoring d'erreurs en production (voir sentry-triage).
---

# Load Test

Monte un harnais de test de charge réutilisable, tire, puis rend un verdict chiffré.

Le livrable n'est pas un script jetable : c'est un dossier `load-test/` que l'on copie d'un projet à l'autre, posable en CI.

## Prérequis

- **k6** (Grafana) : `brew install k6`. Vérifier avec `command -v k6` avant toute chose.
- L'application doit tourner. Pour des chiffres réalistes, un build de production (`pnpm build && pnpm start`), jamais le serveur de développement.
- **Un traceur d'erreurs déployé sur la cible** (Sentry ou équivalent). Sans lui, le tir ne mesure que des statuts HTTP — voir la règle 4, c'est la limite la plus grave du dispositif.
- Optionnel : une sonde de santé exposant l'état du pool de connexions. Son absence ne bloque pas le tir, elle retire juste la mesure de saturation.

## Règles non négociables

1. **Un seuil, pas une courbe.** Chaque scénario déclare des seuils bloquants. Le run sort en erreur si un seuil est dépassé. Sans seuil, on produit un graphique, pas un test.
2. **Jamais de tir sur une cible non locale sans confirmation humaine explicite.** L'orchestrateur exige une saisie manuelle. Ne jamais contourner ce garde-fou, ne jamais le retirer du script, ne jamais le pré-remplir dans un pipeline non supervisé.
3. **Toujours inclure une page témoin sans base de données.** Si elle ralentit aussi sous charge, le goulot n'est pas la base. Sans témoin, on ne peut rien conclure sur la cause.
4. **Ne jamais conclure « ça tient » sur la foi du statut HTTP.** En rendu streaming (Next App Router, Remix, Nuxt), les en-têtes partent avec les premiers octets, **avant** que le composant serveur échoue : une erreur serveur est alors servie dans une réponse `200`, avec du HTML, et n'apparaît dans **aucune** métrique k6. Un tir vert sur une application en feu est le mode d'échec par défaut de cet outillage, pas un cas rare.
5. **Ne jamais fixer les seuils soi-même sans validation.** Proposer des valeurs, demander confirmation. Un agent qui choisit ses propres critères de réussite les atteint toujours.
6. **Annoncer ce qui n'a pas été couvert.** Le rapport final liste les limites du tir : pages non testées, métriques non collectées, profil de montée utilisé.

## Procédure

### 1. Déduire le parcours réel

Lire le code des routes et de la navigation. Reconstituer le chemin d'un visiteur qui arrive depuis un email ou depuis la page d'accueil, avec les vraies URLs du projet. Ne pas inventer d'endpoints.

Identifier séparément :
- les pages **publiques** (généralement les plus visitées lors d'un pic),
- les pages **authentifiées** (généralement les plus lourdes),
- une page **témoin** qui ne touche pas la base.

### 2. Écrire les trois scénarios

| Scénario | Charge | Question à laquelle il répond |
| --- | --- | --- |
| `smoke` | 1 utilisateur | Est-ce que la cible répond avant qu'on lui envoie une foule ? |
| `load` | la charge attendue | Est-ce qu'on reste sous les seuils ? |
| `stress` | paliers croissants | À partir de combien ça lâche ? |

Chaque scénario tague ses requêtes (`page:docs`, `scenario:traffic`, etc.) pour que les seuils puissent viser une page précise et pas seulement la moyenne globale.

Faire porter les assertions sur **le contenu attendu**, pas seulement sur le code de réponse : un marqueur présent uniquement en cas de succès (un titre, un prix, un identifiant). Une assertion `status === 200` valide les pages d'erreur.

### 3. Poser les seuils

Valeurs de départ à proposer, puis à faire valider :

```js
thresholds: {
  'http_req_duration{scenario:traffic}': ['p(95)<1500'],
  'http_req_failed{scenario:traffic}':   ['rate<0.01'],
  'http_req_duration{page:docs}':        ['p(95)<800'],
}
```

Raisonner en **p95**, jamais en moyenne. La moyenne masque la queue de distribution, et c'est la queue qui fait partir les visiteurs.

Viser la **sous-métrique du parcours**, pas la métrique globale. Une sonde de santé qui répond volontairement 404 sans jeton fait grimper `http_req_failed` global et affiche un taux d'échec sur un tir pourtant intégralement vert.

### 4. Monter l'orchestrateur

Un script unique qui : vérifie la présence de k6, vérifie que la cible répond, applique le garde-fou de confirmation hors local, **borne le tir en UTC (`T0` → `T1`)**, lance le scénario, horodate la sortie brute, **collecte les erreurs du traceur sur cette fenêtre**, génère le rapport, et **sort en code d'erreur dédié si un seuil est dépassé**.

Posé en CI, un test de charge raté fait alors échouer le pipeline.

Chaque source facultative dégrade sans bloquer : traceur injoignable ou sonde absente, le tir se déroule et le rapport dit ce qui manque.

### 5. Tirer

```bash
./load-test/run.sh smoke
VUS=20 ./load-test/run.sh load
MAX_VUS=200 ./load-test/run.sh stress
```

### 6. Dépouiller

**C'est ici que le skill sert le plus.** Une sortie brute de stress pèse plusieurs centaines de mégaoctets. Personne ne l'ouvre.

Parser le JSON, puis produire :
- le tableau **palier par palier** : utilisateurs simultanés, médiane, p95, taux d'erreur ;
- la **distribution complète** : médiane, p90, p95, p99, max. Un écart faible entre p95 et p99 indique un service qui ne souffre pas ; une queue qui explose est le premier signe de saturation, bien avant que le taux d'erreur bouge ;
- le **palier de rupture**, ou son absence explicite.

### 7. Corréler avec le traceur d'erreurs

**L'étape qui empêche de rendre un verdict faux.**

Interroger le traceur sur la **fenêtre exacte du tir** (`T0` → `T1`) et ne retenir que les erreurs dont l'activité la chevauche. Sans ce filtre, le rapport impute au test des bugs vieux de plusieurs jours.

```bash
sentry issue list <org>/<project> --query "is:unresolved" --json \
  --fields shortId,title,culprit,count,userCount,firstSeen,lastSeen
```

Puis appliquer la lecture croisée :

| Statut HTTP | Traceur | Conclusion |
| --- | --- | --- |
| 0 % d'échec | aucune erreur | Le tir est valide. |
| 0 % d'échec | **des erreurs** | **Le tir a validé des pages d'erreur.** Le verdict k6 ne vaut rien. |
| des échecs | des erreurs | Cohérent : lire la cause dans le traceur. |
| des échecs | aucune erreur | Panne réseau, timeout côté client, ou traceur mal branché. |

La deuxième ligne est le cas par défaut sur une application en streaming. Le rapport doit l'afficher comme un avertissement, pas comme une note de bas de page.

Attention : le compteur d'occurrences d'une issue est son **total**, pas celui de la fenêtre. Le dire dans le rapport plutôt que de laisser croire à une précision qu'on n'a pas.

### 8. Vérifier que ce n'est pas du cache

Un résultat plat est suspect. Contrôler les en-têtes de réponse et le confirmer dans le rapport :

```bash
curl -sI "$BASE_URL/" | grep -iE "cache-control|x-vercel-cache|age"
```

Un `MISS` avec `no-store` prouve que les pages sont réellement rendues à chaque requête. Sans cette vérification, le résultat n'est pas défendable.

### 9. Rendre le verdict

Un rapport court : ce qui a été mesuré, les chiffres, la conclusion, et **les limites**. Voir `references/protocole.md` pour le détail des pièges d'interprétation.

## Piège à connaître : le serverless

```
connexions base ≳ POOL_MAX × instances actives
```

Chaque instance ouvre son propre pool. Sur une plateforme qui autoscale, le nombre d'instances grimpe avec le trafic. C'est ce produit qui doit rester sous la limite du serveur de base de données.

Augmenter `POOL_MAX` sans compter les instances ne supprime pas la saturation : ça la déplace vers la base.

### Le corollaire : la sonde de pool est presque aveugle

Une sonde `/api/health/db` exposant `waiting`, `active`, `idle`, `max` **ne voit que le pool local de l'instance qui répond**. Deux angles morts, cumulatifs :

- **Les autres instances.** La sonde en interroge une au hasard parmi N. Elle échantillonne des instances au repos pendant que d'autres saturent.
- **Le pooler en amont.** La limite atteinte est souvent celle du pooler (PgBouncer, Supabase), pas celle du pool applicatif. Une erreur `EMAXCONNSESSION — max clients reached in session mode` ne fera **jamais** bouger le compteur `waiting` local.

**Un pool à 0 en attente ne disculpe donc pas la base.** Ne jamais écrire « le goulot n'est pas la base » sur la seule foi de cette métrique : il faut le traceur d'erreurs pour trancher.

Sur Supabase, vérifier le **mode du pooler** avant toute autre chose : le port `5432` (mode session) monopolise une connexion par client et s'effondre en serverless ; le port `6543` (mode transaction) la rend après chaque transaction. C'est un changement de chaîne de connexion, sans une ligne de code.

## Sorties

- `load-test/` : orchestrateur, scénarios k6, générateur de rapport, analyse du palier de rupture.
- Un rapport markdown horodaté, versionnable, **avec sa section d'erreurs applicatives corrélées**.
- Les sorties brutes, **gitignorées** (une sortie de stress peut dépasser 150 Mo).

## Limites du skill

- Ne teste que ce qu'on lui demande de tester. Les pages authentifiées sont systématiquement oubliées si on ne les mentionne pas.
- Une montée progressive n'est pas un pic instantané. Un envoi d'email massif crée une charge immédiate, que ce profil ne reproduit pas.
- Sans sonde exposant l'état du pool, le tir dit « ça tient » et rien sur la saturation interne — et même avec elle, voir l'avertissement ci-dessus.
- **Sans traceur d'erreurs déployé, un verdict « 0 erreur » n'a aucune valeur probante.** Les tirs effectués avant l'installation du traceur sont à considérer comme non concluants, pas comme réussis.
