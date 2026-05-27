# Trigger Tests for skill-factory

Test suite to validate when skill-factory should and should not load.

**Target Accuracy:** >90% on positive cases, <10% false positives on negative cases

## Test Date: 2026-05-27

## Positive Cases (Should TRIGGER ✅)

### Category: Direct Skill Creation Requests
- [ ] "Build a skill for sprint planning"
- [ ] "Create a Claude skill for Notion workspace setup"
- [ ] "Generate a skill to convert CSV to JSON"
- [ ] "Make a skill for release note generation"
- [ ] "Design a skill for frontend component creation"

### Category: Production-Ready Language
- [ ] "Create a production-ready skill for X"
- [ ] "Build a complete skill package for Y"
- [ ] "Generate a validated skill for Z"
- [ ] "Make a distribution-ready Claude skill"

### Category: Skill Review/Audit
- [ ] "Review this skill for quality"
- [ ] "Audit my skill for best practices"
- [ ] "Check why my skill doesn't trigger"
- [ ] "Validate this SKILL.md"
- [ ] "Improve this skill's trigger phrases"

### Category: Skill Optimization
- [ ] "Optimize this skill for token efficiency"
- [ ] "My skill over-triggers, fix it"
- [ ] "Add test suites to this skill"
- [ ] "Make this skill more reliable"

### Category: Explicit Invocation
- [ ] "Use skill-factory to create a skill"
- [ ] "Run skill-factory on this SKILL.md"
- [ ] "Apply skill-factory to improve this"

### Category: Package/Distribution
- [ ] "Package this skill for GitHub"
- [ ] "Prepare this skill for distribution"
- [ ] "Generate complete skill documentation"
- [ ] "Create a skill with all the files"

### Category: Meta-Skill Language
- [ ] "Build a skill to generate skills" (meta!)
- [ ] "Create a skill that helps make other skills"

### Category: Paraphrases
- [ ] "Help me make a Claude Code skill"
- [ ] "I need to build a skill for my workflow"
- [ ] "Can you create a skill that automates X"
- [ ] "Turn this workflow into a reusable skill"
- [ ] "Make this process into a Claude skill"

### Category: With Context
- [ ] "Build a skill for sprint planning using Linear MCP"
- [ ] "Create a Notion skill that sets up workspaces"
- [ ] "Generate a frontend design skill with templates"

**Total Positive Cases:** 33

## Negative Cases (Should NOT Trigger ❌)

### Category: General Questions
- [ ] "What is a skill?"
- [ ] "Explain how skills work"
- [ ] "Tell me about Claude Code"
- [ ] "What's the difference between a skill and a prompt?"

### Category: Unrelated Tasks
- [ ] "What's the weather in Paris?"
- [ ] "Write a poem about coding"
- [ ] "Summarize this article"
- [ ] "Translate this to French"

### Category: Code Tasks (Not Skill Creation)
- [ ] "Write a Python function"
- [ ] "Debug this JavaScript code"
- [ ] "Create a React component" (actual component, not skill to create components)
- [ ] "Build a web API"
- [ ] "Generate SQL queries"

### Category: Project Management (Not Skill-Related)
- [ ] "Plan this sprint" (action, not skill creation)
- [ ] "Create tasks in Linear" (action)
- [ ] "Set up a Notion workspace" (action, not skill creation)
- [ ] "Review this pull request" (action)

### Category: Documentation (General)
- [ ] "Write documentation for this API"
- [ ] "Create a README for this project"
- [ ] "Generate API docs"
- [ ] "Document this codebase"

### Category: Educational Requests
- [ ] "How do I write good YAML?"
- [ ] "Teach me about progressive disclosure"
- [ ] "What are Anthropic's skill guidelines?"
- [ ] "Explain MCP servers"

### Category: Other Meta Tasks
- [ ] "Create a prompt for X" (use promptor skill instead)
- [ ] "Generate a system prompt" (use promptor)
- [ ] "Build a custom agent" (different from skill)

### Category: Existing Skill Usage (Not Creation)
- [ ] "Use the frontend-design skill" (using, not creating)
- [ ] "Run the skill-creator skill" (using existing skill)
- [ ] "Apply the tdd-hybrid workflow" (using, not creating)

### Category: Edge Cases
- [ ] "skill" (just the word, no context)
- [ ] "factory" (just the word)
- [ ] "meta" (just the word)
- [ ] "I'm working on skills" (informational, not action)
- [ ] "Skills are interesting" (opinion, not action)

**Total Negative Cases:** 30

## Paraphrase Tests (Should TRIGGER ✅)

These test that skill-factory recognizes different ways users might express the same intent:

- [ ] "I want to make a skill for X"
- [ ] "Could you help me build a skill"
- [ ] "Let's create a Claude skill together"
- [ ] "I need to turn this into a skill"
- [ ] "Transform this workflow into a skill"
- [ ] "Package this as a reusable skill"
- [ ] "Make this into something Claude can reuse"
- [ ] "Create an automated skill for this"
- [ ] "Build me a skill that does Y"
- [ ] "Generate a skill from this workflow"

