# Claude Skills Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-12-blue.svg)](./skills)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple.svg)](https://claude.ai/code)
[![TDD](https://img.shields.io/badge/methodology-TDD-green.svg)](https://en.wikipedia.org/wiki/Test-driven_development)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/valorisa/claude-skills/graphs/commit-activity)

> **Community-contributed skills for [Claude Code](https://claude.ai/code) to enhance productivity, optimize token usage, and improve development workflows.**

[🇫🇷 Version française](./README_FR.md)

---

## 📋 Table of Contents

- [What Are Claude Skills?](#-what-are-claude-skills)
- [Quick Start](#-quick-start-5-minutes)
- [Which Skill Should I Use?](#-which-skill-should-i-use)
- [Installation](#-installation)
- [Complete Development Workflow](#-complete-development-workflow)
- [Available Skills](#-available-skills-detailed-reference)
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

## 🚀 Quick Start (5 minutes)

**New to Claude Skills? Start here:**

### Try Your First Skill

```bash
# 1. Clone this repository
git clone https://github.com/valorisa/Claude-Skills.git
cd Claude-Skills

# 2. Install one skill to try (rescue-tokens is great for beginners)
cp -r skills/rescue-tokens ~/.claude/skills/
```

### Test It in Claude Code

1. Open Claude Code (CLI, desktop app, or web)
2. Start a conversation and mention: **"I'm getting rate limit warnings"**
3. Claude will automatically activate the `rescue-tokens` skill
4. Watch how Claude optimizes its behavior to save tokens!

### What Happens?

**Without skill:** Claude might write verbose explanations (950 words), wasting tokens

**With skill:** Claude responds concisely (97 words), taking immediate action

### Next Steps

- **Want the full development workflow?** → See [Complete Development Workflow](#-complete-development-workflow)
- **Not sure which skill to use?** → See [Which Skill Should I Use?](#-which-skill-should-i-use)
- **Ready to install all skills?** → See [Installation](#-installation)

---

## 🎯 Which Skill Should I Use?

**Choose your path based on what you need:**

### For Everyone

| Skill | When to Use | Why You Need This |
|-------|-------------|-------------------|
| [rescue-tokens](./skills/rescue-tokens/README.md) | Getting rate limits, context warnings, or slow responses | Prevents token waste that causes rate limits. **Start here if unsure!** |

### For Starting New Work

| Skill | When to Use | Why You Need This |
|-------|-------------|-------------------|
| [spec-driven](./skills/spec-driven/README.md) | Starting a new feature or complex task | Prevents "coding too early" syndrome. Forces you to think through requirements before writing code, avoiding costly rewrites. |
| [create-github-issues](./skills/create-github-issues/README.md) | You have a plan/spec and need to break it into tasks | Converts big plans into small, independent, shippable chunks. Each issue = complete feature slice (UI → API → DB). |

### For Writing Code

| Skill | When to Use | Why You Need This |
|-------|-------------|-------------------|
| [tdd-hybrid](./skills/tdd-hybrid/README.md) | Implementing any feature or bugfix | Write tests before code = fewer bugs, better design. Prevents "it works on my machine" problems. |
| [diagnose](./skills/diagnose/README.md) | Stuck on a hard bug or performance issue | Systematic debugging prevents guessing. Reproduce → minimize → fix → test. Ensures bug stays fixed. |

### For Improving Existing Code

| Skill | When to Use | Why You Need This |
|-------|-------------|-------------------|
| [improve-codebase-architecture](./skills/improve-codebase-architecture/README.md) | Periodic codebase reviews, or code feels messy | Finds architectural improvements based on your domain language (CONTEXT.md). Suggests consolidation opportunities. |

### For Advanced Decision-Making

| Skill | When to Use | Why You Need This |
|-------|-------------|-------------------|
| [llm-council](./skills/llm-council/README.md) | Big decisions, tradeoff analysis, architecture choices | Gets 5 independent AI perspectives, peer-reviewed. Catches blind spots you'd miss alone. |
| [promptor](./skills/promptor/README.md) | Creating optimized prompts for AI tools | Generates production-ready prompts using 18 optimization techniques. Copy-paste-ready. |

### Setup (Run Once Per Repo)

| Skill | When to Use | Why You Need This |
|-------|-------------|-------------------|
| [setup-matt-pocock-skills](./skills/setup-matt-pocock-skills/README.md) | First time setting up a new repository | Creates issue tracker, triage labels, and documentation structure. One-time setup. |

### Utilities

| Skill | When to Use | Why You Need This |
|-------|-------------|-------------------|
| [skill-creator](./skills/skill-creator/README.md) | Creating your own custom skills | Guides you through TDD methodology and proper structure. |
| [find-bugs](./skills/find-bugs/README.md) | Systematic bug hunting in codebase | Structured approach to finding and documenting bugs. |

**💡 Tip:** Skills work together! Common workflow: `spec-driven` → `create-github-issues` → `tdd-hybrid` (per issue) → `diagnose` (if bugs found)

---

## 📦 Available Skills (Detailed Reference)

This collection includes **12 skills** organized into workflows and utilities.

> **💡 Note on Triggers:** When you mention any of the trigger keywords in your conversation with Claude, the skill automatically activates. For example, saying "I'm getting rate limit warnings" activates `rescue-tokens`.

### 🎯 Core Development Workflow

**Recommended workflow:** `/spec-driven` → `/create-github-issues` → `/tdd-hybrid` (per issue)

#### 1. [spec-driven](./skills/spec-driven/README.md)

**Spec-driven development with enforced pipeline and token budgets.**

Activates structured spec-first workflow (SPEC→PLAN→IMPL→VERIF→SYNTHESE) with 3-way triage (FULL/LIGHT/SHIP), token budgets, and explicit gates. Use when starting features or complex tasks.

**Triggers:** `spec-driven`, `/spec-driven`, `mode spec`, `spec first`, `pipeline complet`

#### 2. [create-github-issues](./skills/create-github-issues/README.md)

**Break plans into vertical-slice GitHub issues.**

Converts plans, specs, or PRDs into independently-grabbable GitHub issues using tracer-bullet vertical slices. Each issue is a complete feature slice (UI → API → DB).

**Triggers:** User wants to convert plan into issues, create implementation tickets, or break down work

#### 3. [tdd-hybrid](./skills/tdd-hybrid/README.md)

**Test-driven development with strict discipline and intelligent workflow.**

Combines TDD rigor (Iron Law, mandatory verification) with intelligent planning, vertical slicing, and domain awareness. Includes LIGHT/FULL triage and optional spec/verify gates.

**Triggers:** Implementing features or fixing bugs with TDD, `/tdd-hybrid`

#### 4. [diagnose](./skills/diagnose/README.md)

**Disciplined diagnosis loop for hard bugs and performance regressions.**

Structured debugging: reproduce → minimize → hypothesize → instrument → fix → regression-test. Prevents premature conclusions and ensures reproducible fixes.

**Triggers:** `diagnose this`, `debug this`, bug reports, something broken/failing, performance regressions

#### 5. [improve-codebase-architecture](./skills/improve-codebase-architecture/README.md)

**Find deepening opportunities in codebases.**

Analyzes codebases for architectural improvements informed by domain language (CONTEXT.md) and architectural decisions (docs/adr/). Suggests consolidation of tightly-coupled modules and testability improvements.

**Triggers:** Improve architecture, find refactoring opportunities, periodic codebase review

---

### 🛠️ Supporting Skills

#### Setup & Configuration

##### [setup-matt-pocock-skills](./skills/setup-matt-pocock-skills/README.md)

**Initial repository configuration (run once).**

Configures issue tracker, creates 5 triage labels (LIGHT/FULL/SHIP/BLOCKED/WONTFIX), sets up CONTEXT.md + docs/adr/ structure. One-time setup per repository.

---

#### Token & Context Optimization

##### [rescue-tokens](./skills/rescue-tokens/README.md)

**Prevents token exhaustion through 9 optimization patterns.**

Automatically detects and fixes token waste: eternal conversations, verbose output, wrong model choice, MCP bloat, expensive files. Activates when context ≥40%, rate limits, or 5+ MCPs loaded.

**Verified results:** 90% token reduction in emergency scenarios.

[📖 Full Documentation](./skills/rescue-tokens/SKILL.md)

---

#### Advanced Decision-Making

##### [llm-council](./skills/llm-council/README.md)

**Multi-perspective decision analysis via 5-advisor council.**

Runs questions through a council of 5 AI advisors who independently analyze, peer-review anonymously, and synthesize a verdict. Based on Karpathy's LLM Council methodology.

**Mandatory triggers:** `council this`, `run the council`, `war room this`, `pressure-test this`

##### [promptor](./skills/promptor/README.md)

**Generate optimized prompts via 5-circle validation pipeline.**

Produces domain-agnostic, auditable, copy-paste-ready prompts using 18 optimization hacks fused with 5-circle validation.

**Triggers:** `create a prompt`, `optimize this prompt`, `promptor`, `generate a system prompt`

##### [promptor-council](./skills/promptor-council/README.md)

**Promptor v3 with multi-perspective deliberation.**

Enhanced version of promptor with council-based validation and architectural deliberation.

---

#### Development Utilities

##### [skill-creator](./skills/skill-creator/README.md)

**Create new skills following best practices.**

Guides skill creation process with TDD methodology, proper structure, and validation.

##### [find-bugs](./skills/find-bugs/README.md)

**Systematic bug detection and analysis.**

Structured approach to finding and documenting bugs in codebases.

---

## 🔄 Complete Development Workflow

This collection implements a **spec-first, test-driven, vertical-slice workflow** inspired by Matt Pocock's methodology.

### Initial Repository Setup (Once)

```bash
# 1. Install skills to ~/.claude/skills/
# 2. In your project repository:
/setup-matt-pocock-skills
```

This creates:

- GitHub Issues configuration via `gh` CLI
- 5 triage labels (LIGHT/FULL/SHIP/BLOCKED/WONTFIX)
- `CONTEXT.md` for domain documentation
- `docs/adr/` for architectural decisions

### Development Cycle (Per Feature)

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 1: SPECIFICATION                                      │
│ /spec-driven                                                │
│ → Creates detailed spec with requirements, constraints      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 2: ISSUE BREAKDOWN                                    │
│ /create-github-issues                                       │
│ → Converts spec into vertical-slice GitHub issues           │
│ → Each issue = UI → API → DB (complete feature slice)       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 3: IMPLEMENTATION (Per Issue)                         │
│ /tdd-hybrid                                                 │
│ → Test-first development with LIGHT/FULL triage             │
│ → RED → GREEN → REFACTOR cycle                              │
│ → Mandatory verification before completion                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 4: DEBUGGING (When Needed)                            │
│ /diagnose                                                   │
│ → Reproduce → Minimize → Hypothesize → Fix → Regression     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 5: PERIODIC MAINTENANCE                               │
│ /improve-codebase-architecture                              │
│ → Find deepening opportunities                              │
│ → Consolidate tightly-coupled modules                       │
│ → Improve testability                                       │
└─────────────────────────────────────────────────────────────┘
```

### Example Session

```bash
# Start new feature
You: "Add user authentication with OAuth2"

# 1. Create specification
/spec-driven

# 2. Break into issues (after spec approved)
/create-github-issues

# 3. Pick first issue from GitHub
# Example: "Issue #42: OAuth2 login button UI"

# 4. Implement with TDD
/tdd-hybrid
# → Creates failing tests
# → Implements minimal code
# → Refactors
# → Verifies all tests pass

# 5. If bug found
/diagnose
# → Reproduces issue
# → Creates minimal reproduction
# → Fixes root cause
# → Adds regression test

# 6. Periodic architecture review
/improve-codebase-architecture
```

### Triage System

Each skill and issue uses **5 canonical labels**:

| Label | Meaning | When to Use |
|-------|---------|-------------|
| **LIGHT** | Simple, low-risk | Small changes, obvious fixes |
| **FULL** | Complex, needs rigor | New features, refactors, critical bugs |
| **SHIP** | Ready to merge | All tests pass, reviewed |
| **BLOCKED** | Can't proceed | Missing dependencies, design unclear |
| **WONTFIX** | Intentionally skipped | Out of scope, obsolete |

**Benefits:**

- Clear communication (team knows risk level)
- Appropriate rigor (no over-engineering simple fixes)
- Efficient workflow (skip unnecessary process for LIGHT)

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
