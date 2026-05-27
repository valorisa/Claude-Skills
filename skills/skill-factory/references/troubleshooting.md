# Troubleshooting Guide

Common issues when building and deploying Claude skills, with solutions.

## Category 1: Structure & Upload Issues

### Issue: "Could not find SKILL.md in uploaded folder"

**Symptom:** Skill won't upload to Claude.ai or Claude Code rejects it

**Causes:**
1. File not named exactly `SKILL.md` (case-sensitive)
2. File is in a subdirectory instead of skill root
3. Folder structure incorrect

**Solution:**
```bash
# Check filename (must be exact)
ls -la | grep SKILL.md  # Should show: SKILL.md

# Common mistakes:
# ❌ skill.md
# ❌ SKILL.MD
# ❌ Skill.md
# ✅ SKILL.md

# Verify folder structure
tree my-skill/
# ✅ Correct:
# my-skill/
# ├── SKILL.md          ← At root
# ├── references/
# └── scripts/

# ❌ Wrong:
# my-skill/
# └── docs/
#     └── SKILL.md      ← Too deep
```

**Fix:**
```bash
# Rename if wrong case
mv skill.md SKILL.md

# Move if in wrong location
mv docs/SKILL.md ./SKILL.md
```

### Issue: "Invalid frontmatter"

**Symptom:** Upload fails with YAML parsing error

**Causes:**
1. Missing `---` delimiters
2. Unclosed quotes
3. Invalid YAML syntax
4. Special characters not escaped

**Solution:**
```yaml
# ❌ Wrong: Missing delimiters
name: my-skill
description: Does things

# ❌ Wrong: Unclosed quote
---
name: my-skill
description: "Does things
---

# ❌ Wrong: Special characters
---
name: my-skill
description: Uses <tools> and {variables}
---

# ✅ Correct:
---
name: my-skill
description: Does things with proper YAML
---
```

**Debug steps:**
1. Validate YAML online: https://www.yamllint.com/
2. Check for unclosed quotes
3. Ensure `---` on its own line at start and end
4. Run validation script: `python scripts/validate_skill.py .`

### Issue: "Invalid skill name"

**Symptom:** Name rejected during upload

**Causes:**
1. Name has spaces
2. Name has capitals
3. Name has underscores
4. Name starts with reserved prefix (`claude-`, `anthropic-`)

**Solution:**
```yaml
# ❌ Wrong formats:
name: My Cool Skill          # Spaces, capitals
name: my_cool_skill          # Underscores
name: MyCoolSkill            # CamelCase
name: claude-my-skill        # Reserved prefix

# ✅ Correct:
name: my-cool-skill          # Kebab-case only
```

**Fix:**
```bash
# Convert to kebab-case
# "My Cool Skill" → "my-cool-skill"
# "my_cool_skill" → "my-cool-skill"
# "MyCoolSkill" → "my-cool-skill"
```

### Issue: Folder name doesn't match skill name

**Symptom:** Warning during validation, potential confusion

**Causes:**
- Folder named differently than `name` in frontmatter

**Solution:**
```bash
# ❌ Mismatch:
# Folder: sprint-planning/
# Frontmatter: name: sprint-planner

# ✅ Match:
# Folder: sprint-planning/
# Frontmatter: name: sprint-planning
```

**Fix:**
```bash
# Rename folder to match frontmatter
mv sprint-planner/ sprint-planning/

# Or update frontmatter to match folder
# Edit SKILL.md: name: sprint-planning
```

## Category 2: Triggering Issues

### Issue: Skill doesn't trigger when it should (under-triggering)

**Symptom:**
- User says trigger phrase, skill doesn't load
- Must manually enable skill
- Skill appears irrelevant to Claude

**Causes:**
1. Description too vague
2. Missing trigger phrases
3. No mention of specific tasks/file types

**Diagnosis:**
```bash
# Ask Claude: "When would you use the [skill-name] skill?"
# Claude will quote the description back
# If description doesn't match user's actual language → bad trigger
```

**Solution:**

❌ **Before (vague):**
```yaml
description: Helps with projects.
```

✅ **After (specific):**
```yaml
description: Manages Linear project workflows including sprint planning, 
task creation, backlog grooming, and status tracking. Use when user 
mentions "sprint", "Linear tasks", "project planning", "create tickets", 
"plan iteration", or asks to "organize the backlog".
```

**Fix process:**
1. List 10 realistic phrases users would actually say
2. Add top 5-7 to description
3. Test each phrase
4. Iterate until >90% trigger rate

