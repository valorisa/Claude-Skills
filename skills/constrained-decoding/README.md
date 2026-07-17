# Skill & Middleware : constrained-decoding

Ce dossier contient deux briques complémentaires autour du **décodage contraint** (“constrained decoding”) pour LLM :

- une **skill d’agent** : `skills/constrained-decoding/SKILL.md`
- un **middleware provider‑aware** : `constrained_decoding_middleware.py`

Elles ne servent pas au même niveau : la skill parle au **modèle**, le middleware parle aux **APIs** (OpenAI, Anthropic, backend local).

---

## 1. Vue d’ensemble

Objectif global :

- Garantir que les sorties destinées à être lues par du code (JSON, DSL, commandes…) sont structurellement valides et conformes à un schéma ou une grammaire.
- Séparer explicitement :
  - une phase de raisonnement libre (`reasoning`),
  - d’une phase de sortie structurée contrainte (`final_answer`).

Architecture logique :

- La skill `constrained-decoding` définit le **protocole** pour l’agent.
- Le middleware `ConstrainedDecodingMiddleware` fournit l’**implémentation technique** côté orchestrateur.

---

## 2. Skill d’agent : `skills/constrained-decoding/SKILL.md`

### Rôle

La skill `constrained-decoding` est un contrat conceptuel pour l’agent LLM :

- Elle explique comment l’agent doit structurer sa réponse :
  - d’abord un champ `reasoning` (texte libre, raisonnement à voix haute),
  - ensuite un champ `final_answer` (réponse finale strictement structurée).
- Elle insiste sur le fait que le prompt seul (“Réponds en JSON valide”) ne suffit jamais à garantir 100 % de validité de format.

### Ce que la skill exige de l’agent

L’agent doit :

- Utiliser le pattern en deux phases :

  ```jsonc
  {
    "reasoning": "texte libre, détaillé, potentiellement long",
    "final_answer": {
      // structure strictement conforme au schéma fourni
    }
  }
  ```

- Comprendre que la contrainte de format ne s’applique qu’à `final_answer`, pas à `reasoning`.
- Activer ce pattern dès que la sortie :
  - est parsée par du code (`JSON.parse`, sérialisation, validation),
  - est utilisée pour des outils, APIs, bases de données, pipelines, workflows d’agents, etc.
- Éviter les anti‑patterns :
  - se fier uniquement au prompt pour obtenir du JSON valide,
  - “réparer” les sorties avec des regex post‑hoc,
  - boucler en retry jusqu’à ce qu’un JSON parse (sans contrainte forte).

### Hypothèse implicite

La skill suppose qu’il existe, côté système, un orchestrateur ou un middleware capable de :

- utiliser les Structured Outputs d’OpenAI (JSON Schema strict),
- utiliser le tool use de Claude / Anthropic avec `input_schema`,
- ou utiliser une lib locale (Outlines, GBNF, etc.) pour faire le décodage contraint.

La skill ne dit pas comment c’est implémenté, seulement que ça doit l’être.

---

## 3. Middleware : `constrained_decoding_middleware.py`

### Rôle

Le fichier `constrained_decoding_middleware.py` fournit une classe :

```python
from constrained_decoding_middleware import ConstrainedDecodingMiddleware

middleware = ConstrainedDecodingMiddleware(
    openai_client=...,      # client OpenAI initialisé
    anthropic_client=...,   # client Anthropic initialisé
    local_backend=...,      # optionnel : backend Outlines / GBNF
)
```

Cette classe implémente réellement le décodage contraint en fonction du provider, via :

- OpenAI : Structured Outputs + `response_format: { type: "json_schema", strict: true }`.
- Anthropic : tool use avec un `input_schema` JSON.
- local : délégation à un backend (ex. Outlines, llama.cpp GBNF).

### API de haut niveau

La méthode principale :

