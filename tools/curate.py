#!/usr/bin/env python3
"""Curation pass over data/repos.json: remove off-topic repos, fix misplacements.
REMOVE/MOVE lists are maintained by the maintainer after each collection run.
"""
import json

REMOVE = {
    # --- chat-platforms: politics spam & junk matched via chat keywords ---
    "cirosantilli/china-dictatorship", "cirosantilli/china-dictatroship-7",
    "mRFWq7LwNPZjaVv5v6eo/cihna-dictattorshrip-8", "panbinibn/OpenPacketFix_",
    "zpc1314521/PCL2", "gege-circle/.github",
    # --- skills-marketplaces: agent products, not skill collections ---
    "morluto/rea", "ruvnet/RuView", "nexu-io/open-design", "paperclipai/paperclip",
    # --- claude-code: agent apps, not extensions ---
    "career-ops-hq/career-ops", "calesthio/OpenMontage",
    # --- cursor: app platform matched via MCP query ---
    "ToolJet/ToolJet",
    # --- mcp-ecosystem: agents/platforms, not MCP servers ---
    "google-gemini/gemini-cli", "D4Vinci/Scrapling", "koala73/worldmonitor",
    "sansan0/TrendRadar", "reactive-resume/reactive-resume", "casdoor/casdoor",
    # --- other-coding-agents: editors/SDKs/workbenches matched wrongly ---
    "purocean/yn", "hey-api/hey-api", "Devin-AXIS/iPolloWork",
    "internet-court/internet-court-skill",
    # --- github-copilot: generic AI lists, not Copilot-specific ---
    "e2b-dev/awesome-ai-agents", "friuns2/Leaked-GPTs",
    "business-science/awesome-generative-ai-data-scientist", "wsxiaoys/awesome-ai-coding",
    # --- openai-codex: app mirrors & stale VSCode ChatGPT extensions ---
    "Wangnov/codex-app-mirror", "ajikan/ScribeAI", "VincentHch/vscodex",
    # --- automation-workflows: personal dumps ---
    "1itt1eB0y/MyCollection",
}

MOVE = {  # full_name -> (from_cat, to_cat)
    # generic MCP servers landed in cursor via "cursor mcp" query -> mcp-ecosystem
    "headroomlabs-ai/headroom": ("cursor", "mcp-ecosystem"),
    "DeusData/codebase-memory-mcp": ("cursor", "mcp-ecosystem"),
    "CoplayDev/unity-mcp": ("cursor", "mcp-ecosystem"),
    "IvanMurzak/Unity-MCP": ("cursor", "mcp-ecosystem"),
    "tadata-org/fastapi_mcp": ("cursor", "mcp-ecosystem"),
    "AgentDeskAI/browser-tools-mcp": ("cursor", "mcp-ecosystem"),
    "executeautomation/mcp-playwright": ("cursor", "mcp-ecosystem"),
    # n8n itself matched topic:mcp-server
    "n8n-io/n8n": ("mcp-ecosystem", "automation-workflows"),
    # cross-agent skill lists landed in copilot/codex categories
    "skillmatic-ai/awesome-agent-skills": ("github-copilot", "skills-marketplaces"),
    "JackyST0/awesome-agent-skills": ("github-copilot", "skills-marketplaces"),
    "kael-odin/awesome-academic-research-skills": ("other-coding-agents", "skills-marketplaces"),
}

def main():
    with open("data/repos.json", encoding="utf-8") as f:
        data = json.load(f)
    removed, moved = [], []
    for cat in list(data):
        kept = []
        for r in data[cat]:
            fn = r["full_name"]
            if fn in REMOVE:
                removed.append(fn)
                continue
            if fn in MOVE and MOVE[fn][0] == cat:
                moved.append((fn, cat, MOVE[fn][1]))
                data[MOVE[fn][1]].append(r)
                continue
            kept.append(r)
        data[cat] = kept
    for cat in data:
        seen, uniq = set(), []
        for r in data[cat]:
            if r["full_name"] in seen:
                continue
            seen.add(r["full_name"])
            uniq.append(r)
        uniq.sort(key=lambda r: -r["stars"])
        data[cat] = uniq[:30]
    with open("data/repos.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"removed {len(removed)}: {removed}")
    print(f"moved {len(moved)}: {[m[0] for m in moved]}")
    print(f"totals: { {k: len(v) for k, v in data.items()} }, sum={sum(len(v) for v in data.values())}")

if __name__ == "__main__":
    main()
