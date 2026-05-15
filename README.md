# memo — Agent-Friendly Memory Manager

**memo** is a structured, persistent memory system designed to be shared between **humans and AI agents**. It turns the chaos of "I need to remember this" into a clean, auto-maintained directory of markdown files.

```
project/
├── .memo/
│   ├── INDEX.md        ← Auto-generated catalog of all entries
│   ├── entries/
│   │   ├── clients.md
│   │   ├── team.md
│   │   ├── tech.md
│   │   ├── design.md
│   │   └── general.md
│   ├── logs/            ← Daily activity logs
│   └── backup/          ← Rotated archives
└── (your project files)
```

## Why memo?

Every AI agent has its own memory format — CLAUDE.md, .cursorrules, .windsurfrules — and none of them talk to each other. **memo** is a universal, file-based memory layer that any agent can read, and any human can edit.

```
Agent A           Agent B           You
  │                  │               │
  └──────────┬───────┴──────┬───────┘
             │              │
        .memo/INDEX.md   .memo/entries/
             │              │
        "load clients.md"   │
             └──────────────┘
```

## Quick Start

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/caoyiqing1987/memo/main/install.sh | bash

# Or locally
git clone https://github.com/<user>/memo.git
cd memo && bash install.sh

# Use
cd your-project
memo init                    # Create .memo/ structure
memo add "客户说预算提高到50万"  # Auto-categorizes → entries/clients.md
memo add "服务器改用新加坡节点"  # Auto-categorizes → entries/tech.md
memo list                    # See all categories
memo status                  # Show stats
```

## Commands

| Command | Description |
|---------|-------------|
| `memo init` | Initialize `.memo/` in current directory |
| `memo add "<text>"` | Add a memory entry (auto-categorized) |
| `memo list [category]` | List all entries, or filter by category |
| `memo status` | Show memory stats |
| `memo sync` | Archive old logs, prune backups, rebuild index |
| `memo help` | Show help |

## Design Philosophy

1. **Files over databases** — Markdown files are human-readable, git-friendly, and universally accessible
2. **INDEX as entry point** — One file tells agents what's available; load on demand, not everything at once
3. **Auto-categorization** — You type naturally; the tool figures out where it goes
4. **Agent first, human second** — Designed so that AI agents can self-maintain their memory without human intervention

## For AI Agents

When you (the agent) start a session in a project with `.memo/`:

1. Read `INDEX.md` to see available categories
2. Load relevant category files based on the user's current task
3. When the user says something worth remembering, call `memo add "<text>"`
4. Periodically run `memo sync` for maintenance

## License

MIT
