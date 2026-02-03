#!/usr/bin/env python3
"""Update sitemap.xml and robots.txt for a static daily archive site.

Usage:
  python3 scripts/update_sitemap.py --domain https://jobs.kokakoka.com

It will:
- scan for YYYY-MM-DD.html files in repo root
- write sitemap.xml (homepage + all daily pages)
- write robots.txt (Allow all + Sitemap line)

No external deps.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import glob
from pathlib import Path


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--domain",
        required=True,
        help="Base site origin, e.g. https://jobs.kokakoka.com (no trailing slash)",
    )
    ap.add_argument("--out-sitemap", default="sitemap.xml")
    ap.add_argument("--out-robots", default="robots.txt")
    return ap.parse_args()


def is_daily_html(name: str) -> bool:
    if len(name) != 15 or not name.endswith(".html"):
        return False
    try:
        _dt.date.fromisoformat(name[:-5])
        return True
    except ValueError:
        return False


def main() -> int:
    args = parse_args()
    domain = args.domain.rstrip("/")

    files = [Path(p).name for p in glob.glob("*.html")]
    daily = sorted([f for f in files if is_daily_html(f)])

    urls = [{"loc": f"{domain}/", "changefreq": "daily", "priority": "1.0"}]
    for f in daily:
        d = f[:-5]
        urls.append(
            {
                "loc": f"{domain}/{f}",
                "lastmod": _dt.date.fromisoformat(d).isoformat(),
                "changefreq": "yearly",
                "priority": "0.6",
            }
        )

    lines = [
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{u['loc']}</loc>")
        if "lastmod" in u:
            lines.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        lines.append(f"    <changefreq>{u['changefreq']}</changefreq>")
        lines.append(f"    <priority>{u['priority']}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    Path(args.out_sitemap).write_text("\n".join(lines) + "\n", encoding="utf-8")

    Path(args.out_robots).write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {domain}/sitemap.xml\n",
        encoding="utf-8",
    )

    print(f"Updated {args.out_sitemap} and {args.out_robots} with {len(urls)} URLs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
