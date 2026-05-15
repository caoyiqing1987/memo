<p align="center">
  <img src="https://img.shields.io/badge/AI-Agent%20Memory-blue?style=flat-square" alt="AI Agent Memory">
  <img src="https://img.shields.io/badge/Claude%20Code-ready-green?style=flat-square" alt="Claude Code">
  <img src="https://img.shields.io/badge/Cursor-ready-green?style=flat-square" alt="Cursor">
  <img src="https://img.shields.io/badge/ChatGPT-ready-green?style=flat-square" alt="ChatGPT">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="MIT">
</p>

<h1 align="center">🧠 memo</h1>
<p align="center"><b>AI 智能体的长期记忆系统</b></p>
<p align="center">让 Claude Code、Cursor、ChatGPT 记住你的一切<br>不再每次对话从零开始</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/caoyiqing1987/memo?style=social" alt="stars">
  <img src="https://img.shields.io/github/forks/caoyiqing1987/memo?style=social" alt="forks">
</p>

---

## 🤷 你是不是也这样？

> "我刚告诉过你的啊……"
> "这是第三次解释这个项目了……"
> "Claude 怎么又不记得我的配置了……"

**每次和 AI 对话，它都不记得上一次说了什么。**

不是它笨，是它没有长期记忆。

**memo 就是来解决这个问题的。**

---

## 🎯 memo 是什么

一个 CLI 工具，帮你和 AI 建立**共享的长期记忆**。

```
你： "这个项目的客户是智己汽车，预算50万"
↓
memo add "客户智己汽车，预算50万"
↓
.memo/entries/clients.md  ← 自动分类存好了
↓
下次 AI 启动时： "我记得，客户智己汽车，预算50万"
```

**一句话：你和 AI 共用同一份记忆。**

---

## ✨ 为什么你需要 memo

| 痛点 | memo 解决 |
|------|-----------|
| 每次对话 AI 都不记得你 | ✅ 记忆跨 session 持久化 |
| 同时用 Claude Code + Cursor + ChatGPT | ✅ 统一记忆层，全家桶共享 |
| 重要信息散落在聊天记录里 | ✅ 自动分类归档，一条命令搞定 |
| 项目做到一半换工具 | ✅ 文件系统，什么工具都能读 |
| AI 记忆动不动就满了 | ✅ 按需加载，不占上下文 |

---

## 🚀 30 秒上手

```bash
# 安装
curl -fsSL https://raw.githubusercontent.com/caoyiqing1987/memo/main/install.sh | bash

# 在项目里初始化记忆库
cd your-project
memo init

# 让 AI 记住事情
memo add "客户预算50万，下周五提案"
memo add "技术方案用 FastAPI + TailwindCSS"
memo add "团队成员：小王前端、小李后端"

# 查看记住了什么
memo list

# stats
memo status
```

---

## 📖 命令一览

| 命令 | 作用 |
|------|------|
| `memo init` | 在当前目录创建 `.memo/` 记忆仓库 |
| `memo add "..."` | 添加一条记忆（自动分类） |
| `memo list` | 按分类浏览所有记忆 |
| `memo list clients` | 只看客户相关记忆 |
| `memo status` | 记忆仓库统计 |
| `memo sync` | 归档旧日志、清理备份、重建索引 |

---

## 🧩 结构

```
your-project/
├── .memo/
│   ├── INDEX.md        ← 记忆目录（AI从这里查有哪些记忆）
│   ├── entries/        ← 分类存放
│   │   ├── clients.md  ← 客户信息
│   │   ├── tech.md     ← 技术方案
│   │   ├── team.md     ← 团队信息
│   │   ├── design.md   ← 设计决策
│   │   └── ...
│   ├── logs/           ← 每日日志
│   └── backup/         ← 自动备份
├── (你的项目文件)
```

AI 启动时只要做三件事：
1. 读 `INDEX.md` — 看有哪些记忆类别
2. 按需加载对应文件
3. 有新信息就 `memo add` 写回去

---

## 🔌 兼容性

| 工具 | 支持 | 说明 |
|------|------|------|
| Claude Code | ✅ | 读 INDEX.md 后按需加载 entry |
| Cursor | ✅ | 同 | 
| Windsurf | ✅ | 同 |
| ChatGPT | ✅ | 粘贴 INDEX.md 即可 |
| 任何 AI Agent | ✅ | 文件系统无锁，谁都能读 |
| 你（人类） | ✅ | VSCode 直接编辑或 `memo add` |

---

## 💡 设计理念

**好的记忆系统，人和 AI 都能用。**

- 不用数据库，不依赖任何服务
- 不锁定某个 AI 品牌
- 不限制记忆容量（文件系统多大就能记多少）
- 人可以用编辑器改，AI 可以用 CLI 读写
- 双向同步，谁改的对方都知道

---

## 📦 技术细节

- 纯 Python 3 实现，零依赖
- 自动分类：根据关键词智能匹配 clients / tech / team / design 等类别
- 30 天日志归档，90 天备份清理
- INDEX.md 自动维护，无需手动编辑
- MIT 开源，随便改

---

<p align="center">
  <b>🧠 memo — 让 AI 不再是金鱼</b><br>
  <a href="https://github.com/caoyiqing1987/memo">GitHub</a> ·
  <a href="https://github.com/caoyiqing1987/memo/issues">反馈</a> ·
  <a href="https://github.com/caoyiqing1987/memo/blob/main/README.md">文档</a>
</p>
