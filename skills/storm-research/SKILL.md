---
name: storm-research
description: "À utiliser quand on demande de lancer une Storm Recherche, d'utiliser le skill storm-research, d'appliquer la méthode STORM à un sujet, dit « storm recherche sur X » / « briefing STORM sur X ». Ce skill exécute la méthode STORM en plusieurs phases et produit un briefing HTML vérifié."
argument-hint: "[sujet à rechercher]"
---

# Storm Recherche

## Ce que fait ce skill

Transforme un sujet en un briefing HTML multi-perspectives et vérifié. Il simule cinq angles experts sur le sujet, cartographie leurs contradictions, synthétise tout dans un rapport HTML autonome, et applique une revue critique et une vérification des sources. Le pipeline est exhaustif et ne saute aucune phase : c'est intentionnellement plus lourd qu'une recherche web rapide.

C'est une adaptation maison de la méthode STORM de Stanford (Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking, NAACL 2024). Différences assumées à toujours garder à l'esprit sont décrites dans la documentation interne : priorisation des sources primaires, contrainte de vérification systématique et panel construit par l'auteur.

## Positionnement honest broker (non négociable)

Ce skill n'existe que si ces trois garde-fous tiennent. Sans eux, ce n'est pas une Storm Recherche.

1. **Recherche réelle uniquement.** Chaque angle et chaque citation doit remonter à une source réelle, ouverte et lue. Aucune étude, aucun chiffre, aucune URL inventés. Si un chiffre n'est pas vérifiable, il doit être explicitement marqué comme non confirmé.
2. **Le panel est construit maison.** Toujours le divulguer dans le rapport. L'accord entre les angles est une hypothèse forte, pas une preuve indépendante, et surtout pas un consensus du champ.
3. **La vérification est obligatoire.** Un rapport livré sans la Phase 4 n'est pas une Storm Recherche. La bannière de vérification doit être vraie (compte réel d'inventées / corrigées / rétrogradées).

## Portabilité

Ce skill est autonome. Il dépend uniquement des outils intégrés de Claude Code (l'outil `Agent` avec l'agent `general-purpose`, `Write`, et la recherche/fetch web utilisée dans ces agents) plus des fichiers du dossier de skill (template HTML, CSS). Il n'exige pas d'autres ressources externes non standard.

## Langue et style

Sortie en français, vouvoiement neutre côté rapport (c'est un livrable). Ton sobre, factuel, sans survente. Pas de tirets cadratins, des virgules. Charte du rapport HTML : navy #0D1B2A, orange #F47C3C, cream #F7F1E1 (conserver le CSS du template). Police Inter. Respecter la mise en page fournie par le template.

## Phase 0 : cadrer le sujet

1. Si `$ARGUMENTS` contient le sujet, utilise-le. Sinon, demande quoi rechercher.
2. Énonce ton interprétation du sujet en une ligne et avance. Ne pose une question de clarification que si le sujet est réellement ambigu d'une façon qui change la recherche. Par défaut, avance.
3. Identifie le **rôle du lecteur** pour que la section "action" le cible. Déduis-le du sujet et du contexte donné ; si ce n'est pas clair, demande en une ligne, ou prends par défaut "un·e créateur·rice de produit / décideur·se stratégique".
4. Dérive un `topic-slug` en kebab-case à partir du sujet, pour le nom de fichier.
5. Indique au lecteur que le pipeline tourne (5 angles, puis vérification). Une ligne suffit.

## Phase 1 : cinq angles experts (agents en parallèle)

Lance **cinq agents `general-purpose` dans un seul message** pour qu'ils tournent en parallèle. Chacun reçoit le MÊME cadrage du sujet plus son propre angle. Utilise ces prompts exacts, en substituant les variables {SUJET} et {CADRE}.

1. LE PRATICIEN — `Tu es LE PRATICIEN pour : {SUJET} ({CADRE}). Tu travailles ce sujet au quotidien. Fais de la vraie recherche web (priorité aux sources récentes, études de cas, retours d'opérateurs). Produis : a) un résumé opérationnel, b) 6–10 points concrets, c) 6 références réelles (URL + citation courte).`
2. L'ACADÉMIQUE — `Tu es L'ACADÉMIQUE pour : {SUJET} ({CADRE}). Tu te fies aux preuves évaluées par les pairs et aux tailles d'effet, pas aux anecdotes. Fais de la vraie recherche web (études revues par les pairs, méta-analyses). Produis : a) synthèse des preuves, b) lacunes méthodologiques, c) 6 références principales.`
3. LE SCEPTIQUE — `Tu es LE SCEPTIQUE pour : {SUJET} ({CADRE}). Tu penses que la vue dominante est surestimée ou fausse. Construis le steelman le plus solide du scénario pessimiste. Fais de la vraie recherche web pour trouver contre-exemples, limites et biais. Produis : a) arguments contraires, b) scénarios où ça casse, c) 6 références.`
4. L'ÉCONOMISTE — `Tu es L'ÉCONOMISTE pour : {SUJET} ({CADRE}). Tu suis l'argent. Fais de la vraie recherche web sur les revenus, valorisations, taille de marché, flux de financement, unit economics et modèles de monétisation. Produis : a) chiffres de marché, b) acteurs clés, c) 6 références (rapports financiers, études de marché).`
5. L'HISTORIEN — `Tu es L'HISTORIEN pour : {SUJET} ({CADRE}). Tu as déjà vu des cycles de disruption et tu cherches les motifs. Fais de la vraie recherche web pour trouver de vrais parallèles historiques et des enseignements. Produis : a) analogies pertinentes, b) cycles comparables, c) 6 références historiques ou d'archives.`

