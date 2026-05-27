# Test Cases & Validation

Complete test suite template for skill validation.

## Test Suite Structure

Every production-ready skill should have:
1. **Trigger tests** (when to load)
2. **Functional tests** (does it work)
3. **Performance baseline** (is it better than manual)

## Template: Trigger Tests

### Positive Cases (Should TRIGGER)

Test that skill loads when it should.

**Target: >90% trigger rate**

```markdown
## Skill: [skill-name]

### Should TRIGGER - Obvious Phrases
- "[Primary trigger phrase 1]"
- "[Primary trigger phrase 2]"
- "[Primary trigger phrase 3]"

### Should TRIGGER - Paraphrases
- "[Casual variation 1]"
- "[Casual variation 2]"
- "[Slang/shorthand version]"

### Should TRIGGER - With Context
- "[Trigger phrase] for [specific use case]"
- "Can you [trigger phrase] using [tool/technique]"
- "I need to [trigger phrase] because [reason]"

### Should TRIGGER - File Type Mentions (if applicable)
- "Process this .fig file"
- "Analyze this CSV data"
- "Review this PDF contract"
```

### Negative Cases (Should NOT Trigger)

Test that skill doesn't load on unrelated queries.

**Target: <10% false positive rate**

```markdown
### Should NOT Trigger - Unrelated Domain
- "What's the weather in Paris?"
- "Explain quantum physics"
- "Write a poem about coding"

### Should NOT Trigger - Similar But Different
- "[Query that sounds similar but is out of scope]"
- "[Related task that another skill handles]"
- "[Informational query vs. action query]"

### Should NOT Trigger - Edge Cases
- "Tell me about [skill domain]" (informational, not action)
- "What is [tool name]" (education, not execution)
- "History of [technique]" (background, not task)
```

## Example: Trigger Tests for Sprint Planning Skill

```markdown
## Skill: sprint-planning-automation

### Should TRIGGER ✅

**Obvious phrases:**
- "Help me plan this sprint"
- "Create sprint tasks from this backlog"
- "Set up the next sprint"
- "Plan sprint 23"

**Paraphrases:**
- "Let's organize the next iteration"
- "Can you help me with sprint planning?"
- "I need to plan our two-week sprint"
- "Set me up for the upcoming sprint"

**With context:**
- "Plan this sprint using our velocity from last sprint"
- "Create sprint tasks for the design team"
- "Help me plan Q2 sprint 1 with these priorities"

**Tool-specific:**
- "Plan a sprint in Linear"
- "Set up Jira sprint for next week"

### Should NOT Trigger ❌

**Unrelated:**
- "What's the weather today?"
- "Write a Python function"
- "Explain agile methodology" (educational, not action)

**Similar but different:**
- "Show me last sprint's results" (reporting, not planning)
- "Create a roadmap for Q2" (roadmap ≠ sprint)
- "Schedule a sprint planning meeting" (calendar, not task planning)
- "What is sprint planning?" (definition, not execution)

**Edge cases:**
- "Tell me about sprint planning best practices" (informational)
- "History of agile sprints" (education)
- "Compare sprint vs kanban" (comparison)
```

## Template: Functional Tests

### Happy Path Test

```markdown
## Test Case 1: Happy Path

**Test ID:** FUNC-001  
**Category:** Positive  
**Priority:** Critical

**Given:**
- [Initial state/preconditions]
- [Required inputs available]
- [Dependencies working]

**When:**
User says: "[Exact trigger phrase]"

**Then:**
Expected behavior:
1. [ ] [Step 1 completes successfully]
2. [ ] [Step 2 completes successfully]
3. [ ] [Step 3 completes successfully]

Expected output:
- [ ] [Output format correct]
- [ ] [Output content accurate]
- [ ] [Confirmation message shown]

Expected side effects:
- [ ] [Database/API updated correctly]
- [ ] [Files created/modified as expected]
- [ ] [Zero errors in logs]

**Success Criteria:**
- All steps complete in correct order
- Output matches specification
- Zero API/MCP errors
- Execution time <X seconds
```

### Error Handling Test

