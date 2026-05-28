# CLAUDE.md Templates — Token Optimization

Ready-to-use configuration blocks for optimizing token consumption.

## Concise Response Block (Caveman-inspired)

```markdown
## Response Style
- Ultra-concise responses, bullet points only
- Remove: superfluous articles, politeness phrases, reformulations, intros, conclusions
- Format: direct action, direct result
- I'm ADHD, no time for walls of text
```

## Web Search Delegation Block

```markdown
## Web Search
All web research must be delegated to isolated subagent (context fork).
Subagent returns ONLY extracted relevant information.
Never inject raw page Markdown history into main context.
```

## File Path Specification Block

```markdown
## Memory/Learning Commands
`/learn` command: updates ONLY these files:
- ./docs/project-memory.md
- ./CLAUDE.md (section "Project Context")
Do not scan other files unless explicitly instructed.
```

## Reasoning Effort Block

```markdown
## Reasoning Effort
- Simple task / known command → minimal effort, no `think`
- Design / architecture task → medium effort
- Complex unsolved problem → high effort only on explicit request
Never over-reason a simple task.
```

## Agent Delegation Block

```markdown
## Agents and Subtasks
Any long or high-volume task (transcription, test generation, planning,
codebase exploration) must run in subagent with context fork.
Subagent returns its result only, not work history.
```

## Complete Minimal CLAUDE.md Template

```markdown
# Project [NAME]

## Context
[Brief project description]

## Response Style
Concise responses. Bullet points. No intro or conclusion.

## Web Search
Delegate to isolated subagent. Return only relevant results.

## Agents
Long tasks → context fork. Result only, not history.

## Key Files
- [path/to/file1.md]: [role]
- [path/to/file2.ts]: [role]

## Available Commands
- `/learn`: updates [./docs/memory.md]
- `/review`: reviews [./src/] looking for [specific criteria]
```

## Advanced: Project-Specific Blocks

### For Backend API Projects

```markdown
## API Testing
Use HTTP client directly (curl/httpie) instead of screenshot-based testing.
Output: status code + key response fields only, not full JSON dumps.
```

### For Frontend Projects

```markdown
## Component Development
Use Stagehand for browser automation (DOM-based, no screenshots).
Test results: pass/fail + error message only, not full browser logs.
```

### For Data Pipeline Projects

```markdown
## Pipeline Debugging
Query logs via CLI with filters, not GUI screenshots.
Commands: use `--tail 20` and `--format compact` flags.
Output: timestamp + error + affected record count only.
```

### For Documentation Projects

```markdown
## Documentation Generation
Generate docs in subagent with context fork.
Return: ToC + validation results only, not full doc content.
Main context accesses docs by reference when needed.
```

## Context Window Sizing Guide

```markdown
## Context Window Configuration
# Add to settings.json (not committed, local only)

# Small codebase (<10k LOC)
{ "contextWindow": 150000 }

# Medium codebase (10k-50k LOC)
{ "contextWindow": 200000 }

# Large codebase (>50k LOC)
{ "contextWindow": 500000 }

# Very large monorepo
{ "contextWindow": 1000000 }  # Use with strict optimization discipline
```

## MCP Configuration Examples

### Minimal Setup (Solo Developer)

```markdown
## Enabled MCPs
- github: PR and issue management
- filesystem: Local file operations

Disabled by default:
- email (use only when needed)
- calendar (enable per-session if scheduling task)
- all others
```

### Team Setup (Collaborative Work)

```markdown
## Enabled MCPs
- github: PR/issue management
- slack: Team notifications
- linear: Task tracking
- filesystem: Local operations

Session-specific MCPs (enable only when needed):
- notion: Documentation work
- figma: Design handoff sessions
- sentry: Error investigation sessions
```

### Enterprise Setup (Full Toolchain)

```markdown
## Core MCPs (Always Enabled)
- github: Code management
- slack: Communications
- linear/jira: Task tracking
- datadog/sentry: Monitoring

Optional MCPs (Enable per workflow):
- terraform: Infrastructure work
- kubernetes: Deployment work
- confluence: Documentation work
- salesforce: CRM integration work

Rule: Never exceed 5 concurrent MCPs per session.
```

