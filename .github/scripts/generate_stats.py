"""
generate_stats.py — Generates github-stats.svg and top-langs.svg
from the GitHub GraphQL API using a GITHUB_TOKEN.

Outputs:
  github-stats.svg   — contributions, stars, PRs, issues, followers, repos
  top-langs.svg      — top 6 languages across public repos
"""

import os
import sys
import json
import urllib.request
import urllib.error
import html

TOKEN = os.environ.get("GITHUB_TOKEN", "")
USERNAME = os.environ.get("GITHUB_USERNAME", "RahilAlam929")
GRAPHQL_URL = "https://api.github.com/graphql"
REST_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/vnd.github+json",
}


def gql(query: str, variables: dict = None) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(GRAPHQL_URL, data=payload, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def rest_get(path: str) -> dict:
    req = urllib.request.Request(f"{REST_URL}{path}", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


# ── Fetch stats ───────────────────────────────────────────────────────────────

STATS_QUERY = """
query($login: String!) {
  user(login: $login) {
    name
    followers { totalCount }
    pullRequests(states: [OPEN, MERGED, CLOSED]) { totalCount }
    issues(states: [OPEN, CLOSED]) { totalCount }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      contributionCalendar { totalContributions }
    }
    repositories(ownerAffiliations: OWNER, isFork: false, first: 100) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""

data = gql(STATS_QUERY, {"login": USERNAME})
if "errors" in data:
    print("GraphQL errors:", data["errors"], file=sys.stderr)
    sys.exit(1)

user = data["data"]["user"]
cc = user["contributionsCollection"]

total_commits = cc["totalCommitContributions"]
total_prs = user["pullRequests"]["totalCount"]
total_issues = user["issues"]["totalCount"]
total_contributions = cc["contributionCalendar"]["totalContributions"]
followers = user["followers"]["totalCount"]
public_repos = user["repositories"]["totalCount"]

total_stars = sum(r["stargazerCount"] for r in user["repositories"]["nodes"])

# ── Top languages ─────────────────────────────────────────────────────────────

lang_sizes: dict[str, int] = {}
lang_colors: dict[str, str] = {}

for repo in user["repositories"]["nodes"]:
    for edge in repo["languages"]["edges"]:
        name = edge["node"]["name"]
        color = edge["node"]["color"] or "#858585"
        size = edge["size"]
        lang_sizes[name] = lang_sizes.get(name, 0) + size
        lang_colors[name] = color

top_langs = sorted(lang_sizes.items(), key=lambda x: x[1], reverse=True)[:6]
total_size = sum(s for _, s in top_langs) or 1

# ── SVG helpers ───────────────────────────────────────────────────────────────

BG = "#0d1117"
BORDER = "#30363d"
TEXT_PRIMARY = "#e6edf3"
TEXT_SECONDARY = "#8b949e"
ACCENT = "#58a6ff"
GREEN = "#3fb950"
ORANGE = "#f78166"
PURPLE = "#bc8cff"
YELLOW = "#e3b341"


def esc(s) -> str:
    return html.escape(str(s))


# ── github-stats.svg ──────────────────────────────────────────────────────────

def build_stat_row(y: int, icon: str, label: str, value, icon_color: str = ACCENT) -> str:
    return f"""
  <text x="40" y="{y}" font-size="13" fill="{icon_color}" font-family="monospace">{esc(icon)}</text>
  <text x="60" y="{y}" font-size="13" fill="{TEXT_SECONDARY}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">{esc(label)}</text>
  <text x="310" y="{y}" font-size="13" fill="{TEXT_PRIMARY}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif" text-anchor="end" font-weight="600">{esc(value)}</text>"""


rows_svg = ""
rows_svg += build_stat_row(90,  "★", "Total Stars Earned",     f"{total_stars:,}",         YELLOW)
rows_svg += build_stat_row(115, "↑", "Total Commits (year)",   f"{total_commits:,}",        GREEN)
rows_svg += build_stat_row(140, "⎇", "Total PRs",              f"{total_prs:,}",            ACCENT)
rows_svg += build_stat_row(165, "!", "Total Issues",           f"{total_issues:,}",         ORANGE)
rows_svg += build_stat_row(190, "♦", "Public Repositories",   f"{public_repos:,}",         PURPLE)
rows_svg += build_stat_row(215, "●", "Followers",              f"{followers:,}",            TEXT_SECONDARY)
rows_svg += build_stat_row(240, "✦", "Contributions (year)",  f"{total_contributions:,}",  GREEN)

stats_svg = f"""<svg width="350" height="270" xmlns="http://www.w3.org/2000/svg">
  <rect width="350" height="270" rx="10" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>

  <!-- Title -->
  <text x="20" y="35" font-size="15" fill="{TEXT_PRIMARY}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif" font-weight="700">
    {esc(USERNAME)}'s GitHub Stats
  </text>
  <line x1="20" y1="48" x2="330" y2="48" stroke="{BORDER}" stroke-width="1"/>

  {rows_svg}
</svg>"""

with open("github-stats.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)
print("✓ github-stats.svg written")


# ── top-langs.svg ─────────────────────────────────────────────────────────────

BAR_HEIGHT = 8
BAR_Y = 95
LABEL_ROW_HEIGHT = 22
CHART_WIDTH = 310

# Build proportional bar segments
bar_segments = ""
x_offset = 20
for lang, size in top_langs:
    color = lang_colors.get(lang, "#858585")
    width = round((size / total_size) * CHART_WIDTH)
    if width < 1:
        continue
    bar_segments += f'  <rect x="{x_offset}" y="{BAR_Y}" width="{width}" height="{BAR_HEIGHT}" fill="{esc(color)}"/>\n'
    x_offset += width

# Build legend dots
legend_rows = ""
col = 0
row = 0
for lang, size in top_langs:
    color = lang_colors.get(lang, "#858585")
    pct = round((size / total_size) * 100, 1)
    lx = 20 + col * 155
    ly = BAR_Y + BAR_HEIGHT + 25 + row * LABEL_ROW_HEIGHT
    legend_rows += f"""  <circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{esc(color)}"/>
  <text x="{lx + 16}" y="{ly}" font-size="11" fill="{TEXT_PRIMARY}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">{esc(lang)} <tspan fill="{TEXT_SECONDARY}">{pct}%</tspan></text>\n"""
    col += 1
    if col == 2:
        col = 0
        row += 1

rows_used = (len(top_langs) + 1) // 2
svg_height = BAR_Y + BAR_HEIGHT + 25 + rows_used * LABEL_ROW_HEIGHT + 20

langs_svg = f"""<svg width="350" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="350" height="{svg_height}" rx="10" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>

  <!-- Title -->
  <text x="20" y="35" font-size="15" fill="{TEXT_PRIMARY}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif" font-weight="700">
    Most Used Languages
  </text>
  <line x1="20" y1="48" x2="330" y2="48" stroke="{BORDER}" stroke-width="1"/>

  <!-- Bar -->
  <rect x="20" y="{BAR_Y}" width="{CHART_WIDTH}" height="{BAR_HEIGHT}" rx="4" fill="{BORDER}"/>
{bar_segments}
  <!-- Legend -->
{legend_rows}
</svg>"""

with open("top-langs.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)
print("✓ top-langs.svg written")
