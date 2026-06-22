# Find Bugs — A Claude Code Skill

Point it at a file, get a numbered list of real bugs with line numbers, impact assessments, and ready-to-apply fixes. Nothing else.

**No refactoring suggestions. No style notes. Just bugs.**

---

## The Problem

Most code review tools mix bugs, warnings, style issues, and performance suggestions into a single undifferentiated list. When everything is flagged, nothing is urgent.

This skill does one thing: finds defects that can cause incorrect behavior — and stops there.

## How It Works

1. **Identifies the target file** — if you don't specify one, it asks before doing anything else
2. **Reads the file** — full content, no sampling
3. **Runs available static analysis tools** via Bash — linter, type-checker, compiler — to collect signals beyond what's visible in the source text alone
4. **Analyzes for seven bug categories:**
   - Logical errors
   - Off-by-one errors
   - Unhandled `null`/`undefined`
   - Race conditions
   - Resource leaks
   - Poor error handling
   - Security vulnerabilities
5. **Presents results as a numbered list** — for each bug:
   - **Line(s):** affected line number(s)
   - **Issue:** clear description of the bug
   - **Impact:** what can go wrong if left unfixed
   - **Proposed fix:** the correction as a diff or snippet
6. **Asks for confirmation** before touching anything — "Do you want me to apply these fixes? (all / some / none)"
7. **Applies only the confirmed fixes** via Edit

If no bugs are found, it says so clearly rather than inventing problems.

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/valorisa/Claude-Skills ~/.claude/skills/
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

1. Create folder `~/.claude/skills/find-bugs/`
2. Drop `SKILL.md` inside it
3. Restart Claude Code

---

## Use

Mention any of these triggers:

- `/find-bugs`
- `find bugs`
- `debug this file`
- `what bugs in`
- `analyze this file for errors`
- `bug hunt`
- `cherche les bugs`
- `quels bugs dans`
- `analyse ce fichier pour les erreurs`

**Example:**

> find bugs in src/auth/token-validator.ts

Find Bugs will:

1. Read `src/auth/token-validator.ts` in full
2. Run the available type-checker and linter on it
3. Analyze for all seven bug categories
4. Return a numbered list — e.g. "1. Line 47: unhandled null on `user.token` — can throw if token is expired. Fix: add null guard before access."
5. Ask which fixes to apply, then apply only the confirmed ones

---

## What It Won't Do

- **No refactoring suggestions** — restructuring code that works is out of scope
- **No style notes** — formatting, naming conventions, and code style are not bugs
- **No performance optimizations** — unless a performance issue directly causes incorrect behavior (e.g. a timeout that causes data loss)
- **No multi-file analysis in one pass** — if you ask for multiple files, it processes them sequentially, asking confirmation for each one before moving to the next
- **No silent edits** — it will never modify a file without asking you first

---

## When To Use It

**Good find-bugs candidates:**

- A file that's behaving unexpectedly and you want a structured second pass
- Pre-PR review of a specific module you've just written
- Auditing an unfamiliar file before making changes to it
- Anything touching authentication, data validation, or resource management

**Skip find-bugs for:**

- Whole-codebase scans — use `diagnose` or a dedicated linter pipeline for that
- Refactoring or cleanup tasks — use `improve-codebase-architecture`
- Writing new code — use `tdd-hybrid` or `spec-driven` instead

---

## What Makes It Different

### One file, full focus

Find Bugs doesn't try to give you a broad project health report. It reads one file completely, runs tooling on it, and produces an exhaustive analysis of that file only. Sequential multi-file processing is supported, but each file gets its own full pass.

### Fixes included, not just findings

Every entry in the results list comes with a proposed fix — a diff or snippet you can apply immediately. You're not handed a problem report and left to figure out the solution yourself.

### Confirmation before any edit

The skill never modifies your code without an explicit "yes". You get to review the full list of proposed fixes before choosing which ones to apply — all, some, or none.

---

## Credit

- Implemented as a Claude Code skill by [@valorisa](https://github.com/valorisa)

---

## License

MIT — do whatever you want with it.
