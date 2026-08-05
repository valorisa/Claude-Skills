# 1. Installer et utiliser les skills

## Où poser les fichiers

Un skill est un fichier Markdown avec un en-tête. L'agent le charge quand la conversation correspond à sa description.

### Claude Code

```
ton-projet/
└── .claude/
    └── skills/
        ├── load-test/
        │   ├── SKILL.md              ← renomme load-test.md en SKILL.md
        │   └── references/
        │       └── protocole.md      ← load-test-protocole.md
        └── sentry-triage/
            └── SKILL.md              ← sentry-triage.md
```

Le nom du **dossier** compte, pas celui du fichier : chaque skill vit dans son répertoire avec un `SKILL.md` à la racine.

Pour les rendre disponibles sur tous tes projets, pose-les dans `~/.claude/skills/` au lieu du dossier du dépôt.

### Autres agents

Le format est du Markdown standard. Cursor, Windsurf, Copilot ou un agent maison peuvent lire ces fichiers : place-les là où ton outil cherche ses instructions, ou colle simplement le contenu dans le contexte de la session.

## L'en-tête, et ce qui déclenche un skill

```yaml
---
name: load-test
description: Construire et exécuter des tests de charge k6 sur une application web.
  Produit trois scénarios (smoke, load, stress), des seuils bloquants, un rapport
  corrélé aux erreurs du traceur. Utiliser quand on demande « est-ce que ça tient ? »,
  « test de charge », « combien d'utilisateurs simultanés », avant un envoi massif
  d'emails ou un lancement produit. NE PAS utiliser pour du profilage front.
---
```

Deux champs suffisent : `name` et `description`.

**C'est la `description` qui déclenche le skill, pas son nom.** Tu ne tapes jamais « lance load-test ». Tu demandes « est-ce que mon site tient la charge ? » et l'agent charge le bon skill parce que ta phrase correspond à sa description.

Deux conséquences pratiques :

- Une description vague ne se déclenche jamais. Elle doit contenir les formulations réelles que tu emploies.
- La phrase « NE PAS utiliser pour... » évite les faux déclenchements. C'est aussi utile que la partie positive.

## Vérifier que le skill est bien chargé

Dans Claude Code, `/skills` liste les skills visibles dans la session en cours. Si le tien n'apparaît pas, vérifie l'emplacement du dossier et la présence de l'en-tête entre les deux `---`.

Test simple : pose la question la plus évidente de la description (« est-ce que ça tient ? ») et regarde si l'agent applique la procédure au lieu d'improviser. S'il te propose directement d'écrire un script k6 sans parler de seuils ni de page témoin, il n'a pas chargé le skill.

## Ce qu'un skill apporte par rapport à un prompt

Un prompt décrit un résultat attendu, et disparaît à la fin de la session. Un skill fixe une **méthode** et des **interdits** qui restent valables sur toutes les exécutions suivantes, y compris celles que tu ne supervises pas.

Les interdits de `load-test`, par exemple :

- jamais de tir sur une cible non locale sans confirmation humaine explicite ;
- toujours une page témoin qui n'interroge pas la base de données ;
- ne jamais fixer les seuils de réussite tout seul.

Le dernier est le plus important. Un agent qui choisit ses propres critères de réussite les atteint toujours.

## Adapter les skills à ton projet

Les deux skills sont génériques, mais quelques éléments méritent d'être ajustés :

| À adapter | Où | Pourquoi |
| --- | --- | --- |
| Les seuils de départ | `load-test`, section « Poser les seuils » | Un site vitrine et une application métier n'ont pas les mêmes cibles |
| La page témoin | `load-test`, section « Déduire le parcours réel » | Il faut une page réelle de ton projet qui ne touche pas la base |
| Le nom du traceur | `sentry-triage` | Si tu utilises autre chose que Sentry, seule la partie accès change |

Le reste de la procédure ne dépend pas de ta stack.
