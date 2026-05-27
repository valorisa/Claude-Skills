---
name: skill-factory
description: Advanced meta-skill for creating, reviewing, validating, and improving Claude skills following Anthropic's official patterns. Use when the user asks to build a production-ready skill, audit skill quality, generate complete skill packages with tests and validation, review skill architecture, or optimize skill triggering. Handles all 3 categories (document creation, workflow automation, MCP enhancement).
metadata:
  author: Bertrand Brodeau (valorisa)
  version: 1.0.0
  category: meta-skill
  based-on: Anthropic Complete Guide to Building Skills (Feb 2026)
compatibility: Claude Code, Claude.ai, Claude API
---

# Skill Factory

Production-grade meta-skill for creating, validating, and optimizing Claude skills following Anthropic's official best practices.

## Purpose

Skill Factory transforms workflows, processes, or repeated tasks into reliable, portable Claude skills. It handles the complete lifecycle: design → implementation → validation → iteration → distribution.

**Complementary to skill-creator:** While skill-creator focuses on rapid prototyping, skill-factory produces production-ready skills with validation, tests, and complete documentation following Anthropic's 3-level progressive disclosure pattern.

## When to use

Use this skill when you need to:

- **Create production-ready skills** with YAML frontmatter, references, and validation
- **Audit existing skills** for triggering quality, scope, and structure
- **Generate complete skill packages** ready for GitHub distribution
- **Design skills by category**: Document creation, Workflow automation, or MCP enhancement
- **Build test suites** for trigger validation and functional testing
- **Optimize skill performance** (under-triggering, over-triggering, token efficiency)
- **Prepare skills for distribution** (team deployment or public release)

**Don't use for:**
- Quick prototyping (use `/skill-creator` instead)
- Simple one-off tasks without reuse value
- General coding or documentation tasks

## Core Workflow

### Phase 0: Discovery & Classification

**First, identify the skill category:**

#### Category 1: Document & Asset Creation
**Signals:** "create X", "generate Y", "build Z artifact"
**Examples:** frontend-design, docx-creator, pptx-builder
**Key pattern:** Embedded style guides, templates, quality checklists, no external tools

#### Category 2: Workflow Automation  
**Signals:** "automate X", "multi-step process", "coordinate Y"
**Examples:** sprint-planning, release-notes, code-review-flow
**Key pattern:** Sequential steps, validation gates, iterative refinement

#### Category 3: MCP Enhancement
**Signals:** "use [Service] MCP", "integrate with X", "enhance Y connector"
**Examples:** sentry-code-review, notion-workspace-setup, linear-sprint-automation
**Key pattern:** Workflow guidance layered on top of MCP tool access

**Ask the user:**
1. What's the end goal? (concrete outcome, not abstract capability)
2. Which category fits best? (show examples if unclear)
3. What are 2-3 realistic trigger phrases?
4. Which tools are involved? (built-in Claude tools or MCP servers)
5. What does success look like? (specific criteria, not vague "works well")

**Red flag:** If the user can't describe 2-3 concrete use cases, **pause and clarify** before proceeding.

### Phase 1: Architecture Design

Based on category, choose the architectural pattern:

#### Pattern 1: Sequential Workflow Orchestration
**Best for:** Category 2 & 3 with clear step order
```
Step 1 → Validation → Step 2 → Validation → Step 3 → Output
```

#### Pattern 2: Multi-MCP Coordination
**Best for:** Category 3 spanning multiple services
```
Phase 1 (MCP A) → Phase 2 (MCP B) → Phase 3 (MCP C) → Notification
```

#### Pattern 3: Iterative Refinement
**Best for:** Category 1 with quality improvement loops
```
Draft → Quality Check → Refine → Re-validate → Finalize
```

#### Pattern 4: Context-Aware Tool Selection
**Best for:** Category 2 with conditional logic
```
Analyze Context → Choose Tool → Execute → Validate
```

#### Pattern 5: Domain-Specific Intelligence
**Best for:** Category 3 with embedded expertise
```
Compliance Check → Business Logic → Execution → Audit Trail
```

**Output a 1-page architecture doc** showing:
- Chosen pattern
- Major phases/steps
- Decision points
- Tool dependencies
- Error handling strategy

