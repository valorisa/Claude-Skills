# Setup Matt Pocock's Skills — A Claude Code Skill

One-time scaffolding that tells the rest of the engineering skills *where things live in this repo* — which issue tracker to use, which triage labels apply, and how domain docs are laid out.

**Run it once per repo. Everything else reads from what it writes.**

---

## The Problem

Skills like `to-issues`, `triage`, `diagnose`, `tdd-hybrid`, and `improve-codebase-architecture` all need to know the same handful of things about a repo: where issues are tracked, what the triage labels are actually called here, and whether domain docs live in one place or several.

Without a shared answer, each skill either guesses, asks the same onboarding questions over and over, or — worse — assumes GitHub and `needs-triage`-style labels when the repo actually uses GitLab and a completely different vocabulary.

This skill answers those questions once, writes the answer down, and every other skill reads it from there.

## How It Works

Run **setup-matt-pocock-skills** and Claude will:

1. **Explore the repo first** — checks `git remote -v`, looks for an existing `CLAUDE.md`/`AGENTS.md`, `CONTEXT.md`/`CONTEXT-MAP.md`, `docs/adr/`, `docs/agents/`, and `.scratch/` — never assumes, always reads what's actually there
2. **Walks you through three decisions, one at a time**, each with a plain-language explainer before the choice:
   - **Issue tracker** — GitHub, GitLab, local markdown under `.scratch/`, or "other" (described in your own words)
   - **Triage label vocabulary** — maps the five canonical roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`) to whatever your repo actually calls them
   - **Domain docs layout** — single `CONTEXT.md` at the root, or a `CONTEXT-MAP.md` pointing at multiple contexts (monorepo)
3. **Shows you a draft** of the `## Agent skills` block and the three `docs/agents/*.md` files before writing anything — you can edit before it commits to disk
4. **Writes the config** — adds (or updates in-place) an `## Agent skills` section in whichever of `CLAUDE.md`/`AGENTS.md` already exists, and creates `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, `docs/agents/domain.md`

This is **not** auto-invoked — it has `disable-model-invocation: true`, meaning Claude will never trigger it on its own just because a conversation looks relevant. You have to run it explicitly.

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/valorisa/Claude-Skills ~/.claude/skills/
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

1. Create folder `~/.claude/skills/setup-matt-pocock-skills/`
2. Drop `SKILL.md` plus the five reference files (`domain.md`, `issue-tracker-github.md`, `issue-tracker-gitlab.md`, `issue-tracker-local.md`, `triage-labels.md`) inside it
3. Restart Claude Code

---

## Use

Run it explicitly — there's no keyword trigger:

```
/setup-matt-pocock-skills
```

Or in chat:

> "Use the setup-matt-pocock-skills skill to configure this repo"

**When to run it:**

- First time setting up a new repository for the engineering skills
- Before the first use of `to-issues`, `to-prd`, `triage`, `diagnose`, `tdd-hybrid`, `improve-codebase-architecture`, or `zoom-out`
- If one of those skills seems to be missing context about the issue tracker, triage labels, or domain docs
- When switching issue trackers (e.g. moving from local markdown to GitHub) or restarting the config from scratch

You won't need to run it again after that — the other skills read `docs/agents/*.md` directly. You can also edit those files by hand later without re-running the setup.

---

## What It Writes

A `## Agent skills` block, added to `CLAUDE.md` if it exists, else `AGENTS.md`, else wherever you choose (it asks — it never picks for you, and never creates one when the other already exists):

```markdown
## Agent skills

### Issue tracker

[one-line summary]. See `docs/agents/issue-tracker.md`.

### Triage labels

[one-line summary]. See `docs/agents/triage-labels.md`.

### Domain docs

[single-context or multi-context]. See `docs/agents/domain.md`.
```

Plus three files under `docs/agents/`:

| File | Content |
|------|---------|
| `issue-tracker.md` | CLI conventions for your tracker — `gh issue ...` for GitHub, `glab issue ...` for GitLab, `.scratch/<feature>/` file layout for local markdown, or your own description for "other" |
| `triage-labels.md` | A table mapping the five canonical roles to your repo's actual label strings |
| `domain.md` | Where `CONTEXT.md`/`CONTEXT-MAP.md` and `docs/adr/` live, and the consumer rules other skills follow when reading them |

If an `## Agent skills` block already exists, it's updated in place — never duplicated, and never overwriting the surrounding sections you wrote yourself.

---

## What Makes It Different

### Reads before it asks

Most setup wizards ask every question regardless of context. This one inspects `git remote -v` first and proposes GitHub or GitLab automatically based on what it finds — you only get asked when the repo doesn't already signal an answer.

### One question at a time

The three decisions (tracker, labels, domain layout) are presented sequentially, each with a short explainer of *why* the engineering skills need that answer — not dumped as a single configuration form.

### Confirm before write

Nothing touches disk until you've seen a draft of the `## Agent skills` block and the three `docs/agents/*.md` files and had a chance to edit them.

### Built for repos that aren't GitHub

GitHub is the default assumption baked into most of these skills, but this one ships first-class support for GitLab (`glab` instead of `gh`, "merge requests" instead of "PRs", "notes" instead of "comments") and local markdown tracking for solo projects with no remote at all.

---

## Example Session

**You:** `/setup-matt-pocock-skills`

**Claude:**

> I checked this repo: `git remote -v` points at `github.com/you/your-project`, there's no `CLAUDE.md` or `AGENTS.md` yet, and no `CONTEXT.md`. Let's set this up in three steps.
>
> **Issue tracker.** This is where `to-issues`, `triage`, and `to-prd` will read from and write to. Since your remote points at GitHub, I'd default to GitHub Issues via the `gh` CLI — want me to use that, or do you track work somewhere else?

**You:** "Yeah, GitHub is fine."

**Claude:**

> **Triage labels.** When `triage` processes an issue, it applies one of five roles: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. By default each role's label string matches its name exactly. Does your repo already use different label names I should map instead?

**You:** "We use `bug:triage` instead of `needs-triage`, rest is fine."

**Claude:**

> **Domain docs.** Some skills read `CONTEXT.md` for your project's domain language and `docs/adr/` for past decisions. Is this a single-context repo (one `CONTEXT.md` at the root), or a monorepo with multiple contexts (a `CONTEXT-MAP.md` pointing at several)?

**You:** "Single context."

**Claude:** *(shows draft of the `## Agent skills` block and the three docs/agents/*.md files, you confirm, it writes them)*

> Done. `CLAUDE.md` now has an `## Agent skills` section, and `docs/agents/issue-tracker.md`, `triage-labels.md`, `domain.md` are in place. `to-issues`, `triage`, `diagnose`, and the others will read from these automatically — you won't need to run this again unless you switch trackers.

---

## Credit

- Methodology: adapted from [Matt Pocock's engineering skills](https://github.com/mattpocock/skills) repo-configuration convention
- Implemented as a Claude Code skill by [@valorisa](https://github.com/valorisa)

---

## License

MIT — do whatever you want with it.
