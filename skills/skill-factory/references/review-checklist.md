# Skill Review Checklist

Comprehensive quality audit checklist based on Anthropic's official guide.

## Phase 1: Structure Validation

### File System

- [ ] Folder name is `kebab-case` (lowercase, hyphens only)
- [ ] Main file is exactly `SKILL.md` (case-sensitive)
- [ ] No `README.md` inside skill folder (only at repo level)
- [ ] Optional folders named correctly: `references/`, `scripts/`, `tests/`

### YAML Frontmatter

- [ ] Frontmatter starts with `---` on its own line
- [ ] Frontmatter ends with `---` on its own line
- [ ] `name` field exists
- [ ] `name` is kebab-case (matches folder name)
- [ ] `description` field exists
- [ ] `description` is 50-1024 characters
- [ ] No XML angle brackets (`<` or `>`) anywhere
- [ ] No reserved names (`claude-*`, `anthropic-*`)

### Optional Metadata

- [ ] `metadata.author` present (recommended)
- [ ] `metadata.version` present (recommended for public skills)
- [ ] `metadata.category` matches one of: document-creation, workflow-automation, mcp-enhancement
- [ ] `metadata.mcp-server` specified if MCP-dependent
- [ ] `compatibility` field lists target surfaces if limited

## Phase 2: Triggering Quality

### Description Field (Most Critical)

**Formula check:**

- [ ] Describes WHAT the skill does (action + domain)
- [ ] Describes WHEN to use it (trigger conditions)
- [ ] Includes 2-3 realistic trigger phrases
- [ ] Uses language users would actually say
- [ ] Mentions relevant file types if applicable
- [ ] Includes negative scope if needed ("NOT for X")

**Trigger language audit:**

- [ ] Contains at least one of: "Use when", "triggers on", "asks to", "says", "mentions"
- [ ] Trigger phrases are specific, not generic
- [ ] Includes paraphrases/synonyms
- [ ] Covers domain-specific jargon if relevant
- [ ] Clear enough that Claude knows when to load it

**Scope audit:**

