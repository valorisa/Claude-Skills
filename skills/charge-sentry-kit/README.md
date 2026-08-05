# Kit Test de charge + Sentry, pilotés par agent

Deux skills Claude Code et trois guides pour répondre à deux questions que la plupart des projets ne se posent qu'après le lancement :

- **Est-ce que ça tient ?** quand 200 personnes arrivent en même temps.
- **Qu'est-ce qui casse ?** quand une erreur survient en production.

Ce kit est issu d'un cas réel : un test de charge annonçait 40 689 requêtes sans une seule erreur. Une fois un traceur d'erreurs déployé, le même test rejoué à 20 utilisateurs au lieu de 200 a révélé 29 erreurs de base de données. Les deux skills contiennent les règles qui évitent de reproduire ce faux négatif.

## Contenu

```
skills/
  load-test.md               le skill de test de charge k6
  load-test-protocole.md     vocabulaire, faux positifs, pièges d'interprétation
  sentry-triage.md           le skill de triage des erreurs de production

guides/
  01-installer-et-utiliser.md    où poser les skills, comment les déclencher
  02-briefer-un-scenario.md      comment demander un scénario de test
  03-setup-sentry-nextjs.md      installer Sentry sans l'imposer au projet
```

## Prérequis

- Un agent capable de charger des skills : Claude Code, ou tout agent lisant un dossier de procédures.
- **k6** pour les tests de charge : `brew install k6`.
- Un compte **Sentry** pour la partie erreurs. Le plan gratuit suffit largement.

## Par où commencer

1. Lire `guides/01-installer-et-utiliser.md`, cinq minutes.
2. Poser les deux `.md` du dossier `skills/` dans le dossier de skills de ton agent.
3. Demander « est-ce que mon app tient la charge ? » et suivre `guides/02-briefer-un-scenario.md`.

## Licence

Réutilise, modifie, adapte à ton projet. Ces skills sont faits pour être copiés d'un dépôt à l'autre.