### Phase 2: Frontmatter Design (Critical)

The frontmatter is **the most important part** — it controls when Claude loads your skill.

**Required structure:**
```yaml
---
name: your-skill-name
description: [WHAT it does] + [WHEN to use it] + [Key capabilities]
---
```

**Description formula (1-3 sentences, <1024 chars):**
```
[Action verb] + [domain/output] + [techniques/tools]. 
Use when user [trigger phrase 1], [trigger phrase 2], 
or asks to [task 3]. [Optional: negative scope if needed].
```

**Examples of good descriptions:**

✅ **Good (specific, actionable, clear triggers):**
```yaml
description: Analyzes Figma design files and generates developer 
handoff documentation with component specs, design tokens, and asset 
exports. Use when user uploads .fig files, asks for "design specs", 
"component documentation", "design-to-code handoff", or mentions 
Figma-to-development workflows.
```

✅ **Good (includes domain, triggers, and negative scope):**
```yaml
description: End-to-end customer onboarding workflow for PayFlow. 
Handles account creation, payment setup, subscription management, and 
compliance validation. Use when user says "onboard new customer", 
"set up subscription", "create PayFlow account". NOT for existing 
customer support (use customer-support skill instead).
```

❌ **Bad (too vague, no triggers):**
```yaml
description: Helps with projects.
```

❌ **Bad (technical but no user triggers):**
```yaml
description: Implements the Project entity model with hierarchical 
relationships and CRUD operations.
```

**Ask user to validate:**
- Does this description capture the actual task language they'd use?
- Are there paraphrases or synonyms missing?
- Is the scope too broad or too narrow?

**Add optional metadata:**
```yaml
metadata:
  author: Your Name
  version: 1.0.0
  mcp-server: server-name  # If MCP-dependent
  category: [document-creation|workflow-automation|mcp-enhancement]
  requires: [list any system dependencies]
```

### Phase 3: Instruction Writing

**Keep SKILL.md body focused — use progressive disclosure.**

**Standard structure:**
```markdown
# Skill Name

## Instructions

### Step 1: [First Major Step]
Clear, actionable explanation.

Example:
\`\`\`bash
python scripts/validate.py --input data.csv
\`\`\`

Expected output: [describe success criteria]

### Step 2: [Next Step]
[...]

## Examples

### Example 1: [Common scenario]
**User says:** "Set up a new marketing campaign"

**Actions:**
1. Fetch existing campaigns via MCP
2. Validate campaign name is unique
3. Create campaign with provided parameters
4. Return confirmation link

**Expected result:** Campaign ID #1234 created at [URL]

## Troubleshooting

### Error: [Common error message]
**Cause:** [Why it happens]  
**Solution:** [How to fix it]

## References

For detailed API patterns, see `references/api-guide.md`.  
For compliance rules, see `references/compliance-checklist.md`.
```

**Best practices for instructions:**

✅ **Specific and actionable:**
```markdown
Run `python scripts/validate.py --input {filename}` to check format.

If validation fails with "Missing required field", common fixes:
- Add 'email' column to CSV
- Ensure dates use YYYY-MM-DD format
- Check for trailing commas
```

❌ **Vague and generic:**
```markdown
Validate the data before proceeding.
```

✅ **Progressive disclosure:**
```markdown
Before writing queries, consult `references/api-patterns.md` for:
- Rate limiting guidance (section 2.1)
- Pagination best practices (section 3.4)
- Error code reference (appendix A)
```

❌ **Everything inline (bloats context):**
```markdown
[5 pages of API documentation inline in SKILL.md]
```

**Critical rule:** If a section isn't needed to decide whether to trigger the skill or how to execute the core workflow, **move it to `references/`**.

### Phase 4: Reference Files (Progressive Disclosure Level 3)

Create supporting files in `references/` for:

**Typical reference files:**
- `api-patterns.md` — Detailed API usage, pagination, rate limits
- `examples.md` — Extended use cases beyond core examples
- `troubleshooting.md` — Edge cases, error codes, debugging
- `compliance-checklist.md` — Domain-specific rules (legal, security)
- `style-guide.md` — Brand standards, templates, design rules

