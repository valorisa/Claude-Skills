---
name: tdd-hybrid
description: Test-driven development combining strict discipline (Iron Law, mandatory verification) with intelligent workflow (planning, vertical slicing, domain awareness). Use when implementing features or fixing bugs with TDD.
---

# Test-Driven Development (Hybrid Edition)

## Overview

**Core principle:** Tests verify behavior through public interfaces, not implementation. If you didn't watch the test fail, you don't know if it tests the right thing.

**Hybrid approach:** Superpowers discipline (Iron Law, Delete means delete) + MattPocock intelligence (Planning, Domain awareness, Vertical slicing).

---

## Scope Triage

Before starting, classify the work:

| Signal | Voie | Pipeline |
|--------|------|----------|
| Bug fix isolé OU fonction simple <20 lignes OU <3 behaviors | **LIGHT** | Skip Planning → Tracer Bullet → Loop |
| Feature ≥3 behaviors OU touche architecture OU nouveau module | **FULL** | Planning → Tracer Bullet → Loop → Refactor avancé |

**LIGHT:** 1 question ("Behaviors à tester ?"), discipline stricte, refactor basique  
**FULL:** Planning complet, domain awareness, deep modules

En cas de doute → LIGHT, puis upgrade to FULL si complexité émerge.

---

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? **Delete it. Start over.**

**No exceptions:**

- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Thinking "skip TDD just this once"? Stop. That's rationalization.

---

## Anti-Pattern: Horizontal Slices

**DO NOT write all tests first, then all implementation.** This is "horizontal slicing" — treating RED as "write all tests" and GREEN as "write all code."

This produces **crap tests:**

- Tests written in bulk test _imagined_ behavior, not _actual_ behavior
- You end up testing the _shape_ of things (data structures, function signatures) rather than user-facing behavior
- Tests become insensitive to real changes

**Correct approach:** Vertical slices via tracer bullets. One test → one implementation → repeat.

```
WRONG (horizontal):
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

RIGHT (vertical):
  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
```

---

## Workflow LIGHT

For bug fixes, simple functions (<20 lines), or <3 behaviors.

### 1. Quick Planning

