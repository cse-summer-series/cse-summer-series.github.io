#!/usr/bin/env python3
"""Scaffold a new week's page and link it from that year's index.

    python3 tools/newweek.py 2

Fills the shared links (Discord, welcome form, office hours) from links.json so
they only have to be right in one place, and adds the index entry immediately --
that's the step that got missed for weeks 4 and 5 of 2025.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"


def main(argv):
    if len(argv) != 1 or not argv[0].isdigit():
        sys.exit("usage: newweek.py <week-number>")
    n = int(argv[0])

    links = json.loads((TOOLS / "links.json").read_text())
    year = links["year"]
    slug = "welcome" if n == 1 else f"week{n}"

    page = ROOT / year / f"{slug}.md"
    if page.exists():
        sys.exit(f"{page.relative_to(ROOT)} already exists; not overwriting")

    body = (TOOLS / "week-template.md").read_text()
    for key, value in links.items():
        body = body.replace("{{" + key + "}}", value)
    page.parent.mkdir(exist_ok=True)
    page.write_text(body)

    index = ROOT / year / "index.md"
    entry = f"- [Week {n}](./{slug}.html)"
    text = index.read_text() if index.exists() else ""
    if entry in text:
        print(f"{index.relative_to(ROOT)}: already links week {n}")
    else:
        text = text.rstrip("\n") + "\n" + entry + "\n"
        index.write_text(text)
        print(f"{index.relative_to(ROOT)}: added {entry}")

    todos = len(re.findall(r"TODO", body))
    print(f"{page.relative_to(ROOT)}: created ({todos} TODOs to fill in)")


if __name__ == "__main__":
    main(sys.argv[1:])
