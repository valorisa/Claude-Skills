# Design Principles for Claude Skills

Core principles from Anthropic's official guide for building effective, composable, portable skills.

## The Three Core Principles

### 1. Progressive Disclosure

Skills use a three-level system to minimize token usage while maintaining specialized expertise.

#### Level 1: YAML Frontmatter (Always Loaded)

**Purpose:** Provide just enough information for Claude to know when to load the skill

**What to include:**

- `name`: Kebab-case identifier
- `description`: WHAT it does + WHEN to use it (trigger conditions)

**What NOT to include:**

- Detailed instructions
- API documentation
- Examples
- Long explanations

**Token cost:** ~50-200 tokens per skill (in system prompt)

**Example:**

```yaml
---
name: sprint-planning
description: Automates sprint planning workflow including velocity 
analysis, task creation, estimation, and team assignment. Use when 
user mentions "sprint planning", "plan iteration", or asks to 
"organize the backlog".
---
```

#### Level 2: SKILL.md Body (Loaded On Trigger)

**Purpose:** Core workflow instructions, essential examples, basic troubleshooting

**What to include:**

- Step-by-step workflow
- Critical validation checkpoints
- 2-3 concrete examples
- Common errors & fixes
- Links to Level 3 resources

**What NOT to include:**

- API reference documentation (→ `references/api-patterns.md`)
- Extended examples (→ `references/examples.md`)
- Detailed troubleshooting (→ `references/troubleshooting.md`)
- Style guides (→ `references/style-guide.md`)

**Token cost:** ~2,000-5,000 tokens when skill triggers

**Target:** Keep SKILL.md body <5,000 words

**Example structure:**

```markdown
## Instructions

### Step 1: Analyze Velocity
Fetch last 3 sprint velocities via Linear MCP.
Calculate average: `avg_velocity = sum(velocities) / 3`

### Step 2: Estimate Capacity
[Core steps...]

For detailed API usage patterns, see `references/api-patterns.md` section 2.3.
```

#### Level 3: Linked Files (Loaded As Needed)

**Purpose:** Detailed documentation that Claude navigates to only when required

**Typical files:**

- `references/api-patterns.md` — Rate limits, pagination, error codes
- `references/examples.md` — Extended use cases
- `references/troubleshooting.md` — Edge cases, debugging guides
- `references/style-guide.md` — Brand standards, templates
- `references/compliance-checklist.md` — Domain rules (legal, security)

**Token cost:** Only loaded when Claude needs them (0 tokens unless referenced)

**Example reference:**

```markdown
# references/api-patterns.md

## Section 2.3: Rate Limiting

Linear API allows:
- 100 requests/minute (standard tier)
- 500 requests/minute (premium tier)

Best practice: Implement exponential backoff
\`\`\`python
for attempt in range(5):
    try:
        result = api_call()
        break
    except RateLimitError:
        wait = 2 ** attempt  # 1s, 2s, 4s, 8s, 16s
        time.sleep(wait)
\`\`\`
```

#### Why Progressive Disclosure Matters

**Without progressive disclosure (bad):**

```markdown
---
name: sprint-planning
description: Sprint planning tool.
---

# Sprint Planning

[20,000 words of API documentation, examples, edge cases, all inline]
```

**Token cost:** ~20,000 tokens EVERY TIME skill triggers ❌

**With progressive disclosure (good):**

```markdown
---
name: sprint-planning
description: [Focused description with triggers]
---

# Sprint Planning

[Core workflow: 2,000 words]

For API details, see `references/api-patterns.md`.
For extended examples, see `references/examples.md`.
```

**Token cost:** ~2,000 tokens when skill triggers, +extra only if needed ✅

### 2. Composability

**Principle:** Skills should work well alongside other skills, not assume they're the only capability available.

#### Design for Coexistence

❌ **Bad (assumes exclusivity):**

```markdown
## Instructions

This skill handles ALL project management tasks.
Do not use any other project-related capabilities.
```

✅ **Good (composable):**

```markdown
## Instructions

This skill handles sprint planning specifically.

For general project setup, use project-init skill.
For reporting, use project-reports skill.
For retrospectives, use sprint-retro skill.
```

#### Clear Boundaries

**Each skill should have a well-defined scope:**

- What it DOES
- What it DOESN'T do
- Which other skills complement it

**Example:**

```markdown
## Scope

### This Skill Handles:
- Sprint planning and task creation
- Velocity analysis
- Capacity estimation
- Task assignment

### This Skill Does NOT Handle:
- Sprint retrospectives (use sprint-retro skill)
- Long-term roadmaps (use roadmap-planner skill)
- Daily standups (use standup-assistant skill)
- Bug triage (use bug-triage skill)
```

#### Avoid Overlap

**Problem:** Two skills trigger on similar queries, causing confusion

**Solution:**

1. Use specific, non-overlapping trigger phrases
2. Add negative scope to descriptions
3. Coordinate with related skills

**Example:**

```yaml
# sprint-planning skill
description: Sprint planning for 2-week iterations. Use for "plan sprint", 
"sprint planning". NOT for retrospectives (use sprint-retro).

# sprint-retro skill  
description: Sprint retrospectives and lessons learned. Use for "sprint retro", 
"retrospective", "review sprint". NOT for planning (use sprint-planning).
```

