# Find Bugs

Analyze a file to detect bugs and propose fixes.

## Trigger

Slash command: `/find-bugs`

Auto-detection: "find bugs", "debug this file", "what bugs in", "analyze this file for errors", "bug hunt", "cherche les bugs", "quels bugs dans", "analyse ce fichier pour les erreurs".

## Process

1. Identify the target file. If the user doesn't specify, ask which file to analyze.
2. Read the file with Read.
3. If relevant, run available static analysis tools (linter, type-checker, compiler) via Bash to collect additional signals.
4. Analyze the code to detect bugs: logical errors, off-by-one, unhandled null/undefined, race conditions, resource leaks, poor error handling, security vulnerabilities.
5. Present results as a numbered list. For each bug:
   - **Line(s)**: affected line number(s)
   - **Issue**: clear description of the bug
   - **Impact**: what can go wrong
   - **Proposed fix**: the correction as a diff or snippet
6. Ask the user: "Do you want me to apply these fixes? (all / some / none)"
7. Apply only the confirmed fixes via Edit.

## Constraints

- Never modify the file without explicit user confirmation.
- Focus on real bugs — no refactoring, no stylistic suggestions, no performance optimizations unless they cause a bug.
- One file at a time. If the user requests multiple files, process sequentially asking confirmation for each.
- If no bugs are found, say so clearly rather than inventing problems.

## Output

A numbered list of bugs with explanation and fix, followed by a proposal to apply the corrections after user agreement.
