# External Tools — Token Optimization

## Stagehand — DOM-Based Browser Automation

### Overview

Stagehand is a DOM-based browser automation tool that eliminates the need for screenshots, drastically reducing token consumption.

**Repository:** <https://github.com/browserbase/stagehand>

### Why Use It

- Native Claude Code browser agent takes screenshots at every step → expensive
- Stagehand operates directly on DOM → 10× faster, ~90% token reduction
- Invisible operation, no visual overhead

### Installation

```bash
# In Claude Code, run:
# "Install Stagehand from https://github.com/browserbase/stagehand"
```

### Usage Example

**Before (native browser agent):**

```
User: "Test the login flow on staging"
Claude: [Takes screenshot] → [Analyzes] → [Clicks] → [Takes screenshot] → [Analyzes] → ...
Result: 15k tokens consumed
```

**After (Stagehand):**

```
User: "Test the login flow on staging"
Claude: [DOM query] → [Action] → [DOM verify] → ...
Result: 1.5k tokens consumed
```

### Integration with CLAUDE.md

```markdown
## Browser Testing
Use Stagehand for all browser automation (DOM-based, no screenshots).
Native browser agent: only for visual regression testing requiring screenshots.
```

## RTK — CLI Output Filter

### Overview

RTK (developed by Simon Willison) filters CLI command output before injection into context, removing verbose boilerplate.

**Repository:** <https://github.com/simonw/rtk>

### Why Use It

- Commands like `git status`, `npm test` dump massive output
- Most of that output is boilerplate or redundant
- RTK strips it down to essentials → 80-90% token savings on CLI operations

### Installation

```bash
# Global installation in Claude Code
npx rtk init --global
```

This configures RTK as a wrapper for common commands.

### Filtered Commands

RTK automatically optimizes:

| Command | Before | After | Savings |
|---|---|---|---|
| `git status` | ~50 lines | ~5 lines | ~90% |
| `git log` | Full history | Last 10 commits, oneline | ~95% |
| `npm test` | Full output | Summary + failures only | ~80% |
| `git diff` | Full diff | Stat + changed lines count | ~70% |

### Configuration

RTK uses `~/.config/rtk/config.json`:

```json
{
  "filters": {
    "git-status": {
      "command": "git status --short",
      "maxLines": 10
    },
    "git-log": {
      "command": "git log --oneline --graph -n 10",
      "maxLines": 15
    },
    "npm-test": {
      "command": "npm test --",
      "extractPattern": "(PASS|FAIL|Tests:.*)",
      "maxLines": 20
    }
  }
}
```

### Custom Filters

Add project-specific filters:

```json
{
  "filters": {
    "docker-ps": {
      "command": "docker ps --format 'table {{.Names}}\t{{.Status}}'",
      "maxLines": 10
    },
    "kubectl-get-pods": {
      "command": "kubectl get pods --no-headers",
      "maxLines": 20
    }
  }
}
```

### Integration with CLAUDE.md

```markdown
## CLI Commands
RTK filtering enabled for all git, npm, docker, kubectl commands.
Output: essentials only (status, errors, summaries).
Full output: on explicit request, delegate to subagent with context fork.
```

## Caveman Skill — Ultra-Concise Responses

### Overview

Community-created skill (GitHub, ~50k stars) that configures Claude for minimal-token responses.

**Typical location:** Community skill repositories (search "caveman skill claude")

### Core Directive

The Caveman Skill essentially implements:

```markdown
Talk like caveman. Short. Direct. No waste.
- Remove: articles (a, the), politeness phrases, reformulations
- Format: bullet points, imperative commands
- Examples:
  ❌ "I've successfully updated the configuration file"
  ✅ "Updated config"
  ❌ "Let me help you with that task"
  ✅ "Starting task"
```

### Adaptation for CLAUDE.md

Instead of installing as a skill, add to your CLAUDE.md:

```markdown
## Response Style — Ultra-Concise
- Max 10 lines per response unless detail requested
- Format: [Action] → [Result] → [Next]
- Remove: intros, conclusions, politeness, reformulations
- Use: bullet points, imperative verbs

Examples:
✅ "Installed deps → tests pass → ready to deploy"
❌ "I've successfully installed the dependencies. The tests are now passing. We're ready to proceed with deployment."
```

### When to Use

- Solo developer projects (speed-focused)
- Rapid prototyping sessions
- Well-understood codebases

### When NOT to Use

- Open source (community needs context)
- Teaching/mentoring scenarios
- Complex debugging requiring detailed explanations
- Team environments with junior developers

## Context Window Sizer (Custom Tool)

### Overview

Custom script to analyze codebase and recommend optimal context window size.

### Installation

Create `scripts/size-context-window.sh`:

```bash
#!/bin/bash

# Count lines of code
LOC=$(find . -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.jsx" -o -name "*.py" | xargs wc -l | tail -1 | awk '{print $1}')

# Calculate recommended context window
if [ $LOC -lt 10000 ]; then
    WINDOW=150000
    SIZE="small"
elif [ $LOC -lt 50000 ]; then
    WINDOW=200000
    SIZE="medium"
elif [ $LOC -lt 100000 ]; then
    WINDOW=500000
    SIZE="large"
else
    WINDOW=1000000
    SIZE="very large"
fi

echo "Codebase: $LOC lines of code ($SIZE)"
echo "Recommended context window: $WINDOW tokens"
echo ""
echo "Add to .claude/settings.json:"
echo "{ \"contextWindow\": $WINDOW }"
```

Make executable:

```bash
chmod +x scripts/size-context-window.sh
```

### Usage

```bash
./scripts/size-context-window.sh
```