**Example: `references/troubleshooting.md`**
```markdown
# Troubleshooting

## MCP Connection Issues

### Error: "Connection refused"
**Diagnosis:**
1. Check Settings > Extensions > [Service] shows "Connected"
2. Verify API key is not expired (check console logs)
3. Test MCP directly: "Use [Service] to list my projects"

**If direct MCP call fails:**
- Issue is in MCP configuration, not this skill
- Re-authenticate via Settings > Extensions

### Error: "Rate limit exceeded"
**Cause:** API called >100 times/minute  
**Solution:**
- Add exponential backoff: wait 2^n seconds between retries
- Batch operations where possible
- Check `references/api-patterns.md` section 2.3
```

### Phase 5: Validation & Testing

**Generate 3 test suites:**

#### Test Suite 1: Trigger Tests (Most Critical)

```markdown
# Trigger Tests

## Should TRIGGER (positive cases)
- "Help me set up a new ProjectHub workspace"
- "I need to create a project in ProjectHub"  
- "Initialize ProjectHub for Q4 planning"
- "Build a ProjectHub workspace from this spec"

## Should NOT trigger (negative cases)
- "What's the weather in San Francisco?"
- "Help me write Python code"
- "Create a spreadsheet" (unless ProjectHub handles sheets)
- "Explain how ProjectHub works" (informational, not action)

## Paraphrase tests
- "Set me up with a ProjectHub thing" → SHOULD trigger
- "Can you ProjectHub this for me?" → SHOULD trigger  
- "Make a project space thingy" → Edge case, may not trigger
```

**How to test triggers:**
1. Run each query in Claude Code
2. Check if skill loads (visible in context)
3. Track: triggered / total queries
4. **Target: >90% on positive cases, <10% on negative cases**

#### Test Suite 2: Functional Tests

```markdown
# Functional Tests

## Test Case 1: Happy Path
**Given:** Project name "Q4 Planning", 5 task descriptions  
**When:** User says "Create ProjectHub workspace for Q4 Planning"  
**Then:**
- ✅ Project created with correct name
- ✅ 5 tasks created with descriptions
- ✅ All tasks linked to project
- ✅ Zero API errors
- ✅ Confirmation message with project URL

## Test Case 2: Error Handling
**Given:** Duplicate project name exists  
**When:** User tries to create with same name  
**Then:**
- ✅ Skill detects duplicate via API
- ✅ Asks user: "Project 'Q4 Planning' exists. Use suffix or rename?"
- ✅ Does not create duplicate
- ✅ No partial state left behind

## Test Case 3: Edge Case
**Given:** User provides 0 tasks  
**When:** Skill executes  
**Then:**
- ✅ Creates project
- ✅ Warns: "Project created with no tasks. Add tasks via [command]"
- ✅ Does not fail or hang
```

#### Test Suite 3: Performance Comparison

```markdown
# Performance Baseline

## Without skill (baseline)
- User provides instructions each time
- 15 back-and-forth messages
- 3 failed API calls requiring retry
- ~12,000 tokens consumed
- 4 minutes elapsed time

## With skill (target)
- Automatic workflow execution
- 2 clarifying questions max
- 0 failed API calls (error handling built-in)
- ~6,000 tokens consumed
- 1 minute elapsed time

## Success criteria
- ≥50% reduction in tokens
- ≥50% reduction in messages
- ≥80% reduction in API errors
- ≥60% reduction in time
```

**Create validation script:**

