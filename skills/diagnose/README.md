# Diagnose

Disciplined debugging loop for hard bugs and performance regressions.

## When to use

- Bug reports, test failures, unexpected behavior
- Performance regressions
- Intermittent issues

## Process

1. **Reproduce** — consistent repro steps
2. **Minimise** — smallest example that fails
3. **Hypothesise** — what's wrong and why
4. **Instrument** — add logging/breakpoints
5. **Fix** — minimal change
6. **Regression test** — prevent recurrence

## Key principle

Diagnose before fixing. No guessing, no shotgun debugging.

See [SKILL.md](./SKILL.md) for full loop details.
