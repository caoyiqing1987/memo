#!/usr/bin/env python3
"""memo — Agent-Friendly Memory Manager

A structured, persistent memory system for AI agents and humans.
Inspired by WorkBuddy's MEMORY.md + nexus/ architecture.

Usage:
  memo init              Initialize memory in current directory
  memo add "<text>"      Add a memory entry (auto-categorizes)
  memo list [category]   List entries
  memo status            Show memory stats
  memo sync              Archive old logs, prune backups
  memo help              Show this help
"""

import sys
import os
import re
import json
import shutil
from datetime import datetime, timedelta
from pathlib import Path

MEMO_DIR = Path(".memo")
INDEX_FILE = MEMO_DIR / "INDEX.md"
ENTRIES_DIR = MEMO_DIR / "entries"
LOGS_DIR = MEMO_DIR / "logs"
BACKUP_DIR = MEMO_DIR / "backup"

# ===== Helpers =====

def red(s): return f"\033[91m{s}\033[0m"
def green(s): return f"\033[92m{s}\033[0m"
def yellow(s): return f"\033[93m{s}\033[0m"
def blue(s): return f"\033[94m{s}\033[0m"
def bold(s): return f"\033[1m{s}\033[0m"
def dim(s): return f"\033[2m{s}\033[0m"

def _ensure_init():
    if not MEMO_DIR.exists():
        print(red("✗ Not a memo repository. Run 'memo init' first."))
        sys.exit(1)

# ===== Core Commands =====

def cmd_init():
    if MEMO_DIR.exists():
        print(yellow("⚠  memo already initialized here."))
        return

    MEMO_DIR.mkdir(parents=True)
    ENTRIES_DIR.mkdir()
    LOGS_DIR.mkdir()
    BACKUP_DIR.mkdir()

    # Create INDEX.md
    INDEX_FILE.write_text(f"""# .memo INDEX

> Auto-generated memory index. Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
> 
> Each entry is a markdown file in `entries/` named `<category>.md`.
> Agents: load the relevant file(s) when the category is referenced.

## Categories

_(none yet — run `memo add "..."` to create your first entry)_

---

## Rules

1. Each category = one file in `entries/`
2. INDEX.md is auto-generated from entries/
3. Old logs in `logs/` are rotated by `memo sync`
4. Backup snapshots in `backup/`
""")

    print(green("✓ Initialized empty memo repository in") + f" {MEMO_DIR.resolve()}")
    print(f"  {dim('INDEX.md')}     — Memory index (auto-maintained)")
    print(f"  {dim('entries/')}     — Each category = one file")
    print(f"  {dim('logs/')}       — Daily logs")
    print(f"  {dim('backup/')}     — Sync snapshots")
    print()
    print(f"  {dim('Next:')}  memo add \"<what you want to remember>\"")


def cmd_add(text: str):
    _ensure_init()
    if not text:
        print(red("✗ Usage: memo add \"<text>\""))
        sys.exit(1)

    # Auto-categorize
    category = _auto_category(text)
    entry_path = ENTRIES_DIR / f"{category}.md"

    # Append to entry file
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open(entry_path, 'a') as f:
        f.write(f"\n- [{timestamp}] {text}")

    # Also append to today's log
    log_file = LOGS_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(log_file, 'a') as f:
        f.write(f"\n- [{timestamp}] [{category}] {text}")

    _rebuild_index()
    print(green(f"✓ Remembered") + f" ({category})")
    print(f"  {dim(text[:80])}{'...' if len(text) > 80 else ''}")


def _auto_category(text: str) -> str:
    """Simple keyword-based auto-categorization."""
    rules = [
        (r'(客户|客户说|客户要求|客户反馈|客户需求|报价|报价单|合同|预算|项目|甲方)', 'clients'),
        (r'(团队|员工|招人|招聘|面试|入职|离职|工资|薪资|月薪|实习)', 'team'),
        (r'(公司|注册|税务|银行|域名|发票|增资|商标|版权|法人)', 'company'),
        (r'(家|儿子|孩子|女儿|老婆|太太|老婆|教育|幼儿园|学校|学习)', 'family'),
        (r'(技术|代码|部署|服务器|域名|API|Key|Token|账号|密码|配置)', 'tech'),
        (r'(设计|风格|颜色|字体|品牌色|UI|页面|布局|视觉)', 'design'),
        (r'(财务|收入|支出|利润|分红|股权|投资|融资|贷款)', 'finance'),
        (r'(人脉|朋友|合作|介绍|伙伴|关系|认识|微信|电话)', 'network'),
        (r'(创意|方案|idea|灵感|方向|策略|策划|广告)', 'creative'),
    ]
    for pattern, cat in rules:
        if re.search(pattern, text):
            return cat
    return 'general'


def _rebuild_index():
    """Regenerate INDEX.md from files in entries/."""
    _ensure_init()
    entries = sorted(ENTRIES_DIR.glob("*.md"))
    
    lines = [
        f"# .memo INDEX",
        f"",
        f"> Auto-generated memory index. Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f">",
        f"> Total: {len(entries)} categories",
        f"",
        f"## Categories",
        f"",
    ]
    
    for ep in entries:
        count = len(ep.read_text().strip().split('\n')) if ep.stat().st_size > 0 else 0
        lines.append(f"| `{ep.stem}` | {count} entries | entries/{ep.name} |")
    
    if not entries:
        lines.append("_(none yet — run `memo add \"...\"`)_")
    
    lines.extend(["", "---", "", "## Rules", "", "1. Each category = one file in `entries/`", "2. INDEX.md is auto-generated", "3. Old logs rotated by `memo sync`", ""])
    
    INDEX_FILE.write_text('\n'.join(lines))