```python
# scripts/validate_skill.py
#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml

def validate_skill(skill_dir: Path) -> list[str]:
    errors = []
    skill_md = skill_dir / "SKILL.md"
    
    # Check file exists
    if not skill_md.exists():
        errors.append("❌ Missing SKILL.md (case-sensitive)")
        return errors
    
    content = skill_md.read_text(encoding="utf-8")
    
    # Check frontmatter
    if not content.startswith("---"):
        errors.append("❌ Missing YAML frontmatter (must start with ---)")
    
    # Extract and parse frontmatter
    try:
        fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            errors.append("❌ Invalid frontmatter structure")
        else:
            fm = yaml.safe_load(fm_match.group(1))
            
            # Check required fields
            if "name" not in fm:
                errors.append("❌ Missing 'name' in frontmatter")
            elif not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", fm["name"]):
                errors.append(f"❌ Invalid name '{fm['name']}' (must be kebab-case)")
            
            if "description" not in fm:
                errors.append("❌ Missing 'description' in frontmatter")
            elif len(fm["description"]) < 50:
                errors.append("⚠️  Description very short (<50 chars)")
            elif len(fm["description"]) > 1024:
                errors.append("❌ Description too long (>1024 chars)")
            
            # Check for trigger language
            desc = fm.get("description", "").lower()
            trigger_words = ["use when", "trigger", "asks to", "says", "mentions"]
            if not any(tw in desc for tw in trigger_words):
                errors.append("⚠️  Description missing trigger phrases")
    
    except yaml.YAMLError as e:
        errors.append(f"❌ Invalid YAML: {e}")
    
    # Security checks
    if "<" in content or ">" in content:
        errors.append("❌ XML angle brackets forbidden in frontmatter")
    
    # Check content length
    if len(content) < 200:
        errors.append("⚠️  SKILL.md suspiciously short (<200 chars)")
    
    # Check folder name matches skill name
    if fm_match and "name" in yaml.safe_load(fm_match.group(1)):
        skill_name = yaml.safe_load(fm_match.group(1))["name"]
        if skill_dir.name != skill_name:
            errors.append(f"⚠️  Folder name '{skill_dir.name}' != skill name '{skill_name}'")
    
    return errors

if __name__ == "__main__":
    skill_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    errors = validate_skill(skill_path)
    
    if errors:
        print(f"\n🔍 Validation results for: {skill_path.name}\n")
        for err in errors:
            print(err)
        print()
        sys.exit(1 if any("❌" in e for e in errors) else 0)
    else:
        print(f"✅ Skill validation passed: {skill_path.name}")
```

### Phase 6: Iteration & Refinement

**Common issues and fixes:**

#### Issue: Under-triggering (skill doesn't load when it should)

**Signals:**
- User says "use skill-name" explicitly
- Skill doesn't appear in loaded skills list
- Manual enabling required

**Fixes:**
1. Add more trigger phrases to description
2. Include synonyms and paraphrases
3. Mention relevant file types (.fig, .csv, etc.)
4. Add domain-specific jargon users actually say

**Example fix:**
```yaml
# Before (under-triggers)
description: Manages project workflows.

# After (better triggering)
description: Manages Linear project workflows including sprint planning, 
task creation, backlog grooming, and status tracking. Use when user 
mentions "sprint", "Linear tasks", "project planning", "create tickets", 
"plan iteration", or asks to "organize the backlog".
```

#### Issue: Over-triggering (skill loads for irrelevant queries)

**Signals:**
- Skill loads on general queries
- User disables skill
- Confusion about purpose

**Fixes:**
1. Add negative scope: "NOT for X, use Y skill instead"
2. Be more specific about domain
3. Narrow the use case to concrete tasks

**Example fix:**
```yaml
# Before (over-triggers)
description: Processes documents.

# After (better scoped)
description: Processes PDF legal documents for contract review, clause 
extraction, and compliance checking. Use for legal PDF analysis ONLY. 
NOT for general document editing (use doc-editor skill) or non-legal 
PDFs (use pdf-tools skill).
```

#### Issue: Inconsistent results

**Signals:**
- Same query produces different outputs
- Steps skipped randomly
- Quality varies

**Fixes:**
1. Move detailed instructions from text to validation scripts
2. Add explicit validation gates between steps
3. Include "DO NOT skip" language for critical steps
4. Add quality checklist that must be satisfied

**Example fix:**
```markdown
## Step 3: Create Tasks

CRITICAL: Do NOT proceed to Step 4 until ALL validations pass.

Validation checklist:
- [ ] Each task has non-empty title
- [ ] Each task has assignee
- [ ] Each task has due date
- [ ] No duplicate task IDs

Run validation: `python scripts/validate_tasks.py`

If validation fails, fix issues and re-run before continuing.
```

### Phase 7: Distribution Package

**Generate complete distribution-ready structure:**

