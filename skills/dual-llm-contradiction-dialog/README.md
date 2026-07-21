# dual-llm-contradiction-dialog

`dual-llm-contradiction-dialog` est une skill d’orchestration de **dialogue structuré entre deux LLMs** (A et B) autour d’un même sujet : plan, design, architecture, décision à fort enjeu.

Elle combine la logique de tes skills existantes :

- `multi-llm-debate-grill-me` pour les rounds de débat et la lecture croisée.
- `angle-mort` pour la divergence organisée et les angles morts tagués.
- `intent-guard-shield` pour la protection contre le contournement et la formalisation de l’intention.
- `grill-me` pour l’interrogatoire systématique par arbre de décision.

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

- une skill de débat multi-LLM, avec plusieurs modèles et un juge final ;
- une skill de divergence qui retourne les cadrages évidents pour faire apparaître des angles morts ;
- une skill de garde-fou qui verrouille l’intention contre les faux succès ;
- une skill d’interrogatoire qui pousse un plan branche par branche.

`dual-llm-contradiction-dialog` sert à les **fusionner pour un cas spécifique** :  
un dialogue entre deux LLMs seulement, où chacun doit :

- penser seul d’abord,
- produire ses angles morts sur le sujet,
- lire la position de l’autre,
- signaler les contradictions,
- pointer les contournements potentiels,
- proposer une synthèse structurée.

Cette skill devient ton outil de base pour :

- mettre en tension deux modèles (par exemple GLM et DeepSeek, ou Qwen et Claude),
- faire des revues croisées sur des designs de repo, des architectures système, des skills, des workflows CI/CD,
- voir où les modèles ne sont pas alignés, plutôt que seulement où ils sont d’accord.

---

## Quand l’utiliser

Utilise `dual-llm-contradiction-dialog` quand :

- tu as un sujet unique (plan, design, idée de repo, architecture) et deux LLMs à disposition ;
- tu veux voir où leurs positions se contredisent, pas seulement où elles convergent ;
- tu as besoin de faire ressortir les angles morts et les contournements silencieux avant de trancher ;
- tu prépares un projet GitHub (orchestrateur multi-agents, skill set, framework) et tu veux un stress-test croisé sur le design.

Exemples :

- Concevoir un repo GitHub pour un orchestrateur multi-agents inspiré de Trinity et Conductor, avec GLM en architecte et DeepSeek en implémenteur.
- Comparer deux architectures de CI/CD (GitHub Actions contre une autre solution) avec Qwen et Claude, en cherchant les contradictions de sécurité.
- Mettre au grill un design de skill (par exemple une nouvelle version d’`intent-guard-shield` ou d’`angle-mort`) avec deux LLMs qui jouent architecte et critique.

---

## Quand ne pas l’utiliser

Évite cette skill si :

- tu veux une réponse courte et immédiate sur une question factuelle simple ;
- tu n’as qu’un seul LLM disponible (dans ce cas, `grill-me` ou `angle-mort` seuls suffisent) ;
- le sujet est très peu critique (micro-idée sans impact, détail sans enjeu) ;
- tu cherches juste une reformulation ou une synthèse rapide sans débat.

Elle n’est pas conçue pour :

- les requêtes triviales (explications, résumés simples) ;
- les tâches purement opérationnelles sans choix d’architecture ;
- remplacer des tests, des benchmarks ou du terrain.

---

## Principe de fonctionnement

La skill fonctionne par **rounds**, en reprenant l’esprit de tes autres skills.

### Round 0 — Cadrage silencieux

Chaque LLM :

- reformule l’intention en une phrase claire ;
- identifie but, contraintes, interdictions, critères de réussite et d’échec ;
- cartographie rapidement les branches de décision (style `grill-me`) ;
- signale les informations manquantes qui changeraient le sens du plan.

### Round 1 — Position initiale et angles morts

Chaque LLM :

- produit sa position sur le sujet (plan, branches, critères, risques) ;
- génère trois à sept angles morts avec le format `angle-mort` :
  - moves explicites (inversion, décalage temporel, test du clou, changement d’échelle, inversion de point de vue, etc.) ;
  - tags `[à vérifier]` ou `[spéculatif]` ;
  - filtre anti-slop (test du remplacement) ;
  - éventuellement un ou deux ⚡ pour les angles les plus contre-intuitifs.

### Round 2 — Lecture croisée et contradictions

Chaque LLM reçoit la position et les angles de l’autre, et doit :

- résumer la position de l’autre ;
- comparer sa propre position aux angles et choix de l’autre ;
- chercher des contradictions :
  - factuelles,
  - logiques,
  - de contraintes,
  - de priorités ;
- pour chaque contradiction :
  - reformuler les deux affirmations,
  - expliquer en quoi elles sont incompatibles,
  - proposer une question pour l’utilisateur ;
