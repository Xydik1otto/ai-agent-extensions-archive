#!/usr/bin/env python3
"""Generate README.md from data/repos.json (AI-agent extensions indexed by agent platform)."""
import json, datetime, html, os

CAT_TITLES = {
    "claude-code": ("Claude Code (plugins, skills, subagents, hooks)", "Claude Code"),
    "skills-marketplaces": ("Agent Skills & Marketplaces (cross-agent)", "Скіли та маркетплейси"),
    "cursor": ("Cursor (rules, extensions)", "Cursor"),
    "github-copilot": ("GitHub Copilot (extensions, agents)", "GitHub Copilot"),
    "openai-codex": ("OpenAI Codex CLI", "OpenAI Codex"),
    "gemini-cli": ("Gemini CLI (extensions)", "Gemini CLI"),
    "other-coding-agents": ("Other Coding Agents (Aider, Cline, Roo, Windsurf, OpenCode, Continue)", "Інші кодингові агенти"),
    "mcp-ecosystem": ("MCP Ecosystem (servers, registries, clients)", "Екосистема MCP"),
    "agent-frameworks": ("Agent Frameworks & Tool Libraries (LangChain, crewAI, AutoGPT...)", "Фреймворки агентів"),
    "automation-workflows": ("Automation Platforms (n8n, Dify, Flowise...)", "Платформи автоматизації"),
    "local-offline": ("Local / Offline Agents (Ollama, llama.cpp)", "Локальні агенти"),
    "chat-platforms": ("Chat Platforms (ChatGPT, Slack, Telegram, Discord)", "Чат-платформи"),
}

CAT_ORDER = list(CAT_TITLES.keys())

def fmt_num(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)

def main():
    with open("data/repos.json", encoding="utf-8") as f:
        data = json.load(f)

    total = sum(len(v) for v in data.values())
    today = datetime.date.today().isoformat()

    lines = []
    a = lines.append
    a("# 🤖 AI Agent Extensions Archive / Карта розширень для ШІ-агентів")
    a("")
    a(f"**A map of plugins, skills, MCP servers, rules and upgrades for AI coding agents** — Claude Code, Cursor, GitHub Copilot, Codex, Gemini CLI, Cline, Windsurf, Aider and more, organized **by agent platform**. ({total} repos, last refreshed {today})")
    a("")
    a("> **Українською:** індекс плагінів, скілів, MCP-серверів, rules-колекцій та апгрейдів для ШІ-агентів, розбитий **за агентами**. Кожен пункт — посилання на оригінальний репозиторій GitHub. Індекс оновлюється автоматично через офіційний GitHub Search API (див. [`tools/collect.py`](tools/collect.py)).")
    a("")
    a("> ⚠️ All links point to the **original repositories** — nothing is copied; each repo keeps its own license. / Усі посилання ведуть на оригінальні репозиторії — нічого не копіюється, ліцензії зберігаються у авторів.")
    a("")
    a("---")
    a("")
    a("## 📑 Table of Contents")
    a("")
    for cat in CAT_ORDER:
        repos = data.get(cat, [])
        if not repos:
            continue
        en, _ = CAT_TITLES[cat]
        a(f'- [`{en}`](#cat-{cat}) — {len(repos)} repos')
    a("")
    a("---")
    a("")

    for cat in CAT_ORDER:
        repos = data.get(cat, [])
        if not repos:
            continue
        en, uk = CAT_TITLES[cat]
        a(f'<a id="cat-{cat}"></a>')
        a(f"## {en}")
        a(f"**{uk}**")
        a("")
        a("| Repository | ⭐ | Lang | Type | Description |")
        a("|---|---|---|---|---|")
        for r in repos:
            desc = html.escape((r["desc"] or "").replace("|", "/")) or "—"
            lang = r["lang"] or "—"
            kind = r.get("kind", "")
            a(f'| [{r["full_name"]}]({r["url"]}) | {fmt_num(r["stars"])} | {lang} | {kind} | {desc} |')
        a("")

    a("---")
    a("")
    a("## 🌐 Big web registries (not GitHub repos, but worth knowing)")
    a("")
    a("| Registry | Scale | Notes |")
    a("|---|---|---|")
    a("| [Official MCP Registry](https://registry.modelcontextprotocol.io) | canonical metadata | Authoritative source; aggregators poll it |")
    a("| [Glama](https://glama.ai/mcp/servers) | 100k+ servers | Largest directory, quality/maintenance grades |")
    a("| [Smithery](https://smithery.ai) | ~26k servers | Registry + hosted servers with managed OAuth |")
    a("| [mcp.so](https://mcp.so) | ~20k servers | Community submissions, also lists skills |")
    a("| [PulseMCP](https://www.pulsemcp.com) | ~22k servers | Editorial curation + ecosystem news |")
    a("| [cursor.directory](https://cursor.directory) | community hub | Cursor rules & MCP for Cursor |")
    a("")
    a("## 🤝 Contributing")
    a("")
    a("Found a great plugin/skill pack that's missing? Open an issue or PR with: repo URL, target agent category, and one-line description. Quality bar: active (non-archived), ≥40 stars, real installable content (not just a blog post).")
    a("")
    a("## 🔁 How the index is built")
    a("")
    a("- Collected automatically via the official **GitHub Search API** (`tools/collect.py`), curated (`tools/curate.py`), rendered by `tools/gen_readme.py` (data in `data/repos.json`).")
    a(f"- Filters: stars ≥ 40, not archived, deduplicated across categories. Snapshot: **{today}**.")
    a("- Browsed **by agent platform** — pick your agent, see its whole extension ecosystem in one table.")
    a("")
    a("## 📄 License")
    a("")
    a("This index: MIT. The linked projects keep their own licenses — check each repo before reuse.")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"README.md written: {total} repos across {sum(1 for v in data.values() if v)} categories")

if __name__ == "__main__":
    main()
