# Skill Template

Reference template following Anthropic's official structure.

## Minimal Required Structure

```markdown
---
name: your-skill-name
description: What it does. Use when user asks to [specific phrases].
---

# Skill Name

## Instructions

[Core workflow steps]

## Examples

[Concrete use cases]

## Troubleshooting

[Common errors and fixes]
```

## Complete Production Structure

```markdown
---
name: your-skill-name
description: [WHAT] + [WHEN] + [Key capabilities]. Use when user [trigger 1], [trigger 2], or asks to [task 3]. [Optional: NOT for X].
metadata:
  author: Your Name
  version: 1.0.0
  category: [document-creation|workflow-automation|mcp-enhancement]
  mcp-server: server-name  # If MCP-dependent
compatibility: Claude Code, Claude.ai, Claude API
---

# Skill Name

[One-line purpose statement]

## Purpose

[What problem this solves, what value it provides]

## When to use

Use this skill when you need to:
- [Concrete task 1]
- [Concrete task 2]
- [Concrete task 3]

**Don't use for:**
- [Out of scope task 1]
- [Out of scope task 2]

## Instructions

### Step 1: [First Major Step]

Clear, actionable explanation of what happens.

Example:
\`\`\`bash
python scripts/validate.py --input data.csv
\`\`\`

Expected output: [Describe what success looks like]

**Validation checkpoint:**
- [ ] Criterion 1 met
- [ ] Criterion 2 met

### Step 2: [Second Major Step]

[...]

## Examples

### Example 1: [Common scenario name]

**User says:** "[Realistic trigger phrase]"

**Actions:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected result:** [Specific output or state]

### Example 2: [Edge case]

**User says:** "[Another phrase]"

**Actions:**
[...]

## Error Handling

### Error: [Specific error message]

**Cause:** [Why this happens]

**Solution:**
1. [Fix step 1]
2. [Fix step 2]
3. [Verification]

### Error: [Another error]

[...]

## Quality Checklist

Before marking complete:
- [ ] [Quality criterion 1]
- [ ] [Quality criterion 2]
- [ ] [Quality criterion 3]

## References

For detailed guidance, see:
- `references/api-patterns.md` — API usage details
- `references/examples.md` — Extended examples
- `references/troubleshooting.md` — Advanced debugging

## Performance Notes

[Optional section for token optimization, speed tips]

## Version History

- v1.0.0 (YYYY-MM-DD) — Initial release
```

## Description Formula

**Template:**
```
[Action verb] + [domain/output] + [techniques/tools]. 
Use when user [trigger phrase 1], [trigger phrase 2], 
or asks to [task 3]. [Optional negative scope].
```

**Examples:**

✅ **Category 1 (Document Creation):**
```yaml
description: Creates production-grade frontend interfaces with 
distinctive design, semantic HTML, modern CSS, and accessibility 
best practices. Use when user asks to "build a component", "create 
a page", "design an interface", or uploads design mockups.
```

✅ **Category 2 (Workflow Automation):**
```yaml
description: Automates sprint planning workflow including velocity 
analysis, task creation, estimation, and team assignment. Use when 
user mentions "sprint planning", "plan iteration", "create sprint", 
or asks to "organize the backlog for next sprint".
```

✅ **Category 3 (MCP Enhancement):**
```yaml
description: Manages Notion workspaces including page creation, 
database setup, template application, and permission configuration 
via Notion MCP. Use when user asks to "set up Notion workspace", 
"create Notion project", or "initialize Notion database". Requires 
Notion MCP connection.
```

## Common Mistakes to Avoid

❌ **Too vague:**
```yaml
description: Helps with projects.
```

❌ **Missing triggers:**
```yaml
description: Creates sophisticated multi-page documentation systems 
with advanced navigation.
```
*(No mention of what user would say)*

❌ **Too technical, no user language:**
```yaml
description: Implements the Project entity model with hierarchical 
relationships and CRUD operations via GraphQL mutations.
```

❌ **Over-broad scope:**
```yaml
description: Does anything related to data analysis, visualization, 
reporting, or data science.
```
