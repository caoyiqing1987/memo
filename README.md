<p align="center">
  <img src="https://img.shields.io/badge/AI-Agent%20Memory-blue?style=flat-square" alt="AI Agent Memory">
  <img src="https://img.shields.io/badge/Claude%20Code-ready-green?style=flat-square" alt="Claude Code">
  <img src="https://img.shields.io/badge/Cursor-ready-green?style=flat-square" alt="Cursor">
  <img src="https://img.shields.io/badge/ChatGPT-ready-green?style=flat-square" alt="ChatGPT">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="MIT">
</p>

<h1 align="center">🧠 memo</h1>
<p align="center"><b>Long-term memory for AI agents</b></p>
<p align="center">One memory layer for Claude Code, Cursor, ChatGPT, and every other AI tool you use.<br>Stop repeating yourself. Make your AI remember.</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/caoyiqing1987/memo?style=social" alt="stars">
  <img src="https://img.shields.io/github/forks/caoyiqing1987/memo?style=social" alt="forks">
</p>

---

## 🤷 Ever had this conversation?

> **You:** "Remember, the client's budget is $50k and we're pitching next Friday."

> **AI:** "Got it!"

> *Next session...*

> **You:** "So about that client..."

> **AI:** "What client?"

Every AI conversation starts from zero. Not because AI is dumb — because it has **no long-term memory**.

**memo fixes that.** One CLI tool. Shared memory. Human and AI on the same page.

---

## 🎯 What is memo?

A CLI tool that gives your AI agents **persistent, structured, file-based memory**. Think of it as a shared notebook between you and every AI you work with.

```
You: "The project uses FastAPI + TailwindCSS"
↓
memo add "Tech stack: FastAPI + TailwindCSS"
↓
.memo/entries/tech.md  ← auto-categorized
↓
Next AI session: "I remember — FastAPI + TailwindCSS"
```

**One memory. Any AI. Any project.**

---

## ✨ Why memo?

| The Problem | How memo Helps |
|-------------|---------------|
| AI forgets everything between sessions | ✅ Persistent memory, cross-session |
| Using Claude Code + Cursor + ChatGPT together | ✅ Single memory layer, all tools share it |
| Important details lost in chat history | ✅ Auto-categorized, one command to save |
| Switching AI tools mid-project | ✅ File-based, no lock-in |
| Context windows fill up | ✅ Load only what you need, on demand |

---

## 🚀 Quick Start

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/caoyiqing1987/memo/main/install.sh | bash

# Start remembering in any project
cd your-project
memo init

# Save what matters
memo add "Client budget is $50k, pitch next Friday"
memo add "Tech stack: FastAPI + TailwindCSS"
memo add "Team: Alice frontend, Bob backend"

# See what's been saved
memo list

# Statistics
memo status
```

---

## 📖 Commands

| Command | What it does |
|---------|-------------|
| `memo init` | Create `.memo/` in current directory |
| `memo add "..."` | Save a memory (auto-categorized) |
| `memo list` | Browse all memories by category |
| `memo list clients` | Show only client-related memories |
| `memo status` | Memory statistics |
| `memo sync` | Archive old logs, clean backups, rebuild index |

---

## 🧩 How it works

```
your-project/
├── .memo/
│   ├── INDEX.md        ← Table of contents (AI reads this first)
│   ├── entries/        ← One file per category
│   │   ├── clients.md
│   │   ├── tech.md
│   │   ├── team.md
│   │   ├── design.md
│   │   └── general.md
│   ├── logs/           ← Daily activity log
│   └── backup/         ← Rotated snapshots
├── (your actual project files)
```

**For AI agents**, the protocol is simple:

1. Read `INDEX.md` to discover available categories
2. Load the relevant `.md` files based on the task
3. When new info surfaces, write it back with `memo add`

---

## 🔌 Compatibility

| Tool | Status | How |
|------|--------|-----|
| Claude Code | ✅ | Auto-read via CLAUDE.md → [guide](AGENT_INTEGRATION.md) |
| Cursor | ✅ | Auto-read via .cursorrules → [guide](AGENT_INTEGRATION.md) |
| Windsurf | ✅ | Auto-read via .windsurfrules → [guide](AGENT_INTEGRATION.md) |
| ChatGPT / GPTs | 🔄 | Manual paste → [guide](AGENT_INTEGRATION.md) |
| GitHub Copilot Chat | ✅ | Via copilot-instructions → [guide](AGENT_INTEGRATION.md) |

No API keys. No servers. No vendor lock-in. Just files.

---

## 💡 Why files?

Most AI memory systems are closed databases locked to one platform. memo takes the opposite approach:

- **No database** — plain Markdown, git-friendly
- **No service** — runs locally, zero dependencies
- **No limits** — your disk is your memory cap
- **No lock-in** — any tool can read and write files
- **Human accessible** — open in any editor, changes sync both ways

> "A memory system that only AI can read isn't a memory system — it's a black box."

---

## 📦 Technical

- Pure Python 3, zero external dependencies
- Auto-categorization via keyword matching
- 30-day log rotation, 90-day backup pruning
- INDEX.md auto-generated, never manual
- MIT License — free to use, modify, share

---

<p align="center">
  <b>🧠 memo — Make your AI remember.</b><br>
  <a href="https://github.com/caoyiqing1987/memo">GitHub</a> ·
  <a href="https://github.com/caoyiqing1987/memo/issues">Feedback</a> ·
  <a href="https://github.com/caoyiqing1987/memo/blob/main/README.md">Docs</a>
</p>