```
skill-name/
├── SKILL.md                          # Main skill (required)
├── README.md                         # For humans browsing repo
├── LICENSE                           # MIT, Apache-2.0, etc.
├── references/                       # Level 3 progressive disclosure
│   ├── api-patterns.md
│   ├── troubleshooting.md
│   ├── examples.md
│   └── style-guide.md
├── scripts/                          # Validation & helpers
│   ├── validate_skill.py
│   └── format_output.py
├── tests/                            # Test suites
│   ├── trigger-tests.md
│   ├── functional-tests.md
│   └── performance-baseline.md
├── templates/                        # If Category 1 (document creation)
│   ├── report-template.md
│   └── presentation-outline.md
└── .github/                          # CI for public release
    └── workflows/
        └── validate-skill.yml
```

**Generate README.md for humans:**
```markdown
# [Skill Name]

[One-line description]

## Installation

### For Claude Code
1. Download this folder
2. Copy to `~/.claude/skills/[skill-name]/`
3. Restart Claude Code

### For Claude.ai
1. Zip this folder
2. Upload via Settings > Capabilities > Skills

### For API
See [Skills API documentation](https://docs.anthropic.com/skills)

## Usage

### Trigger automatically
"[Example trigger phrase 1]"  
"[Example trigger phrase 2]"

### Example workflows
[3-5 concrete examples with screenshots if applicable]

## Testing

Run validation:
\`\`\`bash
python scripts/validate_skill.py .
\`\`\`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

[MIT / Apache-2.0 / etc.]
```

**Generate GitHub Actions workflow (optional):**
```yaml
# .github/workflows/validate-skill.yml
name: Validate Skill

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install pyyaml
      
      - name: Validate skill structure
        run: python scripts/validate_skill.py .
      
      - name: Check trigger tests exist
        run: test -f tests/trigger-tests.md
      
      - name: Check functional tests exist
        run: test -f tests/functional-tests.md
```

## Output Format

When asked to create a skill, output:

1. **Architecture Summary** (1 page)
   - Category & pattern chosen
   - Major phases/steps
   - Tools/dependencies
   - Success criteria

2. **Complete Skill Package**
   - `SKILL.md` with optimized frontmatter
   - `references/` files
   - `scripts/validate_skill.py`
   - Test suites (trigger, functional, performance)

3. **Installation Instructions**
   - How to install locally
   - How to test
   - How to iterate

4. **Next Steps**
   - Test trigger coverage (target: >90%)
   - Run functional tests
   - Measure performance vs. baseline
   - Iterate based on failures

When asked to review a skill, output:

1. **Issues Found**
   - Trigger quality (under/over)
   - Structure issues
   - Security concerns
   - Missing validation

2. **Impact Assessment**
   - Critical (blocks usage)
   - Important (reduces quality)
   - Nice-to-have (polish)

3. **Proposed Fixes**
   - Specific changes to frontmatter
   - Restructuring recommendations
   - New test cases needed

4. **Revised Version** (if requested)

## Quality Checklist

Before delivering a skill, verify:

### Structure
- [ ] Folder name is kebab-case
- [ ] `SKILL.md` is exactly named (case-sensitive)
- [ ] YAML frontmatter has `---` delimiters
- [ ] `name` is kebab-case, matches folder
- [ ] `description` includes WHAT and WHEN
- [ ] No XML angle brackets anywhere

### Content
- [ ] Instructions are actionable and ordered
- [ ] Examples include realistic user queries
- [ ] Error handling is explicit
- [ ] Long details moved to `references/`
- [ ] Critical validations use scripts, not just text

### Testing
- [ ] Trigger tests exist (positive + negative + paraphrases)
- [ ] Functional tests cover happy path + errors + edge cases
- [ ] Performance baseline defined
- [ ] Validation script runs successfully

### Distribution
- [ ] README.md exists (for humans)
- [ ] LICENSE file present
- [ ] Installation instructions clear
- [ ] Version in metadata

### Compatibility
- [ ] Works standalone (composable)
- [ ] No assumptions about other skills
- [ ] Portable across Claude surfaces (where supported)

## Advanced Techniques

### Token Optimization

**Problem:** Large skills consume too much context.

**Solutions:**
1. Keep `SKILL.md` <5,000 words
2. Move API docs to `references/api-patterns.md`
3. Move examples to `references/examples.md`
4. Use scripts for deterministic logic instead of text instructions