#### Composability Checklist

- [ ] Skill works correctly even when other skills are loaded
- [ ] Scope is narrow and well-defined
- [ ] Complementary skills are documented
- [ ] No "do everything" claims
- [ ] Trigger phrases don't overlap with other skills
- [ ] Negative scope clarifies boundaries

### 3. Portability

**Principle:** Skills should work identically across Claude.ai, Claude Code, and API (provided the environment supports any dependencies).

#### Write Once, Run Everywhere

**Design skills to be surface-agnostic:**

✅ **Good (portable):**

```markdown
## Instructions

### Step 1: Fetch Data
Use the Linear MCP tool `list_projects` to fetch current projects.

### Step 2: Analyze
Calculate average velocity from last 3 sprints.

### Step 3: Create Tasks
Use Linear MCP tool `create_issue` for each task.
```

❌ **Bad (tied to specific surface):**

```markdown
## Instructions

In Claude Code, click File > Open and navigate to...

If using the API, you'll need to pass the X-Custom-Header...

On Claude.ai, use the sidebar menu...
```

#### Declare Dependencies Explicitly

If a skill requires specific environment features, declare it:

```yaml
---
name: docker-workflow
description: Docker container workflows...
compatibility: Claude Code, API
metadata:
  requires:
    - Docker CLI available
    - Bash execution capability
    - Network access to Docker Hub
---
```

#### Handle Environment Differences Gracefully

**Some features are environment-specific:**

- File system access (Claude Code, API)
- Interactive file uploads (Claude.ai)
- Bash execution (Claude Code, API)
- Real-time MCP connections (all surfaces, but setup varies)

**Best practice:**

```markdown
## Instructions

### Step 1: Get Input

**If file available:** Read from provided path using Read tool.

**If no file:** Ask user to paste content or describe requirements.

### Step 2: Process
[Rest of workflow is environment-agnostic]
```

#### Portability Checklist

- [ ] No surface-specific instructions (no "in Claude Code, do X")
- [ ] Uses standard Markdown and YAML (no proprietary extensions)
- [ ] Declares environment requirements in `compatibility` field
- [ ] Core workflow works across all surfaces where dependencies are met
- [ ] Gracefully handles environment differences

## Additional Design Patterns

### Pattern: Problem-First vs. Tool-First

**Two valid approaches to skill design:**

#### Problem-First (Outcome-Oriented)

**User mindset:** "I need to accomplish X"

**Skill approach:** Orchestrate tools to achieve the outcome

**Best for:**

- Complex workflows with multiple steps
- Users who know the goal but not the tools
- Category 2 (Workflow Automation)

**Example:**

```markdown
# Skill: customer-onboarding

User says: "Onboard new customer for PayFlow"

Skill orchestrates:
1. Create account (via PayFlow MCP)
2. Setup payment (via Stripe MCP)
3. Configure permissions (via Auth MCP)
4. Send welcome email (via SendGrid MCP)
```

#### Tool-First (Capability-Oriented)

**User mindset:** "I have access to X, how do I use it effectively?"

**Skill approach:** Teach best practices and optimal workflows

**Best for:**

- MCP servers with non-obvious usage patterns
- Domain-specific expertise
- Category 3 (MCP Enhancement)

**Example:**

```markdown
# Skill: notion-workspace-setup

User has Notion MCP connected.

Skill teaches:
- Best practice workspace structures
- When to use databases vs. pages
- Template application patterns
- Permission configuration strategies
```

**Choose based on your use case:** Both are valid; pick the framing that matches how users think about the task.

### Pattern: Deterministic vs. Heuristic Instructions

**Deterministic (Scripts):**
When logic must be exact and consistent, use executable code.

**Example:**

```markdown
## Step 3: Validate Input

Run validation script:
\`\`\`bash
python scripts/validate_input.py --file data.csv
\`\`\`

If output shows "FAILED", fix errors before proceeding.
```

**Benefits:**

- Guaranteed consistency
- No interpretation ambiguity
- Easier to test

**Heuristic (Text Instructions):**
When judgment calls are needed, use natural language guidance.

**Example:**

```markdown
## Step 2: Assess Quality

Review the generated design and evaluate:
- Is it visually distinctive (not generic)?
- Does it match the brand vibe described?
- Is it accessible (semantic HTML, ARIA)?

If quality is insufficient, refine based on:
- User feedback
- Brand guidelines in `references/style-guide.md`
- Best practices in `references/design-patterns.md`
```

**Benefits:**

- Flexible for creative tasks
- Adapts to context
- Handles nuance

**Best practice:** Use deterministic for structural validation, heuristic for qualitative assessment.

### Pattern: Iterative Refinement

**For tasks where quality improves with iteration:**