Output:

```
Codebase: 23,456 lines of code (medium)
Recommended context window: 200000 tokens

Add to .claude/settings.json:
{ "contextWindow": 200000 }
```

## Token Usage Dashboard (Team Tool)

### Overview

Local dashboard for monitoring team token consumption patterns.

**Use case:** Engineering managers tracking optimization efforts across team.

### Setup

Create `scripts/token-dashboard.py`:

```python
#!/usr/bin/env python3
import json
from pathlib import Path
from collections import defaultdict

# Parse Claude Code session logs
logs_dir = Path.home() / ".claude" / "logs"
sessions = []

for log_file in logs_dir.glob("session-*.json"):
    with open(log_file) as f:
        session_data = json.load(f)
        sessions.append({
            "date": session_data.get("date"),
            "tokens": session_data.get("totalTokens", 0),
            "model": session_data.get("model"),
            "user": session_data.get("user"),
            "project": session_data.get("project"),
        })

# Aggregate by user
by_user = defaultdict(lambda: {"sessions": 0, "tokens": 0})
for s in sessions:
    user = s.get("user", "unknown")
    by_user[user]["sessions"] += 1
    by_user[user]["tokens"] += s.get("tokens", 0)

# Report
print("Token Consumption Dashboard")
print("=" * 60)
for user, stats in sorted(by_user.items(), key=lambda x: x[1]["tokens"], reverse=True):
    avg = stats["tokens"] / stats["sessions"] if stats["sessions"] > 0 else 0
    print(f"{user:20} | Sessions: {stats['sessions']:4} | Tokens: {stats['tokens']:10,} | Avg: {avg:10,.0f}")
```

Make executable:

```bash
chmod +x scripts/token-dashboard.py
```

### Usage

```bash
./scripts/token-dashboard.py
```

Output:

```
Token Consumption Dashboard
============================================================
alice@company.com    | Sessions:   42 | Tokens:  1,234,567 | Avg:     29,394
bob@company.com      | Sessions:   38 | Tokens:  2,345,678 | Avg:     61,728
charlie@company.com  | Sessions:   35 | Tokens:    456,789 | Avg:     13,051
```

**Insights:**

- Bob using 2× tokens of Alice → investigate (wrong model? cache issues?)
- Charlie very efficient → learn from their practices

## Pre-Session Configuration Checker

### Overview

Script to verify optimal configuration before starting work session.

### Setup

Create `scripts/check-config.sh`:

```bash
#!/bin/bash

echo "🔍 Claude Code Configuration Check"
echo "==================================="

# Check MCP count
MCP_COUNT=$(cat ~/.claude/settings.json 2>/dev/null | jq '.mcpServers | length' 2>/dev/null || echo 0)
echo "MCPs enabled: $MCP_COUNT"
if [ $MCP_COUNT -gt 5 ]; then
    echo "  ⚠️  Warning: >5 MCPs may bloat context"
fi

# Check context window
CTX_WINDOW=$(cat .claude/settings.json 2>/dev/null | jq '.contextWindow' 2>/dev/null || echo "default")
echo "Context window: $CTX_WINDOW"

# Check for RTK
if command -v rtk &> /dev/null; then
    echo "✅ RTK installed (CLI filtering enabled)"
else
    echo "⚠️  RTK not found (consider installing for CLI filtering)"
fi

# Check for Stagehand
if grep -q "stagehand" ~/.claude/plugins/*.json 2>/dev/null; then
    echo "✅ Stagehand configured (DOM-based browser automation)"
else
    echo "⚠️  Stagehand not configured (browser tests will use screenshots)"
fi

# Check CLAUDE.md
if [ -f "CLAUDE.md" ]; then
    if grep -q "concise\|bullet" CLAUDE.md; then
        echo "✅ CLAUDE.md includes concise response directives"
    else
        echo "⚠️  CLAUDE.md missing concise response configuration"
    fi
else
    echo "⚠️  No CLAUDE.md found (consider creating one)"
fi

echo ""
echo "Estimated base session cost: ~${MCP_COUNT}000 tokens"
```

Make executable:

```bash
chmod +x scripts/check-config.sh
```

### Usage

Run before starting work:

```bash
./scripts/check-config.sh
```

Output:

```
🔍 Claude Code Configuration Check
===================================
MCPs enabled: 3
Context window: 200000
✅ RTK installed (CLI filtering enabled)
✅ Stagehand configured (DOM-based browser automation)
✅ CLAUDE.md includes concise response directives

Estimated base session cost: ~3000 tokens
```

## Integration Checklist

Before deploying these tools project-wide:

- [ ] RTK installed globally (`npx rtk init --global`)
- [ ] Stagehand configured in Claude Code plugins
- [ ] Context window sized per project in `.claude/settings.json`
- [ ] CLAUDE.md includes concise response directives
- [ ] Pre-session checker script in project root
- [ ] Team trained on tool usage (if applicable)
- [ ] Monitoring dashboard deployed (teams only)

## Troubleshooting

### RTK not filtering commands

**Diagnosis:**

```bash
which git  # Should show RTK wrapper, not direct git
```

**Fix:**

```bash
npx rtk init --global --force
# Restart shell
```

### Stagehand not loading

**Diagnosis:**

```bash
ls ~/.claude/plugins/ | grep stagehand
```

**Fix:**
Re-install via Claude Code: "Install Stagehand plugin"

### Dashboard showing no data

**Diagnosis:**

```bash
ls ~/.claude/logs/
```

**Fix:**
Logs may be in different location depending on Claude Code version. Check settings.

## Version History

- v1.0.0 (2026-05-28): Initial tool documentation
