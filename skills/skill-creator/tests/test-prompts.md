# Test Prompts for Skill Creator

Use these to verify the skill works correctly.

## Test 1 — Vague request
> "I want a skill that helps me write better commit messages"

Expected: The skill should ask clarifying questions (what style? conventional commits? what language?) before generating.

## Test 2 — Precise request
> "Create a skill called 'sql-explainer' that takes a SQL query and explains it step by step in plain French. Trigger: /sql-explain. No tools needed."

Expected: The skill should generate a complete SKILL.md immediately without asking many questions, then propose test prompts.

## Test 3 — Improvement request
> "My existing skill /convert is too verbose. Can you help me tighten it?"

Expected: The skill should read the existing skill, identify verbosity, propose edits, and iterate.
