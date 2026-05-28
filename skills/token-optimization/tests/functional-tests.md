# Functional Tests — Token Optimization Skill

## Test Case 1: Initial Session Audit (Happy Path)

### Setup

- Fresh Claude Code session
- 5 MCPs loaded (github, slack, gmail, calendar, notion)
- No project CLAUDE.md
- Default context window (1M tokens)

### User Action

"Audit my current session for token optimization opportunities"

### Expected Behavior

1. ✅ Run `/context` to check current token consumption
2. ✅ Run `/plugin` to list active plugins
3. ✅ Identify >3 MCPs as problematic
4. ✅ Calculate base session cost (~25k tokens)
5. ✅ Recommend disabling non-essential MCPs
6. ✅ Suggest context window sizing based on codebase
7. ✅ Provide specific next steps

### Expected Output Format

```
Current session: 25,342 tokens (5 MCPs loaded)

Issues found:
- gmail, calendar, notion MCPs unnecessary for this project
- No CLAUDE.md (missing concise response directives)
- Context window: 1M (oversized for this codebase)

Recommendations:
1. Disable gmail, calendar, notion MCPs
2. Create CLAUDE.md with response optimization
3. Set context window to 200k (medium codebase)

Estimated savings: ~20k base tokens, ~60% per session
```

### Success Criteria

- [x] All diagnostic commands executed
- [x] Issues correctly identified
- [x] Recommendations specific and actionable
- [x] Estimated savings provided

---

## Test Case 2: Cache Invalidation Detection

### Setup

- Active session at 50k tokens
- User about to add new MCP mid-session

### User Action

"I need to add the Figma MCP for the next task"

### Expected Behavior

1. ✅ Detect mid-session MCP addition attempt
2. ✅ Warn about cache invalidation
3. ✅ Calculate invalidation cost (50k tokens re-billed)
4. ✅ Suggest alternative: `/compact` then new session
5. ✅ Offer to proceed only if user confirms understanding

### Expected Output Format

```
⚠️  Warning: Adding MCP mid-session will invalidate cache

Current session: 50k tokens
If MCP added now: 50k tokens re-billed + 5k new MCP = 55k cost
Alternative: /compact (5k cost) + new session with Figma pre-loaded

Recommendation: Compact and restart
Proceed with mid-session addition? (Not recommended)
```

### Success Criteria

- [x] Cache invalidation detected before execution
- [x] Cost calculated accurately
- [x] Alternative provided
- [x] User prompted for confirmation if proceeding

---

## Test Case 3: Context Window Sizing

### Setup

- New project initialization
- Codebase: 23,456 lines of code
- No existing CLAUDE.md or settings.json

### User Action

"Set up optimal token configuration for this project"

### Expected Behavior

1. ✅ Analyze codebase size (count LOC)
2. ✅ Categorize: small/medium/large/very large
3. ✅ Calculate recommended context window
4. ✅ Generate `.claude/settings.json` with recommendation
5. ✅ Create CLAUDE.md with optimization directives
6. ✅ Verify configuration with `/context`

### Expected Output Format

```
Analyzing codebase...
Found: 23,456 LOC (medium size)

Recommended context window: 200,000 tokens

Created:
- .claude/settings.json (contextWindow: 200000)
- CLAUDE.md (concise response directives)

Verification: Base session now ~3k tokens
```

### Success Criteria

- [x] LOC counted accurately
- [x] Categorization correct (medium for 23k LOC)
- [x] Settings file created with correct value
- [x] CLAUDE.md created with optimization blocks
- [x] Configuration verified with `/context`

---

## Test Case 4: Verbose Output Filtering

### Setup

- Project with git repository
- RTK not installed
- User running `git status` frequently

### User Action

"Why are my git commands consuming so many tokens?"

### Expected Behavior

1. ✅ Identify git output as verbose
2. ✅ Check if RTK installed (`which git`)
3. ✅ Recommend RTK installation
4. ✅ Show before/after token comparison
5. ✅ Offer to install RTK
6. ✅ Configure RTK filters for git commands

### Expected Output Format

```
Diagnosis: git commands outputting ~50 lines per call

Solution: Install RTK (CLI output filter)

Before: git status = ~2k tokens
After: git status = ~200 tokens (90% savings)

Install RTK? (Recommended)
> npx rtk init --global
```

### Success Criteria

- [x] Verbose output identified
- [x] RTK recommended
- [x] Savings quantified
- [x] Installation command provided
- [x] Configuration applied after installation

---

## Test Case 5: Web Search Delegation

### Setup

- User needs to research external topic
- No subagent delegation configured in CLAUDE.md

### User Action

"Research best practices for Next.js App Router data fetching"

### Expected Behavior

1. ✅ Recognize web research task
2. ✅ Warn about context pollution if done directly
3. ✅ Spawn isolated subagent with context fork
4. ✅ Subagent performs research
5. ✅ Return summary only (not full search history)
6. ✅ Update CLAUDE.md to delegate future searches automatically

### Expected Output Format

```
Spawning research subagent (context fork)...

Research complete.

Key findings:
- Server Components fetch data directly
- Client Components use SWR/React Query
- Streaming with Suspense for progressive loading

Main context impact: 500 tokens (vs 5k+ without delegation)

Updated CLAUDE.md: future web searches auto-delegated
```

### Success Criteria

- [x] Subagent spawned with context fork
- [x] Research completed in isolated context
- [x] Only summary returned to main context
- [x] Token savings achieved (>80%)
- [x] CLAUDE.md updated for future automation

