🇺🇸 [English](README.md) | 🇫🇷 [Français](README.fr.md)

# Skill Factory

**Production-ready meta-skill for creating, validating, and optimizing Claude skills.**

Based on [Anthropic's Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) (February 2026).

## What It Does

Skill Factory transforms workflows, processes, or repeated tasks into reliable, portable Claude skills following official best practices. It handles the complete lifecycle:

**Design** → **Implementation** → **Validation** → **Iteration** → **Distribution**

## Key Features

✅ **Follows Anthropic's Official Patterns**

- 3-level progressive disclosure (frontmatter → SKILL.md → references/)
- Category-based design (Document Creation, Workflow Automation, MCP Enhancement)
- Token-efficient structure (<5,000 words in main file)

✅ **Complete Production Package**

- Optimized YAML frontmatter with trigger phrases
- Structured instructions with validation gates
- Reference files for progressive disclosure
- Validation scripts for consistency
- Test suites (trigger, functional, performance)

✅ **Quality Assurance**

- Automated validation (structure, security, triggers)
- Trigger accuracy testing (>90% target)
- Performance baseline comparison
- Iterative refinement process

✅ **Distribution-Ready**

- GitHub-ready structure
- Installation instructions
- CI/CD workflow templates
- Version management

## When to Use

Use Skill Factory when you need to:

- **Create production-ready skills** with proper structure and validation
- **Audit existing skills** for triggering quality and best practices
- **Generate complete skill packages** ready for distribution
- **Design skills by category**: Document creation, Workflow automation, or MCP enhancement
- **Build test suites** for trigger and functional testing
- **Optimize skill performance** (token efficiency, trigger accuracy)
- **Prepare skills for team deployment** or public release

**Don't use for:**

- Quick prototyping → Use `/skill-creator` instead
- Simple one-off tasks without reuse value
- General coding or documentation tasks

## Complementary to skill-creator

**skill-creator** (existing): Fast prototyping, simple skills, quick iteration  
**skill-factory** (new): Production-ready, tested, validated, distribution-ready

Think of skill-creator as "sketch mode" and skill-factory as "production mode".

## Installation

### For Claude Code

1. Copy the `skill-factory/` folder to your Claude skills directory:

   ```bash
   cp -r skill-factory ~/.claude/skills/
   ```

2. Restart Claude Code or refresh skills.

3. Verify installation:

   ```bash
   ls ~/.claude/skills/skill-factory/
   # Should show: SKILL.md, references/, scripts/, tests/
   ```

### For Claude.ai

1. Zip the `skill-factory/` folder:

   ```bash
   zip -r skill-factory.zip skill-factory/
   ```

2. Upload via Settings > Capabilities > Skills

3. Enable the skill in the skills panel.

## Usage

### Create a New Skill

```
"Use skill-factory to build a skill for sprint planning"
"Create a production-ready skill for Notion workspace setup"
"Build a skill to generate release notes from git commits"
```

Skill Factory will:

1. Classify the use case (Category 1, 2, or 3)
2. Choose the architectural pattern
3. Design optimal frontmatter with trigger phrases
4. Generate complete SKILL.md with instructions
5. Create reference files for progressive disclosure
6. Provide validation script and test suites
7. Package for distribution

### Review an Existing Skill

```
"Review this skill for trigger quality"
"Audit my sprint-planning skill for best practices"
"Check why my skill doesn't trigger reliably"
```

Skill Factory will:

1. Validate structure and security
2. Analyze trigger phrase coverage
3. Check instruction quality
4. Identify token efficiency issues
5. Suggest specific improvements
6. Provide revised version if requested

### Optimize a Skill

```
"My skill over-triggers, fix the description"
"Optimize this skill for token efficiency"
"Add test suites to validate my skill"
```

## File Structure

```
skill-factory/
├── SKILL.md                          # Main skill instructions
├── README.md                         # This file
├── references/                       # Progressive disclosure level 3
│   ├── skill-template.md            # Reusable template
│   ├── review-checklist.md          # Quality audit checklist
│   ├── test-cases.md                # Testing guide & templates
│   ├── design-principles.md         # Anthropic's core patterns
│   ├── troubleshooting.md           # Common issues & solutions
│   └── examples.md                  # Real-world skill examples
├── scripts/                         # Validation & helpers
│   └── validate_skill.py            # Structure validator
└── tests/                           # Test suites (optional)
    ├── trigger-tests.md
    ├── functional-tests.md
    └── performance-baseline.md
```

## Quick Start

### Example 1: Create a Simple Skill

```
User: "Build a skill to convert CSV to JSON"

Skill Factory:
1. "This fits Category 2 (Workflow Automation). 
   What trigger phrases would users say?"

User: "convert CSV", "transform CSV to JSON", "parse CSV"

Skill Factory:
2. [Generates complete skill with]:
   - Frontmatter with trigger phrases
   - Step-by-step workflow
   - Validation gates
   - Error handling
   - Test suite

3. "Here's your complete skill. Run validation:"
   python scripts/validate_skill.py csv-to-json/
```

### Example 2: Review Existing Skill

```
User: "My skill doesn't trigger. Here's the frontmatter:"
---
name: project-helper
description: Helps with projects.
---

Skill Factory:
"❌ Issues found:

1. Description too vague (no trigger phrases)
2. Scope too broad (what kind of projects?)
3. Missing WHEN clause

Suggested fix:
---
name: agile-sprint-planner
description: Automates Agile sprint planning including velocity 
analysis, task creation, and team assignment. Use when user says 
"plan sprint", "sprint planning", "organize iteration", or asks to 
"set up next sprint".
---
```

## Validation

Run the validation script to check skill quality:

```bash
cd your-skill-folder
python ../skill-factory/scripts/validate_skill.py .
```

Expected output:

```
✅ Skill validation PASSED
   ✅ SKILL.md found
   ✅ Frontmatter structure valid
   ✅ Name 'your-skill' is valid kebab-case
   ✅ Description length OK (287 chars)
   ✅ Description includes trigger language
   ✅ Content length reasonable (2,143 words)
   ✅ Uses progressive disclosure (links to references/)
   ✅ Folder name matches skill name
```

## Testing

### Trigger Tests

Test if your skill loads when it should:

```bash
# Positive cases (should trigger)
"Build a skill for sprint planning"  → Should load ✅
"Create a Claude skill"                → Should load ✅

# Negative cases (should NOT trigger)
"What's the weather?"                  → Should NOT load ✅
"Write a Python function"              → Should NOT load ✅
```

**Target: >90% accuracy**

### Functional Tests

Verify the skill produces correct outputs:

```bash
# Happy path
Given: User asks to create skill for X
When: Skill executes workflow
Then: Complete skill package generated
      All validation checks pass
      Test suites created
```

### Performance Tests

Compare with baseline (without skill):

| Metric | Baseline | With Skill | Improvement |
|--------|----------|------------|-------------|
| Messages | 15-20 | 3-5 | -70% ✅ |
| Tokens | 12k-15k | 5k-7k | -55% ✅ |
| Time | 8-12 min | 2-4 min | -70% ✅ |
| Errors | 2-4 | 0-1 | -80% ✅ |

## Examples

See `references/examples.md` for complete real-world examples:

- **Category 1:** frontend-design, docx-creator
- **Category 2:** sprint-planning, release-notes-generator
- **Category 3:** sentry-code-review, notion-workspace-setup

## Troubleshooting

### Skill Factory doesn't trigger

**Issue:** Skill Factory doesn't load when you ask to create a skill

**Fix:** Try more specific phrases:

- "Use skill-factory to create a skill for X"
- "Build a production-ready skill for Y"
- "Generate a complete Claude skill package"

### Created skill doesn't trigger

**Issue:** The skill you created doesn't trigger reliably

**Fix:** Run through Skill Factory's review mode:

```
"Review this skill for trigger quality"
```

Skill Factory will audit trigger phrases and suggest improvements.

### Validation script fails

**Issue:** `python scripts/validate_skill.py .` reports errors

**Common issues:**

1. File not named exactly `SKILL.md` (case-sensitive)
2. Frontmatter missing `---` delimiters
3. Name not kebab-case (use hyphens, not spaces/underscores)

See `references/troubleshooting.md` for detailed solutions.

## Resources

### Included Documentation

- `references/skill-template.md` — Reusable template
- `references/review-checklist.md` — Quality audit guide
- `references/test-cases.md` — Testing templates
- `references/design-principles.md` — Anthropic's patterns
- `references/troubleshooting.md` — Common issues
- `references/examples.md` — Real-world examples

### External Resources

- [Anthropic Skills Guide (PDF)](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) — Official 33-page guide
- [Anthropic Skills Documentation](https://docs.anthropic.com/skills) — API docs
- [Example Skills Repository](https://github.com/anthropics/skills) — Public examples

## Contributing

Found an issue or have a suggestion?

1. Test with validation script first: `python scripts/validate_skill.py .`
2. Check `references/troubleshooting.md` for known issues
3. Open an issue in the repository with:
   - Skill frontmatter
   - Error message or unexpected behavior
   - Steps to reproduce

## License

MIT License

## Author

Bertrand Brodeau ([@valorisa](https://github.com/valorisa))

Based on Anthropic's Complete Guide to Building Skills for Claude (February 2026)

---

## Version History

- **v1.0.0** (2026-05-27)
  - Initial release
  - Full implementation of Anthropic's official patterns
  - All 3 skill categories supported
  - Complete validation and testing suite
  - Production-ready distribution package

---

**Need help?** Open an issue or check the [troubleshooting guide](references/troubleshooting.md).
