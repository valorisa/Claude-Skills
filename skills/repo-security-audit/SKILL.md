---
allowed-tools: Bash(gh issue create:*), Bash(gh issue list:*), Bash(gh repo view:*), Bash(gh api:*), Bash(git log:*), Bash(git diff:*), Bash(find:*), Bash(cat:*), Bash(grep:*), Bash(jq:*), Read, Glob, Grep, Agent, WebFetch
description: Use this skill when the user asks to "audit repo", "analyze repository", "find bugs", "find gaps", "review codebase", "check code quality", or wants to analyze a repository for bugs, missing features, test coverage gaps, security issues and create GitHub issues for findings. Performs a deep technical audit and optionally opens GitHub issues for high-priority problems.
version: 1.0.0
---

# Repo Audit

Perform a deep technical audit of a repository: find bugs, gaps, missing tests, security issues, and API design problems. Optionally create GitHub issues for findings.

Make a todo list and track progress through all steps.

---

## Step 0 — Determine target

If the user provided a GitHub URL (e.g. `https://github.com/owner/repo`), extract `owner/repo`.

If the user provided a local path, use that directly.

If neither was provided, use the current working directory as the target.

Ask the user: **"Should I create GitHub issues for high-priority findings?"** before proceeding if not already specified.

---

## Step 1 — Explore repository structure

Read the repository to understand its purpose and architecture:

```bash
gh repo view <owner/repo>
```

Then explore locally (if available) or via GitHub API:

1. Read `README.md` to understand the project's goals and documented features
2. Read `pyproject.toml` / `package.json` / `go.mod` / `Cargo.toml` to identify language, dependencies and version
3. List source files and test files to understand coverage ratio
4. Read the main entry point and core modules

Build a mental model of:
- What the project does
- Tech stack and architecture
- Execution modes or major features
- How tests are organized

---

## Step 2 — Deep code analysis

Systematically read and analyze the source code. For each module, check for:

### Bugs
- Logic errors in conditionals, setters, or property accessors
- Incorrect use of standard library (e.g. `isinstance` with `typing` types instead of `abc`)
- Wrong argument order in function calls
- `sys.modules` or import cache misuse
- Race conditions in threaded/async code
- Off-by-one errors in counters or indices

### Performance Issues
- Busy-wait loops (while loops without sleep/blocking)
- Missing connection pooling or caching
- Redundant re-computation inside loops
- Unbounded memory growth (queues, lists, caches)

### Security Issues
- Dynamic code execution (`exec`, `eval`, `exec_module`) without input validation
- World-readable file/directory creation without permission mode
- Serialization of untrusted data (pickle, JSON from user input)
- Credentials or secrets hardcoded or logged

### API Design Issues
- Return type annotations that don't match actual return values
- Inconsistent method naming or behavior across similar methods
- Methods that silently swallow exceptions during retries
- Missing input validation at public API boundaries
- Unclear or undocumented side effects

### Test Coverage Gaps
- Features documented in README but with no tests
- CLI commands with no integration tests
- Timeout and retry logic with no verification tests
- Platform-specific code paths never exercised

### Documentation Gaps
- Features implemented but not mentioned in README
- Behavior that contradicts documentation
- Missing examples for non-obvious configuration options

---

## Step 3 — Compile findings

Organize findings into four severity tiers:

### Critical (runtime failures, data loss, security)
These break the software or expose serious vulnerabilities. Include:
- File path and line number
- What the bug is
- Why it fails
- Suggested fix (code snippet)

### High Priority (incorrect behavior, performance, API breakage)
These cause incorrect behavior under common use cases or degrade performance significantly.

### Medium Priority (missing features, coverage gaps, bad UX)
These don't break existing functionality but limit reliability or usability.

### Low / Nice-to-have (style, docs, minor improvements)
Small improvements that improve maintainability or developer experience.

---

## Step 4 — Present summary to user

Show a structured report:

```
## Audit Summary — <repo name>

### Critical Bugs (N)
- [file.py:line] Short description

### High Priority (N)
- [file.py:line] Short description

### Medium Priority (N)
- Short description

### Test Coverage Gaps (N)
- Short description

### Security Concerns (N)
- Short description
```

Ask the user: **"Which severity levels should I open GitHub issues for?"**
Default (if not specified): Critical + High Priority only.

---

## Step 5 — Create GitHub issues (if confirmed)

For each finding in the selected severity tiers, create a GitHub issue using:

```bash
gh issue create --repo <owner/repo> \
  --title "<short descriptive title>" \
  --body "<full markdown body>"
```

Each issue body must follow this structure:

```markdown
## Description

<One paragraph explaining the problem clearly.>

## Location

`<file/module>` line ~<N>

## Current Behavior

<Code snippet showing the problematic code>

<Explanation of what it does wrong>

## Expected Behavior

<What it should do instead>

## Suggested Fix

<Code snippet with the fix>

## Impact

<Who is affected and how severely>

## Priority

<Critical / High / Medium>
```

Rules:
- Write all issues **in English**
- One issue per finding (do not bundle unrelated problems)
- Do not mention AI or automated tools in the issue body
- Keep titles under 80 characters, specific and actionable
- Use inline code formatting for file paths and function names

---

## Step 6 — Final report

After creating all issues, show the user a summary table:

| Issue | Title | Severity |
|-------|-------|----------|
| #N    | title | Critical |
| #N    | title | High     |

Then suggest next steps:
- Which critical bugs to fix first
- Whether a 1.0 release is advisable given the findings
- Any architectural changes worth considering