**Total Paraphrase Cases:** 10

## Edge Case Tests

### Ambiguous Cases (Document Expected Behavior)

1. **"Review this skill"**
   - **Context:** User pastes a SKILL.md file
   - **Expected:** TRIGGER (review action)
   - **Actual:** ___

2. **"Build a sprint planning tool"**
   - **Context:** No mention of "skill"
   - **Expected:** MAY TRIGGER (tool ≈ skill)
   - **Actual:** ___

3. **"Create a workflow for X"**
   - **Context:** No explicit "skill" mention
   - **Expected:** MAY NOT TRIGGER (workflow ≠ skill explicitly)
   - **Actual:** ___

4. **"I'm creating skills for my team"**
   - **Context:** Informational statement, not action request
   - **Expected:** NOT TRIGGER
   - **Actual:** ___

5. **"skill-factory this"**
   - **Context:** Using skill name as verb
   - **Expected:** TRIGGER (explicit invocation)
   - **Actual:** ___

## Test Results Template

```markdown
## Test Run: [DATE]

**Tester:** [NAME]
**Environment:** Claude Code / Claude.ai / API
**Skill Version:** v1.0.0

### Positive Cases
- Tested: [X] / 33
- Triggered correctly: [Y] / [X]
- Accuracy: [Y/X * 100]%

### Negative Cases
- Tested: [X] / 30
- Did NOT trigger: [Y] / [X]
- Accuracy: [Y/X * 100]%

### Paraphrase Cases
- Tested: [X] / 10
- Triggered correctly: [Y] / [X]
- Accuracy: [Y/X * 100]%

### Overall Trigger Accuracy
- Total tests: [sum]
- Correct behavior: [sum correct]
- **Accuracy: [%]**

### Issues Found
1. [Issue description]
   - Query: "[exact query]"
   - Expected: TRIGGER / NOT TRIGGER
   - Actual: [what happened]
   - Severity: Critical / High / Medium / Low

### Recommendations
1. [Specific fix to frontmatter description]
2. [Adjust trigger phrases]
3. [Add negative scope]
```

## Example Test Results

```markdown
## Test Run: 2026-05-27

**Tester:** Bertrand Brodeau
**Environment:** Claude Code
**Skill Version:** v1.0.0

### Positive Cases
- Tested: 33 / 33
- Triggered correctly: 31 / 33
- Accuracy: 93.9% ✅

### Negative Cases
- Tested: 30 / 30
- Did NOT trigger: 29 / 30
- False positive: 1 (triggered on "Build a sprint planning tool")
- Accuracy: 96.7% ✅

### Paraphrase Cases
- Tested: 10 / 10
- Triggered correctly: 9 / 10
- Accuracy: 90.0% ✅

### Overall Trigger Accuracy
- Total tests: 73
- Correct behavior: 69
- **Accuracy: 94.5% ✅ PASS**

### Issues Found
1. Under-triggered on "Make a skill that automates X"
   - Query: "Make a skill that automates sprint planning"
   - Expected: TRIGGER
   - Actual: Did not trigger
   - Severity: Medium
   - Fix: Add "automates" to trigger phrases

2. False positive on tool creation
   - Query: "Build a sprint planning tool"
   - Expected: NOT TRIGGER (ambiguous)
   - Actual: Triggered
   - Severity: Low
   - Fix: Accept as edge case (user may mean skill)

### Recommendations
1. Add to description: "automates", "turn into", "package as"
2. Current accuracy (94.5%) exceeds target (90%) ✅
3. No critical changes needed
```

## Continuous Testing

### When to Re-test
- After modifying frontmatter description
- After adding/removing trigger phrases
- Before public release
- After user reports trigger issues
- Quarterly (for maintained skills)

### How to Test Manually
1. Open Claude Code or Claude.ai
2. Clear conversation (fresh context)
3. Try each test case
4. Observe if skill-factory loads in context
5. Record results in template above

### Automated Testing (Future)
```python
# tests/run_trigger_tests.py (future implementation)
import json

test_cases = {
    "positive": [...],
    "negative": [...],
    "paraphrases": [...]
}

for query in test_cases["positive"]:
    triggered = check_if_skill_triggered("skill-factory", query)
    assert triggered, f"Should trigger on: {query}"

for query in test_cases["negative"]:
    triggered = check_if_skill_triggered("skill-factory", query)
    assert not triggered, f"Should NOT trigger on: {query}"
```

## Success Criteria

✅ **Pass:** Trigger accuracy ≥90% overall
⚠️ **Warning:** Trigger accuracy 80-89%
❌ **Fail:** Trigger accuracy <80%

**Current Status:** [To be filled after first test run]
