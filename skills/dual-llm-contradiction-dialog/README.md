# dual-llm-contradiction-dialog

`dual-llm-contradiction-dialog` est une skill d’orchestration de **dialogue structuré entre deux LLMs** (A et B) autour d’un même sujet : plan, design, architecture, décision à fort enjeu.

Elle combine la logique de tes skills existantes :

- `multi-llm-debate-grill-me` pour les **rounds de débat** et la lecture croisée.
- `angle-mort` pour la **divergence organisée** et les angles morts tagués.
- `intent-guard-shield` pour la **protection contre le contournement** et la formalisation de l’intention.
- `grill-me` pour l’**interrogatoire systématique** par arbre de décision.

L’objectif n’est pas d’obtenir une réponse unique “propre” le plus vite possible.  
L’objectif est de faire débattre deux LLMs sur un même sujet, en :

- clarifiant l’intention,
- générant des angles morts spécifiques,
- chassant les contradictions,
- exposant les contournements silencieux possibles,
- produisant une synthèse où les désaccords restent visibles.

---

## Pourquoi cette skill existe

Tu as déjà :

- une skill de débat multi‑LLM (`multi-llm-debate-grill-me`) avec plusieurs modèles et un juge final ; [cite:3]  
- une skill de divergence (`angle-mort`) qui retourne les cadrages évidents pour faire apparaître des angles morts ; [cite:7]  
- une skill de garde‑fou (`intent-guard-shield`) qui verrouille l’intention contre les faux succès ; [cite:11]  
- une skill d’interrogatoire (`grill-me`) qui pousse un plan branche par branche.

`dual-llm-contradiction-dialog` sert à les **fusionner pour un cas spécifique** :  
un dialogue entre deux LLMs seulement, où chacun doit :

- penser seul d’abord,
- produire ses angles morts sur le sujet,
- lire la position de l’autre,
- signaler les contradictions,
- pointer les contournements potentiels,
- proposer une synthèse structurée.

Cette skill devient ton outil de base pour :

- mettre en tension **deux modèles** (par exemple GLM et DeepSeek, ou Qwen et Claude),  
- faire des revues croisées sur des designs de repo, des architectures système, des skills, des workflows CI/CD, etc.,  
- voir où les modèles ne sont pas alignés, plutôt que juste où ils sont d’accord. [web:55][web:57]

---

## Quand l’utiliser

Utilise `dual-llm-contradiction-dialog` quand :

- tu as **un sujet unique** (plan, design, idée de repo, architecture) et **deux LLMs** à disposition ;  
- tu veux voir **où leurs positions se contredisent**, pas seulement où elles convergent ;  
- tu as besoin de faire ressortir les **angles morts** et les **contournements silencieux** avant de trancher ;  
- tu prépares un projet GitHub (orchestrateur multi‑agents, skill set, framework) et tu veux un stress‑test croisé sur le design.

Exemples concrets :

- “Concevoir un repo GitHub pour un orchestrateur multi‑agents inspiré de Trinity/Conductor, avec GLM en architecte et DeepSeek en implémenteur.” [cite:6]  
- “Comparer deux architectures de CI/CD (GitHub Actions vs autre) avec Qwen et Claude, en cherchant les contradictions de sécurité.”  
- “Mettre au grill un design de skill (`intent-guard-shield` v2, `angle-mort` v2, etc.) avec deux LLMs qui jouent architecte et critique.”

---

## Quand ne pas l’utiliser

Évite cette skill si :

- tu veux une **réponse courte et immédiate** sur une question factuelle simple ;  
- tu n’as qu’**un seul LLM** disponible (dans ce cas, `grill-me` ou `angle-mort` seuls suffisent) ;  
- le sujet est très peu critique (une micro‑idée sans impact, un détail sans enjeu) ;  
- tu cherches juste une reformulation ou une synthèse rapide sans débat.

Elle n’est pas conçue pour :

- les requêtes triviales (“explique-moi X”, “résume Y”) ;  
- les tâches purement opérationnelles sans choix d’architecture ;  
- remplacer des tests, des benchmarks ou du terrain.

---

## Principe de fonctionnement

La skill fonctionne par **rounds**, en reprenant l’esprit de tes autres skills :

1. **Round 0 — Cadrage silencieux (intent-guard + cartographie)**  
   Chaque LLM :
   - reformule l’intention en une phrase claire ;
   - identifie but, contraintes, interdictions, critères de réussite/échec ;
   - cartographie rapidement les branches de décision (style `grill-me`) ;
   - signale les informations manquantes qui changeraient le sens du plan.

2. **Round 1 — Position initiale + angles morts (indépendante)**  
   Chaque LLM :
   - produit sa position sur le sujet (plan, branches, critères, risques) ;
   - génère 3 à 7 angles morts avec le format `angle-mort` :
     - moves (inversion, décalage temporel, test du clou, etc.),
     - tags `[à vérifier]` / `[spéculatif]`,
     - filtre anti‑slop (test du remplacement),
     - éventuellement ⚡ pour un angle très contre‑intuitif.

3. **Round 2 — Lecture croisée + contradictions**  
   Chaque LLM reçoit la position et les angles de l’autre.  
   Il doit :
   - résumer la position de l’autre ;
   - comparer sa propre position aux angles et choix de l’autre ;
   - chercher des **contradictions** :
     - factuelles,
     - logiques,
     - de contraintes,
     - de priorités ;
   - point par point :
     - reformuler les deux affirmations,
     - dire en quoi elles sont incompatibles,
     - proposer une question pour l’utilisateur ;
   - repérer les **contournements silencieux** (intent‑guard) :
     - dilution de contraintes,
     - changement de métrique,
     - violation d’interdiction.

