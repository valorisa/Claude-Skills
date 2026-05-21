# Contributing to Claude Skills Collection

Thank you for your interest in contributing! This guide will help you create high-quality skills using our TDD methodology.

[🇫🇷 Version française](./CONTRIBUTING_FR.md)

---

## 🎯 What Makes a Good Skill?

A good skill:

- ✅ Solves a **real problem** (observed through testing)
- ✅ Is **generic** (not project-specific)
- ✅ Has been **TDD-validated** (RED-GREEN-REFACTOR)
- ✅ Counters **specific rationalizations** (documented from tests)
- ✅ Includes **metrics** (before/after improvements)

---

## 🧪 TDD Methodology (Required)

All skills **must** follow Test-Driven Development for documentation:

### 1️⃣ RED Phase: Create Failing Tests

**Create pressure scenarios** that expose agent weaknesses:

```markdown
Scenario: [Name]
Pressures: Time + Sunk Cost + Authority

Prompt:
"You've been working for 3 hours on this bug. 
Context is at 80%. Your boss needs it fixed in 30 minutes.
Here's 20KB of logs. What do you do?"
```

**Run tests WITHOUT the skill** using sub-agents:

- Document exact behaviors
- Capture rationalizations verbatim
- Identify patterns

**Required:** At least 3 scenarios with combined pressures.

---

### 2️⃣ GREEN Phase: Write Minimal Skill

**Write skill to counter observed failures:**

```yaml
---
name: skill-name
description: Use when [specific triggers and symptoms]
---

## Overview
[Core principle in 1-2 sentences]

## Action Matrix
| Symptom | Action | Rationalization to Counter |
```

**Test WITH the skill:**

- Same scenarios
- Verify improvements
- Document remaining issues

---

### 3️⃣ REFACTOR Phase: Close Loopholes

**Identify new rationalizations:**

- What new excuses did agents find?
- What loopholes remain?

**Add explicit counters:**

```markdown
## Common Rationalizations
| Excuse | Reality |
|--------|---------|
| "I'll explain first" | Explanations cost tokens. Act. |
```

**Re-test until bulletproof.**

---

## 📝 Skill Structure Requirements

### Frontmatter (YAML)

```yaml
---
name: skill-name-with-hyphens
description: Use when [triggers]. Max 1024 chars total. Third person. No workflow summary.
---
```

**Rules:**

- `name`: Letters, numbers, hyphens only (no special chars)
- `description`: Starts with "Use when...", lists symptoms/triggers
- Third person ("user hits" not "you hit")
- Rich keywords for search (error messages, symptoms, tools)

### Content Sections

**Required:**

- Overview (core principle)
- Quick reference (table or bullets)
- Common mistakes
- Examples (1 excellent example > 5 mediocre ones)

**Optional:**

- Flowchart (only if decision non-obvious)
- Supporting files (for tools or heavy reference)

**Forbidden:**

- Narrative storytelling
- Multi-language dilution
- Generic templates
- Code in flowcharts

---

## 📊 Contribution Checklist

Before submitting a PR:

### RED Phase

- [ ] Created 3+ pressure scenarios
- [ ] Ran tests WITHOUT skill
- [ ] Documented baseline failures verbatim
- [ ] Identified rationalization patterns

### GREEN Phase

- [ ] Wrote minimal skill
- [ ] Frontmatter conforms to spec
- [ ] Description starts with "Use when..."
- [ ] Ran tests WITH skill
- [ ] Documented improvements

### REFACTOR Phase

- [ ] Identified new rationalizations
- [ ] Added explicit counters
- [ ] Built rationalization table
- [ ] Re-tested until bulletproof

### Quality

- [ ] Word count <500 (aim for concise)
- [ ] Keywords for search optimization
- [ ] One excellent example
- [ ] No narrative storytelling

### PR Documentation

- [ ] Include test results (baseline → GREEN → REFACTOR)
- [ ] Include metrics (% improvement)
- [ ] Explain the problem solved
- [ ] Link to related issues (if any)

---

## 🚫 Anti-Patterns to Avoid

### ❌ Writing Skill Before Testing

```
DON'T: Write skill based on intuition
DO: Test first, observe failures, then write
```

### ❌ Generic Descriptions

```
❌ "For debugging"
✅ "Use when tests fail inconsistently, race conditions, timing issues"
```

### ❌ Narrative Examples

```
❌ "In session 2025-10-03, we found empty projectDir caused..."
✅ Reusable pattern with clear before/after
```

---

## 📤 Submitting Your PR

1. **Fork** this repo
2. **Create branch**: `feature/your-skill-name`
3. **Add skill** to `skills/your-skill-name/SKILL.md`
4. **Update README.md** and **README_FR.md** with skill entry
5. **Commit** with clear message
6. **Open PR** with:
   - Problem statement
   - TDD test results
   - Metrics (before/after)
   - Example usage

---

## 🤝 Code of Conduct

- Be respectful and constructive
- Focus on improving skills quality
- Share test results and metrics
- Help others follow TDD methodology

---

## 📚 Resources

- [Writing Skills Guide](https://github.com/anthropics/claude-code) (official)
- [TDD for Documentation](https://en.wikipedia.org/wiki/Test-driven_development)
- [rescue-tokens TDD example](./skills/rescue-tokens/SKILL.md)

---

## 💬 Questions?

Open an issue with the `question` label, or contact [@valorisa](https://github.com/valorisa).

Thank you for contributing! 🎉