```python
result = middleware.constrained_call(
    provider="openai",       # "openai" | "anthropic" | "local"
    model="gpt-4.1",
    prompt="Ton prompt métier ici",
    schema=MyPydanticModel,  # ou dict JSON Schema
    allow_reasoning=True,
    max_output_tokens=512,
    temperature=0.0,
)
```

Retourne :

```python
{
    "reasoning": str | None,
    "final_answer": Any,  # dict / objet conforme au schéma
    "raw": Any,           # réponse brute provider
}
```

### Comportement par provider

- **OpenAI**

  - Normalise le schéma (Pydantic → JSON Schema).
  - Construit un prompt qui explique le pattern `reasoning` + `final_answer`.
  - Appelle l’API Responses avec Structured Outputs (`json_schema`, `strict: true`), ce qui garantit la conformité du JSON.
  - Parse la sortie JSON et expose `reasoning` + `final_answer`.

- **Anthropic (Claude)**

  - Encode le schéma dans un “tool” unique avec `input_schema`.
  - Construit un `system` qui impose l’usage de l’outil pour la réponse finale.
  - Lit les blocs de type `text` comme `reasoning` (optionnel),
    et le bloc `tool_use` (ou équivalent) comme `final_answer` (JSON déjà structuré).

- **Local backend**

  - Si tu fournis un backend local (ex. Outlines), le middleware lui délègue simplement l’appel :
    - à toi de garantir le logit masking / grammaire côté backend.

---

## 4. Différences essentielles entre la skill et le middleware

### 4.1. Niveau d’abstraction

- `SKILL.md`  
  - Niveau conceptuel / protocole.  
  - Cible : LLM / agent.  
  - Décrit ce que l’agent doit faire (séparer raisonnement et sortie, utiliser la contrainte dès qu’on parle à du code).

- `constrained_decoding_middleware.py`  
  - Niveau implementation / infra.  
  - Cible : orchestrateur / code Python.  
  - Décrit comment utiliser OpenAI, Anthropic, ou un backend local pour garantir la structure.

### 4.2. Utilisateurs

- La skill est injectée dans les prompts (système ou contexte) pour guider le comportement d’un modèle (Claude, Qwen, DeepSeek, etc.).
- Le middleware est importé dans ton code pour piloter les appels API de manière unifiée.

### 4.3. Couplage aux providers

- La skill est provider‑agnostique : elle mentionne OpenAI/Anthropic/Outlines seulement comme ressources de référence.
- Le middleware est provider‑aware :
  - logique spécifique OpenAI Structured Outputs,
  - logique spécifique Claude tool use,
  - hook explicite pour un backend local.

---

## 5. Pattern recommandé d’utilisation

1. **Côté agent / skill**

   - Tu attaches la skill `constrained-decoding` à l’agent qui doit produire du JSON ou des réponses parsables.
   - Le modèle apprend à :
     - toujours structurer sa réponse avec `reasoning` + `final_answer`,
     - ne jamais se contenter de “Réponds en JSON valide” sans support infra.

2. **Côté orchestrateur / middleware**

   - Quand tu dois réellement appeler un LLM :
     - tu passes le schéma (Pydantic / JSON Schema),
     - tu choisis `provider="openai"`, `"anthropic"` ou `"local"`,
     - tu appelles `middleware.constrained_call(...)`.

   - Le middleware sélectionne la bonne stratégie :
     - Structured Outputs pour OpenAI,
     - tool use pour Anthropic,
     - backend local (Outlines, GBNF…) pour les modèles open‑weights.

---

## 6. Résumé

- La skill est le langage que tu donnes au modèle pour lui expliquer la capacité “constrained decoding”.
- Le middleware est la colle technique qui parle aux APIs et applique réellement le décodage contraint.

En production :

- tu ne demandes pas gentiment “du JSON valide”,
- tu combines **skill + middleware** pour le garantir, tout en laissant un espace de raisonnement libre avant la sortie structurée.
