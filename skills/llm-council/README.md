# LLM Council — A Claude Code Skill

Stop trusting Claude's first answer. Run any decision through 5 AI advisors who argue, peer-review each other anonymously, and hand you a verdict you can actually trust.

Based on [Andrej Karpathy's LLM Council](https://x.com/karpathy/status/1962263486196867115) methodology, adapted to run entirely inside Claude Code using sub-agents with different thinking styles.

---

## The Problem

Claude is incredibly agreeable. Ask it "should I launch this product?" and it'll find 5 reasons why you should. Ask "is this product a bad idea?" and it'll find 5 reasons why it is. Same product, different framing, opposite answers.

That's fine for writing emails. It's dangerous for making decisions.

## How It Works

When you say **"council this"**, the skill:

1. **Scans your workspace** for relevant context (CLAUDE.md, memory files, etc.)
2. **Frames your question** into a neutral prompt
3. **Spawns 5 advisors in parallel**, each with a different thinking style:
   - **The Contrarian** — hunts for what will fail
   - **The First Principles Thinker** — asks if you're solving the right problem
   - **The Expansionist** — looks for upside you're missing
   - **The Outsider** — responds with zero context (catches curse of knowledge)
   - **The Executor** — only cares what you do Monday morning
4. **Anonymizes their responses** and runs a peer review — advisors review each other without knowing who said what
5. **Chairman synthesizes** the verdict: where the council agrees, where it clashes, blind spots it caught, a clear recommendation, and one concrete next step
6. **Generates a visual HTML report** + full markdown transcript

All in one session. About 4 minutes.

---

## Install

### Option 1 — Git clone (recommended)

```bash
git clone https://github.com/tenfoldmarc/llm-council-skill ~/.claude/skills/llm-council
```

Then open Claude Code (`claude` in Terminal).

### Option 2 — Manual

1. Create folder `~/.claude/skills/llm-council/`
2. Drop `SKILL.md` inside it
3. Restart Claude Code

---

## Use

Type any of these triggers followed by your question:

- `council this`
- `run the council`
- `pressure-test this`
- `stress-test this`
- `war room this`
- `debate this`

**Example:**

> council this: I'm thinking of pivoting from a $297 course to a $97 live workshop for my audience of non-technical solopreneurs. Is that the right move?

Give it context. The richer the input, the sharper the output.

You'll get:
- A visual HTML report that opens automatically
- A full markdown transcript saved alongside it

---

## When To Use It

**Good council questions:**
- "Should I launch a $97 workshop or a $497 course?"
- "Which of these 3 positioning angles is strongest?"
- "I'm thinking of pivoting from X to Y. Am I crazy?"
- "Here's my landing page copy. What's weak?"
- "Should I hire a VA or build an automation first?"

**Skip the council for:**
- Factual questions with one right answer
- Pure creation tasks ("write me a tweet")
- Summaries or processing tasks
- Validation-seeking when you already know the answer

The council tells you things you don't want to hear. That's the feature, not a bug.

---

## Credit

- Methodology: [Andrej Karpathy's LLM Council](https://x.com/karpathy/status/1962263486196867115)
- Adapted for Claude Code sub-agents by [@olelehmann](https://x.com/olelehmann)
- Published as an installable skill by the community

---

## License

MIT — do whatever you want with it.
