# Trigger Tests — Token Optimization Skill

## Should TRIGGER (Positive Cases)

### Direct mentions

- "My token costs are too high"
- "How can I reduce token consumption?"
- "Optimize my token usage"
- "Claude Code is expensive"
- "Sessions consuming too many tokens"

### Symptom-based (implicit)

- "Why is my context window growing so fast?"
- "My sessions are becoming slow"
- "Cache keeps invalidating"
- "Agents are using too many tokens"
- "MCP is loading a lot of data"
- "Responses are too verbose"
- "Context management issues"

### Technical queries

- "How do I reduce context bloat?"
- "What's the best context window size?"
- "Should I use context forking?"
- "Cache miss problems"
- "Token optimization strategies"

### Problem reports

- "Session at 500k tokens after 10 interactions"
- "Base session already 20k tokens"
- "Agent consumed 100k tokens for simple task"
- "Git commands dumping too much output"

## Should NOT Trigger (Negative Cases)

### Unrelated optimization

- "Optimize database queries" (use database-optimization skill)
- "Speed up API responses" (use performance-tuning skill)
- "Reduce bundle size" (use build-optimization skill)

### General questions

- "What is Claude Code?"
- "How do I install Claude?"
- "Explain tokens"
- "What's the difference between models?"

### Feature requests

- "Add new MCP integration"
- "Create a custom skill"
- "Build a chatbot"

### Code-related tasks

- "Write a function to optimize sorting"
- "Refactor this code"
- "Debug this error"

## Paraphrase Tests

### Should trigger

- "My Claude sessions cost too much" → SHOULD trigger
- "Context getting bloated" → SHOULD trigger
- "How to make Claude cheaper?" → SHOULD trigger
- "Sessions eating tokens like crazy" → SHOULD trigger
- "Cache problems wasting money" → SHOULD trigger

### Edge cases (may or may not trigger)

- "Claude is slow" → Edge case (could be token-related or not)
- "Need help with settings" → Edge case (depends on which settings)
- "Optimize my workflow" → Edge case (broad scope)

## Real-World Trigger Examples

### Example 1: Developer complaint

**User says:** "Dude, my Claude Code bill is insane this month. 750 bucks. What's going on?"

**Expected:** ✅ TRIGGERS (cost complaint)

### Example 2: Session audit request

**User says:** "Can you check my current session and see why it's already at 50k tokens?"

**Expected:** ✅ TRIGGERS (token consumption audit)

### Example 3: Configuration question

**User says:** "Should I change my context window setting? Current codebase is about 30k LOC."

**Expected:** ✅ TRIGGERS (context window optimization)

### Example 4: Performance issue (ambiguous)

**User says:** "Claude is running really slow today. Takes forever to respond."

**Expected:** ⚠️ MIGHT trigger (could be token-related, but also could be network/server)

**Resolution:** If slow due to token reprocessing → this skill. If slow due to network → different issue.

### Example 5: Unrelated optimization

**User says:** "My React app is slow, can you optimize it?"

**Expected:** ❌ SHOULD NOT trigger (app performance, not Claude token usage)

## Trigger Coverage Target

- Positive cases: >90% trigger rate
- Negative cases: <10% false positive rate
- Paraphrase cases: >80% trigger rate

## Testing Procedure

1. Input each test query into Claude Code
2. Check loaded skills with `/skills` or inspect context
3. Mark whether skill loaded
4. Calculate trigger rate: (triggered / total) × 100%

## Current Validation Status

- [ ] Positive cases tested (0/15)
- [ ] Negative cases tested (0/10)
- [ ] Paraphrase cases tested (0/5)
- [ ] Real-world examples tested (0/5)
- [ ] Trigger rate calculated
- [ ] False positive rate calculated

Target: Complete all tests before skill release.

## Troubleshooting Poor Trigger Rate

### If under-triggering (<90% on positive cases)

**Diagnosis:**

- Review failed trigger queries
- Look for common patterns or synonyms

**Fix:**

- Add missing trigger phrases to description
- Include domain-specific jargon
- Add symptom-based triggers

### If over-triggering (>10% on negative cases)

**Diagnosis:**

- Review false positive queries
- Identify overly broad trigger phrases

**Fix:**

- Add negative scope to description: "NOT for X"
- Narrow trigger phrases to be more specific
- Specify exact use cases only

## Version History

- v1.0.0 (2026-05-28): Initial trigger test suite
