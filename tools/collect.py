#!/usr/bin/env python3
"""Collect top GitHub repos: plugins, skills, MCP servers & extensions for AI agents,
grouped by agent platform. Uses `gh api search/repositories` (official free API)."""
import json, subprocess, time, os

CATEGORIES = {
    "claude-code": [
        ("topic:claude-code+plugins", "Claude Code"), ("claude+code+skills", "Skills"),
        ("claude+code+subagents", "Subagents"), ("claude+code+hooks", "Hooks"),
        ("claude+commands+slash", "Slash commands"), ("awesome+claude+code", "Meta"),
        ("claude+code+statusline", "UI/statusline"),
    ],
    "skills-marketplaces": [
        ("agent+skills+collection", "Skills"), ("topic:agent-skills", "Skills"),
        ("claude+skills+marketplace", "Marketplace"), ("awesome+claude+skills", "Meta"),
        ("agent+skills+registry", "Registry"), ("skills+for+agents+repository", "Skills"),
    ],
    "cursor": [
        ("topic:cursor-rules", "Rules"), ("cursor+rules+collection", "Rules"),
        ("cursor.directory+rules", "Rules"), ("cursor+ide+extensions", "Extensions"),
        ("cursor+mcp+tools", "MCP"),
    ],
    "github-copilot": [
        ("awesome+copilot", "Meta"), ("copilot+extensions+agent", "Extensions"),
        ("copilot+instructions+collection", "Instructions"), ("github+copilot+custom+agents", "Agents"),
    ],
    "openai-codex": [
        ("codex+cli+plugins", "Codex CLI"), ("topic:openai-codex", "Codex"),
        ("codex+agent+skills", "Skills"), ("openai+codex+extensions", "Extensions"),
    ],
    "gemini-cli": [
        ("topic:gemini-cli", "Gemini CLI"), ("gemini+cli+extensions", "Extensions"),
        ("awesome+gemini+cli", "Meta"), ("gemini+cli+skills", "Skills"),
    ],
    "other-coding-agents": [
        ("aider+extensions", "Aider"), ("cline+mcp+tools", "Cline"),
        ("windsurf+rules", "Windsurf"), ("opencode+plugins", "OpenCode"),
        ("roo+code+modes", "Roo Code"), ("continue+dev+extensions", "Continue"),
        ("awesome+opencode", "OpenCode"),
    ],
    "mcp-ecosystem": [
        ("awesome+mcp+servers", "Meta"), ("topic:mcp-server", "MCP servers"),
        ("mcp+registry+directory", "Registry"), ("mcp+gateway+server", "Gateway"),
        ("mcp+client+library", "Clients"), ("model+context+protocol+server", "MCP servers"),
    ],
    "agent-frameworks": [
        ("langchain+tools+collection", "LangChain"), ("crewai+tools", "crewAI"),
        ("autogpt+plugins", "AutoGPT"), ("composio+tools+agents", "Composio"),
        ("semantic+kernel+plugins", "Semantic Kernel"), ("llama+index+tools", "LlamaIndex"),
        ("agent+framework+tools+library", "Frameworks"),
    ],
    "automation-workflows": [
        ("n8n+community+nodes", "n8n"), ("awesome+n8n", "n8n"),
        ("dify+plugins", "Dify"), ("flowise+custom+nodes", "Flowise"),
        ("activepieces+pieces", "Activepieces"),
    ],
    "local-offline": [
        ("ollama+models+collection", "Ollama"), ("ollama+tools+functions", "Ollama"),
        ("llama+cpp+server+tools", "llama.cpp"), ("local+llm+agent+tools", "Local LLM"),
    ],
    "chat-platforms": [
        ("openai+gpt+actions+collection", "ChatGPT"), ("slack+ai+agent+app", "Slack"),
        ("telegram+ai+agent+bot+tools", "Telegram"), ("discord+ai+agent+bot+tools", "Discord"),
    ],
}

def gh_search(query, per_page=10):
    out = subprocess.run(
        ["gh", "api", f"search/repositories?q={query}&sort=stars&order=desc&per_page={per_page}"],
        capture_output=True, text=True, timeout=60)
    if out.returncode != 0:
        print(f"  !! failed: {query}: {out.stderr.strip()[:150]}", flush=True)
        return []
    try:
        items = json.loads(out.stdout).get("items", [])
    except json.JSONDecodeError:
        print(f"  !! bad json: {query}", flush=True)
        return []
    res = []
    for it in items:
        res.append({
            "full_name": it["full_name"], "url": it["html_url"],
            "desc": (it.get("description") or "")[:220],
            "stars": it["stargazers_count"], "lang": it.get("language"),
            "topics": (it.get("topics") or [])[:6],
            "pushed": (it.get("pushed_at") or "")[:10],
            "archived": it.get("archived", False),
        })
    return res

def main():
    data = {}
    seen = {}
    total = 0
    for cat, queries in CATEGORIES.items():
        data[cat] = []
        print(f"== {cat}", flush=True)
        for q, kind in queries:
            repos = gh_search(q)
            time.sleep(7)
            for r in repos:
                if r["archived"] or r["stars"] < 40:
                    continue
                if r["full_name"] in seen:
                    continue
                seen[r["full_name"]] = cat
                r["kind"] = kind
                data[cat].append(r)
                total += 1
        data[cat].sort(key=lambda r: -r["stars"])
        data[cat] = data[cat][:30]
        print(f"  -> {len(data[cat])} kept", flush=True)
    os.makedirs("data", exist_ok=True)
    with open("data/repos.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"TOTAL unique repos: {total}; saved to data/repos.json")

if __name__ == "__main__":
    main()