Chaque agent renvoie un brief structuré (titre, 6–10 points, références exactes avec URL). Quand les cinq briefs sont reçus, poster une note de 2–3 lignes dans le chat : orientation générale de convergence et le désaccord le plus tranchant. Les briefs détaillés restent en interne (ils alimentent la Phase 2).

## Phase 2 : cartographier les contradictions

En travaillant uniquement à partir des cinq briefs, déterminez (en direct, sans agents) :

1. **Conflits directs** — là où deux angles ou plus affirment le contraire. Nomme les claims précis qui s'opposent, pas juste les thèmes.
2. **Preuve la plus forte vs la plus faible** — quel angle est le mieux étayé (hiérarchie : causal évalué par les pairs > donnée officielle > rapport financier > sondage commandité > anecdote/analogie > préprint) et lequel est le plus faible, avec justification.
3. **La question qui tranche** — la seule question empirique qui réglerait la plus grosse contradiction.
4. **Accord universel** — ce que chaque angle confirme, même les opposants. C'est probablement vrai.
5. **L'angle mort** — ce qu'AUCUN angle n'a traité. Ça devient le "6e angle manquant" et alimente la Question de frontière.

Cette carte est la matière première des enseignements du rapport (soutenu/contesté), de la connexion cachée, de l'encadré 6e angle et de la question de frontière.

## Phase 3 : synthétiser le rapport HTML

1. Lire `report-template.html` dans ce dossier de skill. Cloner-le, ne pas reconstruire le CSS.
2. Remplir chaque section. Correspondance depuis les phases :
   - **Résumé 60 secondes** — niveau décideur, nuance mais clair. Commence par le fait établi, puis l'interprétation contestée.
   - **5 enseignements clés, classés par fiabilité** — les choses les plus importantes désormais connues, la plus fiable en premier. Chaque enseignement porte un score de confiance 1–10 (fixé en Phase 4) et une liste de 1–3 références primaires.
   - **Connexion cachée** — le lien non évident de la Phase 2 qui n'apparaît qu'en croisant les cinq angles.
   - **Hypothèse / 6e angle manquant** — l'angle mort de la Phase 2, présenté comme l'angle qui pourrait changer les conclusions.
   - **Action** — 3 à 6 mouvements précis pour le rôle du lecteur identifié en Phase 0. Précis, opérationnels, datés si possible.
   - **Guide "ce que vous pouvez affirmer"** — trois colonnes : Sûr / Réserve / Éviter, rempli après la vérification de Phase 4.
   - **Question de frontière** — la seule question qui changerait tout.
   - **Références** — chaque citation avec son statut de vérification (fixé en Phase 4) et lien direct à la source primaire.