- [ ] Not too broad (avoid "helps with X" without specifics)
- [ ] Not too narrow (should cover 2-3 related use cases, not just 1)
- [ ] Boundaries clear (what it does AND doesn't do)

**Examples of quality descriptions:**

✅ **Good:**

```yaml
description: Analyzes Figma design files and generates developer handoff 
documentation with component specs, design tokens, and asset exports. 
Use when user uploads .fig files, asks for "design specs", "component 
documentation", "design-to-code handoff", or mentions Figma-to-development 
workflows.
```

✅ **Good (with negative scope):**

```yaml
description: Processes PDF legal documents for contract review, clause 
extraction, and compliance checking. Use for legal PDF analysis ONLY. 
NOT for general document editing (use doc-editor skill) or non-legal 
PDFs (use pdf-tools skill).
```

❌ **Bad (too vague):**

```yaml
description: Helps with projects.
```

❌ **Bad (no triggers):**

```yaml
description: Creates sophisticated multi-page documentation systems.
```

## Phase 3: Instruction Quality

### Structure

- [ ] Has clear section headers (## Instructions, ## Examples, ## Troubleshooting)
- [ ] Steps are numbered or clearly ordered
- [ ] Each step is actionable (tells what to do, not just what happens)
- [ ] Examples include realistic user queries
- [ ] Error handling is explicit

### Content Quality

- [ ] Instructions are specific, not vague
- [ ] Commands/code include concrete examples
- [ ] Expected outputs are described
- [ ] Validation checkpoints between major steps
- [ ] Critical constraints use "DO NOT" language
- [ ] Long details moved to `references/` with links

**Example checks:**

✅ **Specific and actionable:**

```markdown
Run `python scripts/validate.py --input {filename}`.

If validation fails with "Missing required field", common fixes:
- Add 'email' column to CSV (column B)
- Ensure dates use YYYY-MM-DD format
- Remove trailing commas
```

❌ **Vague and generic:**

```markdown
Validate the data before proceeding.
```

### Progressive Disclosure

- [ ] SKILL.md body is <5,000 words
- [ ] API documentation moved to `references/api-patterns.md`
- [ ] Extended examples in `references/examples.md`
- [ ] Troubleshooting in `references/troubleshooting.md`
- [ ] Links to references are clear and specific

## Phase 4: Testing Coverage

### Trigger Tests

- [ ] Test suite exists (`tests/trigger-tests.md` or inline)
- [ ] Includes 5-10 positive trigger cases (should trigger)
- [ ] Includes 5-10 negative cases (should NOT trigger)
- [ ] Includes paraphrase tests
- [ ] Includes edge case tests
- [ ] Target: >90% accuracy on positive cases, <10% false positives

### Functional Tests

- [ ] Happy path test defined (ideal scenario)
- [ ] Error handling test defined (expected failures)
- [ ] Edge case test defined (boundary conditions)
- [ ] Each test has: Given, When, Then structure
- [ ] Success criteria are measurable

### Performance Baseline

- [ ] Baseline measurement exists (without skill)
- [ ] Target metrics defined (with skill)
- [ ] Metrics include: token count, message count, API errors, time
- [ ] Success criteria: ≥50% improvement on at least 2 metrics

## Phase 5: Error Handling

### Coverage

- [ ] Common errors identified and documented
- [ ] Each error has: cause + solution
- [ ] MCP connection issues covered (if applicable)
- [ ] Rate limiting handled (if API-heavy)
- [ ] Invalid input handled
- [ ] Partial failures handled (rollback/cleanup)

### Quality

- [ ] Error messages are specific, not generic
- [ ] Solutions are actionable (steps to fix, not just "try again")
- [ ] Diagnostic steps provided for debugging
- [ ] Fallback options mentioned where applicable

## Phase 6: Security & Safety

### Security Checks

- [ ] No hardcoded credentials or API keys
- [ ] No XML injection vectors (`<` or `>` in frontmatter)
- [ ] No command injection risks in examples
- [ ] No path traversal vulnerabilities in file operations
- [ ] Sensitive data handling documented if applicable

### Safety Checks

- [ ] Destructive operations require confirmation
- [ ] Critical steps have validation gates
- [ ] No "skip validation" shortcuts
- [ ] Compliance requirements documented (if applicable)
- [ ] Audit trail preserved for critical workflows

## Phase 7: Distribution Readiness

### For Public Release

- [ ] `README.md` exists at repo level (not in skill folder)
- [ ] `LICENSE` file present
- [ ] Installation instructions clear
- [ ] Usage examples with screenshots (if applicable)
- [ ] Contributing guidelines (if accepting contributions)
- [ ] Version in metadata
- [ ] GitHub Actions validation workflow (optional but recommended)

### For Team/Internal Use

- [ ] Internal documentation exists
- [ ] Team onboarding guide present
- [ ] Support contact identified
- [ ] Update process documented

## Phase 8: Composability

### Skill Interaction

- [ ] Works standalone (doesn't assume other skills)
- [ ] Doesn't conflict with built-in Claude capabilities
- [ ] Clear boundaries (doesn't overlap with similar skills)
- [ ] Can be used alongside other skills
- [ ] Doesn't try to "do everything"

## Phase 9: Maintenance

### Versioning

- [ ] Version number in metadata
- [ ] Version history documented
- [ ] Breaking changes noted
- [ ] Migration guide for major versions

### Sustainability

- [ ] Skill owner identified
- [ ] Update cadence defined (if applicable)
- [ ] Deprecation path considered
- [ ] Feedback mechanism exists

## Common Issues & Quick Fixes

### Issue: Under-triggering

**Symptom:** Skill doesn't load when it should  
**Fix:** Add more trigger phrases, synonyms, paraphrases to description

### Issue: Over-triggering

**Symptom:** Skill loads on unrelated queries  
**Fix:** Narrow scope, add negative examples ("NOT for X")

### Issue: Inconsistent results

**Symptom:** Same query produces different outputs  
**Fix:** Add validation scripts, explicit checkpoints, "DO NOT skip" language

### Issue: Token bloat

**Symptom:** Skill loads slowly, large context  
**Fix:** Move details to `references/`, keep SKILL.md <5k words

### Issue: Instructions ignored

**Symptom:** Claude doesn't follow steps  
**Fix:** Make deterministic (scripts), put critical steps first, add explicit validation

## Scoring System (Optional)

Rate each phase 0-10:

- Phase 1 (Structure): ___/10
- Phase 2 (Triggering): ___/10  
- Phase 3 (Instructions): ___/10
- Phase 4 (Testing): ___/10
- Phase 5 (Error Handling): ___/10
- Phase 6 (Security): ___/10
- Phase 7 (Distribution): ___/10
- Phase 8 (Composability): ___/10
- Phase 9 (Maintenance): ___/10

**Total: ___/90**

- 80-90: Production-ready
- 70-79: Minor improvements needed
- 60-69: Significant work required
- <60: Major redesign recommended

## Quick Validation Command

```bash
# Run validation script
python scripts/validate_skill.py .

# Check trigger test coverage
grep -c "Should TRIGGER" tests/trigger-tests.md
grep -c "Should NOT trigger" tests/trigger-tests.md

# Check SKILL.md size
wc -w SKILL.md  # Target: <5000 words
```
