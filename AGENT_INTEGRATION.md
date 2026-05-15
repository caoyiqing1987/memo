# 🔌 Integrating memo with AI Agents

memo is designed to work with **any AI agent that can read and write files**. Here's how to connect it with the most popular tools.

## Quick Comparison

| Tool | Setup | Auto-read | Auto-write |
|------|-------|-----------|------------|
| Claude Code | 1 line in CLAUDE.md | ✅ On every session | ⚡ Prompt it once |
| Cursor | 1 line in .cursorrules | ✅ On every session | ⚡ Prompt it once |
| Windsurf | 1 line in .windsurfrules | ✅ On every session | ⚡ Prompt it once |
| ChatGPT / GPTs | Paste INDEX.md manually | 🔄 Per conversation | ✋ Manual |
| Copilot Chat | Instructions | 🔄 Per conversation | ✋ Manual |
| Cline | 1 line in CLAUDE.md | ✅ On every session | ⚡ Prompt it once |

---

## Claude Code

Add this to `CLAUDE.md` in your project root:

```markdown
## Memory System

This project uses `.memo/` for persistent memory.
- At the start of each session, read `.memo/INDEX.md` to see available memory categories.
- If relevant to the task, load the corresponding file(s) from `.memo/entries/`.
- When the user shares new information worth remembering, use `memo add "<summary>"` or write directly to the relevant `.memo/entries/<category>.md` file.
- Run `memo sync` occasionally for maintenance.
```

**That's it.** Claude Code reads CLAUDE.md at startup and follows instructions automatically.

---

## Cursor

Add this to `.cursorrules` in your project root:

```markdown
You have access to a persistent memory system at .memo/

1. Read .memo/INDEX.md at session start
2. Load relevant entries from .memo/entries/ as needed
3. When the user shares important context, save it:
   - Use `memo add "<summary>"` (recommended)
   - Or write directly to the appropriate .memo/entries/<category>.md
```

Cursor applies `.cursorrules` on every new conversation automatically.

---

## Windsurf

Add this to `.windsurfrules` in your project root:

```markdown
This project has a memory system at .memo/.

- Start by reading .memo/INDEX.md
- Load relevant .memo/entries/<category>.md files on demand
- When the user shares information worth keeping, append to the appropriate .memo/entries/ file or run `memo add "<text>"`
```

---

## ChatGPT / GPTs

ChatGPT doesn't auto-read files, but you can use it with memo manually:

**One-time setup:**
1. Open your project
2. Run `memo list` to see all categories
3. Copy the relevant entries and paste into ChatGPT with: "Here's my project memory, read this before we start."

**For GPTs (Custom GPTs):**
Add this to the GPT's Instructions:

> The user may share memory context from their `.memo/` system. When they do, retain key information during this conversation. At the end, remind them to run `memo add "<new information>"` to persist it.

---

## GitHub Copilot Chat

Add to your project's Copilot instructions (`.github/copilot-instructions.md`):

```markdown
This project uses .memo/ for persistent memory.
Reference .memo/INDEX.md and .memo/entries/ for project context.
```

---

## Cline

Add to `CLAUDE.md` (same as Claude Code):

```markdown
## Memory System
This project uses .memo/ for persistent memory.
Read .memo/INDEX.md at startup.
Load relevant entries on demand.
Save new info with `memo add "<text>"`.
```

---

## The Universal Pattern

No matter which agent you use, the protocol is the same:

```
START → Read .memo/INDEX.md
         ↓
TASK  → Load relevant .memo/entries/<category>.md
         ↓
SAVE  → memo add "<new information>"
         ↓
MAINT → memo sync (occasionally)
```

---

## Testing Your Setup

After configuring, try this:

1. `memo add "Test entry: AI agent integration working"`
2. Start a new session with your AI agent
3. Ask: "What do you remember about this project?"
4. If it reads `.memo/` and answers correctly → you're set

---

## Why This Works

memo uses **plain Markdown files**, which every AI agent already knows how to read and write. No API, no plugins, no special SDK. Just a directory convention that any tool can follow.

If your agent can read a file, it can use memo.