```markdown
## Test Case 2: Error Handling

**Test ID:** FUNC-002  
**Category:** Negative  
**Priority:** High

**Given:**
- [Preconditions that will cause error]
- [Example: Duplicate resource name exists]

**When:**
User says: "[Trigger phrase]"

**Then:**
Expected behavior:
1. [ ] Skill detects error condition
2. [ ] Skill explains error to user clearly
3. [ ] Skill suggests fix/workaround
4. [ ] Skill does NOT create partial state
5. [ ] Skill does NOT crash/hang

Expected error message:
"[Clear, actionable error message]"

Expected recovery options:
- Option 1: [How to fix]
- Option 2: [Alternative approach]

**Success Criteria:**
- Error detected before causing damage
- User informed with actionable message
- No partial/corrupted state left behind
- Execution fails gracefully
```

### Edge Case Test

```markdown
## Test Case 3: Edge Case

**Test ID:** FUNC-003  
**Category:** Boundary  
**Priority:** Medium

**Given:**
- [Unusual but valid preconditions]
- [Example: Zero items to process]
- [Example: Maximum limit items]

**When:**
User says: "[Trigger phrase]"

**Then:**
Expected behavior:
1. [ ] Skill recognizes edge case
2. [ ] Skill handles gracefully (doesn't fail)
3. [ ] Skill informs user of special handling
4. [ ] Output is valid (even if empty/minimal)

**Success Criteria:**
- No crashes on edge cases
- User informed of unusual situation
- Behavior is logical and consistent
```

## Template: Performance Baseline

```markdown
## Performance Comparison

### Baseline (Without Skill)

**Scenario:** [Describe task]

Measured on: [Date]  
Measured by: [Person]  
Sample size: 5 runs

**Metrics:**
- **User messages:** [Average count]
- **Claude messages:** [Average count]
- **Total messages:** [Average count]
- **Token consumption:** [Average]
- **API/MCP calls:** [Count]
- **Failed API calls:** [Count]
- **Execution time:** [Average minutes]
- **User corrections needed:** [Count]

**Typical conversation flow:**
1. User explains task
2. Claude asks clarifying questions (3-5 rounds)
3. User provides more details
4. Claude attempts execution
5. Errors occur (1-3 retries)
6. User corrects approach
7. Task completes

### Target (With Skill)

**Same scenario:** [Describe task]

Measured on: [Date]  
Sample size: 5 runs

**Metrics:**
- **User messages:** [Average count] ← Target: ≤50% of baseline
- **Claude messages:** [Average count] ← Target: ≤50% of baseline
- **Total messages:** [Average count]
- **Token consumption:** [Average] ← Target: ≤60% of baseline
- **API/MCP calls:** [Count] ← Target: Similar or fewer
- **Failed API calls:** [Count] ← Target: <20% of baseline
- **Execution time:** [Average minutes] ← Target: ≤50% of baseline
- **User corrections needed:** [Count] ← Target: ≤25% of baseline

**Typical conversation flow:**
1. User triggers skill with phrase
2. Skill executes workflow automatically
3. Skill asks 0-2 clarifying questions (if needed)
4. Task completes with minimal user input

### Success Criteria

Skill is successful if it achieves **3 of 5** improvements:
- [ ] ≥50% reduction in total messages
- [ ] ≥40% reduction in token consumption
- [ ] ≥60% reduction in failed API calls
- [ ] ≥50% reduction in execution time
- [ ] ≥75% reduction in user corrections

### Improvement Summary

| Metric | Baseline | With Skill | Change | Target Met? |
|--------|----------|------------|--------|-------------|
| Messages | 15 | 4 | -73% | ✅ Yes |
| Tokens | 12,000 | 6,500 | -46% | ✅ Yes |
| Failed APIs | 3 | 0 | -100% | ✅ Yes |
| Time (min) | 8 | 2 | -75% | ✅ Yes |
| Corrections | 4 | 1 | -75% | ✅ Yes |

**Result:** 5/5 targets met ✅ Skill is production-ready
```

## Real Example: frontend-design Skill