4. **Round 3 — Convergence / désaccord structuré**  
   Chaque LLM :
   - liste ce qui est compatible,
   - liste ce qui reste contradictoire,
   - met en avant les angles complémentaires utiles,
   - propose un plan ou une recommandation :
     - respect de l’intention,
     - respect des contraintes,
     - désaccords visibles,
     - hypothèses non validées,
     - points à vérifier.

Un **juge final** (troisième LLM) est optionnel : tu peux lui fournir les deux sorties de Round 3 pour arbitrage ou proposition de scénarios alternatifs. [web:48][web:55]

---

## Format de sortie

La skill impose un format de sortie Markdown, compatible avec tes autres skills, pour que les réponses soient :

- comparables entre LLMs,  
- faciles à relire,  
- prêtes à stocker dans un repo ou une note.

Les sections principales :

- `### Contexte reformulé`  
- `### Position initiale (Round 1)`  
- `### Angles morts (Round 1)`  
- `### Lecture de l'autre LLM (Round 2)`  
- `### Synthèse (Round 3)`  
- `### Avertissement`

Chaque LLM suit la même structure, ce qui permet :

- de faire des diff entre modèles,  
- de repérer les contradictions par simple lecture,  
- de brancher ensuite un script ou un orchestrateur pour analyser automatiquement certaines sections (par exemple les contradictions ou les contournements).

---

## Mode d’emploi pas à pas (GLM / DeepSeek / Qwen)

Supposons que tu utilises :

- GLM comme LLM_A (architecte / interrogateur),  
- DeepSeek comme LLM_B (implémenteur / challenger),  
- Qwen comme juge final éventuel.

1. **Préparation**

   - Ouvre un chat GLM (LLM_A).  
   - Ouvre un chat DeepSeek (LLM_B).  
   - Copie la skill `dual-llm-contradiction-dialog` en début de chaque chat.  
   - Précise le rôle :
     - à GLM : “Tu es LLM_A (architecte / interrogateur)…”  
     - à DeepSeek : “Tu es LLM_B (implémenteur / challenger)…”

2. **Brief commun**

   - Donne le même brief aux deux :  
     - par exemple : “Je veux concevoir un repo GitHub pour un orchestrateur multi‑agents inspiré de Trinity et Conductor, avec ces contraintes : …” [cite:6]

3. **Round 0 + Round 1**

   - Demande à GLM : “Applique Round 0 puis Round 1 selon la skill.”  
   - Demande à DeepSeek la même chose.  
   - Récupère leurs réponses (contexte, position, angles morts).

4. **Lecture croisée (Round 2)**

   - Envoie la réponse de GLM à DeepSeek avec :  
     - “Voici la position et les angles de LLM_A. Round 2 : lis et cherche les contradictions.”  
   - Envoie la réponse de DeepSeek à GLM avec la même consigne.  
   - Récupère les listes de contradictions + contournements signalés.

5. **Synthèse (Round 3)**

   - Demande à chacun :  
     - “Fais la synthèse selon Round 3, en gardant visibles les désaccords, les hypothèses non validées, et les points à vérifier.”

6. **Juge final (optionnel)**

   - Ouvre Qwen, colle la skill ou un mini‑prompt de juge.  
   - Fournis les deux sorties de Round 3 (GLM + DeepSeek).  
   - Demande :
     - “Résume les points d’accord, de désaccord, et propose soit un arbitrage, soit deux options claires.”

---

## Cas d’usage typiques

Quelques scénarios où cette skill est particulièrement pertinente :

- **Design de repo GitHub**  
  Tu veux créer un repo pour un orchestrateur multi‑agents, une suite de skills, ou un framework CI/CD.  
  Tu fais débattre deux LLMs sur :
  - structure de dossiers,
  - conventions,
  - workflow d’orchestration,
  - intégration des skills (dont celles que tu viens de construire).

- **Conception ou refonte de skill**  
  Tu écris une nouvelle skill (par exemple `angle-mort v2` ou une skill de routing d’agents).  
  Tu la passes au grill partagé :
  - LLM_A propose le design,
  - LLM_B trouve les angles morts, les contradictions, les contournements possibles,
  - la synthèse te donne une carte des désaccords.

- **Décisions stratégiques autour de projets IA / dev**  
  Tu hésites entre plusieurs architectures, stacks, ou modes d’orchestration.  
  Tu utilises deux LLMs pour :
  - faire ressortir les contradictions de priorité,
  - voir où tu risques de contourner une contrainte importante (sécurité, coût, maintenance).

---

## Limites et avertissements

Comme pour tes autres skills :

- Cette skill teste la **cohérence interne d’un plan**, pas sa validité externe ni sa faisabilité réelle.  
- Un plan peut être logique, bien cadré, cohérent… et échouer en pratique.  
- Les contradictions repérées sont des signaux pour toi, pas des verdicts absolus.

À retenir :

> L’intention guide l’action, mais la vérification garde la vérité.  
> Le dialogue entre deux LLMs te montre où ça coince, à toi ensuite de vérifier dans le réel.

---
