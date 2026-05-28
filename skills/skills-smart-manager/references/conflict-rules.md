# Skill Conflict Resolution Rules

This document defines known conflicts between skills and how to resolve them.

## Format

```markdown
### CONFLICT: skill-a vs skill-b

**Reason:** Brief explanation of why they conflict

**Priority Logic:**
- skill-a: priority N (reason)
- skill-b: priority M (reason)

**Resolution:** Keep [higher-priority-skill], unload [lower-priority-skill]

**Exceptions:** List any cases where this rule should not apply
```

---

## Code Formatters

### CONFLICT: prettier-formatter vs standard-js-linter

**Reason:** Both modify JavaScript/TypeScript formatting with incompatible rules

**Priority Logic:**

- prettier-formatter: priority 5 (widely adopted standard)
- standard-js-linter: priority 3 (opinionated subset)

**Resolution:** Keep prettier-formatter, unload standard-js-linter

**Exceptions:** If project explicitly uses Standard.js (detected via `package.json` config)

---

### CONFLICT: eslint-auto-fix vs prettier-formatter

**Reason:** ESLint can auto-fix style issues, overlaps with Prettier

**Priority Logic:**

- prettier-formatter: priority 5 (formatting specialist)
- eslint-auto-fix: priority 4 (linting + formatting)

**Resolution:** Keep both, but configure ESLint to defer style rules to Prettier

**Exceptions:** None — they should work together via `eslint-config-prettier`

---

## Testing Frameworks

### CONFLICT: jest-tdd vs vitest-tdd

**Reason:** Both provide test runners and TDD workflows for same ecosystem

**Priority Logic:**

- vitest-tdd: priority 5 (modern, faster, better DX)
- jest-tdd: priority 4 (established, more mature ecosystem)

**Resolution:** Detect which test runner is in `package.json`:

- If `vitest` → keep vitest-tdd
- If `jest` → keep jest-tdd
- If both → keep vitest-tdd (modern default)

**Exceptions:** Project has extensive Jest-specific setup (custom transformers, etc.)

---

### CONFLICT: tdd-hybrid vs spec-driven

**Reason:** Both guide development workflow but with different philosophies

**Priority Logic:**

- spec-driven: priority 6 (higher-level, includes TDD as subprocess)
- tdd-hybrid: priority 5 (focused on test-first coding)

**Resolution:** Keep both — they work at different abstraction levels

**Exceptions:** None — `spec-driven` invokes `tdd-hybrid` during implementation phase

---

## Documentation Generators

### CONFLICT: jsdoc-generator vs typedoc-generator

**Reason:** Both generate API documentation for TypeScript projects

**Priority Logic:**

- typedoc-generator: priority 5 (TypeScript-native)
- jsdoc-generator: priority 3 (JavaScript-focused)

**Resolution:** Detect TypeScript:

- If `tsconfig.json` exists → keep typedoc-generator
- Otherwise → keep jsdoc-generator

**Exceptions:** Legacy JavaScript project with extensive JSDoc annotations

---

## Deployment Skills

### CONFLICT: vercel:deploy vs netlify:deploy

**Reason:** Both deploy to hosting platforms — project can only target one at a time

**Priority Logic:**

- Context-dependent (whichever is configured in project)

**Resolution:** Detect deployment config:

- If `vercel.json` or `.vercel/` → keep vercel:deploy
- If `netlify.toml` or `netlify/` → keep netlify:deploy
- If both → ask user which to use

**Exceptions:** Multi-platform deployment (rare — keep both)

---

## Meta-Skills

### CONFLICT: skills-smart-manager vs token-optimization

**Reason:** Both aim to optimize token usage, but at different scopes

**Priority Logic:**

- skills-smart-manager: priority 7 (meta-management layer)
- token-optimization: priority 6 (session-wide optimization)

**Resolution:** Keep both — they complement each other

**Exceptions:** None — skills-smart-manager can even optimize token-optimization itself if it becomes stale

---

### CONFLICT: rescue-tokens vs token-optimization

**Reason:** Both address token management, but with different triggers

**Priority Logic:**

- rescue-tokens: priority 8 (emergency reactive mode)
- token-optimization: priority 6 (proactive systematic approach)

**Resolution:** Keep both — rescue-tokens is emergency response, token-optimization is prevention

**Exceptions:** None

---

## Domain-Specific Conflicts

### CONFLICT: rust-best-practices vs go-best-practices

**Reason:** Different languages — rarely both needed simultaneously

**Priority Logic:**

- Depends on current working directory

**Resolution:** Detect primary language:

- If `Cargo.toml` → keep rust-best-practices
- If `go.mod` → keep go-best-practices
- If both → keep whichever was used more recently

**Exceptions:** Polyglot monorepo (keep both)

---

### CONFLICT: docker-compose vs kubernetes-deploy

**Reason:** Different orchestration approaches — typically not both needed

**Priority Logic:**

- kubernetes-deploy: priority 5 (production scale)
- docker-compose: priority 4 (local development)

**Resolution:** Context-dependent:

- If in production context → keep kubernetes-deploy
- If local development → keep docker-compose
- If unclear → ask user

**Exceptions:** Migration projects (keep both temporarily)

---

## Adding New Conflict Rules

When you discover a new conflict:

1. Document the conflict here using the template format
2. Explain *why* they conflict (overlapping functionality)
3. Define priority logic based on:
   - Maturity / adoption (Prettier > Standard)
   - Specificity (TypeDoc > JSDoc for TS)
   - Modernity (Vitest > Jest)
   - Context (Rust skills in Rust project)
4. Provide clear resolution steps
5. List exceptions where the rule shouldn't apply

---

## Resolution Priority Scale

| Priority | Meaning | Examples |
|----------|---------|----------|
| 8-10 | **Critical** — Always keep unless explicitly disabled | rescue-tokens, core workflows |
| 6-7 | **Important** — Keep in most contexts | spec-driven, tdd-hybrid |
| 4-5 | **Useful** — Keep when relevant | Language-specific skills |
| 2-3 | **Nice-to-have** — Unload if context pressure | Documentation generators |
| 1 | **Experimental** — First to unload | Beta skills, deprecated tools |

---

## Automatic Conflict Detection

The `analyze_context.py` script uses these rules to detect conflicts:

```python
# Simplified example
conflicts = [
    ("prettier-formatter", "standard-js-linter"),
    ("jest-tdd", "vitest-tdd"),
    # ... more pairs
]

for skill_a, skill_b in conflicts:
    if skill_a in active and skill_b in active:
        resolve_conflict(skill_a, skill_b)
```

See `scripts/analyze_context.py` for full implementation.