3. Écrire le fichier final sous `storm-reports/{topic-slug}-briefing.html` (relatif au dossier de travail courant ; créer le dossier si besoin).

## Phase 4 : peer review adversarial + vérification (à ne pas sauter)

C'est ce qui sépare une Storm Recherche d'un rapport normal. Faire cette phase avant de livrer.

4a. Auto-review (en direct). Note chacun des 5 enseignements 1–10 pour la fiabilité et justifie. Identifier le maillon faible et ce qui le vérifierait. Faire un bias check (quel angle a dominé la preuve ? quelles hypothèses guidées ?).

4b. Vérifier chaque citation (agents en parallèle). Lancer des agents `general-purpose` en un seul message, un par grappe de citations distincte (regrouper les claims liés ; ~4–6 agents). Prompt-type : `Vérifie indépendamment cette citation contre sa source PRIMAIRE. Sois sceptique, ne te fie pas aux résumés de blogs secondaires. CLAIM : {claim + chiffre cité + source nommée}. Trouve la vraie source primaire, vérifie chiffre/date/contexte, et rends un verdict (VÉRIFIÉ / CORRIGÉ / NON TROUVÉ) avec preuve (URL + extrait).` Chaque agent retourne une liste de verdicts structurés pour sa grappe.

4c. Appliquer les corrections. Éditer le rapport :

- Corriger tout chiffre, titre, date ou caractérisation faux.
- Baisser les scores de confiance là où la preuve s'est révélée mince ; rétrograder les preprints et claims disputés dans l'encadré "Signal contesté".
- Ré-attribuer honnêtement les stats de sondage unique ou commandité.
- Remplir la bannière de vérification (`X inventée(s), Y corrigée(s), Z rétrogradée(s)`) et les tags de statut par citation.
- Remplir le guide "ce que vous pouvez affirmer" à partir des verdicts.

La livraison n'est autorisée qu'une fois toutes les étapes de vérification et correction complétées.

## Sortie

1. Livrable final : `storm-reports/{topic-slug}-briefing.html` (la v2, après vérification).
2. Ouvrir le fichier pour le lecteur avec l'ouvreur par défaut de la plateforme : macOS `open <chemin>`, Linux `xdg-open <chemin>`, Windows `start "" <chemin>`. Si l'OS n'est pas clair, donner juste le chemin.
3. Dans le chat, fournir : le chemin du fichier, le compte de vérification (`N/N vérifiées, X inventée(s), Y corrigée(s), Z rétrogradée(s)`), le seul résultat universel, la question de frontière, et la liste des actions proposées.

## Garde-fous

- **Recherche réelle uniquement.** Voir positionnement honest broker. Jamais de source inventée.
- **Le panel est construit maison.** Toujours divulguer la composition du panel dans le rapport. La convergence est une hypothèse, pas un consensus du champ.
- **Vérification obligatoire.** Pas de Phase 4, pas de Storm Recherche. La bannière doit refléter la réalité des vérifications effectuées.
- **Fiabilité = qualité de preuve, pas confiance.** Noter selon la hiérarchie : causal évalué par les pairs > donnée officielle/financière > sondage commandité unique > analogie > preprint.
- **Vise le lecteur, pas une personne par défaut.** L'action et le guide parlent au rôle identifié en Phase 0. Rester générique si aucun rôle n'est donné.
- **Coût.** Une exécution lance ~9 à 11 agents par run. C'est normal. Ne dépasser pas cinq angles ni un vérificateur par grappe de citations.
- **Design.** Charte navy/orange/cream, Inter. Conserver le CSS du template tel quel, ne pas remplacer par un autre style visuel.
