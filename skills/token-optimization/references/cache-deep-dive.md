# Cache — Technical Reference

## Cache Structure in Claude Code

```
┌─────────────────────────────────────────────┐
│  BASE SYSTEM INSTRUCTIONS (CLAUDE.md + tools)│  ← Invalidated if tool added
├─────────────────────────────────────────────┤
│  SESSION STATE (project files, memory)       │  ← Invalidated if file changes
├─────────────────────────────────────────────┤
│  MESSAGE HISTORY                             │  ← Invalidated if message edited
│  msg 1 → msg 2 → msg 3 → ...                │     (invalidates everything after)
└─────────────────────────────────────────────┘
```

## Cache Behavior (HTTP analogy)

- Each layer is a **cache prefix**
- Modifying a layer invalidates all layers **below**
- Effects are **multiplicative**: invalidating base instructions also invalidates session state AND history

## What Invalidates Cache

| Action | Invalidated Layer | Impact |
|---|---|---|
| Add MCP mid-session | Base instructions | Very high |
| Add tool (tool calling) | Base instructions | Very high |
| Modify CLAUDE.md | Base instructions | Very high |
| Edit message in middle of history | Message history (from that point) | Moderate |
| Load new file into context | Session state | Moderate |

## Optimal Session Strategy

```
1. Full configuration (MCP, tools, CLAUDE.md) → BEFORE starting
2. Work session → NEVER modify configuration
3. If modification needed → /compact → new session
4. Agents → context fork → isolated work → result only
```

## Technical Details

### Cache TTL

- Claude Code maintains cache for the duration of the session
- Cache is invalidated on session restart
- Cache is shared across all agents in same session (unless context forked)

### Token Billing

- First request: full token count billed
- Cached requests: only new tokens billed (prompt cache hit)
- Invalidated cache: re-billed as if first request

### Cache Size Limits

- Maximum cached content: ~1M tokens
- Beyond this, oldest cache entries are evicted
- Frequent eviction indicates poor cache strategy

## Real-World Impact

**Example 1: Mid-session MCP addition**

- Session at 50k tokens
- Add new MCP (5k base instructions)
- Cache invalidated: 50k tokens re-billed
- Total cost: 55k new tokens (5k MCP + 50k re-billing)

**Example 2: Optimal session**

- Pre-configure all MCPs before session start
- Work through entire session
- Cache hits on every request
- Token cost: only incremental new content

## Monitoring Cache Performance

### Commands to check cache status

```bash
/context    # Shows total tokens consumed
/plugin     # Lists active plugins (cache impact)
```

### Signs of cache problems

- Unexpectedly high token consumption
- Slow response times (re-processing cache)
- Token count jumps without apparent cause

### Measuring cache efficiency

- Track tokens per session over time
- Compare sessions with/without mid-session changes
- Target: >80% cache hit rate for stable work

## Anthropic Postmortem

Cache issues have been publicly analyzed on GitHub (Claude Code issues).
Official Anthropic documentation details prompt caching behavior.

**Key references:**

- [Anthropic Prompt Caching Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- [Claude Code GitHub Issues on Cache](https://github.com/anthropics/claude-code/issues?q=cache)

## Best Practices

### DO

✅ Configure all MCPs and tools before session start
✅ Use context forking for isolated subagent work
✅ Keep CLAUDE.md stable during work sessions
✅ Use `/compact` before major configuration changes
✅ Monitor token consumption with `/context`

### DON'T

❌ Add MCPs or skills mid-session
❌ Edit CLAUDE.md during active work
❌ Load large files repeatedly into context
❌ Let agents inherit bloated parent context
❌ Ignore sudden token count increases

## Debugging Cache Issues

### Step 1: Identify invalidation source

```bash
# Check current state
/context
/plugin

# Look for recent changes
# - New MCPs loaded?
# - CLAUDE.md modified?
# - Skills added mid-session?
```

### Step 2: Measure impact

- Note token count before investigation
- Identify the invalidation point
- Calculate re-billed tokens

### Step 3: Remediate

- If early in session: restart with proper config
- If mid-session: use `/compact` and continue
- Document the issue to prevent recurrence

### Step 4: Prevent recurrence

- Update session startup checklist
- Add pre-flight configuration verification
- Train team on cache behavior (if applicable)

## Advanced: Cache Warming Strategies

For large projects with predictable workflows:

1. **Session templates**: Pre-configured settings.json per project type
2. **Startup scripts**: Load all needed skills and MCPs at init
3. **Cached CLAUDE.md**: Single stable configuration file per project
4. **Agent blueprints**: Pre-defined subagent patterns with minimal context

These strategies ensure cache is optimally populated before work begins.