## Git Command Optimization

```markdown
## Git Commands
All git commands use compact output:
- `git status --short`
- `git log --oneline --graph -n 20`
- `git diff --stat` (not full diff, unless explicitly requested)

For detailed diff: use subagent with context fork, return summary only.
```

## Test Execution Optimization

```markdown
## Test Execution
Test runs output:
- Summary: passed/failed/skipped counts
- Failed tests: name + error message only
- Full test logs: on explicit request only

Use test filtering: `npm test -- --testNamePattern="specific test"`
Avoid: running full suite and dumping all output to context.
```

## Validation Checklist for CLAUDE.md

Before committing your CLAUDE.md:

- [ ] Response style: concise directive present
- [ ] Web search: delegation to subagent configured
- [ ] Agents: context fork rules defined
- [ ] File paths: explicit paths for common operations
- [ ] Commands: output filtering specified
- [ ] MCPs: only essential ones enabled
- [ ] Context window: sized appropriately for codebase
- [ ] Reasoning effort: guidelines provided

## Real-World Examples

### Example 1: Startup Project (Fast Iteration)

```markdown
# [Project Name]

Ultra-concise. Bullet points only. Zero fluff.

Web search → subagent fork.
Agents → context fork for tasks >5 min.
Files: ./src/*, ./docs/memory.md only.

MCPs: github, filesystem only.
Context: 150k tokens (small codebase).
```

### Example 2: Enterprise Project (Compliance-Heavy)

```markdown
# [Project Name]

## Compliance
All changes require audit trail. Document: what, why, when, who.

## Response Style
Concise but complete. Include compliance metadata in outputs.

## Agents
Long audits → context fork. Return findings summary + audit log reference.

## MCPs
- github (code)
- jira (tracking)
- confluence (docs)
- datadog (monitoring)

Session-specific: Enable only when explicitly needed.
Context: 500k tokens (large codebase + compliance overhead).
```

### Example 3: Open Source Project (Community-Focused)

```markdown
# [Project Name]

Public repo. Assume contributors are reading outputs.

## Response Style
Clear and helpful. Include context for community members.

## Agents
Issue triage → subagent fork. Return prioritized list + reasoning.

## MCPs
- github (main workflow)
- Optional: discord (community management sessions)

Context: 200k tokens (medium codebase).
```

## Troubleshooting Common Issues

### Issue: Still verbose despite directives

**Fix:**

```markdown
## CRITICAL DIRECTIVE
Maximum response length: 10 lines unless explicitly asked for detail.
Format: [Action] → [Result] → [Next step if needed]
Example:
✅ Installed RTK → git commands now filtered → verify with `git status`
❌ I've successfully installed the RTK tool which will help us filter git command outputs. Now let's verify...
```

### Issue: Agents not using context fork

**Fix:**

```markdown
## Agent Spawning (MANDATORY)
ALL agent spawns MUST include: `{ "context": "fork" }`
No exceptions. Verify in /context after spawning.
If agent appears in main context: STOP, respawn with fork.
```

### Issue: MCPs loading unexpectedly

**Fix:**

```markdown
## MCP Auto-Load Prevention
Disable global MCP settings. Use project-local .claude/settings.json only.
Verify at session start: `/plugin` should show ≤3 active plugins.
If more: disable excess immediately before any work.
```

## Performance Metrics

Target metrics after applying these templates:

- Base session: <5k tokens
- After 10 interactions: <30k tokens
- Agent task (isolated): <50k tokens
- Full work session (4 hours): <150k tokens

**Red flags:**

- Base session >10k tokens → too many MCPs
- After 10 interactions >50k tokens → responses too verbose
- Agent task >100k tokens → missing context fork
- Work session >300k tokens → cache invalidation or bloat

## Version History

- v1.0.0 (2026-05-28): Initial templates based on token optimization research
