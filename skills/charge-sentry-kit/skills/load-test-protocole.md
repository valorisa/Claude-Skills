# Protocole et pièges d'interprétation

Complément de `SKILL.md`. À lire avant de conclure quoi que ce soit d'un tir.

## Vocabulaire

| Terme | Définition | Pourquoi ça compte |
| --- | --- | --- |
| **VU** | utilisateur virtuel | 200 VU = 200 personnes qui naviguent en même temps, pas 200 requêtes |
| **Palier** | marche de charge tenue quelques dizaines de secondes | on cherche la marche à laquelle ça casse |
| **p95** | 95 % des requêtes ont été servies plus vite | la moyenne masque la queue, et c'est la queue qui fait partir les gens |
| **p99** | 99 % des requêtes | l'écart p95 → p99 est le meilleur indicateur précoce de saturation |
| **Seuil** | limite déclarée avant le tir | c'est ce qui transforme un graphique en test |

## Lire une distribution

Un service en bonne santé montre un écart faible entre p95 et p99. Un service qui commence à souffrir voit sa queue s'étirer **avant** que le taux d'erreur bouge.

Un taux d'erreur à 0 % avec un p99 très éloigné du p95 n'est pas un bon résultat : c'est un début de saturation qui n'a pas encore produit d'échec.

## La courbe n'est pas une droite

Tant que la demande reste sous la capacité, la latence bouge à peine. Un cran au-dessus, la file d'attente s'auto-alimente et tout s'effondre d'un coup.

Conséquence directe : **on ne peut pas extrapoler**. Un test réussi à 50 utilisateurs ne dit rien du comportement à 100. Il faut monter jusqu'à la rupture, ou déclarer explicitement qu'on ne l'a pas trouvée.

## Les faux positifs

| Symptôme | Cause probable | Vérification |
| --- | --- | --- |
| Latence parfaitement plate | les réponses viennent d'un cache | en-têtes `cache-control`, `x-vercel-cache`, `age` |
| Tout est lent, même la page témoin | goulot réseau ou machine de tir saturée | tirer depuis une autre machine, vérifier la charge locale |
| Résultats meilleurs à haute charge | montée en température, instances déjà chaudes | rejouer en inversant l'ordre des paliers |
| Erreurs dès le premier palier | rate limiting ou pare-feu applicatif | vérifier les codes de réponse, pas seulement leur nombre |

## Ce qu'un tir ne dit pas

À écrire systématiquement dans le rapport final :

- **Les pages non testées.** L'espace authentifié et l'administration sont presque toujours les plus lourds, et presque jamais mis sous charge.
- **Les métriques non collectées.** Sans sonde exposant l'état du pool, on mesure des latences et des erreurs, pas la saturation interne.
- **Le profil de montée.** Une montée progressive laisse à la plateforme le temps d'ajouter des instances. Un envoi d'email massif crée un pic immédiat : c'est un scénario différent, à rejouer séparément.
- **La durée.** Quatre minutes ne révèlent ni les fuites mémoire, ni la dérive d'un pool sur plusieurs heures.

## Le pic instantané

Pour reproduire le scénario d'un envoi massif, il faut un profil sans rampe : tous les utilisateurs virtuels arrivent en même temps, sur les pages ciblées par le lien de l'email, et pas sur la page d'accueil.

C'est le scénario le plus proche de la réalité d'un lancement, et le plus souvent oublié.

## Poser le test en CI

L'orchestrateur sort avec un code d'erreur dédié quand un seuil est dépassé. En CI, cela fait échouer le pipeline.

Ne poser en CI que le scénario `load`, jamais `stress` : un test de rupture sur chaque commit coûte cher et finit par être désactivé. Le `stress` se rejoue à la main avant un lancement, ou après un changement d'infrastructure.