**Advanced fix:**
```yaml
# Add file type triggers if applicable
description: ... Use when user uploads .fig files, mentions "Figma", 
or asks for "design handoff documentation".

# Add domain jargon
description: ... Use for "velocity analysis", "story points", "sprint 
capacity", "backlog refinement".

# Add paraphrases
description: ... Use when user says "plan sprint", "organize iteration", 
"set up next cycle", or "prep the two-week sprint".
```

### Issue: Skill triggers when it shouldn't (over-triggering)

**Symptom:**
- Skill loads on unrelated queries
- Users disable skill due to noise
- Confusion about skill purpose

**Causes:**
1. Description too broad
2. No negative scope
3. Generic trigger words

**Diagnosis:**
```bash
# Test negative cases
# Try: "What's the weather?" "Write a poem" "Explain X"
# If skill triggers on these → over-triggering problem
```

**Solution:**

❌ **Before (too broad):**
```yaml
description: Processes documents.
```

✅ **After (scoped with negatives):**
```yaml
description: Processes PDF legal documents for contract review, clause 
extraction, and compliance checking. Use for legal PDF analysis ONLY. 
NOT for general document editing (use doc-editor skill) or non-legal 
PDFs (use pdf-tools skill).
```

**Fix techniques:**

**1. Add negative scope:**
```yaml
description: ... Use for sprint planning. NOT for retrospectives 
(use sprint-retro skill) or daily standups (use standup-assistant).
```

**2. Be more specific about domain:**
```yaml
# ❌ Too broad:
description: Manages projects.

# ✅ Specific:
description: Manages Linear software development projects for Agile teams.
```

**3. Narrow to concrete tasks:**
```yaml
# ❌ Abstract:
description: Helps with planning.

# ✅ Concrete:
description: Creates sprint task lists with estimates and assignments.
```

### Issue: Skill triggers on paraphrases inconsistently

**Symptom:**
- Works for "plan sprint" but not "organize iteration"
- Requires exact wording

**Solution:**
Add synonym coverage to description:

```yaml
description: ... Use when user says "plan sprint", "organize iteration", 
"set up next cycle", "prep the sprint", "sprint planning", "iteration 
planning", or asks to "get ready for next sprint".
```

**Paraphrase discovery process:**
1. Ask 5 people how they'd describe the task
2. Document all variations
3. Add top 7 to description
4. Test with team members
5. Iterate based on real usage

## Category 3: Execution Issues

### Issue: Instructions ignored or skipped

**Symptom:**
- Claude doesn't follow steps
- Critical validations skipped
- Inconsistent results

**Causes:**
1. Instructions too verbose (buried in text)
2. Ambiguous language
3. Critical steps not emphasized
4. No enforcement mechanism

**Solution:**

❌ **Before (vague, easy to skip):**
```markdown
Make sure to validate things properly before continuing.
```

✅ **After (specific, emphatic):**
```markdown
## Step 3: Validation (CRITICAL)

⛔ DO NOT proceed to Step 4 until ALL checks pass:

Run validation:
\`\`\`bash
python scripts/validate.py --input data.csv
\`\`\`

Required output: "All checks passed ✅"

If validation fails:
1. Read error output
2. Fix issues in data
3. Re-run validation
4. REPEAT until passed

ONLY after seeing "All checks passed" → Continue to Step 4.
```

**Advanced techniques:**

**1. Use scripts for critical logic:**
```markdown
# Instead of:
"Check that dates are valid"

# Use:
Run `python scripts/validate_dates.py`
Proceed ONLY if exit code is 0.
```

**2. Add explicit "DO NOT" statements:**
```markdown
DO NOT skip the compliance check.
DO NOT create duplicate resources.
DO NOT proceed if API returns error.
```

**3. Add "model encouragement":**
```markdown
IMPORTANT: Take time to do this thoroughly.
Quality is more important than speed.
Do not skip validation steps to save time.
```

**4. Put critical steps first:**
```markdown
# ❌ Critical step buried at end:
## Step 1: Fetch data
## Step 2: Process
## Step 3: Format
## Step 10: Validate (CRITICAL)  ← Too late!

# ✅ Critical step up front:
## Step 1: Validate Input (CRITICAL)
## Step 2: Fetch data
## Step 3: Process
```

### Issue: Inconsistent results across runs

**Symptom:**
- Same query produces different outputs
- Quality varies unpredictably
- Sometimes works, sometimes doesn't

**Causes:**
1. Non-deterministic instructions (too much interpretation)
2. No quality gates
3. Missing validation
4. Heuristic logic where deterministic is needed

**Solution:**

**1. Add explicit quality checklist:**
```markdown
## Quality Gate

Before delivering output, verify ALL criteria:
- [ ] Meets functional requirements (all features present)
- [ ] Passes validation script: `python scripts/validate.py`
- [ ] Matches style guide: `references/style-guide.md`
- [ ] No errors in console/logs
- [ ] Output is complete (no placeholders)

Deliver ONLY if all 5 checks passed.
```

