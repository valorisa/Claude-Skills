# TDD Hybrid

Test-driven development combining strict discipline with intelligent workflow.

## When to use

- Implementing features with tests
- Fixing bugs with TDD
- Any code change requiring test coverage

## What it does

**Triage:** Classifies work as LIGHT (simple, <20 lines) or FULL (complex, architectural).

**LIGHT:** 1 question, tracer bullet, vertical slicing.  
**FULL:** Planning phase + domain awareness (CONTEXT.md/ADRs) + deep modules.

**Always enforces:** Iron Law (test before code), Verify RED/GREEN mandatory, anti-rationalisations.

## Workflow

```
/tdd-hybrid
  ↓ Triage (LIGHT/FULL)
  ↓ Planning (FULL only)
  ↓ Tracer Bullet (first test end-to-end)
  ↓ Incremental Loop (RED→Verify RED→GREEN→Verify GREEN)
  ↓ Refactor
```

## Best of both worlds

- **Superpowers:** Iron Law, strict verification, anti-rationalisations
- **MattPocock:** Planning, vertical slicing, domain awareness, deep modules

See [SKILL.md](./SKILL.md) for full documentation.
