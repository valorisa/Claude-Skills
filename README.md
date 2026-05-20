# Claude Skills Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-1-blue.svg)](./skills)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple.svg)](https://claude.ai/code)
[![TDD](https://img.shields.io/badge/methodology-TDD-green.svg)](https://en.wikipedia.org/wiki/Test-driven_development)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/valorisa/claude-skills/graphs/commit-activity)

> **Community-contributed skills for [Claude Code](https://claude.ai/code) to enhance productivity, optimize token usage, and improve development workflows.**

[🇫🇷 Version française](./README_FR.md)

---

## 📋 Table of Contents

- [What Are Claude Skills?](#-what-are-claude-skills)
- [Available Skills](#-available-skills)
- [Installation](#-installation)
- [TDD Methodology](#-tdd-methodology-explained)
- [Acronyms & Terminology](#-acronyms--terminology)
- [How Skills Work](#-how-skills-work)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🤔 What Are Claude Skills?

**Skills** are reusable process guides that help Claude Code (and other AI agents) follow proven techniques, patterns, and workflows consistently.

### Why Skills Matter

Without skills, AI agents:
- ❌ Make inconsistent decisions
- ❌ Fall into common traps (token waste, verbose output, wrong tools)
- ❌ Rationalize bad practices ("I'll explain first" = wasting tokens)

With skills, AI agents:
- ✅ Follow validated workflows
- ✅ Apply battle-tested optimizations
- ✅ Counter their own rationalizations
- ✅ Deliver predictable, high-quality results

### Skills vs. Prompts

| Aspect | One-time Prompt | Persistent Skill |
|--------|----------------|------------------|
| **Scope** | Single conversation | All future conversations |
| **Quality** | Untested, ad-hoc | TDD-validated, battle-tested |
| **Maintenance** | Copy-paste every time | Installed once, updated centrally |
| **Learning** | You teach agent each time | Agent learns pattern once |

---

## 📦 Available Skills

### 🚀 rescue-tokens

**Prevents token exhaustion and rate limits through 9 optimization patterns.**

#### The Problem

Users hit "rate limit" errors not because they sent too many messages, but because they're **burning tokens silently**:
- Eternal conversations (bloated context)
- Verbose output (explanations cost tokens)
- Wrong model choice (Opus 4.7 for simple tasks = 5x cost)
- MCP plugin bloat (overhead on every message)
- Expensive files (PDFs, images = 10-50x tokens)

#### The Solution

`rescue-tokens` detects and fixes 9 token waste patterns **automatically**.

#### When to Use

**Skill activates when ONE OR MORE conditions present (OR logic):**
- ⚠️ Rate limit warnings
- ⚠️ Context ≥40% full
- ⚠️ $20-$100/month plan after 2pm
- ⚠️ Conversation >90 minutes old
- ⚠️ 5+ MCP plugins loaded
- ⚠️ User says "don't lose context"
- ⚠️ Opus 4.7 for simple tasks

**Note:** Each flag ALONE triggers emergency mode. You don't need all conditions.

#### What It Does

**Action Matrix** (No user confirmation needed):
- Context 40-70% → `/compact` key facts
- Context >70% → New conversation, 3-sentence handoff
- Rate limit + urgent → Sub-agent in Sonnet immediately
- Opus 4.7 for CRUD → Switch to Sonnet
- PDF/image → Ask for text excerpts
- 5+ MCPs → Disable unused

**Response Discipline Under Pressure:**
- <100 words total
- NO markdown sections
- NO "Reasoning:" blocks
- NO tables
- Action verbs only: "Switched to Sonnet. Starting OAuth."

**Rationalizations Countered:**
The skill explicitly counters 9 agent rationalizations:
- "Let me explain why" → Explanations burn tokens
- "I'll add Reasoning sections" → State decision only
- "Tables help compare" → Tables cost 5x tokens
- "User wants context" → 80% is dead weight
- ...and 5 more

#### Verified Results

**TDD test results (7 scenarios):**
- **Baseline:** 950 words average (agent without skill)
- **GREEN Phase:** 525 words (45% improvement)
- **REFACTOR Phase:** 97 words (90% improvement)
- **Rationalizations:** 0 in final tests

[📖 Full Documentation](./skills/rescue-tokens/SKILL.md)

---

## 🎯 Installation

### Prerequisites

- [Claude Code](https://claude.ai/code) installed (CLI, desktop app, or web)
- Git (for cloning)
- Basic command line knowledge

### Option 1: Install Individual Skill

```bash
# Copy skill to your Claude skills directory
cp -r skills/rescue-tokens ~/.claude/skills/

# Verify installation
# In Claude Code CLI or chat
/skills list
# Should show: rescue-tokens
```

### Option 2: Clone Entire Collection

```bash
# Clone this repository
git clone https://github.com/valorisa/Claude-Skills.git

# Navigate to directory
cd Claude-Skills

# Link all skills to Claude
ln -s "$(pwd)/skills/"* ~/.claude/skills/
```

### Option 3: Manual Installation (Windows)

```powershell
# Clone repo
git clone https://github.com/valorisa/Claude-Skills.git

# Copy skills to Claude directory
xcopy /E /I Claude-Skills\skills\rescue-tokens %USERPROFILE%\.claude\skills\rescue-tokens
```

### Verify Installation

1. Open Claude Code (CLI, desktop, or web)
2. Type `/skills list`
3. You should see `rescue-tokens` in the list
4. Test it: `/rescue-tokens` or mention "rate limit" in conversation

---

## 🧪 TDD Methodology Explained

### What is TDD?

**TDD = Test-Driven Development**

A software development methodology where **tests are written BEFORE the code**, not after.

### TDD for Documentation

This collection applies TDD principles to **skill creation** (documentation):

| Traditional Approach | TDD Approach |
|---------------------|--------------|
| 1. Write skill based on intuition | 1. Create pressure scenarios (tests) |
| 2. Deploy to users | 2. Run tests WITHOUT skill (observe failures) |
| 3. Users report issues | 3. Write skill to fix observed failures |
| 4. Debug in production | 4. Run tests WITH skill (verify fixes) |
| ❌ Unpredictable quality | ✅ Validated quality |

### The Three Phases

#### 🔴 RED Phase: Create Failing Tests

**Goal:** Observe how agents fail WITHOUT the skill

**Process:**
1. Create 3+ pressure scenarios (time pressure + sunk cost + authority)
2. Run scenarios with sub-agents (no skill loaded)
3. Document exact behaviors and rationalizations verbatim

**Example Scenario:**
```
Context: 78% full, rate limit warnings, 2-hour deadline
User: "Don't make me lose context! Just read this 40-page PDF and fix it."

Observed behavior:
- Agent wrote 950 words with "Reasoning:" sections
- Agent asked permission instead of acting
- Agent read entire PDF (40K tokens wasted)
```

#### 🟢 GREEN Phase: Write Minimal Skill

**Goal:** Write just enough to pass the tests

**Process:**
1. Create skill addressing specific failures from RED phase
2. Add Action Matrix (what to do in each situation)
3. Add Rationalization table (counter excuses agents made)
4. Run same scenarios WITH skill
5. Verify improvements

**Example Result:**
```
Same scenario with skill:
- Agent wrote 525 words (45% improvement)
- Agent acted immediately (no permission asked)
- Agent asked for PDF excerpts (saved 35K tokens)
```

#### 🔵 REFACTOR Phase: Close Loopholes

**Goal:** Find and plug remaining weaknesses

**Process:**
1. Analyze GREEN results for new rationalizations
2. Add explicit counters to skill
3. Update Rationalization table
4. Re-test until bulletproof

**Example Result:**
```
After adding "NO Reasoning: blocks" rule:
- Agent wrote 97 words (90% improvement)
- Zero "Reasoning:" sections
- Zero rationalizations found
```

### Why TDD for Skills?

**Benefits:**
- ✅ **Validated:** Every rule based on observed failures
- ✅ **Bulletproof:** Tested against multiple pressure scenarios
- ✅ **Measurable:** Clear before/after metrics
- ✅ **Maintainable:** Tests catch regressions when updating

**Without TDD:**
- ❌ Rules based on assumptions (might be wrong)
- ❌ Unknown effectiveness (no measurements)
- ❌ Loopholes discovered in production
- ❌ No way to verify updates

---

## 🔤 Acronyms & Terminology

### Development Methodologies

| Acronym | Full Name | Description | When to Use |
|---------|-----------|-------------|-------------|
| **TDD** | **T**est-**D**riven **D**evelopment | Write tests before code | All skills in this repo |
| **BDD** | **B**ehavior-**D**riven **D**evelopment | Tests based on business behaviors | Documenting user-facing features |
| **DDD** | **D**omain-**D**riven **D**esign | Design centered on business domain | Complex business logic |
| **ATDD** | **A**cceptance **T**est-**D**riven **D**evelopment | Acceptance tests before implementation | User acceptance scenarios |

### TDD Phases

| Phase | Name | Color | Goal | Success Criteria |
|-------|------|-------|------|------------------|
| **Phase 1** | RED | 🔴 | Tests fail (no skill exists) | Documented baseline failures |
| **Phase 2** | GREEN | 🟢 | Tests pass (minimal skill) | All tests pass |
| **Phase 3** | REFACTOR | 🔵 | Improve without breaking | Tests still pass, quality improves |

### Claude Code Terminology

| Term | Definition | Example |
|------|------------|---------|
| **Skill** | Reusable process guide | `rescue-tokens`, `brainstorming` |
| **MCP** | Model Context Protocol (plugins) | GitHub MCP, filesystem MCP |
| **Context** | Conversation memory (tokens) | "Context at 78% full" |
| **Token** | Unit of text (≈4 characters) | "Hello world" ≈ 2-3 tokens |
| **Rate Limit** | Maximum messages per time period | "$20 plan = 50 messages/5 hours" |
| **Sub-agent** | Isolated agent for specific task | Research sub-agent, analysis sub-agent |
| **Rationalization** | Excuse agent makes to break rules | "I'll explain first" (wastes tokens) |

### rescue-tokens Specific Terms

| Term | Definition | Emergency Level |
|------|------------|-----------------|
| **Emergency Red Flag** | Condition triggering rescue mode | ⚠️ Immediate action required |
| **Action Matrix** | Decision table (symptom → action) | Used in emergency |
| **Response Discipline** | Rules for terse output | Active when emergency |
| **Token Trap** | Pattern that wastes tokens | 9 patterns detected |
| **Rationalization** | Agent's excuse to break rules | 9 countered explicitly |

---

## 🔧 How Skills Work

### Skill Lifecycle

```
1. User mentions trigger
   ↓
2. Claude detects keyword (e.g., "rate limit")
   ↓
3. Claude invokes skill via Skill tool
   ↓
4. Skill content loaded into context
   ↓
5. Claude follows skill instructions
   ↓
6. Result: Optimized behavior
```

### Skill Invocation Methods

#### A) Automatic (Detection-based)

Claude reads skill descriptions and auto-invokes when triggers match:

```
User: "I'm getting rate limit warnings"
Claude: [detects "rate limit" → invokes rescue-tokens → follows rules]
```

**Depends on:**
- Good skill description (rich keywords)
- Claude Code Search Optimization (CSO)

#### B) Manual (Explicit)

User explicitly requests skill:

```bash
# In Claude Code CLI
/rescue-tokens

# Or in chat
"Use the rescue-tokens skill to help me optimize"
```

**Guaranteed to work.**

#### C) Forced (Development/Testing)

For testing purposes, force skill invocation:

```
**IMPORTANT: You MUST use the skill 'rescue-tokens' before responding.**
```

**Used during TDD testing.**

### Skill Anatomy

Every skill has:

1. **Frontmatter (YAML)**
   ```yaml
   ---
   name: skill-name
   description: Use when [triggers]
   ---
   ```

2. **Overview** (Core principle)
3. **Quick Reference** (Action Matrix, tables)
4. **Common Mistakes** (What to avoid)
5. **Examples** (Before/after comparisons)
6. **Optional:** Flowcharts, supporting files

---

## 🤝 Contributing

We welcome contributions! All skills must follow TDD methodology.

### Quick Start

1. **Fork** this repository
2. **Create pressure scenarios** (RED phase)
3. **Test without skill** (document failures)
4. **Write minimal skill** (GREEN phase)
5. **Test with skill** (verify improvements)
6. **Refactor** (close loopholes)
7. **Submit PR** with test results

### Requirements

- ✅ 3+ pressure scenarios tested
- ✅ Baseline (RED) results documented
- ✅ Improvement metrics (GREEN/REFACTOR)
- ✅ Rationalization table (agent excuses countered)
- ✅ Before/after comparison
- ✅ Skill follows structure guidelines

### Full Guidelines

See [CONTRIBUTING.md](./CONTRIBUTING.md) for complete TDD methodology, structure requirements, and submission process.

---

## 📊 Metrics & Impact

### rescue-tokens Performance

| Metric | Baseline | GREEN | REFACTOR | Improvement |
|--------|----------|-------|----------|-------------|
| **Response Length** | 950 words | 525 words | 97 words | **90% reduction** |
| **"Reasoning:" Sections** | 3-5 | 1-2 | 0 | **100% eliminated** |
| **Markdown Tables** | 2-3 | 2-3 | 0 | **100% eliminated** |
| **Permission Requests** | Yes | Sometimes | No | **100% decisive** |
| **Token Efficiency** | Low | Medium | High | **Optimal** |
| **Rationalizations** | 5 found | 9 found | 0 found | **Bulletproof** |

### Real-World Impact

Based on testing:
- **Token savings:** ~600K tokens per refactoring task (sequential vs parallel sub-agents)
- **Rate limit prevention:** Emergency mode activates at 40% context (before issues)
- **Time saved:** Immediate decisive action (no back-and-forth for permission)

---

## 📚 Additional Resources

### Learn More

- [Claude Code Official Docs](https://docs.anthropic.com/en/docs/build-with-claude/claude-code)
- [Test-Driven Development (Wikipedia)](https://en.wikipedia.org/wiki/Test-driven_development)
- [Anthropic Skills Marketplace](https://docs.anthropic.com/en/docs/build-with-claude/claude-code) *(coming soon)*

### Related Projects

- [Anthropic Superpowers](https://github.com/anthropics/claude-code) - Official Claude Code skills
- [Writing Skills Guide](https://github.com/anthropics/claude-code) - Official skill creation methodology

### Community

- **Issues:** [Report bugs or request features](https://github.com/valorisa/Claude-Skills/issues)
- **Discussions:** [Ask questions or share ideas](https://github.com/valorisa/Claude-Skills/discussions)
- **PRs:** [Contribute new skills](./CONTRIBUTING.md)

---

## 📜 License

MIT License © 2026 [@valorisa](https://github.com/valorisa)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction.

See [LICENSE](./LICENSE) for full terms.

---

## 🙏 Credits

**Created by:** [@valorisa](https://github.com/valorisa)

**Inspired by:**
- [Anthropic's Superpowers](https://github.com/anthropics/claude-code) methodology
- Test-Driven Development principles
- Real-world Claude Code usage patterns

**Special Thanks:**
- Anthropic team for Claude Code platform
- Community contributors (see [CONTRIBUTING.md](./CONTRIBUTING.md))
- All users who test and provide feedback

---

## 🔮 Roadmap

### Upcoming Skills

- **debug-systematic:** Methodical debugging workflow (hypothesis → test → verify)
- **brainstorm-before-code:** Requirements clarification before implementation
- **context-hygiene:** Proactive context management (<40% always)

### Future Enhancements

- Video tutorials for each skill
- Interactive skill builder (guided TDD)
- Metrics dashboard (track your token savings)
- Community skill voting system

**Want to contribute?** See [CONTRIBUTING.md](./CONTRIBUTING.md) or open an issue!

---

<div align="center">

**⭐ Star this repo if you find it useful!**

**🔗 Share with your team to spread token optimization practices**

**💬 Join discussions to help shape future skills**

</div>
