#!/usr/bin/env python3
"""Render a week's markdown to HTML: preview it, and paste it into the email.

    ~/.venvs/ss/bin/python tools/render.py 2026/welcome.md

Writes an .html file and prints its path. Open it in a browser to proofread,
then select-all/copy from the browser and paste into the mail client -- links,
bolds and code blocks survive as rich text, so the email and the archived page
say the same thing without writing them twice.

Also warns about leftover TODOs, so a placeholder can't quietly ship.
"""
import re
import sys
from pathlib import Path

import markdown

CSS = """
body { max-width: 42em; margin: 2em auto; padding: 0 1em;
       font: 16px/1.6 -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }
pre { background: #f6f8fa; padding: 1em; overflow-x: auto; border-radius: 6px; }
code { font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 90%; }
pre code { font-size: 100%; }
blockquote { color: #57606a; border-left: 4px solid #d0d7de; margin: 0; padding: 0 1em; }
.todo { background: #fff8c5; }
"""


def main(argv):
    if not argv:
        sys.exit("usage: render.py <path-to-markdown> [-o out.html]")
    src = Path(argv[0])
    if len(argv) > 2 and argv[1] == "-o":
        out = Path(argv[2])
    else:
        # Never beside the source: Jekyll would see welcome.md and welcome.html
        # as competing pages for the same URL.
        out = Path(__file__).resolve().parent.parent / "build" / f"{src.stem}.html"
    out.parent.mkdir(parents=True, exist_ok=True)

    text = src.read_text()
    html = markdown.markdown(text, extensions=["fenced_code", "nl2br", "sane_lists", "md_in_html", "attr_list"])
    out.write_text(f"<!doctype html>\n<meta charset='utf-8'>\n<title>{src.stem}</title>\n"
                   f"<style>{CSS}</style>\n{html}\n")

    todos = re.findall(r"^.*TODO.*$", text, re.M)
    for line in todos:
        print(f"  TODO: {line.strip()[:78]}", file=sys.stderr)
    if todos:
        print(f"{len(todos)} TODO line(s) still in {src}", file=sys.stderr)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1:])