**2. Use deterministic validation:**
```markdown
# Instead of:
"Make sure the output looks good"

# Use:
Run quality checks:
\`\`\`bash
npm run test         # Must pass
npm run lint         # Must pass: 0 errors
python validate.py   # Must output "PASS"
\`\`\`
```

**3. Add iteration bounds:**
```markdown
## Refinement Loop

FOR each issue (max 3 iterations):
1. Fix issue
2. Re-validate
3. If all checks pass → STOP
4. If 3 iterations done → STOP (prevent infinite loops)

Deliver best version after loop completes.
```

### Issue: API/MCP calls fail

**Symptom:**
- "Connection refused"
- "Rate limit exceeded"
- "Authentication failed"

**Diagnosis:**

**1. Check MCP connection:**
```markdown
# In Claude.ai or Claude Code:
Settings > Extensions > [Service Name]
Status should show: "Connected ✅"
```

**2. Test MCP directly (bypass skill):**
```markdown
# Ask Claude:
"Use [Service] MCP to list my projects"

# If this fails → MCP issue, not skill issue
# If this works → skill configuration issue
```

**Solutions by error:**

**Error: "Connection refused"**
```markdown
**Cause:** MCP server not running or not authenticated

**Fix:**
1. Check Settings > Extensions > [Service]
2. If "Disconnected": Click "Connect"
3. Re-authenticate if needed
4. Verify API key is not expired
5. Test direct MCP call to confirm
```

**Error: "Rate limit exceeded"**
```markdown
**Cause:** API called too frequently

**Fix:**
Add rate limiting to skill:

\`\`\`python
import time

def call_api_with_backoff(api_func, max_retries=5):
    for attempt in range(max_retries):
        try:
            return api_func()
        except RateLimitError:
            wait_time = 2 ** attempt  # Exponential backoff
            print(f"Rate limited. Waiting {wait_time}s...")
            time.sleep(wait_time)
    raise Exception("Max retries exceeded")
\`\`\`

See `references/api-patterns.md` section 2.3 for details.
```

**Error: "Authentication failed"**
```markdown
**Cause:** API token expired or invalid

**Fix:**
1. Regenerate API token in service dashboard
2. Update in Settings > Extensions > [Service] > Reconnect
3. Verify token has required scopes/permissions
```

### Issue: Skill produces partial results then stops

**Symptom:**
- Workflow starts correctly
- Stops midway without explanation
- Some outputs created, others missing

**Causes:**
1. Error occurred but not handled
2. Validation failed silently
3. Resource limit hit (tokens, time, API quota)

**Diagnosis:**
```bash
# Check for errors in logs
# Claude Code: View > Output > Claude Code Extension
# Look for: API errors, timeouts, rate limits

# Check token usage
# If context is full → skill may have truncated
```

**Solutions:**

**1. Add checkpoints:**
```markdown
## Workflow with Checkpoints

### Phase 1: Setup
[Actions...]
✅ Checkpoint: Verify setup complete before Phase 2

### Phase 2: Execution
[Actions...]
✅ Checkpoint: Verify execution successful before Phase 3

### Phase 3: Finalization
[Actions...]
✅ Checkpoint: Verify all outputs created

If ANY checkpoint fails:
- Report which phase failed
- Explain what went wrong
- Do NOT continue to next phase
```

**2. Add explicit error handling:**
```markdown
## Step 2: Create Resources

FOR EACH resource in list:
    TRY:
        Create resource
    EXCEPT error:
        Log error: "Failed to create {resource}: {error}"
        Add to failed_resources list
        CONTINUE (don't stop entire workflow)

After loop:
    IF failed_resources is not empty:
        Report: "Created X of Y resources. Failed: {failed_resources}"
    ELSE:
        Report: "All resources created successfully"
```

## Category 4: Performance Issues

### Issue: Skill loads slowly

**Symptom:**
- Long delay after trigger
- High token consumption
- Slow responses

**Causes:**
1. SKILL.md too large (>5,000 words)
2. Too many references loaded inline
3. Verbose examples

**Diagnosis:**
```bash
# Check SKILL.md size
wc -w SKILL.md
# Target: <5,000 words
# Warning: >5,000 words
# Critical: >10,000 words

# Check token estimate (rough)
# ~1 token per 4 characters
wc -c SKILL.md  # Characters
# Divide by 4 for token estimate
```

**Solution:**

