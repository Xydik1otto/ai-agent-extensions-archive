# 🤖 AI Agent Extensions Archive / Карта розширень для ШІ-агентів

**A map of plugins, skills, MCP servers, rules and upgrades for AI coding agents** — Claude Code, Cursor, GitHub Copilot, Codex, Gemini CLI, Cline, Windsurf, Aider and more, organized **by agent platform**. (284 repos, last refreshed 2026-11-05)

> **Українською:** індекс плагінів, скілів, MCP-серверів, rules-колекцій та апгрейдів для ШІ-агентів, розбитий **за агентами**. Кожен пункт — посилання на оригінальний репозиторій GitHub. Індекс оновлюється автоматично через офіційний GitHub Search API (див. [`tools/collect.py`](tools/collect.py)).

> ⚠️ All links point to the **original repositories** — nothing is copied; each repo keeps its own license. / Усі посилання ведуть на оригінальні репозиторії — нічого не копіюється, ліцензії зберігаються у авторів.

---

## 📑 Table of Contents

- [`Claude Code (plugins, skills, subagents, hooks)`](#cat-claude-code) — 28 repos
- [`Agent Skills & Marketplaces (cross-agent)`](#cat-skills-marketplaces) — 29 repos
- [`Cursor (rules, extensions)`](#cat-cursor) — 20 repos
- [`GitHub Copilot (extensions, agents)`](#cat-github-copilot) — 16 repos
- [`OpenAI Codex CLI`](#cat-openai-codex) — 21 repos
- [`Gemini CLI (extensions)`](#cat-gemini-cli) — 26 repos
- [`Other Coding Agents (Aider, Cline, Roo, Windsurf, OpenCode, Continue)`](#cat-other-coding-agents) — 25 repos
- [`MCP Ecosystem (servers, registries, clients)`](#cat-mcp-ecosystem) — 30 repos
- [`Agent Frameworks & Tool Libraries (LangChain, crewAI, AutoGPT...)`](#cat-agent-frameworks) — 30 repos
- [`Automation Platforms (n8n, Dify, Flowise...)`](#cat-automation-workflows) — 27 repos
- [`Local / Offline Agents (Ollama, llama.cpp)`](#cat-local-offline) — 22 repos
- [`Chat Platforms (ChatGPT, Slack, Telegram, Discord)`](#cat-chat-platforms) — 10 repos

---

<a id="cat-claude-code"></a>
## Claude Code (plugins, skills, subagents, hooks)
**Claude Code**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 297.7k | JavaScript | Skills | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 229.8k | — | Skills | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy&#x27;s observations on LLM coding pitfalls. |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 152.1k | Rust | Skills | A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode,DeepSeek Harness and more. Only official website: ccswitch.io |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 142.8k | Python | Skills | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 117.7k | Go | Skills | 🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman. |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 93.8k | JavaScript | Skills | Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more. |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 81.0k | TypeScript | Skills | 🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG int |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 58.7k | JavaScript | Skills | Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering. |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 57.3k | Python | Claude Code | A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC (no affiliation). A delectable sho |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 49.2k | Python | Claude Code | 2,926+ reusable AI agent skills for Claude Code, Codex, Cursor and Gemini CLI. AAS Core adds local catalog discovery, agent-owned selection and plan preview. CLI, MCP and plugins. |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 46.2k | Python | Claude Code | Official, Anthropic-managed directory of high quality Claude Code Plugins. |
| [wshobson/agents](https://github.com/wshobson/agents) | 42.2k | Python | Claude Code | Plugins, agents, skills, and commands for Claude Code, Codex CLI, Cursor, OpenCode, Antigravity CLI, GitHub Copilot, and Pi, written once in Markdown and adapted to each tool by generators with validation and evals. |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 36.9k | — | Meta | A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more. |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | 33.5k | JavaScript | Claude Code | Free, local plugin that keeps tool output out of your coding agent&#x27;s context window. Sandbox and SQLite FTS5 search, 99% fewer bytes in context. Works with Claude Code, Codex, Pi, OpenCode, Gemini CLI, Copilot CLI and 4  |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 29.3k | Python | Claude Code | 410 Claude Code skills &amp; agent skills &amp; plugins (120+ Agents, custom commands, 410+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing,  |
| [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | 29.1k | JavaScript | Claude Code | A Claude Code plugin that shows what&#x27;s happening - context usage, active tools, running agents, and todo progress |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 27.9k | Shell | Claude Code | Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion ga |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 26.3k | Shell | Subagents | A collection of 100+ specialized Claude Code subagents covering a wide range of development use cases |
| [YishenTu/claudian](https://github.com/YishenTu/claudian) | 15.9k | TypeScript | Claude Code | An Obsidian plugin that embeds Claude Code, Codex and other agents as an AI collaborator in your vault. |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 15.7k | — | Meta | A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows — particularly Claude Code |
| [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) | 13.5k | TypeScript | UI/statusline | 🚀 Beautiful highly customizable statusline for Claude Code CLI with powerline support, themes, and more. |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | 13.1k | JavaScript | UI/statusline | All parts of Claude Code&#x27;s system prompt, 27 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact,  statusline, magic docs, WebFetch, Bash cmd, security review, agent crea |
| [diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase) | 10.0k | TypeScript | Hooks | Examples of my Claude Code infrastructure with skill auto-activation, hooks, and agents |
| [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | 6.9k | Python | Meta | 77 game-dev skills for AI coding agents — Godot, Unity, Unreal, Phaser, PixiJS, three.js, Bevy, pygame, LÖVE, Roblox. Portable SKILL.md Agent Skills (the format Anthropic launched as Claude Skills), with a router that lo |
| [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | 6.4k | Python | Hooks | The most comprehensive Claude Code guide: agentic workflows, hooks, skills, MCP servers, quizzes, and production-ready templates. 430K+ lines. |
| [dontriskit/awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) | 6.3k | TypeScript | Meta | 🧠 Curated collection of system prompts for top AI tools. Perfect for AI agent builders and prompt engineers. Incuding: ChatGPT, Claude, Perplexity, Manus, Claude-Code, Loveable, v0, Grok, same new, windsurf, notion, and  |
| [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | 6.3k | Rust | Hooks | A fast Rust safety hook that blocks destructive shell, git, and filesystem commands before AI coding agents run them. 50+ security packs (databases, Kubernetes, Docker, cloud, Terraform), heredoc/inline-script scanning,  |
| [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | 6.1k | JavaScript | Hooks | Comprehensive Claude Code project configuration example with hooks, skills, agents, commands, and GitHub Actions workflows |

<a id="cat-skills-marketplaces"></a>
## Agent Skills & Marketplaces (cross-agent)
**Скіли та маркетплейси**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | 187.7k | Python | Skills | Public repository for Agent Skills |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 185.0k | JavaScript | Skills | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 113.4k | JavaScript | Skills | Production-grade engineering skills for AI coding agents. |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 110.5k | JavaScript | Skills | Agent skills that give coding agents taste: art direction, reference images and a browser check instead of generic AI pages |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 103.6k | Rust | Skills | The design vocabulary for your coding agent. Steer with polish and bolder, review with critique and audit, catch AI slop before it ships. |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 78.8k | Python | Meta | A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 33.6k | JavaScript | Skills | Vercel&#x27;s official collection of agent skills |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 18.3k | Python | Skills | A comprehensive collection of Agent Skills for context engineering, multi-agent architectures, and production agent systems. Use when building, optimizing, or debugging agent systems that require effective context manage |
| [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | 15.3k | TypeScript | Marketplace | 本地优先的跨平台 Claude Code / AI Agent 桌面工作台：多 Agent 协作、Git Worktree、代码 Diff、技能市场、多模型、Computer Use、桌面宠物；支持微信、飞书、钉钉及 H5 等远程访问。 / Local-first Claude Code / AI Agent desktop workspace: multi-agent teams, Git worktrees, diffs, skil |
| [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | 14.0k | JavaScript | Skills | ConardLi&#x27;s open-source Skills collection, featuring web design, knowledge retrieval, image generation, and more. |
| [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | 10.9k | Markdown | Skills | A collection of agent skills that help you build great interfaces. |
| [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) | 10.3k | — | Meta | A curated list of Claude Skills. |
| [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | 7.1k | TypeScript | Registry | The secure, validated skill registry for professional AI coding agents. Extend Antigravity, Claude Code, Cursor, Copilot and more with absolute confidence. |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | 6.3k | TypeScript | Meta | Tutorials, Guides and Agent Skills Directories |
| [antfu/skills](https://github.com/antfu/skills) | 6.0k | TypeScript | Skills | Anthony Fu&#x27;s curated collection of agent skills. |
| [dotnet/skills](https://github.com/dotnet/skills) | 5.8k | C# | Skills | Repository for skills to assist AI coding agents with .NET and C# |
| [iflytek/skillhub](https://github.com/iflytek/skillhub) | 5.4k | Java | Registry | Self-hosted, open-source agent skill registry for enterprises. Publish &amp; version skill packages, govern with RBAC and audit logs, deploy   on-premise with Docker or Kubernetes. |
| [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 4.9k | Stata | Skills | 🔬 A curated collection of 23,000+ agent skills for empirical research across 8 social science disciplines. / 精选 23,000+ AI Agent 技能库，覆盖8大社会科学学科的实证研究。CoPaper.AI 20分钟完成一篇可复现的规范实证论文，并支持用户上传 Skills。-- Maintained by CoPaper.A |
| [AgenticResourceRegistry/AgenticResourceRegistry](https://github.com/AgenticResourceRegistry/AgenticResourceRegistry) | 4.4k | Python | Registry | Share and discover coding agent resources across your team. Self-hosted, Apache 2.0, works with Claude Code, Kiro, Cursor, Codex, Pi and more. |
| [expo/skills](https://github.com/expo/skills) | 4.1k | Shell | Skills | A collection of AI agent skills for working with Expo projects and Expo Application Services |
| [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) | 3.8k | Go | Skills | 🧑‍🎨 A collection of Golang agentic skills that works |
| [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 1.8k | TypeScript | Marketplace | Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemini CLI, and others. Includes CodeRabbit open-source alternative. |
| [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) | 1.5k | Python | Marketplace | Professional Claude Code skills marketplace featuring production-ready skills for enhanced development workflows. |
| [data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development) | 1.1k | C# | Marketplace | Power BI AI skills and Power BI agents for Claude Code and GitHub Copilot: a plugin marketplace of Power BI skills, subagents, and hooks for semantic models, DAX, TMDL, reports, and AI dashboards. Includes Microsoft Fabr |
| [numman-ali/n-skills](https://github.com/numman-ali/n-skills) | 1.1k | TypeScript | Marketplace | Curated plugin marketplace for AI agents - works with Claude Code, Codex, and openskills |
| [agentic-community/mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry) | 1.0k | Python | Registry | Enterprise-ready MCP Gateway &amp; Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform |
| [skillmatic-ai/awesome-agent-skills](https://github.com/skillmatic-ai/awesome-agent-skills) | 693 | — | Meta | The definitive resource for Agent Skills - modular capabilities revolutionizing AI agent architecture |
| [JackyST0/awesome-agent-skills](https://github.com/JackyST0/awesome-agent-skills) | 666 | JavaScript | Meta | 🤖 精选的 AI Agent Skills 列表，适用于 Cursor、Claude Code、GitHub Copilot 等 AI 编程工具 |
| [kael-odin/awesome-academic-research-skills](https://github.com/kael-odin/awesome-academic-research-skills) | 197 | Python | OpenCode | 面向中文用户的学术论文与科研 Agent Skill 每日排行榜 · 自动搜索、过滤并排名 GitHub 上的 Claude Code / Codex / OpenCode 科研 Skill 仓库 |

<a id="cat-cursor"></a>
## Cursor (rules, extensions)
**Cursor**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | 21.9k | Shell | Rules | 🎭 277 个即插即用的 AI 专家角色 — 支持 Claude Code/Cursor/Copilot 等 20 种工具，覆盖工程/设计/营销/金融等 20 个部门。含 64 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉/Qt 上位机/机械设计）。搭配编排器 agency-orchestrator，一句话即可让多位专家按 DAG 自动协作。 |
| [ciembor/agent-rules-books](https://github.com/ciembor/agent-rules-books) | 3.2k | — | Rules | AGENTS.md rules / skills for AI coding agents: Codex, Cursor &amp; Claude Code. Inspired by Clean Code, Refactoring, DDD, Clean Architecture and DDIA programming books. |
| [flyeric0212/cursor-rules](https://github.com/flyeric0212/cursor-rules) | 1.9k | — | Rules | 整理和收集来自不同项目的Cursor规则文件，提供多种编程语言和框架的规则支持。 |
| [software-mansion/radon-ide](https://github.com/software-mansion/radon-ide) | 1.7k | TypeScript | Extensions | VSCode/Cursor extension that turns your editor into a full featured IDE for React Native and Expo. |
| [devtoolsd/awesome-devtools](https://github.com/devtoolsd/awesome-devtools) | 689 | — | Rules | A curated list of awesome developer tools and services — from cloud platforms and IDEs to AI-powered coding assistants and productivity utilities. |
| [HoangNguyen0403/agent-skills-standard](https://github.com/HoangNguyen0403/agent-skills-standard) | 583 | TypeScript | Rules | A collection of Agent Skills Standard and Best Practice for Programming Languages, Frameworks that help our AI Agent follow best practies on frameworks and programming laguages |
| [hanlulong/stata-mcp](https://github.com/hanlulong/stata-mcp) | 520 | Python | Extensions | Stata MCP Extension for VS Code, Cursor, and Antigravity IDE |
| [blazejkustra/react-compiler-marker](https://github.com/blazejkustra/react-compiler-marker) | 460 | TypeScript | Extensions | Universal IDE extension that shows which React components are optimized by the React Compiler ✨ |
| [mhfed/vn-law-check](https://github.com/mhfed/vn-law-check) | 433 | Shell | Rules | Audit pháp lý website theo luật Việt Nam (BVDLCN 91/2025, TMĐT 122/2025, ANM 116/2025, AI 134/2025) cho Claude Code, Cursor, Copilot, Windsurf, Cline |
| [matank001/cursor-security-rules](https://github.com/matank001/cursor-security-rules) | 383 | — | Rules | This repository contains Cursor Security Rules designed to improve the security of both development workflows and AI agent usage within the Cursor environment. These rules aim to enforce safe coding practices, control se |
| [kleosr/cursorkleosr](https://github.com/kleosr/cursorkleosr) | 325 | — | Rules | Make AI Development Feel Natural in Cursor |
| [tomlin7/biscuit](https://github.com/tomlin7/biscuit) | 266 | Python | Extensions | biscuit is a native, extensible, AI code editor. lightweight &lt;20 mb in size. install and start using in seconds. |
| [thehimel/cursor-rules-and-prompts](https://github.com/thehimel/cursor-rules-and-prompts) | 251 | Shell | Rules | A comprehensive, open-source collection of rules and prompts designed to guide Cursor AI in generating better, more consistent code. Enhance code quality, enforce coding standards, and streamline development workflows au |
| [Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift) | 246 | TypeScript | Extensions | Persistent local memory layer for AI. ArcRift uses a extension and a native MCP server to sync context and decisions from your browser chats (Claude, ChatGPT, DeepSeek) straight to your local IDE agents (Cursor, Claude C |
| [qczone/switch2idea](https://github.com/qczone/switch2idea) | 199 | TypeScript | Extensions | A Cursor extension enabling smooth switching between Cursor and IDEA, with automatic cursor position sync and convenient shortcuts. Supports multiple JetBrains IDEs and enhances development workflow efficiency. |
| [DataDog/IDE-SHEPHERD-extension](https://github.com/DataDog/IDE-SHEPHERD-extension) | 122 | TypeScript | Extensions | A VS Code/Cursor extension capable of performing realtime security monitoring from inside the IDE |
| [GulajavaMinistudio/awesome-copilot-id](https://github.com/GulajavaMinistudio/awesome-copilot-id) | 93 | JavaScript | Rules | A curated collection of custom agents, skills, rules, and prompts for GitHub Copilot, Google Antigravity, OpenCode, ChatGPT Codex, and Oh My Pi. Tailored for Indonesian and International developers to streamline SDLC wor |
| [lasoons/AgentSkillsManager](https://github.com/lasoons/AgentSkillsManager) | 90 | TypeScript | Extensions | AgentSkills multi-IDE management extension: browse and install skill repositories for Antigravity, CodeBuddy, Cursor, Qoder, Trae, Windsurf (and VS Code), and search a cloud catalog (~58K skills) from https://claude-plug |
| [matlab/rules](https://github.com/matlab/rules) | 54 | — | Rules | A collection of MATLAB coding rules and guidelines optimized for use with AI coding assistants like Cursor, Windsurf, Claude Code, and GitHub Copilot |
| [OpenPawz/OPIDE](https://github.com/OpenPawz/OPIDE) | 52 | Rust | Extensions | Rust-native AI IDE — AST indexing, QuickJS sandbox, AES-256-GCM encrypted, O VSX: the first extension runtime for a Rust IDE. Zero Electron. Zero compromise. |

<a id="cat-github-copilot"></a>
## GitHub Copilot (extensions, agents)
**GitHub Copilot**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 40.8k | JavaScript | Meta | Community-contributed instructions, agents, skills, and configurations to help you make the most of GitHub Copilot. |
| [nicepkg/aide](https://github.com/nicepkg/aide) | 2.7k | TypeScript | Extensions | Conquer Any Code in VSCode: One-Click Comments, Conversions, UI-to-Code, and AI Batch Processing of Files! 在 VSCode 中征服任何代码：一键注释、转换、UI 图生成代码、AI 批量处理文件！💪 |
| [microsoft/hve-core](https://github.com/microsoft/hve-core) | 1.6k | PowerShell | Instructions | A refined collection of Hypervelocity Engineering components (instructions, prompts, agents, and skills) to start your project off right, or upgrade your existing projects to get the most out of GitHub Copilot |
| [specstoryai/getspecstory](https://github.com/specstoryai/getspecstory) | 1.4k | Go | Extensions | Install our local first extensions for your favorite AI IDE or Terminal Agent. Process your histories into reusable skills with Lore. Sync your conversations to the cloud. File issues and requests. |
| [new-silvermoon/awesome-android-agent-skills](https://github.com/new-silvermoon/awesome-android-agent-skills) | 1.0k | — | Meta | A collection of standardized Agent Skills to teach GitHub Copilot, Claude, Gemini and Cursor about modern Android development (Kotlin, Jetpack Compose, etc.). |
| [Code-and-Sorts/awesome-copilot-agents](https://github.com/Code-and-Sorts/awesome-copilot-agents) | 591 | TypeScript | Meta | ✨ A curated list of awesome GitHub instructions, prompt, skills, MCPs and agent markdown files for enhancing your GitHub Copilot AI experience. |
| [VikashLoomba/copilot-mcp](https://github.com/VikashLoomba/copilot-mcp) | 507 | TypeScript | Extensions | A VSCode extension that lets you find and install Agent Skills and MCP Apps to use with GitHub Copilot, Claude Code, and Codex CLI. |
| [plmbr/notebook-intelligence](https://github.com/plmbr/notebook-intelligence) | 350 | Python | Extensions | A JupyterLab extension supporting Claude Code, Copilot, Ollama, and OpenAI-compatible LLMs, with MCP, skills, plugins, and notebook agents. |
| [cheaper-inference/OmniCopilot](https://github.com/cheaper-inference/OmniCopilot) | 174 | TypeScript | Extensions | 1200+ AI models in your GitHub Copilot Chat — free &amp; forever free. VS Code extension powered by OmniRoute: 340+ providers (90+ free) — Kimi, Claude, GPT, Gemini, GLM, DeepSeek, Qwen — with agent mode, tool calling, visio |
| [codegraph-ai/CodeGraph](https://github.com/codegraph-ai/CodeGraph) | 143 | C | Extensions | CodeGraph builds a semantic graph of your codebase — functions, classes, imports, call chains — and exposes it through 42 MCP tools, 38 languages, a VS Code extension, and a persistent memory layer. AI agents get structu |
| [0xeb/windbg-agent](https://github.com/0xeb/windbg-agent) | 111 | C++ | Extensions | WinDbg Copilot - Agentic Debugging extension |
| [microsoft/agent-forge](https://github.com/microsoft/agent-forge) | 91 | TypeScript | Agents | AGENT-FORGE is a Context Engineering Toolkit that generates GitHub Copilot customization files for your VS Code project. Instead of manually authoring .github/ configuration, you describe what you need and a multi-agent  |
| [AmadeusITGroup/ai-primitives-hub](https://github.com/AmadeusITGroup/ai-primitives-hub) | 51 | TypeScript | Extensions | VS Code extension and CLI for managing, sharing, and installing AI primitives (Agents, Skills, Prompts, Instructions, MCP) collections for GitHub Copilot and other AI assistants |
| [ruvnet/agentic-search](https://github.com/ruvnet/agentic-search) | 44 | TypeScript | Extensions | An Agentic Github Copilot Extension |
| [lewiswigmore/open-wire](https://github.com/lewiswigmore/open-wire) | 42 | TypeScript | Extensions | OpenWire - VS Code extension that exposes Copilot language models as an OpenAI-compatible REST API |
| [ttxttx1111/sts2-llm](https://github.com/ttxttx1111/sts2-llm) | 41 | Python | Agents | GitHub Copilot player agent customization pack for Slay the Spire 2 via STS2MCP |

<a id="cat-openai-codex"></a>
## OpenAI Codex CLI
**OpenAI Codex**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [blader/humanizer](https://github.com/blader/humanizer) | 65.1k | Python | Skills | Agent skill that removes signs of AI-generated writing from text |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 56.2k | Python | Skills | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 ready-to-use validated skills plus 100+ scientific databases covering biology, chemistry, medici |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 50.8k | — | Skills | Agent skills for Obsidian. Teach your agent to use Obsidian CLI and open formats including Markdown, Bases, JSON Canvas. |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 14.1k | Python | Codex | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 6.0k | Python | Codex | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CLI, and OpenCode across ideation, coding, experiments, writing, and publication. |
| [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | 3.7k | Python | Codex CLI | De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI), with native plugins for Claude Code, Codex, Grok Build, and Antigravity. Narrative-architecture repair for fiction, venue-matched rules  |
| [Dailin521/codex-provider-sync](https://github.com/Dailin521/codex-provider-sync) | 3.6k | JavaScript | Codex | Synchronize Codex session provider metadata across rollout files and SQLite state. |
| [stravu/crystal](https://github.com/stravu/crystal) | 3.1k | TypeScript | Codex | (Crystal is now Nimbalyst) Run multiple Codex and Claude Code AI sessions in parallel git worktrees. Test, compare approaches &amp; manage AI-assisted development workflows in one desktop app. |
| [runkids/skillshare](https://github.com/runkids/skillshare) | 2.9k | Go | Codex CLI | 📚 Sync skills, agents, MCP, plugins to all AI CLI tools with one command and simplify team sharing. |
| [iFurySt/open-computer-use](https://github.com/iFurySt/open-computer-use) | 2.9k | Swift | Codex | 👾 Open Computer Use – Open-Source Alternative to Codex Computer Use |
| [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | 2.6k | JavaScript | Codex | Delegate a coding task to a separate coding agent CLI, review the diff, land the commit yourself — one per implementer. |
| [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | 2.3k | Python | Codex | Let Claude (or any LLM) actually watch a video — scene-aware, deduplicated frames + transcript, from a URL or local file. Runs locally, MIT. |
| [agent-sh/agentsys](https://github.com/agent-sh/agentsys) | 1.0k | JavaScript | Codex CLI | AI writes code. This automates everything else · 24 plugins · 49 agents · 44 skills · for Claude Code, OpenCode, Codex, Cursor, Kiro. |
| [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | 1.0k | JavaScript | Codex CLI | AI video editor for agents. ChatCut plugin and MCP server for Codex, ChatGPT, Claude Code, Cursor, Grok, Gemini CLI, WorkBuddy, Doubao Work and Qwen Work: edit your own footage by chatting, add captions and subtitles, re |
| [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) | 985 | Python | Extensions | A curated list of the best awesome AI plugins for AI assistants including Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok, OpenCodek DSH, Kimi and More. https://hol.org/plugins |
| [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) | 968 | Rust | Codex CLI | Review your agent&#x27;s diff in a terminal pane and send comments back to Claude Code, Codex, OpenCode or Pi. A herdr plugin. |
| [Securiteru/codex-openai-proxy](https://github.com/Securiteru/codex-openai-proxy) | 144 | Rust | Extensions | Proxy server to use ChatGPT Plus tokens with CLINE/Claude Code extensions via OpenAI API compatibility |
| [lhr0909/jupyterlab-codex](https://github.com/lhr0909/jupyterlab-codex) | 92 | TypeScript | Extensions | JupyterLab Extension that unlocks the power of OpenAI&#x27;s Codex Model. |
| [ClaudeCodeUsage/ClaudeCodeUsage](https://github.com/ClaudeCodeUsage/ClaudeCodeUsage) | 74 | TypeScript | Extensions | VS Code extension for local Claude Code and OpenAI Codex token usage, cache, quotas, and API-equivalent cost insights. |
| [mattleong/pi-better-openai](https://github.com/mattleong/pi-better-openai) | 68 | TypeScript | Extensions | A pi extension for OpenAI subscription workflows: fast mode, usage visibility, footer polish, and image generation through openai-codex auth. |
| [MaxMiksa/Codex-Workflow-Folder](https://github.com/MaxMiksa/Codex-Workflow-Folder) | 59 | JavaScript | Extensions | Give you a clean and useful Codex (VS Code extension). |

<a id="cat-gemini-cli"></a>
## Gemini CLI (extensions)
**Gemini CLI**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 35.6k | Python | Skills | 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&amp;CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF &amp; MITRE F3 (Fight Fraud) · agentskills.io standard · Works with Claude Code, GitHub |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | 34.1k | TypeScript | Gemini CLI | Open-source 24/7 Cowork app for OpenClaw, Hermes, Claude Code, Codex, OpenCode and 20+ more CLI Agent / Customize your assistants / Team them up｜Star if you like it! |
| [decolua/9router](https://github.com/decolua/9router) | 32.0k | JavaScript | Gemini CLI | Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini via 40+ providers. Auto-fallback, RTK -40% tokens, never hit limits. |
| [yetone/magpie](https://github.com/yetone/magpie) | 30.4k | Go | Gemini CLI | Every agent&#x27;s model. One place. Codex on DeepSeek, Claude Code on Kimi, from the menu bar. |
| [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | 20.1k | Python | Skills | Unofficial Python API and agentic skill for Google Gemini Notebook. Full programmatic access to Gemini Notebook&#x27;s features—including capabilities the web UI doesn&#x27;t expose—via Python, CLI, and AI agents like Claude Code, |
| [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | 12.8k | JavaScript | Gemini CLI | CRS-自建Claude Code镜像，一站式开源中转服务，让 Claude、OpenAI、Gemini、Droid 订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。 |
| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | 12.7k | TypeScript | Gemini CLI | Code search MCP for Claude Code. Make entire codebase the context for any coding agent. |
| [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin) | 9.4k | JavaScript | Gemini CLI | an open-source alternative to the dots, bots and muses of the world, run an office of claude code/codex like agents on your laptop, sandboxes or anywhere, uses your existing subscriptions |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 8.7k | TypeScript | Skills | A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility with coding agents such as Antigravity, Gemini CLI, Claude Code, Cursor. |
| [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | 8.5k | JavaScript | Gemini CLI | 🦸 AI 编程超能力 · 中文增强版 — superpowers（250k+ ⭐）完整汉化 + 4 个中国原创 skills，让 Claude Code / Copilot CLI / Hermes Agent / Cursor / Windsurf / Kiro / Gemini CLI / Qoder 等 26 款 AI 编程工具真正会干活 |
| [Prat011/awesome-llm-skills](https://github.com/Prat011/awesome-llm-skills) | 1.8k | Python | Meta | A curated list of awesome LLM and AI Agent Skills, resources and tools for customising AI Agent workflows - that works with Claude Code, Codex, Gemini CLI and your custom AI Agents |
| [bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) | 1.4k | Python | Meta | Curated directory of terminal-native AI coding agents and the harnesses that orchestrate them. Covers open-source tools (Pi, OpenCode, Aider, Goose), platform agents (Claude Code, Codex, Gemini CLI), parallel runners, au |
| [gemini-cli-extensions/security](https://github.com/gemini-cli-extensions/security) | 794 | TypeScript | Extensions | Google&#x27;s Security extension for the Gemini CLI that finds vulnerabilities in your code changes and pull requests. |
| [Piebald-AI/awesome-gemini-cli](https://github.com/Piebald-AI/awesome-gemini-cli) | 589 | — | Extensions | A curated list of awesome tools, extensions, and resources for Gemini CLI. |
| [gemini-cli-extensions/code-review](https://github.com/gemini-cli-extensions/code-review) | 534 | — | Extensions | Google&#x27;s Code Review extension for the Gemini CLI that reviews your code changes |
| [gemini-cli-extensions/stitch](https://github.com/gemini-cli-extensions/stitch) | 483 | — | Extensions | The Stitch extension for Gemini CLI enables you to interact with the Stitch MCP server using natural language commands.  |
| [galdawave/pickle-rick-extension](https://github.com/galdawave/pickle-rick-extension) | 452 | TypeScript | Extensions | This extension transforms the Gemini CLI into &quot;Pickle Rick,&quot; a hyper-intelligent, arrogant, yet extremely competent  engineering persona. It enforces a rigid, iterative software development lifecycle through continuous A |
| [gemini-cli-extensions/jules](https://github.com/gemini-cli-extensions/jules) | 412 | JavaScript | Extensions | A Gemini CLI extension that allows you to use the Gemini CLI to orchestrate the Jules asynchronous agent to perform coding tasks like bug fixing, refactoring, and dependency updates. |
| [harish-garg/gemini-cli-prompt-library](https://github.com/harish-garg/gemini-cli-prompt-library) | 409 | — | Extensions | A curated library of high-quality, professionally crafted prompts for common development tasks. Save time and improve your AI interactions with battle-tested prompt templates. You can install it as an Gemini CLI Extensio |
| [zszszszsz/.config](https://github.com/zszszszsz/.config) | 365 | Shell | Extensions | # # Automatically generated file; DO NOT EDIT. # OpenWrt Configuration # CONFIG_MODULES=y CONFIG_HAVE_DOT_CONFIG=y # CONFIG_TARGET_sunxi is not set # CONFIG_TARGET_apm821xx is not set # CONFIG_TARGET_ath25 is not set CON |
| [gemini-cli-extensions/ralph](https://github.com/gemini-cli-extensions/ralph) | 327 | Shell | Extensions | Gemini CLI extension for Ralph loops |
| [seb1n/awesome-ai-agent-skills](https://github.com/seb1n/awesome-ai-agent-skills) | 242 | Python | Meta | 103 ready-to-use AI agent skills for Claude Code, OpenAI Codex, Gemini CLI, Cursor, GitHub Copilot, Windsurf, and other Agent Skills-compatible tools. Complete SKILL.md workflows—not a link directory. |
| [jduncan-rva/skill-porter](https://github.com/jduncan-rva/skill-porter) | 193 | JavaScript | Extensions | Universal tool to convert Claude Code skills to Gemini CLI extensions and vice versa |
| [GoekeLab/awesome-genomic-skills](https://github.com/GoekeLab/awesome-genomic-skills) | 129 | — | Meta | A curated list of awesome genomics and bioinformatics agentic skills, MCPs and benchmarks for Claude Code, Copilot, Codex, Cursor, Gemini CLI, etc |
| [gmh5225/awesome-skills](https://github.com/gmh5225/awesome-skills) | 97 | — | Meta | A curated list of Agent Skills, resources, and tools for AI coding agents like Claude Code, Codex, Gemini CLI, GitHub Copilot, and more. |
| [Piebald-AI/awesome-gemini-cli-extensions](https://github.com/Piebald-AI/awesome-gemini-cli-extensions) | 91 | — | Meta | A curated list of awesome Gemini CLI extensions. |

<a id="cat-other-coding-agents"></a>
## Other Coding Agents (Aider, Cline, Roo, Windsurf, OpenCode, Continue)
**Інші кодингові агенти**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | 10.9k | JavaScript | OpenCode | A curated list of awesome plugins, themes, agents, projects, and resources for https://opencode.ai |
| [intellectronica/ruler](https://github.com/intellectronica/ruler) | 3.0k | TypeScript | Windsurf | Ruler — apply the same rules to all coding agents |
| [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) | 2.3k | — | OpenCode | List of agent orchestrators |
| [GreatScottyMac/RooFlow](https://github.com/GreatScottyMac/RooFlow) | 1.2k | Python | Roo Code | RooFlow - Enhanced Memory Bank System with ☢️Footgun Power☢️  Next-gen Memory Bank system with five integrated modes and system-level customization. Uses Roo Code&#x27;s experimental &quot;Footgun&quot; feature for deep AI assistant cu |
| [instructa/ai-prompts](https://github.com/instructa/ai-prompts) | 1.1k | JavaScript | Windsurf | Curated AI Prompts for Cursor Rules, Cline, Windsurf and Github Copilot |
| [Bhartendu-Kumar/rules_template](https://github.com/Bhartendu-Kumar/rules_template) | 1.1k | — | Windsurf | If using CLINE/RooCode/Cursor/Windsurf Setup these rules. Usable for newbies riding AI wave and experienced folks both . Combines: (1) Memory,(2) Reasoning into subtasks (3) Prompts for best practices. |
| [pathintegral-institute/mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh) | 1.0k | Python | Cline | CLI MCP package manager &amp; registry for all platforms and all clients. Search &amp; configure MCP servers. Advanced Router &amp; Profile features. |
| [perrypixel/10x-Tool-Calls](https://github.com/perrypixel/10x-Tool-Calls) | 852 | Python | Windsurf | 10x-Tool-Calls is a lightweight rules file designed to help you maximize the value of your monthly AI coding tool calls, enabling you to get more done with fewer requests. |
| [infragate/capa](https://github.com/infragate/capa) | 713 | TypeScript | Windsurf | One capabilities.yaml wires skills, tools, rules, sub-agents, MCP servers, and plugins into Cursor, Claude Code, Codex, Windsurf, GitHub Copilot, and 30+ other AI coding agents |
| [evanca/flutter-ai-rules](https://github.com/evanca/flutter-ai-rules) | 669 | Shell | Windsurf | Flutter AI Skills and Rules for Claude, Codex, Cursor, and Other AI-Powered IDEs |
| [WoJiSama/skill-based-architecture](https://github.com/WoJiSama/skill-based-architecture) | 619 | Shell | Windsurf | A meta-skill that produces skills. Point it at any codebase and it distills the project&#x27;s rules, workflows, and hard-won lessons into a dedicated skills/&lt;name&gt;/ directory — a project skill that becomes the single source  |
| [botingw/rulebook-ai](https://github.com/botingw/rulebook-ai) | 614 | Python | Windsurf | Elevate vibe coding to vibe engineering: Get consistent Github Copilot custom instructions, Cursor, Roo Code, Cline, Windsurf, Claude Code, Gemini Cli, Codex CLI, kilo code, warp custom rules via a universal, managed tem |
| [FutureExcited/vibe-rules](https://github.com/FutureExcited/vibe-rules) | 528 | TypeScript | Windsurf | Save, load, distribute your AI rules |
| [lee88688/aider-composer](https://github.com/lee88688/aider-composer) | 451 | TypeScript | Aider | Aider&#x27;s VSCode extension, seamlessly integrated into VSCode  |
| [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | 424 | JavaScript | Windsurf | ai-rules is a governance framework designed to solve &quot;Architectural Decay&quot; in AI-driven development. It forces AI Agents (Cursor, Windsurf, Copilot) to respect your project&#x27;s boundaries, UI libraries, and design patterns |
| [gdli6177/mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server) | 247 | JavaScript | Cline | 这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。 |
| [biegehydra/BifrostMCP](https://github.com/biegehydra/BifrostMCP) | 225 | TypeScript | Cline | VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs |
| [priyankark/lighthouse-mcp](https://github.com/priyankark/lighthouse-mcp) | 217 | TypeScript | Cline | Allows AI assistants such as Amp/Cline/Cursor/Claude Code/Codex/GitHub Copilot to use Google&#x27;s lighthouse tool to measure perf metrics for your webpage. You can then run an agentic loop and get the assistants to optimize |
| [jtgsystems/Custom-Modes-Roo-Code](https://github.com/jtgsystems/Custom-Modes-Roo-Code) | 185 | Python | Roo Code | 🚀 Custom modes for Roo Code VS Code extension - Enhanced AI coding assistance configurations |
| [enescingoz/roocode-workspace](https://github.com/enescingoz/roocode-workspace) | 177 | — | Roo Code | The roocode-workspace repository is a project template designed to simplify development workflows using Roo Code. It integrates SPARC orchestration modes and the Memory Bank feature to provide a modular, efficient, and A |
| [makoMakoGo/fish-claude](https://github.com/makoMakoGo/fish-claude) | 173 | Python | OpenCode | Fish&#x27;s custom settings and tools about claude code, codex, oh-my-pi etc  |
| [mandatoryprogrammer/tarnish](https://github.com/mandatoryprogrammer/tarnish) | 166 | JavaScript | Aider | A Chrome extension static analysis tool to help aide in security reviews. |
| [sammcj/mcp-devtools](https://github.com/sammcj/mcp-devtools) | 162 | Go | Cline | A modular MCP server that provides commonly used developer tools for AI coding agents |
| [bromoket/x64dbg_mcp](https://github.com/bromoket/x64dbg_mcp) | 138 | C++ | Cline | Drive x64dbg with your AI. MCP server: 23 mega-tools / 153 endpoints for breakpoints, memory, disasm, tracing, anti-debug &amp; PE dumping. Claude/Cursor/Windsurf/Cline. All local. |
| [enescingoz/roo-advanced-memory-bank](https://github.com/enescingoz/roo-advanced-memory-bank) | 119 | — | Roo Code | Advanced Roo Code Memory Bank is an almost fully automated, next-generation task management system designed for seamless integration with Roo Code custom modes. Leveraging adaptive, just-in-time rule loading and persiste |

<a id="cat-mcp-ecosystem"></a>
## MCP Ecosystem (servers, registries, clients)
**Екосистема MCP**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 97.3k | — | Meta | A collection of MCP servers. |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 91.8k | TypeScript | MCP servers | Model Context Protocol Reference Servers |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 78.9k | Python | MCP | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server. |
| [upstash/context7](https://github.com/upstash/context7) | 64.2k | TypeScript | MCP servers | Context7 Platform -- Up-to-date docs for AI agents |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 54.8k | TypeScript | MCP servers | Chrome DevTools for coding agents |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 48.2k | C | MCP | Local code intelligence for developers and AI agents. Connect code, docs and infrastructure in a persistent graph, with CBM Lens, MCP tools, agent integrations and change-aware test selection. |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | 24.8k | Python | MCP servers | The official Python SDK for Model Context Protocol servers and clients |
| [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) | 15.7k | C# | MCP | Unity MCP acts as a bridge between AI assistants and your Unity Editor. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity. |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | 13.7k | TypeScript | MCP servers | The official TypeScript SDK for Model Context Protocol servers and clients |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | 12.5k | TypeScript | MCP servers | Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and se |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | 12.0k | Python | MCP | Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth! |
| [yzfly/Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH) | 7.8k | — | Meta | MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | 7.4k | Go | MCP servers | A community driven registry service for Model Context Protocol (MCP) servers. |
| [AgentDeskAI/browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp) | 7.3k | TypeScript | MCP | Monitor browser logs directly from Cursor and other MCP compatible IDEs. |
| [getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP) | 6.5k | TypeScript | MCP servers | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. |
| [jacob-bd/gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli) | 6.5k | Python | MCP servers | Programmatic access to Gemini Notebook - via command-line interface (CLI), Model Context Protocol (MCP) server, and AI agent skills. |
| [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) | 5.7k | TypeScript | MCP | Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌 |
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 5.4k | Python | Meta | The Unofficial and Awesome Home Assistant MCP Server |
| [nanbingxyz/5ire](https://github.com/nanbingxyz/5ire) | 5.4k | TypeScript | MCP servers | 5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers . |
| [IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP) | 4.6k | C# | MCP | AI Skills, MCP Tools, and CLI for Unity Engine. Full AI develop and test loop. Use cli for quick setup. Efficient token usage, advanced tools. Any C# method may be turned into a tool by a single line. Works with Claude C |
| [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | 4.4k | — | Meta | A curated list of Model Context Protocol (MCP) servers |
| [supercorp-ai/supergateway](https://github.com/supercorp-ai/supergateway) | 2.9k | TypeScript | Gateway | Run MCP stdio servers over HTTP streamable, SSE and SSE over stdio. AI gateway. |
| [punkpeye/awesome-remote-mcp-servers](https://github.com/punkpeye/awesome-remote-mcp-servers) | 2.6k | — | Meta | A collection of remote MCP servers. |
| [samanhappy/mcphub](https://github.com/samanhappy/mcphub) | 2.6k | TypeScript | Gateway | Self-hosted MCP gateway and control plane for connecting, controlling, and operating MCP servers. |
| [AmoyLab/Unla](https://github.com/AmoyLab/Unla) | 2.3k | TypeScript | Meta | 🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure mod |
| [chatmcp/mcpso](https://github.com/chatmcp/mcpso) | 2.1k | TypeScript | Meta | directory for Awesome MCP Servers |
| [composio-community/awesome-claude-plugins](https://github.com/composio-community/awesome-claude-plugins) | 2.0k | JavaScript | Meta | A curated list of Plugins that let you extend Claude Code with custom commands, agents, hooks, and MCP servers through the plugin system. |
| [fatwang2/search2ai](https://github.com/fatwang2/search2ai) | 1.3k | TypeScript | Gateway | Self-hosted search gateway for AI agents. Unified search, news and page extraction with provider fallback. REST API, MCP server and TypeScript library. |
| [alexgaoth/awesome-reverse-engineered](https://github.com/alexgaoth/awesome-reverse-engineered) | 1.2k | Python | Meta | Don&#x27;t reverse engineer it twice. 17,000+ open-source tools built by reverse engineering closed apps, APIs, devices, protocols, file formats, games and AI tools. Search site + agent skill + MCP server, refreshed nightly. |
| [Azure-Samples/AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) | 1.0k | Jupyter Notebook | Gateway | Labs to explore AI Models, MCP servers, and Agents with the AI Gateway powered by Azure API Management and Microsoft Foundry 🚀 |

<a id="cat-agent-frameworks"></a>
## Agent Frameworks & Tool Libraries (LangChain, crewAI, AutoGPT...)
**Фреймворки агентів**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio) | 30.9k | TypeScript | Composio | Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action. |
| [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | 13.4k | Java | Frameworks | LangChain4j is an idiomatic, open-source Java library for building LLM-powered applications on the JVM. It offers a unified API over popular LLM providers and vector stores, and makes implementing tool calling (including |
| [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere) | 3.8k | Java | crewAI | Portable AI agent runtime for the JVM. One @Agent class runs on Spring AI, LangChain4j, Anthropic, or 9 more behind one SPI. Token streaming, tool calls, human approvals, and governance over WebSocket, SSE, gRPC, or WebT |
| [jgravelle/AutoGroq](https://github.com/jgravelle/AutoGroq) | 1.5k | Python | crewAI | AutoGroq is a groundbreaking tool that revolutionizes the way users interact with Autogen™ and other AI assistants. By dynamically generating tailored teams of AI agents based on your project requirements, AutoGroq elimi |
| [e2b-dev/awesome-ai-sdks](https://github.com/e2b-dev/awesome-ai-sdks) | 1.2k | — | Frameworks | A database of SDKs, frameworks, libraries, and tools for creating, monitoring, debugging and deploying autonomous AI agents |
| [ArcadeAI/arcade-mcp](https://github.com/ArcadeAI/arcade-mcp) | 1.1k | Python | Frameworks | MCP Server Framework and Tool Development library for building custom capabilities into agents.  |
| [ComposioHQ/trustclaw](https://github.com/ComposioHQ/trustclaw) | 911 | TypeScript | Composio | A self-hostable personal AI agent with vector memory, Composio tools, and Telegram. |
| [shuxiachai/academic-commercialization-agent](https://github.com/shuxiachai/academic-commercialization-agent) | 808 | Python | crewAI | AI multi-agent tool that turns research papers into cited commercialization and tech-transfer assessments: TRL, patent landscape, market and risks. CrewAI + FastAPI, with a reproducible benchmark. |
| [rnadigital/agentcloud](https://github.com/rnadigital/agentcloud) | 690 | TypeScript | crewAI | Agent Cloud is like having your own GPT builder with a bunch extra goodies. The GUI features 1) RAG pipeline which can natively embed 260+ datasources 2) Create Conversational apps (like GPTs) 3) Create Multi Agent proce |
| [isaiahbjork/Auto-GPT-MetaTrader-Plugin](https://github.com/isaiahbjork/Auto-GPT-MetaTrader-Plugin) | 565 | Python | AutoGPT | The AutoGPT MetaTrader Plugin is a software tool that enables traders to connect their MetaTrader 4 or 5 trading account to Auto-GPT. |
| [Upsonic/Tiger](https://github.com/Upsonic/Tiger) | 473 | Python | crewAI | Neuralink for your AI Agents - LangChain - Autogen - CrewAI |
| [alexfazio/crewAI-quickstart](https://github.com/alexfazio/crewAI-quickstart) | 426 | Jupyter Notebook | crewAI | A collection of notebooks, cookbooks, and recipes showcasing fun and effective ways to use CrewAI&#x27;s agentic workflow implementations and tools. |
| [Repello-AI/Agent-Wiz](https://github.com/Repello-AI/Agent-Wiz) | 398 | Python | crewAI | A CLI tool for threat modeling and visualizing AI agents built using popular frameworks like LangGraph, AutoGen, CrewAI, and more. |
| [isaiahbjork/Auto-GPT-Crypto-Plugin](https://github.com/isaiahbjork/Auto-GPT-Crypto-Plugin) | 275 | Python | AutoGPT | The AutoGPT Crypto Plugin is a software tool that enables traders to connect their Crypto wallet or exchange to Auto-GPT. |
| [gravelBridge/AutoGPT-Web-Interaction](https://github.com/gravelBridge/AutoGPT-Web-Interaction) | 261 | Python | AutoGPT | A plugin to enable AutoGPT to interact with websites. |
| [GetStream/ai-agent-tools-catalog](https://github.com/GetStream/ai-agent-tools-catalog) | 241 | — | crewAI | Explore the must-have external ready-made toolkits to integrate with your AI agents built with Python and TypeScript |
| [velocitybolt/open-extract](https://github.com/velocitybolt/open-extract) | 192 | Python | crewAI | Structured Data Extractor for AI Agents. Search your documents or the web for specific data and get it back in JSON or Markdown in a single tool call. |
| [doutv/Auto-GPT-Notion](https://github.com/doutv/Auto-GPT-Notion) | 188 | Python | AutoGPT | Auto-GPT Notion Plugin |
| [gravelBridge/AutoGPT-BingAI](https://github.com/gravelBridge/AutoGPT-BingAI) | 166 | Python | AutoGPT | An AutoGPT plugin to enable Bing AI in AutoGPT. |
| [kurtosis-tech/autogpt-package](https://github.com/kurtosis-tech/autogpt-package) | 164 | Starlark | AutoGPT | It&#x27;s like Auto-GPT met Brew. The easiest and fastest way to get started with AutoGPT with any backend of your choice &amp; whatever plugins you may need |
| [IntelligenzaArtificiale/Free-personal-AI-Assistant-with-plugin](https://github.com/IntelligenzaArtificiale/Free-personal-AI-Assistant-with-plugin) | 162 | Python | AutoGPT | 🤗 Would you like to use GPT4 with Plugins but don&#x27;t want to pay $20/month? This is the solution!  With this repository you can have free clone of ChatGPT with plugin  |
| [jpetzke/AutoGPT-YouTube](https://github.com/jpetzke/AutoGPT-YouTube) | 124 | Python | AutoGPT | A plugin for AutoGPT that allows various operations on YouTube, such as downloading Videos |
| [sqliteai/adam](https://github.com/sqliteai/adam) | 124 | C | Frameworks | An embeddable cross-platform AI agent library written in C. Cloud and local LLMs, tool calling, long-term memory, voice, sessions, research mode, self-evolving loops. The SQLite of agent frameworks: small, portable, just |
| [kbeaugrand/SemanticKernel.Assistants](https://github.com/kbeaugrand/SemanticKernel.Assistants) | 114 | C# | Semantic Kernel | Microsoft Semantic Kernel Assistants This enables the usage of assistants for the Semantic Kernel.  It provides different scenarios for the usage of assistants such as:  Assistant with Semantic Kernel plugins Multi-Assis |
| [gravelBridge/AutoGPT-Discord](https://github.com/gravelBridge/AutoGPT-Discord) | 93 | Python | AutoGPT | A plugin to enable you to control your AutoGPT instance from Discord. |
| [felipearosr/RAG-LlamaIndex](https://github.com/felipearosr/RAG-LlamaIndex) | 80 | Python | LlamaIndex | OpenAI document chatbot using llama-index, pinecone and chainlit. With incremental features, giving you the tools to go from a basic RAG into an advanced one. |
| [shinzo-labs/shinzo-ts](https://github.com/shinzo-labs/shinzo-ts) | 68 | TypeScript | Frameworks | TypeScript SDK for MCP server observability, built on OpenTelemetry. Gain insight into agent usage patterns, contextualize tool calls, and analyze server performance across platforms. Integrate with any OpenTelemetry ing |
| [kbeaugrand/SemanticKernel.Connectors.Memory.SqlServer](https://github.com/kbeaugrand/SemanticKernel.Connectors.Memory.SqlServer) | 55 | C# | Semantic Kernel | SQL Server connector for Semantic Kernel plugin and Kernel Memory |
| [anthonypuppo/sk-nl2ef-plugin](https://github.com/anthonypuppo/sk-nl2ef-plugin) | 54 | C# | Semantic Kernel | A ChatGPT plugin built with Semantic Kernel that queries a database via natural language. Winner of Microsoft&#x27;s first Semantic Kernel hackathon in the &quot;Most Useful for the Enterprise&quot; category. |
| [BLaZeKiLL/Codeblaze.SemanticKernel](https://github.com/BLaZeKiLL/Codeblaze.SemanticKernel) | 53 | C# | Semantic Kernel | Some Cool Semantic Kernel Plugins |

<a id="cat-automation-workflows"></a>
## Automation Platforms (n8n, Dify, Flowise...)
**Платформи автоматизації**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 209.6k | TypeScript | MCP servers | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. |
| [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) | 26.3k | — | n8n | 280+ free n8n automation templates — ready-to-use workflows for Gmail, Telegram, Slack, Discord, WhatsApp, Google Drive, Notion, OpenAI, and more. AI agents, RAG   chatbots, email automation, social media, DevOps, and do |
| [langbot-app/LangBot](https://github.com/langbot-app/LangBot) | 18.7k | Python | Dify | Production-grade platform for building agentic IM bots - 生产级多平台智能机器人开发平台/ Agent、知识库编排、插件系统 / Bots for Discord / Slack / LINE / Telegram / WeChat(企业微信, 企微智能机器人, 公众号) / 飞书 / 钉钉 / QQ / Matrix e.g. Integrated with ChatGPT(GP |
| [restyler/awesome-n8n](https://github.com/restyler/awesome-n8n) | 3.0k | — | n8n | Useful n8n resources: list of community nodes and tutorials |
| [dariubs/awesome-workflow-automation](https://github.com/dariubs/awesome-workflow-automation) | 1.3k | — | n8n | A curated list of Workflow Automation  Software, Engines and Tools |
| [junjiem/dify-plugin-repackaging](https://github.com/junjiem/dify-plugin-repackaging) | 768 | Shell | Dify | Scripting tool for downloading Dify plugin package from Dify Marketplace and Github and repackaging [true] offline package. |
| [langgenius/dify-official-plugins](https://github.com/langgenius/dify-official-plugins) | 641 | Python | Dify | — |
| [langgenius/dify-plugins](https://github.com/langgenius/dify-plugins) | 561 | Python | Dify | All Dify Plugins listed in Dify Marketplace, plus illustrated plugin examples. |
| [felipfr/awesome-n8n-workflows](https://github.com/felipfr/awesome-n8n-workflows) | 414 | — | n8n | A curated collection of awesome n8n workflows for automation, integration, and productivity. Explore ready-to-use JSON workflows for analytics, communication, CRM, e-commerce, finance, HR, marketing, monitoring, security |
| [umanamente/n8n-nodes-globals](https://github.com/umanamente/n8n-nodes-globals) | 349 | TypeScript | n8n | N8N community node that allows users to create global constants and use them in all their workflows |
| [bowenliang123/markdown-exporter](https://github.com/bowenliang123/markdown-exporter) | 274 | Python | Dify | An Agent Skill and Dify plugin to transform Markdown to files of DOCX, PPTX, XLSX, PNG, PDF, HTML, MD, CSV, JSON, XML. |
| [WoodGoose/awesome-cow-plugins](https://github.com/WoodGoose/awesome-cow-plugins) | 213 | — | Dify | 这个仓库主要是收集CoW(chatgpt-on-wechat)与DoW(dify-on-wechat)的插件，欢迎补充加入看到、用过或新开发的插件。 |
| [Synaptiv-AI/awesome-n8n](https://github.com/Synaptiv-AI/awesome-n8n) | 193 | — | n8n | Welcome to Awesome n8n – your new favorite destination for everything related to advanced n8n workflows, templates, and resources. After a monumental effort and countless hours of work, we have successfully created a cle |
| [junjiem/dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse) | 186 | Python | Dify | Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools |
| [toema/n8n-playwright](https://github.com/toema/n8n-playwright) | 177 | TypeScript | n8n | n8n-community-node-package for browser automation using Playwright |
| [3dify-project/dify-mcp-client](https://github.com/3dify-project/dify-mcp-client) | 172 | Python | Dify | MCP Client as an Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK. |
| [umanamente/n8n-nodes-imap](https://github.com/umanamente/n8n-nodes-imap) | 166 | TypeScript | n8n | This is an n8n community node that adds support for IMAP email servers. |
| [langgenius/dify-plugin-sdks](https://github.com/langgenius/dify-plugin-sdks) | 150 | Python | Dify | SDK for Dify plugins |
| [lqshow/awesome-n8n-workflows](https://github.com/lqshow/awesome-n8n-workflows) | 144 | HTML | n8n | A curated collection of practical n8n workflows for automation enthusiasts |
| [junjiem/dify-plugin-agent-mcp_sse](https://github.com/junjiem/dify-plugin-agent-mcp_sse) | 139 | Python | Dify | Dify 1.0 Plugin Support MCP Tools Agent strategies |
| [ScraperNode/awesome-n8n-templates](https://github.com/ScraperNode/awesome-n8n-templates) | 121 | Astro | n8n | 🔥 The largest open-source collection of n8n workflow templates — 8,697+ ready-to-import workflows across 25 categories, 236 integrations, and 11 use cases. |
| [shodgson/n8n-nodes-twenty](https://github.com/shodgson/n8n-nodes-twenty) | 120 | JavaScript | n8n | n8n community node for Twenty CRM  |
| [mbakgun/n8n-slack-socket-mode](https://github.com/mbakgun/n8n-slack-socket-mode) | 93 | TypeScript | n8n | This n8n community node enables Slack Socket Mode within your n8n workflows.  Note : Heym (https://heym.run) has slack event subs capabilities |
| [themookfactory/awesome-n8n-msp-nodes](https://github.com/themookfactory/awesome-n8n-msp-nodes) | 76 | — | n8n | A curated list of N8N nodes related to MSP tools (RMM, PSA, Distributors, etc). |
| [rmyndharis/OpenWA-n8n](https://github.com/rmyndharis/OpenWA-n8n) | 72 | TypeScript | n8n | OpenWA Community Nodes for n8n - WhatsApp automation workflow nodes |
| [Azuka-Labs/awesome-n8n-templates-main](https://github.com/Azuka-Labs/awesome-n8n-templates-main) | 53 | — | n8n | 200+ n8n Automations |
| [rorubyy/n8n-nodes-openai-langfuse](https://github.com/rorubyy/n8n-nodes-openai-langfuse) | 44 | TypeScript | n8n | An n8n community node that brings Langfuse observability to your OpenAI chat workflows. |

<a id="cat-local-offline"></a>
## Local / Offline Agents (Ollama, llama.cpp)
**Локальні агенти**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | 13.8k | Python | Local LLM | One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows. |
| [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | 11.4k | TypeScript | Local LLM | Open-source agentic workspace enterprises can make their own. Connect the systems you already run — 100+ integrations, MCP, chat tools, apps, browser, local files — with shared memory. Any agent (Claude Code, Codex), any |
| [gptme/gptme](https://github.com/gptme/gptme) | 4.5k | Python | Local LLM | Your agent in your terminal, equipped with local tools: writes code, uses the terminal, browses the web. Make your own persistent autonomous agent on top! |
| [StartupHakk/OpenMonoAgent.ai](https://github.com/StartupHakk/OpenMonoAgent.ai) | 1.9k | C# | Local LLM | (BETA) AI shouldn&#x27;t have a meter. Unlimited tokens. Forever. Your machine. Your agent. Use it from anywhere. Terminal-native coding agent powered by local LLMs — 100% open source, free forever, and installed with a singl |
| [ling-stack-org/ling-stack](https://github.com/ling-stack-org/ling-stack) | 991 | TypeScript | Local LLM | Local-first AI teammate workspace. Bring your own models and keep project conversations, tool approvals, and results together. |
| [artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) | 893 | TypeScript | Local LLM | Local-first, agent-native control plane for ComfyUI — MCP server + sidebar agent that generates images, video &amp; audio, authors and runs workflows, and edits your live graph in natural language on ANY LLM (Claude, ChatGPT |
| [jonigl/mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama) | 836 | Python | Local LLM | Harness the power of local LLMs with this TUI MCP Client for Ollama. Featuring all core MCP primitives (tools, prompts, resources), agent mode, multi-server, model switching, streaming responses, human-in-the-loop, think |
| [Haervwe/open-webui-tools](https://github.com/Haervwe/open-webui-tools) | 832 | Python | Ollama | Open‑WebUI Tools is a modular toolkit designed to extend and enrich your Open WebUI instance, turning it into a powerful AI workstation. With a suite of over 15 specialized tools, function pipelines, and filters, this pr |
| [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory) | 790 | TypeScript | Local LLM | Stop re-teaching your agent. Make your agent&#x27;s memory work like a brain. Hippo is long-term memory for coding agents. It&#x27;s a critical layer for your AI harness that connects across your different tools (Cursor, Claude Co |
| [mikehasa/agentacct](https://github.com/mikehasa/agentacct) | 755 | Python | Local LLM | See what your coding agents did and what it cost. Breaks each task down into work steps — tools used, files changed, tests run, time and tokens spent. Local-first dashboard for Claude Code, Codex, OpenCode, and more. No  |
| [caspianmoon/memoripy](https://github.com/caspianmoon/memoripy) | 692 | Python | Local LLM | Evidence-first local memory for AI agents with temporal versions, admission policies, citations, explainable recall, MCP, and audit tooling. |
| [alexziskind1/llama-throughput-lab](https://github.com/alexziskind1/llama-throughput-lab) | 475 | Python | llama.cpp | Interactive launcher and benchmarking harness for llama.cpp server throughput, with tests, sweeps, and round‑robin load tools. |
| [classfang/AIHub](https://github.com/classfang/AIHub) | 421 | Vue | Ollama | 一款集合多家大模型能力的客户端。拥有丰富的个性化功能。现已支持：OpenAI，Ollama，谷歌 Gemini，讯飞星火，百度文心，阿里通义，天工，月之暗面，智谱，阶跃星辰，DeepSeek 🎉🎉🎉。A collection of large model capabilities of the client. Has a wealth of personalized functions. English UI support. |
| [llm-guy/jarvis](https://github.com/llm-guy/jarvis) | 340 | Python | Ollama | Jarvis is a voice-activated, conversational AI assistant powered by a local LLM (Qwen via Ollama). It listens for a wake word, processes spoken commands using a local language model with LangChain, and responds out loud  |
| [HoldMyBeer-gg/blenderwright](https://github.com/HoldMyBeer-gg/blenderwright) | 187 | Python | llama.cpp | MCP server for Blender. Hundreds of tools for modeling, materials, rendering and more, driven by Claude, Cursor, Codex, Ollama, llama.cpp, or any MCP client. |
| [civai-technologies/cursor-agent](https://github.com/civai-technologies/cursor-agent) | 137 | Python | Ollama | Cursor Agent Tools - A Python-based AI agent that replicates Cursor&#x27;s coding assistant capabilities, enabling function calling, code generation, and intelligent coding assistance with Claude, OpenAI, and locally hosted O |
| [icebaker/ruby-nano-bots](https://github.com/icebaker/ruby-nano-bots) | 128 | Lua | Ollama | Ruby Implementation of Nano Bots: small, AI-powered bots that can be easily shared as a single file, designed to support multiple providers such as Anthropic Claude, Cohere Command, Google Gemini, Maritaca AI, Mistral AI |
| [Pyenb/Ollama-models](https://github.com/Pyenb/Ollama-models) | 97 | Shell | Ollama | A collection of zipped Ollama models for offline use. Simply download, extract, and set up your desired model anywhere. |
| [KochC/opencode-llm-proxy](https://github.com/KochC/opencode-llm-proxy) | 86 | JavaScript | Ollama | Local OpenCode-backed LLM gateway for OpenAI, Anthropic, Gemini, and Responses API-compatible tools, with streaming and tool/function calling. |
| [Oct4Pie/toolbridge](https://github.com/Oct4Pie/toolbridge) | 81 | TypeScript | Ollama | Enable tool/function calling for any LLM, in OpenAI and Ollama API formats, adding universal function calling to models without native support. Use local or cloud models with full agent capabilities. |
| [yazon/flexllama](https://github.com/yazon/flexllama) | 62 | Python | llama.cpp | 🚀 FlexLLama - Lightweight self-hosted tool for running multiple llama.cpp server instances with OpenAI v1 API compatibility and multi-GPU support |
| [vibheksoni/VerbalCodeAi](https://github.com/vibheksoni/VerbalCodeAi) | 59 | Python | Ollama | VerbalCodeAI is a free, open-source AI tool that simplifies codebase navigation in your terminal, using Python 3.11.6 and Ollama. It indexes projects locally and quickly answers questions like “Where’s this function?”, s |

<a id="cat-chat-platforms"></a>
## Chat Platforms (ChatGPT, Slack, Telegram, Discord)
**Чат-платформи**

| Repository | ⭐ | Lang | Type | Description |
|---|---|---|---|---|
| [OpenCoworkAI/open-cowork](https://github.com/OpenCoworkAI/open-cowork) | 2.3k | TypeScript | Slack | Open-source AI agent desktop app for Windows &amp; macOS. One-click install Claude Code, MCP tools, and Skills — with sandbox isolation, multi-model support, and Feishu/Slack integration. |
| [lemma-work/lemma-platform](https://github.com/lemma-work/lemma-platform) | 639 | Python | Slack | Multiplayer harness that shapes around your work. Agents, apps and workflows your team shares, used from Slack, Telegram, WhatsApp, Teams, Email, Web or your own AI agent. |
| [shaharia-lab/slackcli](https://github.com/shaharia-lab/slackcli) | 265 | TypeScript | Slack | Slack CLI for humans and AI agents. Read, send, search and reply across one or many Slack workspaces from the terminal. No Slack app needed. |
| [suitedaces/dorabot](https://github.com/suitedaces/dorabot) | 247 | TypeScript | Slack | macOS app for 24/7 AI agents in an IDE with memory, scheduled tasks, browser use + access to Whatsapp, Telegram, Slack. |
| [tercumantanumut/selene](https://github.com/tercumantanumut/selene) | 173 | TypeScript | Slack | Selene is a desktop app that runs AI agents on your machine. Connect them to your WhatsApp, Telegram, Slack, or Discord. Write code, generate images, build personal assistants. All from one place. Your data stays on your |
| [zhinjs/zhin](https://github.com/zhinjs/zhin) | 137 | TypeScript | Telegram | AI-native TypeScript bot framework — one codebase for 20+ chat platforms (QQ, Discord, Telegram, Slack, WeChat…). Opt-in AI agent with MCP, tools &amp; security policies. &lt;10MB core. |
| [AbuZar-Ansarii/PocketStrike-AI](https://github.com/AbuZar-Ansarii/PocketStrike-AI) | 105 | Python | Telegram | Turn Android Termux into an autonomous AI agent and security orchestrator. Powered by a local ReAct framework with 50 system tools and MCP support, a background task   │ scheduler, on-device ADB controls, and a unified W |
| [0xtbug/telbot](https://github.com/0xtbug/telbot) | 85 | Go | Telegram | Go-based tool for managing Telkomsel accounts via Telegram Bot, Terminal CLI, or MCP Server (for AI agents). |
| [Bredrumb/TomoriBot](https://github.com/Bredrumb/TomoriBot) | 64 | TypeScript | Discord | A highly customizable personal AI assistant for Discord featuring smart agentic AI features such as memory, personas, tool usage, and more! ｜ 長期記憶やペルソナ、ツール連携を完備。 次世代の「自律型AIエージェント」Discordボット！ |
| [s-nagaev/chibi](https://github.com/s-nagaev/chibi) | 54 | Python | Telegram | Your Digital Companion. Self-hosted Telegram bot orchestrating multiple AI providers (OpenAI, Anthropic, Google, xAI, DeepSeek, Mistral, Alibaba, MiniMax) with autonomous agent capabilities, MCP integrations, and async t |

---

## 🌐 Big web registries (not GitHub repos, but worth knowing)

| Registry | Scale | Notes |
|---|---|---|
| [Official MCP Registry](https://registry.modelcontextprotocol.io) | canonical metadata | Authoritative source; aggregators poll it |
| [Glama](https://glama.ai/mcp/servers) | 100k+ servers | Largest directory, quality/maintenance grades |
| [Smithery](https://smithery.ai) | ~26k servers | Registry + hosted servers with managed OAuth |
| [mcp.so](https://mcp.so) | ~20k servers | Community submissions, also lists skills |
| [PulseMCP](https://www.pulsemcp.com) | ~22k servers | Editorial curation + ecosystem news |
| [cursor.directory](https://cursor.directory) | community hub | Cursor rules & MCP for Cursor |

## 🤝 Contributing

Found a great plugin/skill pack that's missing? Open an issue or PR with: repo URL, target agent category, and one-line description. Quality bar: active (non-archived), ≥40 stars, real installable content (not just a blog post).

## 🔁 How the index is built

- Collected automatically via the official **GitHub Search API** (`tools/collect.py`), curated (`tools/curate.py`), rendered by `tools/gen_readme.py` (data in `data/repos.json`).
- Filters: stars ≥ 40, not archived, deduplicated across categories. Snapshot: **2026-11-05**.
- Browsed **by agent platform** — pick your agent, see its whole extension ecosystem in one table.

## 📄 License

This index: MIT. The linked projects keep their own licenses — check each repo before reuse.