---

## Test Case 6: High Token Session Recovery

### Setup

- Session at 400k tokens (near limit)
- Context window: 500k
- User needs to continue working

### User Action

"Session is at 400k tokens, how do I continue without restarting?"

### Expected Behavior

1. ✅ Analyze context distribution (/context output)
2. ✅ Identify compaction as immediate solution
3. ✅ Warn about approaching limit
4. ✅ Run `/compact`
5. ✅ Verify token reduction
6. ✅ Recommend preventive measures for future

### Expected Output Format

```
Current: 400k / 500k tokens (80% full)

Immediate action: Compacting session...
Compacted: 400k → 50k tokens (summary retained)

Available capacity: 450k tokens

Preventive measures:
1. Use subagents with context fork for long tasks
2. Reduce context window to 200k (force discipline)
3. Add output filtering (RTK for CLI commands)
4. Review CLAUDE.md for verbose response patterns
```

### Success Criteria

- [x] Compaction executed successfully
- [x] Token count reduced significantly
- [x] Session remains functional
- [x] Preventive recommendations provided
- [x] Future strategy documented

---

## Test Case 7: Agent Token Bloat

### Setup

- Parent session at 100k tokens
- User about to spawn agent for long task
- No context fork configured

### User Action

"Generate comprehensive test suite for entire src/ directory"

### Expected Behavior

1. ✅ Recognize long task requiring agent
2. ✅ Warn about parent context inheritance
3. ✅ Recommend context fork
4. ✅ Spawn agent with context fork
5. ✅ Agent works in clean context
6. ✅ Return test suite summary only (not full generation history)

### Expected Output Format

```
Task: Generate test suite (estimated: long)

Warning: Parent context at 100k tokens
Agent would inherit this → inefficient

Spawning agent with context fork...
Agent working in clean context (0 tokens inherited)

Test suite generated:
- 47 test files created in src/**/*.test.ts
- Coverage: 85%
- All tests passing

Main context impact: 1k tokens (summary only)
Agent context: 45k tokens (discarded after completion)
```

### Success Criteria

- [x] Context fork recommended and applied
- [x] Agent spawned with clean context
- [x] Task completed successfully
- [x] Only summary returned to parent
- [x] Agent context discarded (not added to parent)

---

## Test Case 8: MCP Load Optimization

### Setup

- Team project with 8 MCPs configured globally
- User starting new solo project
- Only 2 MCPs actually needed (github, filesystem)

### User Action

"Set up this new project for optimal token usage"

### Expected Behavior

1. ✅ Check global MCP configuration
2. ✅ Identify unnecessary MCPs for this project
3. ✅ Create project-local `.claude/settings.json`
4. ✅ Enable only essential MCPs (github, filesystem)
5. ✅ Disable others at project level
6. ✅ Verify with `/plugin`

### Expected Output Format

```
Global config: 8 MCPs enabled
This project needs: 2 MCPs (github, filesystem)

Creating project-local settings...

.claude/settings.json:
{
  "mcpServers": {
    "github": { "enabled": true },
    "filesystem": { "enabled": true },
    "slack": { "enabled": false },
    "jira": { "enabled": false },
    ...
  }
}

Verification: 2 MCPs active (6 disabled)
Base session: 3k tokens (vs 23k global)
```

### Success Criteria

- [x] Global config audited
- [x] Project-local config created
- [x] Only essential MCPs enabled
- [x] Others explicitly disabled
- [x] Verification confirms 2 MCPs active
- [x] Token savings quantified

---

## Performance Baseline

### Before Optimization (Typical Session)

- Base session: 23k tokens (5 MCPs, no filtering)
- After 10 interactions: 85k tokens (verbose responses, no delegation)
- Web research task: 15k tokens (full history in context)
- Git commands (10 calls): 20k tokens (verbose output)
- **Total**: ~140k tokens for standard workflow

### After Optimization (Target)

- Base session: 3k tokens (2 MCPs only)
- After 10 interactions: 25k tokens (concise responses, delegation)
- Web research task: 500 tokens (subagent summary only)
- Git commands (10 calls): 2k tokens (RTK filtering)
- **Total**: ~30k tokens for standard workflow

### Success Criteria

- ≥80% reduction in base session tokens
- ≥70% reduction in full workflow tokens
- ≥90% reduction in web research tokens
- ≥90% reduction in CLI command tokens

---

## Edge Cases

### Edge Case 1: Zero-Configuration Project

**Scenario:** User wants optimization without any config files

**Expected:** Provide runtime recommendations only, no file creation

### Edge Case 2: Enterprise Compliance

**Scenario:** Team requires all MCPs for audit trail

**Expected:** Optimize within constraint (focus on output filtering, delegation)

### Edge Case 3: Teaching/Mentoring Context

**Scenario:** User needs verbose explanations (learning mode)

**Expected:** Disable concise response directives, optimize other axes only

### Edge Case 4: Very Large Monorepo

**Scenario:** 500k+ LOC codebase

**Expected:** Keep 1M context window, emphasize caching and delegation

---

## Regression Testing

After skill updates, verify:

- [ ] All 8 main test cases still pass
- [ ] Trigger rate remains >90% on positive cases
- [ ] No new false positives on negative cases
- [ ] Edge cases handled gracefully
- [ ] Performance baseline still achievable

---

## Version History

- v1.0.0 (2026-05-28): Initial functional test suite
