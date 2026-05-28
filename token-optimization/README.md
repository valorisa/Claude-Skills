# Token Optimization

Optimize token consumption in Claude Code through systematic cache management, context forking, model selection, and input filtering.

## Overview

This skill helps you drastically reduce token costs in Claude Code by addressing four critical sources of overconsumption:

1. **Cache misses** — Prevent cache invalidation
2. **Context bloating** — Control context window growth
3. **Wrong model/effort** — Choose appropriate reasoning levels
4. **Verbose inputs** — Filter unnecessary output

**Real-world result:** One team reduced costs from $750/month to $100/month using these techniques.

## Installation

### Claude Code

```bash
# Copy to skills directory
cp -r token-optimization ~/.claude/skills/

# Restart Claude Code
```

### Verification

```bash
# Check if skill loaded
/skills

# Should show: token-optimization
```

## Quick Start

### Step 1: Audit your session

```
"Audit my current session for token optimization opportunities"
```

The skill will:

- Check loaded MCPs and plugins
- Measure base token consumption
- Identify optimization opportunities
- Provide actionable recommendations

### Step 2: Apply optimizations

Common quick wins:

- Disable unnecessary MCPs (keeps only 2-3 essential)
- Add concise response directives to CLAUDE.md
- Size context window appropriately for your codebase
- Install RTK for CLI output filtering

### Step 3: Verify savings

```bash
/context    # Check new token count
```

Expected results:

- Base session: <5,000 tokens (vs 20,000+)
- Standard workflow: 30k tokens (vs 140k+)
- 70-80% overall reduction

## Use Cases

### Scenario 1: High token bills

**You say:** "My Claude Code costs are too high, help me optimize"

**Skill does:**

- Runs session audit
- Identifies waste sources
- Implements optimizations
- Measures savings

### Scenario 2: Slow sessions

**You say:** "My sessions are becoming slow and bloated"

**Skill does:**

- Analyzes context growth patterns
- Configures context forking for agents
- Sets up output filtering
- Implements compaction strategy

### Scenario 3: New project setup

**You say:** "Set up optimal token configuration for this new project"

**Skill does:**

- Analyzes codebase size
- Recommends context window
- Creates CLAUDE.md with optimizations
- Configures project-local MCPs

## Key Features

### Cache Management

- Detects mid-session configuration changes
- Warns about cache invalidation costs
- Recommends optimal session strategies

### Context Optimization

- Sizes context window per codebase
- Configures agent context forking
- Implements delegation patterns

### Output Filtering

- Recommends RTK for CLI commands
- Configures Stagehand for browser automation
- Adds concise response directives

### Monitoring

- Real-time token consumption tracking
- Before/after comparisons
- Team dashboard support (optional)

## Examples

### Example 1: Session audit

```
You: "Check my current token usage"

Skill: 
Current session: 25,342 tokens (5 MCPs loaded)

Issues:
- 3 unused MCPs (gmail, calendar, notion)
- No output filtering on git commands
- Context window: 1M (oversized)

Savings potential: ~20k base, ~60% per session
```

### Example 2: Web research

```
You: "Research React Server Components best practices"

Skill:
Spawning research subagent (context fork)...
Research complete.

Key findings: [summary]

Main context impact: 500 tokens (vs 5k+ direct)
```

### Example 3: Configuration

```
You: "Optimize this project"

Skill:
Codebase: 23k LOC (medium)
Recommended context: 200k tokens

Created:
- .claude/settings.json (context window)
- CLAUDE.md (optimization directives)

Base session: 3k tokens (vs 23k before)
```

## Testing

### Validate skill structure

```bash
python scripts/validate_skill.py .
```

### Run trigger tests

See `tests/trigger-tests.md` for validation queries.

### Run functional tests

See `tests/functional-tests.md` for complete test scenarios.

## Troubleshooting

### Still high token consumption?

1. Run `/context` to check current state
2. Verify MCPs with `/plugin`
3. Review CLAUDE.md configuration
4. Check for mid-session changes (cache invalidation)

### Agents consuming too much?

1. Verify context forking is enabled
2. Check agent spawn timing (earlier = lighter)
3. Ensure only results returned (not full history)

### Commands still verbose?

1. Install RTK: `npx rtk init --global`
2. Verify installation: `which git` (should show RTK)
3. Restart shell if needed

## Documentation

- [SKILL.md](SKILL.md) — Complete skill instructions
- [references/cache-deep-dive.md](references/cache-deep-dive.md) — Cache behavior details
- [references/claude-md-templates.md](references/claude-md-templates.md) — Configuration examples
- [references/tools.md](references/tools.md) — External tool setup
- [tests/trigger-tests.md](tests/trigger-tests.md) — Trigger validation
- [tests/functional-tests.md](tests/functional-tests.md) — Functional test cases

## Contributing

Contributions welcome! Please:

1. Validate changes with `python scripts/validate_skill.py .`
2. Run trigger and functional tests
3. Update documentation
4. Submit PR with test results

## License

MIT License - see [LICENSE](../LICENSE)

## Version

1.0.0 (2026-05-28)

## References

- [Anthropic Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- [Stagehand Browser Automation](https://github.com/browserbase/stagehand)
- [RTK CLI Filter](https://github.com/simonw/rtk)
