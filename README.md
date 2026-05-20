# Claude Skills Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-1-blue.svg)](./skills)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple.svg)](https://claude.ai/code)
[![TDD](https://img.shields.io/badge/methodology-TDD-green.svg)](https://en.wikipedia.org/wiki/Test-driven_development)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/valorisa/claude-skills/graphs/commit-activity)

Community-contributed skills for [Claude Code](https://claude.ai/code) to enhance productivity, optimize token usage, and improve development workflows.

## 📦 Available Skills

### 🚀 rescue-tokens

**Prevents token exhaustion and rate limits through 9 optimization patterns.**

**Use when:**
- Rate limit warnings appear
- Context exceeds 40%
- Long conversations (>90 minutes)
- Wrong model choice (Opus for simple tasks)
- MCP plugin bloat

**What it does:**
- Detects 9 token waste patterns
- Forces terse responses under pressure (<100 words)
- Provides Action Matrix for immediate decisions
- Counters 9 common rationalizations

**Results:** 90% reduction in verbosity, eliminates rate limit issues

[📖 Full Documentation](./skills/rescue-tokens/SKILL.md)

---

## 🎯 Installation

### Option 1: Install Individual Skill

```bash
# Copy skill to your Claude skills directory
cp -r skills/rescue-tokens ~/.claude/skills/
```

### Option 2: Clone Entire Collection

```bash
# Clone this repo
git clone https://github.com/valorisa/claude-skills.git

# Link skills to Claude
ln -s "$(pwd)/claude-skills/skills/"* ~/.claude/skills/
```

### Verify Installation

```bash
# In Claude Code CLI
/skills list

# Should show: rescue-tokens
```

---

## 🧪 Skill Development Methodology

All skills in this collection follow **Test-Driven Development (TDD)** for documentation:

1. **RED Phase:** Create pressure scenarios, observe agent failures without skill
2. **GREEN Phase:** Write minimal skill to counter observed rationalizations
3. **REFACTOR Phase:** Identify new loopholes, add explicit counters, re-test

See [rescue-tokens development log](./skills/rescue-tokens/SKILL.md) for TDD example.

---

## 🤝 Contributing

Want to contribute a skill?

1. **Test first:** Create pressure scenarios, document baseline failures
2. **Follow TDD:** RED → GREEN → REFACTOR cycle
3. **Document rationalizations:** What excuses did agents make?
4. **Submit PR:** Include test results and metrics

---

## 📜 License

MIT License - feel free to use, modify, and share.

---

## 🙏 Credits

Created by [@valorisa](https://github.com/valorisa)

Inspired by [Anthropic's Superpowers](https://github.com/anthropics/claude-code) methodology.