```markdown
## Skill: frontend-design

### Trigger Tests

**Should TRIGGER ✅**
- "Build a landing page for a SaaS product"
- "Create a dashboard component"
- "Design a user profile page"
- "Make a pricing table component"
- "Build a signup form with validation"

**Should NOT Trigger ❌**
- "Explain CSS flexbox" (educational)
- "What is frontend design?" (definition)
- "Review this existing component" (code review ≠ creation)
- "Write a Python API" (backend, not frontend)

### Functional Test: Happy Path

**Given:**
- User has Claude Code or Claude.ai
- No external dependencies required

**When:**
User says: "Build a landing page for a SaaS product"

**Then:**
1. ✅ Skill loads automatically
2. ✅ Asks clarifying questions (target audience, brand vibe, key features)
3. ✅ Generates semantic HTML structure
4. ✅ Creates modern CSS with custom properties
5. ✅ Includes responsive breakpoints
6. ✅ Applies accessibility best practices (ARIA, semantic tags)
7. ✅ Produces production-ready code (no placeholders)
8. ✅ Code is distinctive and high-quality (not generic Bootstrap clone)

**Success Criteria:**
- Generated HTML validates (W3C)
- CSS is modern (no floats, uses Grid/Flexbox)
- Accessible (passes aXe audit)
- Responsive (mobile-first)
- Distinctive design (not generic)

### Performance Baseline

**Without skill:**
- 12 messages back-and-forth
- Generic output with placeholders
- Requires 3-4 rounds of refinement
- ~10,000 tokens
- 6 minutes elapsed

**With skill:**
- 3 messages (trigger + 1 clarification + output)
- Production-ready output
- 1 round of refinement (if any)
- ~5,500 tokens
- 2 minutes elapsed

**Improvement:** -75% messages, -45% tokens, -67% time ✅
```

## How to Run Tests

### Manual Testing (Fastest)

```bash
# 1. Test triggering
# Open Claude Code and try each trigger phrase
# Track: Did skill load? Y/N

# 2. Test non-triggering
# Try negative cases
# Track: Did skill incorrectly load? Y/N

# 3. Test execution
# Run happy path test
# Verify each step completes correctly

# 4. Test error handling
# Simulate error conditions
# Verify graceful failure
```

### Scripted Testing (Recommended for Public Skills)

```python
# tests/run_trigger_tests.py
import subprocess
import json

def test_triggers(skill_name, test_cases):
    results = {"passed": 0, "failed": 0, "tests": []}
    
    for case in test_cases:
        query = case["query"]
        should_trigger = case["should_trigger"]
        
        # Simulate Claude Code environment
        # (In real implementation, use Claude API with skills)
        result = check_if_skill_triggered(skill_name, query)
        
        passed = (result == should_trigger)
        results["passed" if passed else "failed"] += 1
        results["tests"].append({
            "query": query,
            "expected": should_trigger,
            "actual": result,
            "passed": passed
        })
    
    return results

# Load test cases
with open("tests/trigger-tests.json") as f:
    test_cases = json.load(f)

# Run tests
results = test_triggers("sprint-planning-automation", test_cases)

# Report
print(f"Passed: {results['passed']}")
print(f"Failed: {results['failed']}")
print(f"Accuracy: {results['passed'] / len(test_cases) * 100:.1f}%")

# Fail if <90% accuracy
if results['passed'] / len(test_cases) < 0.9:
    exit(1)
```

### CI/CD Integration

```yaml
# .github/workflows/test-skill.yml
name: Test Skill

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Validate structure
        run: python scripts/validate_skill.py .
      
      - name: Run trigger tests
        run: python tests/run_trigger_tests.py
      
      - name: Check coverage
        run: |
          total=$(grep -c "^-" tests/trigger-tests.md)
          if [ "$total" -lt 10 ]; then
            echo "Error: Need at least 10 trigger test cases"
            exit 1
          fi
```

## Test Result Tracking

```markdown
## Test Run: 2026-05-27

**Trigger Tests:**
- Positive cases: 15/15 ✅ (100%)
- Negative cases: 14/15 ✅ (93%) - 1 false positive
- Paraphrase cases: 8/10 ✅ (80%)

**Overall Trigger Accuracy: 90% ✅ PASS**

**Functional Tests:**
- Happy path: ✅ PASS
- Error handling: ✅ PASS
- Edge case (zero items): ✅ PASS
- Edge case (max items): ⚠️  TIMEOUT (needs optimization)

**Performance vs. Baseline:**
- Messages: -65% ✅
- Tokens: -48% ✅
- Failed APIs: -90% ✅
- Time: -55% ✅
- Corrections: -80% ✅

**Result: 5/5 performance targets met**

**Issues Found:**
1. False positive trigger on "sprint retrospective" (should not trigger)
2. Timeout on 1000+ item edge case (needs pagination)

**Action Items:**
1. Add negative scope to description: "NOT for retrospectives"
2. Implement pagination for large datasets
3. Re-test after fixes
```
