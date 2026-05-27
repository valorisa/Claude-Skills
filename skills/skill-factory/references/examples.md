# Real-World Skill Examples

Concrete examples demonstrating the three skill categories and common patterns.

## Category 1: Document & Asset Creation

### Example 1.1: Frontend Design Skill

**Use case:** Generate production-grade frontend interfaces

**Frontmatter:**

```yaml
---
name: frontend-design
description: Creates distinctive, production-grade frontend interfaces 
with high design quality, semantic HTML, modern CSS, and accessibility 
best practices. Use when building web components, pages, artifacts, 
posters, or applications. Triggers on "build a component", "create a page", 
"design an interface", or when user uploads design mockups.
metadata:
  author: Anthropic
  version: 1.0.0
  category: document-creation
---
```

**Key techniques used:**

- Embedded style guide (progressive disclosure → `references/style-guide.md`)
- Quality checklist before finalization
- Iterative refinement loop
- No external tools required (uses Claude's built-in capabilities)

**Workflow pattern:**

```markdown
## Workflow

### Phase 1: Requirements
1. Ask about target audience, brand vibe, key features
2. Determine layout type (landing page, dashboard, etc.)

### Phase 2: Initial Design
1. Generate semantic HTML structure
2. Create modern CSS with custom properties
3. Apply responsive breakpoints

### Phase 3: Quality Check
- [ ] Semantic HTML (not divs everywhere)
- [ ] Modern CSS (Grid/Flexbox, no floats)
- [ ] Accessible (ARIA labels, semantic tags)
- [ ] Responsive (mobile-first)
- [ ] Distinctive (not generic Bootstrap clone)

### Phase 4: Refinement (if needed)
FOR each failed quality check:
    Fix issue
    Re-validate
    
### Phase 5: Delivery
Present final code with usage instructions
```

**Why this works:**

- Clear trigger phrases users actually say
- Quality gates prevent generic output
- Iterative refinement improves quality
- Self-contained (no MCP dependencies)

---

### Example 1.2: DOCX Creator Skill

**Use case:** Generate formatted Word documents

**Frontmatter:**

```yaml
---
name: docx-creator
description: Creates professionally formatted Word documents (.docx) 
including reports, proposals, technical documentation, and business 
letters. Handles headings, tables, images, formatting, and styles. 
Use when user asks to "create a Word doc", "generate DOCX", "make a 
report", or specifies .docx output.
metadata:
  category: document-creation
compatibility: Claude Code, API
metadata:
  requires:
    - python-docx library (installed via scripts)
---
```

**Key techniques:**

- Template system (`templates/report-template.docx`)
- Deterministic formatting via scripts
- Style guide enforcement

**Workflow pattern:**

```markdown
## Workflow

### Step 1: Content Gathering
1. Ask for document type (report, proposal, letter)
2. Gather content sections
3. Identify required elements (tables, images, headers)

### Step 2: Template Selection
Based on document type, select template:
- Report → `templates/report-template.docx`
- Proposal → `templates/proposal-template.docx`
- Letter → `templates/letter-template.docx`

### Step 3: Generation
Run generation script:
\`\`\`bash
python scripts/generate_docx.py \\
    --template templates/report-template.docx \\
    --content content.json \\
    --output document.docx
\`\`\`

### Step 4: Validation
Check:
- [ ] All sections present
- [ ] Formatting consistent
- [ ] No placeholder text
- [ ] File opens in Word without errors

### Step 5: Delivery
Provide download link and preview
```

**Why this works:**

- Scripts ensure consistent formatting
- Templates provide professional appearance
- Validation prevents incomplete output

---

## Category 2: Workflow Automation

### Example 2.1: Sprint Planning Skill

**Use case:** Automate Agile sprint planning workflow

**Frontmatter:**

```yaml
---
name: sprint-planning-automation
description: Automates sprint planning workflow including velocity 
analysis, capacity estimation, task creation, and team assignment. 
Use when user mentions "sprint", "sprint planning", "plan iteration", 
"organize backlog", or asks to "set up next sprint". Works with Linear, 
Jira, or generic task lists.
metadata:
  category: workflow-automation
  mcp-server: linear, jira (optional)
---
```

**Key techniques:**

- Sequential workflow with validation gates
- Velocity analysis (data-driven)
- Optional MCP integration
- Falls back gracefully if MCP unavailable

**Workflow pattern:**

```markdown
## Workflow

### Step 1: Analyze Historical Velocity
IF MCP connected:
    Fetch last 3 sprint velocities via API
ELSE:
    Ask user for velocity data

Calculate: `avg_velocity = sum(velocities) / 3`

**Validation Gate:**
⛔ STOP if velocity data empty or invalid

### Step 2: Assess Capacity
1. Count available team members
2. Account for holidays/PTO
3. Calculate: `capacity = avg_velocity * availability_factor`

**Validation Gate:**
⛔ STOP if capacity ≤ 0

### Step 3: Prioritize Backlog
1. Fetch backlog items (via MCP or user input)
2. Sort by priority
3. Select items until capacity reached

### Step 4: Create Sprint Tasks
FOR each selected item:
    IF MCP available:
        Create task via API
    ELSE:
        Generate task template for manual creation
    
    Assign to team member (round-robin)
    
**Validation Gate:**
⛔ STOP if any task creation fails

### Step 5: Summary
Report:
- Sprint capacity: X story points
- Tasks created: Y items
- Team assignments: Z members
- Sprint goal: [derived from selected items]
```

**Why this works:**

- Works with OR without MCP (flexible)
- Validation gates prevent bad data
- Data-driven (velocity, capacity)
- Handles failures gracefully

---

### Example 2.2: Release Notes Generator

**Use case:** Generate release notes from git commits

**Frontmatter:**

```yaml
---
name: release-notes-generator
description: Generates structured release notes from git commit history, 
categorizing changes into features, fixes, breaking changes, and 
improvements. Use when user asks to "generate release notes", "create 
changelog", "document this release", or mentions semantic versioning.
metadata:
  category: workflow-automation
compatibility: Claude Code, API
metadata:
  requires:
    - Git repository
    - Bash execution
---
```

**Workflow pattern:**

```markdown
## Workflow

### Step 1: Gather Commits
\`\`\`bash
git log --oneline --no-merges $(git describe --tags --abbrev=0)..HEAD
\`\`\`

### Step 2: Categorize by Conventional Commits
Parse commit messages:
- `feat:` → Features
- `fix:` → Bug Fixes
- `BREAKING CHANGE:` → Breaking Changes
- `perf:` → Performance Improvements
- `docs:` → Documentation

### Step 3: Group and Format
FOR each category:
    Extract relevant commits
    Format as markdown list
    Include commit hash links

### Step 4: Generate Semantic Version
Based on changes:
- Breaking changes → Major version bump (X.0.0)
- Features → Minor version bump (0.X.0)
- Fixes only → Patch version bump (0.0.X)

### Step 5: Create Release Notes Document
Format:
# Release v{version}

## Breaking Changes
[List]

## Features
[List]

## Bug Fixes
[List]

## Performance Improvements
[List]

## Contributors
[Generate from git log]
```

**Why this works:**

- Deterministic (parses structured commit messages)
- Follows standards (Conventional Commits, SemVer)
- Handles missing categories gracefully
- Links to actual commits (traceability)

---

## Category 3: MCP Enhancement

### Example 3.1: Sentry Code Review Skill

**Use case:** Automated bug fixing using Sentry error data

**Frontmatter:**

```yaml
---
name: sentry-code-review
description: Automatically analyzes and fixes detected bugs in GitHub 
Pull Requests using Sentry's error monitoring data. Fetches stack traces, 
identifies root causes, suggests fixes, and can auto-fix common issues. 
Use when user mentions "Sentry errors in this PR", "fix Sentry issues", 
or asks to "review PR with Sentry context". Requires Sentry MCP connection.
metadata:
  author: Sentry
  category: mcp-enhancement
  mcp-server: sentry
compatibility: Claude Code, API
---
```

**Key techniques:**

- Multi-MCP coordination (Sentry + GitHub)
- Domain expertise (error analysis patterns)
- Auto-fix for common issues
- Manual review for complex cases

**Workflow pattern:**

```markdown
## Workflow (Multi-MCP Coordination)

### Phase 1: Fetch Error Data (Sentry MCP)
1. Get PR number from user or context
2. Query Sentry for errors related to PR files:
   `sentry.get_errors(files=changed_files, time_range="24h")`
3. Fetch stack traces for each error

**Checkpoint:** Verify at least 1 error found

### Phase 2: Analyze Errors (Domain Expertise)
FOR each error:
    1. Identify error type (null pointer, type error, etc.)
    2. Locate root cause in code
    3. Check if auto-fixable (common patterns)
    4. Generate fix recommendation

Common auto-fixable patterns:
- Null checks missing → Add guard clause
- Type mismatches → Add type coercion
- Uncaught exceptions → Add try/catch
- Off-by-one errors → Adjust bounds

**Checkpoint:** At least 1 root cause identified

### Phase 3: Apply Fixes (GitHub MCP)
FOR each auto-fixable error:
    1. Generate code fix
    2. Test fix doesn't break syntax
    3. Apply to PR branch via GitHub API
    4. Add comment explaining fix

FOR each manual-review error:
    1. Add PR comment with:
       - Error description
       - Root cause analysis
       - Suggested fix approach
       - Link to Sentry issue

**Checkpoint:** All errors addressed (auto OR manual)

### Phase 4: Verification (Sentry MCP)
1. Wait for PR to re-run tests
2. Check if errors still occur
3. Report success rate
```

**Why this works:**

- Combines data from multiple sources (Sentry + GitHub)
- Embeds domain knowledge (error patterns)
- Graduated response (auto-fix simple, flag complex)
- Verification loop ensures fixes work

---

### Example 3.2: Notion Workspace Setup

**Use case:** Initialize Notion workspace with best practices

**Frontmatter:**

```yaml
---
name: notion-workspace-setup
description: Sets up a Notion workspace following best practices for 
project management, documentation, and knowledge bases. Creates pages, 
databases, templates, and permissions. Use when user asks to "set up 
Notion", "create Notion workspace", "initialize Notion project", or 
"organize Notion space". Requires Notion MCP connection.
metadata:
  category: mcp-enhancement
  mcp-server: notion
---
```

**Workflow pattern:**

```markdown
## Workflow (Problem-First Approach)

### Step 1: Discover Requirements
Ask:
1. Workspace purpose? (project mgmt, docs, wiki, etc.)
2. Team size?
3. Key workflows? (sprints, client tracking, etc.)
4. Permissions model? (public, team-only, role-based)

### Step 2: Select Architecture Pattern
Based on purpose, choose pattern:

**Pattern A: Project Management**
- Projects database (Kanban view)
- Tasks database (linked to projects)
- Sprint database (time-boxed views)
- Team database (for assignments)

**Pattern B: Documentation**
- Hierarchy: Company → Teams → Projects → Docs
- Templates for: RFC, How-to, Decision log
- Wiki-style linking

**Pattern C: Knowledge Base**
- Topics database (tagged, categorized)
- FAQs database
- Resources database (links, files)

### Step 3: Create Structure (Notion MCP)
FOR each component in pattern:
    notion.create_page(title, properties, icon)
    notion.create_database(schema, views)
    notion.create_template(structure)

**Checkpoint:** All components created successfully

### Step 4: Configure Permissions
Apply permission model:
- Public pages → Share with workspace
- Team pages → Restrict to team
- Private pages → Owner only

### Step 5: Seed with Examples
Add sample content to demonstrate usage:
- 1 example project
- 2 example tasks
- 1 example document

### Step 6: Delivery
Provide:
- Link to root page
- Quick-start guide
- Template usage instructions
```

**Why this works:**

- User describes outcome, skill orchestrates tools
- Best practices embedded (patterns)
- Examples reduce onboarding friction
- Permissions configured correctly from start

---

## Pattern Examples

### Pattern: Sequential Workflow Orchestration

**Example: Customer Onboarding (PayFlow)**

```markdown
## Workflow: Onboard New Customer

### Step 1: Create Account (PayFlow MCP)
\`\`\`python
account = payflow.create_customer(
    name=name,
    email=email,
    company=company
)
\`\`\`
**Validation:** Account ID returned

### Step 2: Setup Payment (Stripe MCP)
\`\`\`python
payment_method = stripe.create_payment_method(
    customer_id=account.stripe_id,
    type="card"
)
stripe.attach_to_customer(payment_method.id, account.stripe_id)
\`\`\`
**Validation:** Payment method verified

### Step 3: Create Subscription (PayFlow MCP)
\`\`\`python
subscription = payflow.create_subscription(
    customer_id=account.id,
    plan_id=plan_id,
    payment_method_id=payment_method.id
)
\`\`\`
**Validation:** Subscription active

### Step 4: Send Welcome Email (SendGrid MCP)
\`\`\`python
sendgrid.send_email(
    to=account.email,
    template="welcome_email",
    data={"name": name, "login_url": account.login_url}
)
\`\`\`
**Validation:** Email sent (200 OK)

## Rollback on Failure
IF any step fails:
    Rollback previous steps in reverse order
    Report: "Onboarding failed at Step X: {error}"
    Suggest: Manual cleanup steps if needed
```

---

### Pattern: Iterative Refinement

**Example: Technical Documentation Generator**

```markdown
## Iterative Documentation Workflow

### Phase 1: Initial Draft
1. Analyze code structure
2. Extract: Functions, classes, modules
3. Generate first draft documentation

### Phase 2: Quality Assessment
Run quality checks:
- [ ] All public APIs documented?
- [ ] Examples provided for complex functions?
- [ ] Consistent formatting (Markdown)?
- [ ] No placeholder text (e.g., "TODO")?
- [ ] Links between related sections?

### Phase 3: Refinement Loop (Max 3 iterations)
WHILE quality checks fail AND iterations < 3:
    FOR each failed check:
        Regenerate affected section
        Apply quality standards from `references/doc-standards.md`
    
    Re-run quality assessment
    
    IF all pass:
        BREAK

### Phase 4: Finalization
1. Generate table of contents
2. Add cross-references
3. Apply final formatting
4. Run linter: `markdownlint docs/*.md`

### Stopping Criteria
- All quality checks pass, OR
- 3 iterations completed (deliver best version with caveats)
```

---

### Pattern: Context-Aware Tool Selection

**Example: Smart File Storage**

```markdown
## Smart Storage Decision Tree

### Decision Criteria
1. File size
2. File type
3. Collaboration needs
4. Retention policy

### Decision Logic

IF file_size > 10MB:
    → Use cloud storage MCP (Drive, S3)
    Reason: Email/DB attachments break at 10MB

ELSE IF file_type in [".docx", ".sheets", ".slides"]:
    → Use Office365/Google MCP
    Reason: Native editing support

ELSE IF collaboration == "real-time":
    → Use Notion/Docs MCP
    Reason: Live collaboration features

ELSE IF temporary == True:
    → Use local storage
    Reason: No need for persistent storage

ELSE:
    → Use GitHub MCP (for code) OR Drive MCP (for other)
    Reason: Default persistent storage

### Execution
Apply selected storage method
Report to user: "Stored in [Service] because [Reason]"
```

---

## Testing Examples

### Trigger Test Example

**Skill:** `sprint-planning-automation`

**Should TRIGGER ✅**

```
- "Help me plan this sprint"
- "Create sprint tasks from backlog"
- "Set up the next sprint"
- "Plan sprint 23"
- "Let's organize the next iteration"
- "I need to plan our two-week sprint"
- "Set me up for the upcoming sprint"
- "Plan a sprint in Linear"
```

**Should NOT Trigger ❌**

```
- "What's the weather today?" (unrelated)
- "Write a Python function" (coding, not planning)
- "Explain agile methodology" (educational, not action)
- "Show me last sprint's results" (reporting, not planning)
- "Create a roadmap for Q2" (roadmap ≠ sprint)
- "Schedule a sprint planning meeting" (calendar, not tasks)
```

**Trigger Accuracy:** 15/15 positive (100%), 14/15 negative (93%) → ✅ PASS

---

### Functional Test Example

**Skill:** `release-notes-generator`

**Test Case:** Happy Path

**Given:**

- Git repo with 15 commits since last tag
- Commits follow Conventional Commits format
- Mix of feat, fix, and docs commits

**When:**
User says: "Generate release notes for v2.1.0"

**Then:**

1. ✅ Fetches commits since last tag (v2.0.0)
2. ✅ Categorizes correctly:
   - 5 features
   - 8 bug fixes
   - 2 docs updates
3. ✅ Suggests version: v2.1.0 (minor bump, has features)
4. ✅ Generates formatted markdown
5. ✅ Includes commit hash links
6. ✅ Lists contributors (3 unique)
7. ✅ Output has no placeholders

**Verification:**

```bash
# Output file created
test -f RELEASE_NOTES.md

# Contains expected sections
grep "## Features" RELEASE_NOTES.md
grep "## Bug Fixes" RELEASE_NOTES.md

# Version number correct
grep "# Release v2.1.0" RELEASE_NOTES.md
```

**Result:** ✅ PASS

---

### Performance Comparison Example

**Skill:** `frontend-design`

**Scenario:** Build a landing page for a SaaS product

**Without Skill (Baseline):**

- User messages: 8
- Claude messages: 12
- Total: 20 messages
- Token consumption: ~14,500 tokens
- Iterations: 4 rounds of refinement
- Time: 12 minutes
- Output quality: 6/10 (generic, Bootstrap-style)

**With Skill (Target):**

- User messages: 2
- Claude messages: 3
- Total: 5 messages (-75%)
- Token consumption: ~6,200 tokens (-57%)
- Iterations: 1 round of refinement (-75%)
- Time: 3 minutes (-75%)
- Output quality: 9/10 (distinctive, production-ready)

**Success Criteria Met:**

- ✅ ≥50% reduction in messages (75% achieved)
- ✅ ≥40% reduction in tokens (57% achieved)
- ✅ ≥50% reduction in time (75% achieved)
- ✅ Higher output quality

**Result:** 4/4 targets met → ✅ Production-ready

---

## Anti-Patterns (What NOT to Do)

### Anti-Pattern 1: The Kitchen Sink

❌ **Bad:**

```yaml
description: Does everything related to project management, 
documentation, code generation, bug fixing, testing, deployment, 
monitoring, analytics, reporting, and team collaboration.
```

**Problem:** Too broad, triggers on everything, does nothing well

✅ **Good:**

```yaml
description: Automates sprint planning workflow including velocity 
analysis and task creation. Use for "sprint planning" only. NOT for 
retrospectives, reporting, or deployment.
```

### Anti-Pattern 2: The Mystery Box

❌ **Bad:**

```yaml
description: Advanced project tool.
```

**Problem:** No trigger phrases, too vague, never loads

✅ **Good:**

```yaml
description: [Specific task] + [Clear triggers] + [Domain context]
```

### Anti-Pattern 3: The Token Bomb

❌ **Bad:**

```markdown
# SKILL.md (25,000 words)
[Everything inline, no references, massive context]
```

**Problem:** Slow to load, wastes tokens, hurts performance

✅ **Good:**

```markdown
# SKILL.md (2,500 words)
[Core workflow + links to references/ for details]
```

### Anti-Pattern 4: The Assumption Trap

❌ **Bad:**

```markdown
## Instructions
Assume the user has already configured MCP.
Assume they know the API structure.
Assume they want the default behavior.
```

**Problem:** Breaks for new users, not portable

✅ **Good:**

```markdown
## Instructions

### Step 1: Verify Prerequisites
IF MCP not connected:
    Guide user: Settings > Extensions > [Service] > Connect
    
### Step 2: Gather Context
Ask user:
- Desired output format?
- Any constraints?

### Step 3: Execute
[Workflow based on actual context, not assumptions]
```
