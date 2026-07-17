from __future__ import annotations

from typing import Any, Dict, Optional, Literal, Union

from pydantic import BaseModel

# Types
Provider = Literal["openai", "anthropic", "local"]
SchemaType = Union[Dict[str, Any], type[BaseModel], BaseModel]


class ConstrainedDecodingMiddleware:
    """
    Middleware provider-aware pour appliquer le décodage contraint
    (constrained decoding) selon la skill 'constrained-decoding'.

    Il fournit une méthode unique `constrained_call` qui :

    - gère OpenAI via Structured Outputs (JSON Schema + strict). [web:36][web:37][web:39][web:42]
    - gère Anthropic via tool use avec un schéma en `input_schema`. [web:43][web:44]
    - délègue aux backends locaux (Outlines / GBNF / autre) si configurés. [web:24][web:28]

    L'interface est volontairement simple :

        result = middleware.constrained_call(
            provider="openai",
            model="gpt-4.1",
            prompt="...",
            schema=MyPydanticModel,
            allow_reasoning=True,
        )

    Et retourne un dict :

        {
            "reasoning": str | None,
            "final_answer": Any,
            "raw": Any,  # réponse brute provider
        }

    Cette classe ne fait pas elle-même le logit masking : elle
    s'appuie sur les mécanismes natifs des providers ou sur un
    backend local qui les implémente.
    """

    def __init__(
        self,
        openai_client: Any | None = None,
        anthropic_client: Any | None = None,
        local_backend: Any | None = None,
    ) -> None:
        """
        Parameters
        ----------
        openai_client:
            Instance de client OpenAI (SDK officiel) initialisée.
        anthropic_client:
            Instance de client Anthropic (SDK Claude) initialisée.
        local_backend:
            Backend local optionnel, par ex. un wrapper Outlines qui expose
            une méthode `constrained_call(...)` avec la même signature.
        """
        self.openai = openai_client
        self.anthropic = anthropic_client
        self.local = local_backend

    # ------------------------------------------------------------------
    # API publique
    # ------------------------------------------------------------------

    def constrained_call(
        self,
        provider: Provider,
        model: str,
        prompt: str,
        schema: Optional[SchemaType] = None,
        allow_reasoning: bool = True,
        max_output_tokens: int = 512,
        temperature: float = 0.0,
        extra: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Appelle un LLM avec décodage contraint, en respectant le contrat
        de la skill 'constrained-decoding' :

        - phase de raisonnement libre optionnelle,
        - phase de sortie structurée conforme au schéma.

        Parameters
        ----------
        provider:
            "openai" | "anthropic" | "local".
        model:
            Nom du modèle côté provider.
        prompt:
            Prompt utilisateur (contenu métier).
        schema:
            Schéma Pydantic ou JSON Schema pour final_answer.
        allow_reasoning:
            True pour autoriser une phase de raisonnement libre avant la
            réponse structurée, False pour forcer uniquement la structure.
        max_output_tokens:
            Limite de tokens pour la réponse structurée.
        temperature:
            Température de génération (souvent 0 pour du structuré).
        extra:
            Paramètres supplémentaires passés au provider.

        Returns
        -------
        dict:
            {
                "reasoning": str | None,
                "final_answer": Any,
                "raw": Any,
            }
        """
        extra = extra or {}

        if provider == "openai":
            return self._call_openai(
                model=model,
                prompt=prompt,
                schema=schema,
                allow_reasoning=allow_reasoning,
                max_output_tokens=max_output_tokens,
                temperature=temperature,
                extra=extra,
            )
        elif provider == "anthropic":
            return self._call_anthropic(
                model=model,
                prompt=prompt,
                schema=schema,
                allow_reasoning=allow_reasoning,
                max_output_tokens=max_output_tokens,
                temperature=temperature,
                extra=extra,
            )
        elif provider == "local":
            if self.local is None:
                raise RuntimeError("Local backend not configured for constrained decoding.")
            return self.local.constrained_call(
                model=model,
                prompt=prompt,
                schema=schema,
                allow_reasoning=allow_reasoning,
                max_output_tokens=max_output_tokens,
                temperature=temperature,
                extra=extra,
            )
        else:
            raise ValueError(f"Unknown provider: {provider}")

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _normalize_schema(self, schema: Optional[SchemaType]) -> Optional[Dict[str, Any]]:
        """
        Normalise le schéma au format JSON Schema (dict) quand c'est possible.
        Accepte :
        - modèle Pydantic (type[BaseModel] ou instance),
        - dict déjà au format JSON Schema,
        - None.
        """
        if schema is None:
            return None
        if isinstance(schema, type) and issubclass(schema, BaseModel):
            return schema.model_json_schema()
        if isinstance(schema, BaseModel):
            return schema.model_json_schema()
        if isinstance(schema, dict):
            return schema
        raise TypeError(f"Unsupported schema type: {type(schema)}")

    def _build_prompt_with_reasoning(
        self,
        user_prompt: str,
        allow_reasoning: bool,
    ) -> str:
        """
        Ajoute au prompt utilisateur les instructions pour séparer
        `reasoning` (texte libre) et `final_answer` (structuré).
        La partie "contrainte" est ensuite appliquée côté provider.
        """
        if not allow_reasoning:
            return (
                "Tu dois répondre STRICTEMENT en JSON conforme au schéma fourni.
"
                "Ne produis pas d'explication en dehors du JSON.

"
                f"{user_prompt}"
            )

        return (
            "Tu vas d'abord réfléchir en texte libre dans un champ `reasoning`, "
            "puis donner ta réponse finale structurée dans un champ `final_answer`, "
            "le tout dans un seul JSON conforme au schéma.

"
            "1. Utilise `reasoning` pour détailler ton raisonnement.
"
            "2. Utilise `final_answer` pour donner la réponse finale, strictement conforme.

"
            f"{user_prompt}"
        )

    # ------------------------------------------------------------------
    # Implémentation OpenAI (Structured Outputs)
    # ------------------------------------------------------------------

    def _call_openai(
        self,
        model: str,
        prompt: str,
        schema: Optional[SchemaType],
        allow_reasoning: bool,
        max_output_tokens: int,
        temperature: float,
        extra: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Utilise OpenAI Structured Outputs (json_schema + strict) pour garantir
        la conformité du JSON au schéma fourni. [web:36][web:37][web:39][web:42]
        """
        import json

        if self.openai is None:
            raise RuntimeError("OpenAI client not configured.")

        json_schema = self._normalize_schema(schema)
        if json_schema is None:
            raise ValueError("JSON schema is required for constrained decoding with OpenAI.")

        # Messages au format Responses API (2024+)
        messages = [
            {
                "role": "user",
                "content": self._build_prompt_with_reasoning(
                    user_prompt=prompt,
                    allow_reasoning=allow_reasoning,
                ),
            }
        ]

        # Voir docs Structured Outputs pour les détails exacts. [web:36][web:37][web:40][web:41]
        response = self.openai.responses.create(
            model=model,
            input=messages,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": json_schema.get("title", "ConstrainedOutput"),
                    "strict": True,
                    "schema": json_schema,
                },
            },
            **extra,
        )

        # Extraction du texte JSON structuré.
        # La forme exacte dépend de la version du SDK.
        # Adapter si besoin (par ex. response.output[0].content[0].text).
        try:
            content = response.output[0].content[0].text
        except Exception:
            # Fallback générique pour d'autres formats
            content = getattr(response, "output_text", None) or str(response)

        data = json.loads(content)

        return {
            "reasoning": data.get("reasoning"),
            "final_answer": data.get("final_answer", data),
            "raw": response,
        }

    # ------------------------------------------------------------------
    # Implémentation Anthropic (tool use synthétique)
    # ------------------------------------------------------------------

    def _call_anthropic(
        self,
        model: str,
        prompt: str,
        schema: Optional[SchemaType],
        allow_reasoning: bool,
        max_output_tokens: int,
        temperature: float,
        extra: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Utilise le mécanisme de tool use de Claude pour encoder le schéma
        dans `input_schema` d'un outil unique. [web:43][web:44]
        """
        if self.anthropic is None:
            raise RuntimeError("Anthropic client not configured.")

        json_schema = self._normalize_schema(schema)
        if json_schema is None:
            raise ValueError("JSON schema is required for constrained decoding with Anthropic.")

        tool = {
            "name": json_schema.get("title", "ConstrainedOutput"),
            "description": "Produit une sortie strictement conforme au schéma JSON donné.",
            "input_schema": json_schema,
        }

        system_parts = [
            "Tu DOIS utiliser l'outil ci-dessous pour produire la sortie finale structurée.",
        ]
        if allow_reasoning:
            system_parts.append(
                "Tu peux raisonner brièvement en texte libre avant l'appel d'outil "
                "mais la réponse finale doit venir de l'outil."
            )
        else:
            system_parts.append("Ne produis pas de texte libre, appelle directement l'outil.")

        system_prompt = "
".join(system_parts)

        msg = self.anthropic.messages.create(
            model=model,
            max_tokens=max_output_tokens,
            temperature=temperature,
            tools=[tool],
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            **extra,
        )

        reasoning_texts = []
        final_data: Any = None

        # Parcours du contenu renvoyé par Claude.
        # Adapter selon la structure exacte (`msg.content` / `content_block.type`).
        for block in getattr(msg, "content", []):
            block_type = getattr(block, "type", None)
            if block_type == "text":
                reasoning_texts.append(getattr(block, "text", ""))
            elif block_type in ("tool_use", "tool_result", "tool_call"):
                # Pour Claude, `tool_use` contient `input` déjà validé.
                final_data = getattr(block, "input", None)

        return {
            "reasoning": "

".join(t for t in reasoning_texts if t) or None,
            "final_answer": final_data,
            "raw": msg,
        }


# ----------------------------------------------------------------------
# Exemple d'utilisation (à adapter dans ton orchestrateur)
# ----------------------------------------------------------------------

if __name__ == "__main__":
    print(
        "Ce module définit uniquement le middleware "
        "`ConstrainedDecodingMiddleware`.
"
        "Instancie-le dans ton orchestrateur avec les clients OpenAI / Anthropic "
        "et appelle `constrained_call(...)`."
    )