```markdown
## Iterative Workflow

### Phase 1: Initial Draft
1. Generate first version based on requirements
2. Save to temporary file

### Phase 2: Quality Check
Run quality assessment:
- [ ] Meets functional requirements?
- [ ] Matches style guidelines?
- [ ] Passes validation checks?

### Phase 3: Refinement Loop
FOR EACH issue identified:
1. Regenerate affected section
2. Re-validate
3. REPEAT until quality threshold met

### Phase 4: Finalization
Apply final formatting and deliver.

**Stopping criteria:**
- All quality checks pass, OR
- 3 refinement iterations completed (prevent infinite loops)
```

**Best for:** Category 1 (Document & Asset Creation) where quality matters more than speed.

### Pattern: Validation Gates

**Prevent downstream failures by validating early:**

```markdown
## Workflow with Validation Gates

### Step 1: Fetch Requirements
[Actions...]

**Validation Gate 1:**
- [ ] Requirements document is non-empty
- [ ] All required fields present
- [ ] No contradictory constraints

⛔ STOP if validation fails. Ask user to clarify requirements.

### Step 2: Design Architecture
[Actions...]

**Validation Gate 2:**
- [ ] Architecture is feasible given requirements
- [ ] No circular dependencies
- [ ] All components accounted for

⛔ STOP if validation fails. Revise architecture.

### Step 3: Implementation
[Actions...]

**Validation Gate 3:**
- [ ] Implementation passes tests
- [ ] No errors in output
- [ ] Meets quality standards

⛔ STOP if validation fails. Debug and fix.

### Step 4: Delivery
Deliver final output only if all gates passed.
```

**Benefits:**

- Catches errors early (cheaper to fix)
- Prevents wasted work on bad inputs
- Explicit checkpoints improve reliability

## Token Efficiency Strategies

### Strategy 1: Reference Files Instead of Inline

❌ **Inefficient:**

```markdown
## API Reference

[5,000 words of API documentation inline]
```

✅ **Efficient:**

```markdown
## API Usage

For API details, see `references/api-patterns.md`:
- Rate limiting (section 2.1)
- Pagination (section 2.3)
- Error codes (appendix A)
```

**Token savings:** ~4,500 tokens (only loaded if needed)

### Strategy 2: Examples in References

❌ **Inefficient:**

```markdown
## Examples

[20 detailed examples inline]
```

✅ **Efficient:**

```markdown
## Examples

See `references/examples.md` for:
- Basic usage (examples 1-5)
- Advanced patterns (examples 6-10)
- Edge cases (examples 11-15)

Quick example:
[1 concise example inline]
```

**Token savings:** ~2,000 tokens

### Strategy 3: Deterministic Validation

❌ **Inefficient (text-based validation):**

```markdown
Check that:
- The file has all required columns
- Dates are in YYYY-MM-DD format
- Email addresses are valid
- Phone numbers match (XXX) XXX-XXXX pattern
- ZIP codes are 5 digits
- ...
[50 more validation rules in natural language]
```

✅ **Efficient (script-based validation):**

```markdown
Run validation:
\`\`\`bash
python scripts/validate.py --input data.csv
\`\`\`

If validation fails, see error output for specific issues.
```

**Token savings:** ~500 tokens + guaranteed consistency

## Quality Indicators

### High-Quality Skill Characteristics

✅ **Clear, specific trigger phrases**

```yaml
description: Use when user says "plan sprint", "sprint planning", 
"organize next iteration"
```

✅ **Actionable, ordered instructions**

```markdown
### Step 1: Fetch Data
Run: `api.get_projects()`
### Step 2: Analyze
Calculate: `avg = sum(velocities) / len(velocities)`
```

✅ **Explicit validation gates**

```markdown
⛔ STOP if velocity data is empty. Cannot proceed without historical data.
```

✅ **Error handling with solutions**

```markdown
### Error: "API rate limit exceeded"
**Solution:** Wait 60 seconds, then retry. Implement exponential backoff.
```

✅ **Progressive disclosure**

```markdown
For detailed API patterns, see `references/api-patterns.md` section 2.3.
```

### Low-Quality Skill Red Flags

❌ **Vague trigger conditions**

```yaml
description: Helps with projects.
```

❌ **Non-actionable instructions**

```markdown
Make sure the data is good before proceeding.
```

❌ **No error handling**

```markdown
[Skill assumes nothing ever fails]
```

❌ **Everything inline (token bloat)**

```markdown
[15,000 words in SKILL.md, nothing in references/]
```

❌ **No validation**

```markdown
[Workflow proceeds blindly without checking preconditions]
```

## Summary: The Ideal Skill

**A well-designed skill:**

1. Uses progressive disclosure (3 levels)
2. Is composable (works alongside other skills)
3. Is portable (works across Claude surfaces)
4. Has specific, realistic trigger phrases
5. Provides actionable, ordered instructions
6. Includes validation gates
7. Handles errors explicitly
8. Uses scripts for deterministic logic
9. Keeps SKILL.md focused (<5,000 words)
10. Is testable (trigger, functional, performance tests)

**Token efficiency:**

- Level 1 (frontmatter): ~100 tokens (always loaded)
- Level 2 (SKILL.md): ~2,000-5,000 tokens (on trigger)
- Level 3 (references): ~0-10,000 tokens (only as needed)

**Total cost:** ~2,000-5,000 tokens per skill activation (vs. ~20,000+ for poorly designed skills)