def cmd_list(category=None):
    _ensure_init()
    entries = sorted(ENTRIES_DIR.glob("*.md"))
    
    if not entries:
        print(dim("No entries yet. Run 'memo add \"...\"'"))
        return
    
    if category:
        target = ENTRIES_DIR / f"{category}.md"
        if not target.exists():
            print(red(f"✗ Category '{category}' not found."))
            print(f"  Available: {', '.join(e.stem for e in entries)}")
            return
        content = target.read_text().strip()
        if content:
            print(bold(f"== {category} =="))
            for line in content.split('\n'):
                if line.strip():
                    print(f"  {line.strip()}")
        else:
            print(dim(f"Category '{category}' is empty."))
        return

    # List all categories with count
    total = 0
    for ep in entries:
        count = len([l for l in ep.read_text().strip().split('\n') if l.strip().startswith('- [')]) if ep.stat().st_size > 0 else 0
        label = f"{'─' if count == 0 else count}"
        print(f"  {green('▸')} {bold(ep.stem):<12} {dim(label)} entries")
        total += count
    print(f"\n  {dim('Total:')} {bold(str(total))} {dim('entries in')} {bold(str(len(entries)))} {dim('categories')}")


def cmd_status():
    _ensure_init()
    entries = sorted(ENTRIES_DIR.glob("*.md"))
    logs = sorted(LOGS_DIR.glob("*.md"))
    backups = sorted(BACKUP_DIR.glob("*.md"))

    total_entries = 0
    for ep in entries:
        total_entries += len([l for l in ep.read_text().strip().split('\n') if l.strip().startswith('- [')]) if ep.stat().st_size > 0 else 0

    print(f"  {bold('📦 memo status')}")
    print()
    print(f"  {blue('Categories:')}   {len(entries)}")
    print(f"  {blue('Entries:')}      {total_entries}")
    print(f"  {blue('Log days:')}     {len(logs)}")
    print(f"  {blue('Backups:')}      {len(backups)}")
    print(f"  {blue('Location:')}     {MEMO_DIR.resolve()}")
    
    if entries:
        print(f"\n  {dim('Categories:')}")
        for ep in entries:
            print(f"    {green('▸')} {ep.stem}")
    if logs:
        newest = logs[-1].stem
        oldest = logs[0].stem
        print(f"\n  {dim('Log range:')}   {oldest} → {newest}")


def cmd_sync():
    _ensure_init()
    
    # Archive logs older than 30 days
    now = datetime.now()
    cutoff = now - timedelta(days=30)
    archived = 0
    
    for log in sorted(LOGS_DIR.glob("*.md")):
        try:
            log_date = datetime.strptime(log.stem, '%Y-%m-%d')
            if log_date < cutoff:
                dest = BACKUP_DIR / log.name
                shutil.move(str(log), str(dest))
                archived += 1
        except ValueError:
            pass
    
    # Prune backups older than 90 days
    prune_cutoff = now - timedelta(days=90)
    pruned = 0
    for bak in BACKUP_DIR.glob("*.md"):
        try:
            bak_date = datetime.strptime(bak.stem, '%Y-%m-%d')
            if bak_date < prune_cutoff:
                bak.unlink()
                pruned += 1
        except ValueError:
            pass

    _rebuild_index()
    print(green(f"✓ Sync complete"))
    print(f"  {dim('Archived:')} {archived} old logs → backup/")
    print(f"  {dim('Pruned:')}   {pruned} old backups")
    print(f"  {dim('Index:')}   rebuilt")


def cmd_help():
    print(bold("memo — Agent-Friendly Memory Manager"))
    print()
    print(f"  {green('memo init')}              Initialize memory in current directory")
    print(f"  {green('memo add')} \"<text>\"      Add a memory entry")
    print(f"  {green('memo list')} [category]   List entries")
    print(f"  {green('memo status')}            Show memory stats")
    print(f"  {green('memo sync')}              Archive old logs, prune backups")
    print(f"  {green('memo help')}              Show this help")
    print()
    print(f"  {dim('Each entry is auto-categorized and stored in .memo/entries/')}")
    print(f"  {dim('INDEX.md is auto-generated. Compatible with AI agents.')}")


# ===== Main =====

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help', 'help'):
        cmd_help()
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        'init': lambda: cmd_init(),
        'add': lambda: cmd_add(' '.join(args) if args else ''),
        'list': lambda: cmd_list(args[0] if args else None),
        'ls': lambda: cmd_list(args[0] if args else None),
        'status': cmd_status,
        'sync': cmd_sync,
        'help': cmd_help,
    }

    if cmd not in commands:
        print(red(f"✗ Unknown command: {cmd}"))
        print(f"  Run 'memo help' to see available commands.")
        sys.exit(1)

    commands[cmd]()


if __name__ == '__main__':
    main()