- repérer les contournements silencieux :
  - dilution de contraintes,
  - changement de métrique,
  - violation d’interdiction explicite au nom de l’intention globale.

### Round 3 — Convergence ou désaccord structuré

Chaque LLM :

- liste ce qui est compatible ;
- liste ce qui reste contradictoire ;
- met en avant les angles complémentaires utiles ;
- propose un plan ou une recommandation :
  - respect de l’intention,
  - respect des contraintes,
  - désaccords visibles,
  - hypothèses non validées,
  - points à vérifier.

Un juge final (troisième LLM) est optionnel : tu peux lui fournir les deux sorties de Round 3 pour arbitrage ou proposition de scénarios.

---

## Format de sortie

La skill impose un format de sortie Markdown pour que les réponses soient :

- comparables entre LLMs,
- faciles à relire,
- prêtes à stocker ou à analyser.

Sections principales :

- `### Contexte reformulé`
- `### Position initiale (Round 1)`
- `### Angles morts (Round 1)`
- `### Lecture de l'autre LLM (Round 2)`
- `### Synthèse (Round 3)`
- `### Avertissement`

Chaque LLM suit cette structure, ce qui permet :

- de faire des diff entre modèles,
- de repérer les contradictions par simple lecture,
- de brancher ensuite un script ou un orchestrateur pour analyser certaines sections.

---

## Mode d’emploi pas à pas (GLM, DeepSeek, Qwen)

Supposons :

- GLM comme LLM_A (architecte et interrogateur),
- DeepSeek comme LLM_B (implémenteur et challenger),
- Qwen comme juge final.

1. **Préparation**

   - Ouvre un chat GLM (LLM_A).
   - Ouvre un chat DeepSeek (LLM_B).
   - Copie la skill `dual-llm-contradiction-dialog` en début de chaque chat.
   - Précise les rôles :
     - GLM : « Tu es LLM_A (architecte et interrogateur)… »
     - DeepSeek : « Tu es LLM_B (implémenteur et challenger)… »

2. **Brief commun**

   - Donne le même brief aux deux :
     - par exemple : “Je veux concevoir un repo GitHub pour un orchestrateur multi-agents inspiré de Trinity et Conductor, avec ces contraintes : …”.

3. **Round 0 et Round 1**

   - Demande à GLM : “Applique Round 0 puis Round 1 selon la skill.”
   - Demande à DeepSeek la même chose.
   - Récupère les deux réponses (contexte, position, angles morts).

4. **Lecture croisée (Round 2)**

   - Envoie la réponse de GLM à DeepSeek avec :
     - “Voici la position et les angles de LLM_A. Round 2 : lis et cherche les contradictions.”
   - Envoie la réponse de DeepSeek à GLM avec la même consigne.
   - Récupère les listes de contradictions et contournements signalés.

5. **Synthèse (Round 3)**

   - Demande à chacun :
     - “Fais la synthèse selon Round 3, en gardant visibles les désaccords, les hypothèses non validées et les points à vérifier.”

6. **Juge final (optionnel)**

   - Ouvre Qwen, définis un rôle de juge.
   - Fournis les deux sorties de Round 3 (GLM et DeepSeek).
   - Demande un résumé des points d’accord et de désaccord, puis soit un arbitrage, soit deux options à soumettre.

---

## Cas d’usage typiques

- **Design de repo GitHub**  
  Conception d’un repo pour un orchestrateur multi-agents, une suite de skills ou un framework CI/CD.  
  Deux LLMs débattent de :
  - la structure des dossiers,
  - les conventions,
  - le workflow d’orchestration,
  - l’intégration des skills.

- **Conception ou refonte de skill**  
  Écriture ou refactor d’une skill (par exemple une nouvelle version d’`intent-guard-shield` ou d’`angle-mort`).  
  LLM_A propose le design, LLM_B trouve les angles morts, les contradictions et les contournements possibles, et la synthèse te donne une carte des désaccords.

- **Décisions stratégiques autour de projets IA ou dev**  
  Choix d’architectures, de stacks ou de modes d’orchestration.  
  Deux LLMs :
  - font ressortir les contradictions de priorité,
  - montrent où tu risques de contourner des contraintes importantes (sécurité, coût, maintenance).

---

## Limites et avertissements

Comme pour tes autres skills :

- Cette skill teste la cohérence interne d’un plan, pas sa validité externe ni sa faisabilité réelle.
- Un plan peut être logique et bien cadré, et malgré tout échouer en pratique.
- Les contradictions repérées sont des signaux pour toi, pas des verdicts absolus.

À retenir :

> L’intention guide l’action, mais la vérification garde la vérité.  
> Le dialogue entre deux LLMs te montre où ça coince ; à toi ensuite de vérifier dans le réel.