**1. Move content to references:**
```markdown
# Before (10,000 words in SKILL.md):
## API Documentation
[5,000 words of API details]

## Examples
[3,000 words of examples]

## Troubleshooting
[2,000 words of debugging]

# After (2,000 words in SKILL.md):
## API Usage
See `references/api-patterns.md` for:
- Rate limiting (section 2.1)
- Authentication (section 2.2)
- Error codes (appendix A)

## Examples
Quick example: [200 words]

For extended examples, see `references/examples.md`:
- Basic usage (examples 1-5)
- Advanced patterns (examples 6-10)

## Troubleshooting
Common issues:
- Issue 1: [50 words + link to references/troubleshooting.md]
- Issue 2: [50 words + link]
```

**Token reduction:** ~8,000 tokens → ~2,000 tokens ✅

**2. Compress verbose instructions:**
```markdown
# Before (verbose):
First, you need to make sure that you have properly configured 
the environment by checking that all the necessary dependencies 
are installed and that the configuration files are in the correct 
locations with the proper permissions set...

# After (concise):
Prerequisites:
- Dependencies installed: `requirements.txt`
- Config at: `~/.config/app/config.yml`
- Permissions: `chmod 600 config.yml`
```

### Issue: Too many skills enabled (context saturation)

**Symptom:**
- Slow overall performance
- Skills not triggering reliably
- Responses less coherent

**Cause:**
- Too many skills loaded simultaneously (>20-50)
- All frontmatter in system prompt

**Solution:**

**1. Audit enabled skills:**
```bash
# Claude Code:
# Settings > Skills > View enabled

# Count enabled skills
# If >50 → consider disabling rarely-used skills
```

**2. Organize by use case:**
```markdown
# Instead of enabling ALL skills:
# Enable skill "packs" based on current work

## Pack 1: Frontend Development
- frontend-design
- react-component-builder
- css-utilities

## Pack 2: Project Management
- sprint-planning
- task-creator
- sprint-retro

## Pack 3: Data Analysis
- csv-processor
- data-viz
- statistical-analysis

Enable only the pack you're currently using.
```

**3. Remove duplicate/overlapping skills:**
```markdown
# Audit for overlap:
# Do you have 3 different "project management" skills?
# → Consolidate into 1 comprehensive skill
# → Or clearly differentiate their scopes
```

## Category 5: Distribution Issues

### Issue: README.md inside skill folder causes confusion

**Symptom:**
- Users expect README.md to be documentation
- Skill structure unclear

**Solution:**
```bash
# ❌ Wrong:
my-skill/
├── SKILL.md
└── README.md        ← Don't put README in skill folder

# ✅ Correct (for public release):
my-skill-repo/       ← GitHub repo root
├── README.md        ← Documentation for humans
├── LICENSE
└── skills/
    └── my-skill/
        ├── SKILL.md ← Actual skill
        ├── references/
        └── scripts/
```

### Issue: Skill works locally but not when shared

**Causes:**
1. Hardcoded paths (e.g., `/Users/yourname/...`)
2. Missing dependencies
3. Environment-specific assumptions

**Solution:**

**1. Use relative paths:**
```markdown
# ❌ Hardcoded:
Read file at: /Users/myname/Documents/template.md

# ✅ Relative:
Read file at: references/template.md
```

**2. Document dependencies:**
```yaml
---
name: my-skill
description: ...
compatibility: Claude Code, API
metadata:
  requires:
    - Python 3.8+
    - npm 8.0+
    - Docker CLI
---
```

**3. Test in clean environment:**
```bash
# Before distributing:
# 1. Copy skill to /tmp/test-skill/
# 2. Remove all local configs
# 3. Test from clean state
# 4. Document any required setup
```

## Debugging Checklist

When a skill isn't working, check in this order:

### 1. Structure (30 seconds)
- [ ] File named exactly `SKILL.md`?
- [ ] Frontmatter has `---` delimiters?
- [ ] Name is kebab-case?
- [ ] Folder name matches skill name?

### 2. Triggering (2 minutes)
- [ ] Description includes trigger phrases?
- [ ] Trigger phrases are specific, not generic?
- [ ] Test with 5 positive cases → >90% trigger?
- [ ] Test with 5 negative cases → <10% trigger?

### 3. Execution (5 minutes)
- [ ] Instructions are actionable?
- [ ] Critical steps emphasized?
- [ ] Validation gates present?
- [ ] Error handling explicit?

### 4. Performance (2 minutes)
- [ ] SKILL.md <5,000 words?
- [ ] Details moved to references/?
- [ ] No token bloat?

### 5. External (if using MCP/APIs)
- [ ] MCP connection working?
- [ ] Test MCP directly (bypass skill)?
- [ ] API rate limits respected?
- [ ] Authentication valid?

Run validation script:
```bash
python scripts/validate_skill.py .
```

If all checks pass but skill still doesn't work:
1. Create minimal test case
2. Share in Claude Developers Discord
3. Include: skill frontmatter + minimal SKILL.md + test query
