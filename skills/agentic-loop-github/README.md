# agentic-loop-github

Structures iterative GitHub tasks (fixing CI, resolving lint violations, iterating on a PR) as an observe-decide-execute-verify loop with explicit stop conditions and guardrails.

## When to use

Use this skill whenever a task could take more than one attempt to succeed:

- CI is failing and the fix isn't obvious on the first try
- A task says "keep trying until X passes"
- You're about to loop on the same file or branch multiple times

Don't use it for single-shot tasks — one clear edit, one commit, no verification loop needed.

## What it does

The skill structures the loop into six steps (observe → decide → execute → verify → decide next → stop), and adds three guardrails that prevent the two most common failure modes of unsupervised iteration:

1. **Objective vs. subjective verification** — distinguishes criteria the agent can judge alone (CI green, tests passing, lint clean) from criteria it can't (doc quality, tone, roadmap relevance), so it knows when to loop autonomously and when to ask.
2. **Iteration framing** — a max attempt count and stagnation detection, so the loop stops and reports instead of guessing indefinitely.
3. **Rollback** — reverting to a known-good state before retrying, instead of stacking fixes on a broken one.

It also distinguishes task-level memory (what's already been tried in this session) from long-term memory (recurring fixes worth remembering across repos).

See [`SKILL.md`](./SKILL.md) for the full loop specification.

## Example

> "CI markdownlint is failing on this repo, fix it."

- Stop condition: `gh pr checks` passes.
- Loop: read the exact error → fix the specific line → push → re-check CI → if the error changes, retry; if it's identical after 2 attempts, stop and report.

## Status

Validated on a real case (trailing blank line / markdownlint failure) in [`valorisa/Claude-Skills` PR #30](https://github.com/valorisa/Claude-Skills/pull/30) — resolved in a single loop cycle. Guardrails (stagnation detection, rollback) not yet exercised by a real failure; a controlled multi-error test case is planned.

## License

MIT, same as the rest of this repository.
