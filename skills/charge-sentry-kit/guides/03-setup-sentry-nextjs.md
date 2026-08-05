# 3. Installer Sentry sur Next.js sans l'imposer au projet

L'objectif de ce montage : que le projet fonctionne **exactement pareil** quand aucune clé Sentry n'est configurée. C'est ce qui permet de poser l'intégration dans un boilerplate ou un projet open source sans forcer personne à créer un compte.

## Installation

```bash
npx @sentry/wizard@latest -i nextjs
```

L'assistant crée la structure de base. Tu peux aussi installer `@sentry/nextjs` à la main et écrire les fichiers toi-même : ils sont courts.

## Les six points d'entrée

| Fichier | Rôle |
| --- | --- |
| `sentry.server.config.ts` | initialisation côté Node |
| `sentry.edge.config.ts` | initialisation côté Edge |
| `src/instrumentation.ts` | `register()` et `onRequestError` |
| `src/instrumentation-client.ts` | initialisation navigateur |
| `src/app/global-error.tsx` | erreurs du layout racine |
| `next.config.ts` | `withSentryConfig` |

## Le principe : inactif sans DSN

Chaque point d'entrée sort avant d'initialiser quoi que ce soit si la variable est absente.

```ts
// sentry.server.config.ts
import * as Sentry from '@sentry/nextjs'

const dsn = process.env.NEXT_PUBLIC_SENTRY_DSN

if (dsn) {
  Sentry.init({
    dsn,
    environment: process.env.NODE_ENV,
    tracesSampleRate: 0.1,
    includeLocalVariables: true,
  })
}
```

Et dans la configuration Next, on n'applique le wrapper que si la clé existe :

```ts
// next.config.ts
const config = { /* ta config habituelle */ }

export default process.env.NEXT_PUBLIC_SENTRY_DSN
  ? withSentryConfig(config, { silent: true, tunnelRoute: '/monitoring' })
  : config
```

Sans DSN, le build produit exactement le même résultat qu'un projet sans Sentry : aucune route générée, aucun surcoût.

## Trois réglages qui comptent

### `environment`

```ts
environment: process.env.NODE_ENV
```

Sans lui, les erreurs de développement et celles des utilisateurs arrivent mélangées dans la même liste. Chaque erreur que tu provoques en codant déclenche alors une alerte, et le classement par nombre d'occurrences devient inexploitable.

### `includeLocalVariables`

```ts
includeLocalVariables: true
```

C'est ce qui fait la différence entre « une erreur s'est produite dans cette fonction » et « voici la valeur exacte de la variable au moment du crash ». Sans ça, la moitié du travail de diagnostic reste à faire à la main.

### `tracesSampleRate`

Commence bas, à `0.1`. Le traçage des performances consomme le quota bien plus vite que les erreurs.

## Le piège du tunnel avec un middleware i18n

`tunnelRoute: '/monitoring'` fait passer les événements par ton propre domaine, ce qui contourne les bloqueurs de publicité. Utile, mais avec un middleware d'internationalisation, cette route se fait réécrire.

**Symptôme :** des `POST /fr/monitoring` en 404 dans les logs, et aucune erreur navigateur qui remonte. Sentry a l'air installé, il ne reçoit rien.

**Cause :** le middleware préfixe la route de tunnel avec la locale. `/monitoring` devient `/fr/monitoring`, qui n'existe pas.

**Correctif :** exclure la route du matcher.

```ts
// middleware.ts
export const config = {
  matcher: [
    '/((?!api|trpc|_next|_vercel|monitoring|.*\\..*).*)',
    '/api/auth/error',
  ],
}
```

Le même problème existe avec tout middleware qui réécrit les URLs : authentification, redirections, A/B testing. Si les événements n'arrivent pas, la route de tunnel est le premier endroit à regarder.

## Vérifier que ça remonte vraiment

Ne te fie pas à l'absence d'erreur dans l'interface : elle peut vouloir dire « rien ne casse » comme « rien n'est branché ».

Provoque une erreur volontaire :

```ts
// src/app/api/sentry-check/route.ts
export function GET() {
  throw new Error('Vérification Sentry, à supprimer après test')
}
```

Appelle la route, puis vérifie que l'événement apparaît dans l'interface **avec sa stack trace lisible**. Si la stack est minifiée, c'est que les sourcemaps ne sont pas envoyées.

Supprime la route ensuite.

## Les variables d'environnement

| Variable | Secret ? | À quoi elle sert |
| --- | --- | --- |
| `NEXT_PUBLIC_SENTRY_DSN` | non, public par conception | identifie ton projet |
| `SENTRY_ORG` | non | upload des sourcemaps |
| `SENTRY_PROJECT` | non | upload des sourcemaps |
| `SENTRY_AUTH_TOKEN` | **oui** | upload des sourcemaps au build |

Le jeton d'authentification ne sert **qu'au build**. Sans lui, tout fonctionne : les stacks navigateur sont simplement minifiées en production. Ne le mets jamais dans un fichier versionné.

## Ce que Sentry ne verra jamais

Sentry capture des **exceptions**. Une saturation de pool de connexions est un **état** : rien n'est levé tant que la file d'attente monte. Sentry ne la voit qu'au moment où elle produit un vrai échec, c'est-à-dire quand les utilisateurs ont déjà pris l'erreur.

Pour ce cas, il faut une sonde de santé qui expose les compteurs du pool (`waiting`, `active`, `idle`, `max`). Deux précautions si tu en poses une :

- **La fermer par un jeton, et répondre 404 plutôt que 401.** Un 401 confirme son existence, et un ping qui consomme une connexion en fait une arme de déni de service.
- **Ne pas lui faire dire plus qu'elle ne sait.** Elle ne voit que le pool local à l'instance qui répond. En serverless, elle en échantillonne une au hasard, et elle ignore la limite d'un pooler en amont. Un compteur d'attente à zéro ne disculpe pas la base.

Un dernier piège, plus subtil : une sonde qui relève l'état une fois par seconde ne verra jamais une attente de connexion qui dure cinq millisecondes. Un instrument correctement branché peut rester incapable de mesurer le phénomène visé, pour une simple question de fréquence d'échantillonnage.

## Brancher un agent sur les erreurs

Une fois Sentry en place, deux façons de laisser un agent l'interroger.

**Le serveur MCP officiel**, pour travailler en conversation :

```bash
claude plugin marketplace add getsentry/sentry-mcp
claude plugin install sentry-mcp@sentry-mcp
```

Cela installe un sous-agent auquel Claude délègue dès que tu parles d'une erreur, d'une issue ou d'une trace.

**La CLI**, pour les scripts et l'intégration continue :

```bash
sentry issue list                 # détecte le projet depuis le .env
sentry issue explain MYAPP-WQ     # analyse de cause racine
sentry issue plan                 # plan de correctif étape par étape
```

Attention à l'homonyme : l'ancien `sentry-cli` ne fait que les releases et les sourcemaps. Celui décrit ici est le nouveau, documenté sur `cli.sentry.dev`.

À partir de là, le skill `sentry-triage` prend le relais : classement par coût réel, récupération des variables locales, croisement avec le dépôt, et remontée au déploiement fautif.