Ask user: **"Which behaviors should we test?"** (prioritize — can't test everything)

### 2. Tracer Bullet

Write ONE test that confirms ONE thing end-to-end:

```
RED:   Write test for first behavior → test fails
Verify RED (mandatory)
GREEN: Write minimal code to pass → test passes
Verify GREEN (mandatory)
```

### 3. Incremental Loop

For each remaining behavior:

#### RED - Write Failing Test

One minimal test showing what should happen.

<Good>
```typescript
test('retries failed operations 3 times', async () => {
  let attempts = 0;
  const operation = () => {
    attempts++;
    if (attempts < 3) throw new Error('fail');
    return 'success';
  };

  const result = await retryOperation(operation);

  expect(result).toBe('success');
  expect(attempts).toBe(3);
});

```
Clear name, tests real behavior, one thing
</Good>

<Bad>
```typescript
test('retry works', async () => {
  const mock = jest.fn()
    .mockRejectedValueOnce(new Error())
    .mockRejectedValueOnce(new Error())
    .mockResolvedValueOnce('success');
  await retryOperation(mock);
  expect(mock).toHaveBeenCalledTimes(3);
});
```

Vague name, tests mock not code
</Bad>

**Requirements:**

- One behavior
- Clear name
- Real code (no mocks unless unavoidable)

#### Verify RED - MANDATORY

```bash
npm test path/to/test.test.ts
```

Confirm:

- Test fails (not errors)
- Failure message is expected
- Fails because feature missing (not typos)

**Test passes?** You're testing existing behavior. Fix test.

#### GREEN - Minimal Code

Write simplest code to pass the test. Don't add features, refactor other code, or "improve" beyond the test.

<Good>
```typescript
async function retryOperation<T>(fn: () => Promise<T>): Promise<T> {
  for (let i = 0; i < 3; i++) {
    try {
      return await fn();
    } catch (e) {
      if (i === 2) throw e;
    }
  }
  throw new Error('unreachable');
}
```
Just enough to pass
</Good>

<Bad>
```typescript
async function retryOperation<T>(
  fn: () => Promise<T>,
  options?: {
    maxRetries?: number;
    backoff?: 'linear' | 'exponential';
    onRetry?: (attempt: number) => void;
  }
): Promise<T> {
  // YAGNI - over-engineered
}
```
</Bad>

#### Verify GREEN - MANDATORY

```bash
npm test path/to/test.test.ts
```

Confirm:

- Test passes
- Other tests still pass
- Output pristine (no errors, warnings)

**Test fails?** Fix code, not test.

### 4. Refactor (Basique)

After all tests pass:

- [ ] Remove duplication
- [ ] Improve names
- [ ] Run tests after each change

Keep tests green. Don't add behavior. **Never refactor while RED.**

---

## Workflow FULL

For features ≥3 behaviors, architectural changes, or new modules.

### Phase 0: Planning

Before writing any code:

1. **Explore codebase**
   - Read `CONTEXT.md` for domain glossary
   - Read ADRs in area you're touching
   - Understand existing patterns

2. **Confirm with user**
   - [ ] What interface changes are needed?
   - [ ] Which behaviors to test? (prioritize — can't test everything)
   - [ ] Identify opportunities for deep modules (small interface, deep implementation)
   - [ ] List behaviors to test (not implementation steps)
   - [ ] Get user approval on the plan

Ask: **"What should the public interface look like? Which behaviors are most important to test?"**

### Phase 1: Tracer Bullet

Write ONE test that confirms ONE thing end-to-end:

```
RED:   Write test for first behavior → test fails
Verify RED (mandatory)
GREEN: Write minimal code to pass → test passes
Verify GREEN (mandatory)
```

This proves the path works end-to-end.

### Phase 2: Incremental Loop

For each remaining behavior, follow LIGHT workflow (RED → Verify RED → GREEN → Verify GREEN).

### Phase 3: Refactor (Avancé)

After all tests pass, look for refactor candidates:

- [ ] Extract duplication
- [ ] **Deepen modules** — move complexity behind simple interfaces
- [ ] Apply SOLID principles where natural
- [ ] Improve names
- [ ] Consider what new code reveals about existing code
- [ ] Run tests after each refactor step

**Deep modules:** Small interface, deep implementation. Good module has rich functionality accessible through simple API. Bad module exposes complexity.

**Never refactor while RED.** Get to GREEN first.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Tests after achieve same goals" | Tests-after = "what does this do?" Tests-first = "what should this do?" |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "Deleting X hours is wasteful" | Sunk cost fallacy. Keeping unverified code is technical debt. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "Need to explore first" | Fine. Throw away exploration, start with TDD. |
| "Test hard = design unclear" | Listen to test. Hard to test = hard to use. |
| "TDD will slow me down" | TDD faster than debugging. Pragmatic = test-first. |
| "Manual test faster" | Manual doesn't prove edge cases. You'll re-test every change. |
| "Existing code has no tests" | You're improving it. Add tests for existing code. |

---

## Red Flags - STOP and Start Over

If ANY of these present, **delete code and restart with TDD:**

- Code before test
- Test after implementation
- Test passes immediately
- Can't explain why test failed
- Tests added "later"
- Rationalizing "just this once"
- "I already manually tested it"
- "Tests after achieve the same purpose"
- "It's about spirit not ritual"
- "Keep as reference" or "adapt existing code"
- "Already spent X hours, deleting is wasteful"
- "TDD is dogmatic, I'm being pragmatic"
- "This is different because..."

---

## Example: Bug Fix

**Bug:** Empty email accepted

**RED**

```typescript
test('rejects empty email', async () => {
  const result = await submitForm({ email: '' });
  expect(result.error).toBe('Email required');
});
```

**Verify RED**

```bash
$ npm test
FAIL: expected 'Email required', got undefined
```

**GREEN**

```typescript
function submitForm(data: FormData) {
  if (!data.email?.trim()) {
    return { error: 'Email required' };
  }
  // ...
}
```

**Verify GREEN**

```bash
$ npm test
PASS
```

**REFACTOR**
Extract validation for multiple fields if needed.

---

## Verification Checklist

Before marking work complete:

- [ ] Every new function/method has a test
- [ ] Watched each test fail before implementing
- [ ] Each test failed for expected reason (feature missing, not typo)
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
- [ ] Output pristine (no errors, warnings)
- [ ] Tests use real code (mocks only if unavoidable)
- [ ] Edge cases and errors covered
- [ ] **FULL only:** Test names use domain glossary vocabulary (from CONTEXT.md)
- [ ] **FULL only:** Tests respect ADRs in area touched

Can't check all boxes? You skipped TDD. Start over.

---

## Integration with Ecosystem

This skill integrates with:

- `/setup-matt-pocock-skills` — configures CONTEXT.md + ADRs location (required for FULL workflow)
- `/grill-with-docs` — builds domain glossary we use for test names
- `/to-issues` — creates vertical slices we implement with TDD
- `/improve-codebase-architecture` — uses tests as safety net for refactoring
- `/spec-driven` — generates spec before invoking this skill

**Typical workflow:**

```
/spec-driven → /tdd-hybrid → implementation with tests
```

---

## Final Rule

```
Production code → test exists and failed first
Otherwise → not TDD
```

No exceptions without user's explicit permission.