### Handling "Model Laziness"

**Problem:** Claude skips critical validation steps.

**Solutions:**
1. Add explicit encouragement:
   ```markdown
   IMPORTANT: Take time to do this thoroughly. 
   Quality matters more than speed. 
   Do NOT skip validation steps.
   ```

2. Make validations programmatic:
   ```markdown
   Run `python scripts/validate.py` and paste output.
   Proceed ONLY if output shows "All checks passed".
   ```

3. Add "DO NOT" statements for critical constraints:
   ```markdown
   DO NOT create duplicate projects.
   DO NOT skip compliance checks.
   DO NOT proceed if validation fails.
   ```

### Multi-MCP Coordination

**Pattern for skills spanning multiple services:**

```markdown
## Phase-Based Execution

### Phase 1: Export (Figma MCP)
1. Validate .fig file exists
2. Export assets to /tmp/assets/
3. Generate manifest.json

**Checkpoint:** Verify manifest has >0 assets before Phase 2.

### Phase 2: Storage (Drive MCP)
1. Create folder: "Design Handoff - [date]"
2. Upload all assets from /tmp/assets/
3. Generate shareable links
4. Store links in handoff_links.json

**Checkpoint:** Verify all assets uploaded (compare count).

### Phase 3: Tasks (Linear MCP)
1. Create parent task: "Design Handoff"
2. Create subtasks per component in manifest
3. Attach asset links to each task
4. Assign to @engineering

**Checkpoint:** Verify task count matches manifest count.

### Phase 4: Notification (Slack MCP)
1. Post to #engineering:
   - Summary of handoff
   - Link to Drive folder
   - Link to Linear parent task
2. Mention @engineering-leads

**Final validation:** Check Slack message posted successfully.
```

### Domain Expertise Embedding

**For Category 3 (MCP Enhancement) with compliance/business rules:**

```markdown
## Compliance Pre-Check (CRITICAL)

Before ANY payment processing:

1. **Sanctions Check**
   - Query sanctions API with customer country
   - If sanctioned: STOP, return "Cannot process"
   
2. **Jurisdiction Validation**
   - Check if payment type allowed in customer region
   - EU: Verify GDPR consent timestamp exists
   - US: Verify state-specific restrictions
   
3. **Risk Assessment**
   - Calculate risk score via risk-engine API
   - If score >7: Flag for manual review
   - If score ≤7: Proceed

4. **Audit Logging**
   - Log all checks with timestamps
   - Store in compliance_log.jsonl
   - Required for audit trail

ONLY after all 4 checks pass: Call payment MCP.
```

## Troubleshooting

### Skill won't upload

**Error:** "Could not find SKILL.md"  
**Fix:** Rename to exactly `SKILL.md` (case-sensitive)

**Error:** "Invalid frontmatter"  
**Fix:** Ensure YAML starts and ends with `---` on separate lines

**Error:** "Invalid skill name"  
**Fix:** Use kebab-case only: `my-skill-name` not `My Skill Name`

### Skill doesn't trigger

**Quick diagnostic:**
1. Ask Claude: "When would you use the [skill-name] skill?"
2. Claude will quote the description back
3. If description doesn't match user's actual language → revise

**Fix process:**
1. Add trigger phrases users actually say
2. Test with paraphrases
3. Iterate description until >90% trigger rate

### Skill triggers too often

**Fix:**
1. Add negative scope: "NOT for X"
2. Be more specific about domain
3. Narrow to concrete tasks only

### Instructions ignored

**Common causes & fixes:**

| Cause | Fix |
|-------|-----|
| Too verbose | Move detail to `references/` |
| Critical steps buried | Put at top, use headers |
| Ambiguous language | Make deterministic, add examples |
| No validation | Add checkpoints with scripts |

## References

For detailed guidance, see:
- `references/skill-template.md` — Reusable template
- `references/review-checklist.md` — Quality audit checklist  
- `references/test-cases.md` — Example test suites
- `references/design-principles.md` — Anthropic's core patterns
- `references/troubleshooting.md` — Common issues & solutions
- `references/examples.md` — Real-world skill examples

## Version History

- v1.0.0 (2026-05-27) — Initial release based on Anthropic Complete Guide
