---
name: sentry-triage
description: Trier et corriger les erreurs de production remontées par Sentry, via le MCP officiel ou la CLI sentry. Classe les issues par coût réel, récupère stack et variables locales, croise avec le code du repo, remonte au déploiement fautif et propose un correctif. Utiliser quand on demande "qu'est-ce qui casse en prod", "les erreurs Sentry", "pourquoi ça plante chez les utilisateurs", "triage des erreurs", "cette issue Sentry", ou après un déploiement. NE PAS utiliser pour installer Sentry dans un projet, ni pour des problèmes de charge ou de saturation (voir load-test).
---

# Sentry Triage

Transforme un flux d'erreurs de production en une décision : quoi corriger d'abord, pourquoi ça casse, et quel correctif proposer.

La procédure est écrite une fois. Elle n'est plus jamais redonnée.

## Accès : MCP ou CLI

Deux façons de brancher un agent sur Sentry. Elles ne servent pas au même usage.

| | MCP `sentry-mcp` | CLI `sentry` |
| --- | --- | --- |
| Forme | subagent dans Claude Code | commandes shell, sortie `--json` |
| Usage | conversation, exploration | scripts, CI, tout agent |
| Installation | `claude plugin install sentry-mcp@sentry-mcp` (marketplace `getsentry/sentry-mcp`) | paquet npm `sentry`, doc sur `cli.sentry.dev` |

```bash
sentry issue list                 # détecte le projet depuis le .env
sentry issue explain MYAPP-WQ     # cause racine analysée par Seer
sentry issue plan                 # plan de correctif étape par étape
```

**Attention à l'homonyme.** Le vieux `sentry-cli` ne fait que les releases et l'envoi de sourcemaps. La CLI décrite ici est la nouvelle, annoncée « for developers and agents ».

## Règles non négociables

1. **Ne jamais refermer une issue soi-même.** L'agent propose, l'humain tranche et ferme. C'est ce qui garde la boucle fermée sur une personne.
2. **Classer par coût, jamais par date.** L'erreur la plus récente n'est presque jamais la plus importante.
3. **Ne jamais conclure sur la seule foi du message d'erreur.** Toujours ouvrir un événement réel et lire ses variables locales avant de proposer une cause.
4. **Vérifier l'environnement.** Une erreur de développement mélangée aux erreurs des utilisateurs fausse tout le classement.
5. **Ne pas inventer de correctif plausible.** Si la stack ne suffit pas à remonter à la ligne fautive, le dire et demander l'accès au contexte manquant.

## Procédure

### 1. Lister et classer

Récupérer les issues non résolues, puis trier par **occurrences et nombre d'utilisateurs touchés**. Une erreur vue 2 400 fois par 340 personnes passe avant une erreur vue trois fois hier soir.

Écarter d'emblée le bruit connu : extensions de navigateur, robots, erreurs réseau côté client.

### 2. Ouvrir la plus coûteuse

Sur le dernier événement de l'issue retenue, récupérer :
- la **stack trace** complète,
- les **variables locales** au moment du crash,
- l'utilisateur et la requête concernés,
- la **première occurrence** et le **volume dans le temps**.

### 3. Croiser avec le repo

Remonter de la stack au fichier et à la ligne dans le code local. Puis répondre à la question qui compte : **depuis quel déploiement cette erreur apparaît-elle ?** Comparer la date de première occurrence avec l'historique git.

Une erreur qui démarre pile après un déploiement désigne son commit.

### 4. Proposer

Rédiger : la cause racine, le correctif, et ce qui reste incertain. Ouvrir la pull request.

**Ne pas refermer l'issue.** Elle se referme quand le correctif est en production et que les occurrences s'arrêtent, ce que l'agent ne peut pas constater seul.

## Ce que Sentry ne verra jamais

Sentry capture des **exceptions**. Une saturation de pool de connexions est un **état**, pas une exception : rien n'est levé tant que la file d'attente monte. Sentry ne la voit qu'au moment où elle produit des timeouts, c'est-à-dire quand les utilisateurs ont déjà pris l'erreur.

Ce cas relève d'une sonde de santé qui expose les compteurs du pool (`waiting`, `active`, `idle`, `max`) et répond en erreur avant le premier échec.

Si une sonde de ce type existe dans le projet, elle doit être **fermée par un jeton** et répondre **404 plutôt que 401** : un 401 confirmerait son existence, et un ping consommant une connexion en ferait une arme de déni de service.

Attention toutefois : cette sonde ne voit que le pool **local à l'instance qui répond**. En serverless, elle en échantillonne une au hasard, et elle ignore la limite du pooler en amont. Une saturation `EMAXCONNSESSION` côté PgBouncer/Supabase laisse son compteur `waiting` à zéro. **Un pool à 0 en attente ne disculpe pas la base** — c'est Sentry qui tranchera, au moment où la saturation produira enfin une exception.

## Ce que Sentry est le seul à voir

Le symétrique compte autant. Sur une application en rendu **streaming** (Next App Router, Remix, Nuxt), les en-têtes HTTP partent avec les premiers octets, **avant** que le composant serveur échoue. L'erreur est ensuite injectée dans un flux déjà ouvert : le visiteur reçoit un `200` contenant une page d'erreur.

Conséquence directe : **un test de charge, un moniteur d'uptime ou un check CI qui juge sur le code de réponse ne verra rien.** Sentry est alors la seule source qui sache que l'application a échoué.

Cas vécu : un tir k6 annonçant `0 %` d'échec sur 2 151 requêtes, pendant que Sentry enregistrait 29 erreurs Postgres sur la même minute. Le tir était vert, le service était par terre.

### Corréler un tir de charge avec les issues

1. Borner le tir en UTC (`T0` → `T1`).
2. Lister les issues et ne retenir que celles dont l'activité **chevauche la fenêtre** — sans ce filtre, on impute au test des bugs de la veille.
3. Croiser les deux verdicts :

| Statut HTTP | Sentry | Conclusion |
| --- | --- | --- |
| 0 % d'échec | rien | Tir valide. |
| 0 % d'échec | **des erreurs** | **Le tir a validé des pages d'erreur.** Le verdict de l'outil de charge est nul. |
| des échecs | des erreurs | Cohérent : la cause est dans le traceur. |
| des échecs | rien | Réseau, timeout client, ou Sentry mal branché. |

Le compteur d'occurrences d'une issue est son **total**, jamais celui de la fenêtre. Le préciser plutôt que de laisser croire à une précision qu'on n'a pas.

Voir le skill `load-test`, qui automatise cette corrélation dans son rapport.

## Pièges d'installation à connaître

- **Tunnel et middleware i18n.** Un `tunnelRoute` contourne les bloqueurs de publicité, mais un middleware d'internationalisation peut réécrire cette route et la casser silencieusement. Symptôme : des `POST` en 404 sur la route de tunnel préfixée par la locale, et zéro erreur navigateur qui remonte. Sentry a l'air installé, il ne reçoit rien. Corriger en excluant la route du matcher.
- **`environment` absent.** Sans lui, les erreurs de développement et celles des utilisateurs arrivent mélangées, et chaque erreur provoquée en codant déclenche une alerte.
- **Inactif sans DSN.** Un point d'entrée qui sort avant d'initialiser quand le DSN est absent rend le build identique à celui d'un projet sans Sentry. C'est ce qui permet de poser l'intégration dans un boilerplate sans l'imposer.

## Sorties

- Une liste d'issues classées par coût réel.
- Pour l'issue traitée : cause racine, déploiement d'origine, correctif proposé, incertitudes.
- Une pull request. Jamais une issue refermée.
