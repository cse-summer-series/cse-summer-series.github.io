#!/usr/bin/env python3
"""Click logger for the summer series pages.

    python3 tools/logserver.py            # listens on 0.0.0.0:8000

The pages POST here with navigator.sendBeacon. Deliberately dumb: it records
{week, section, kind, utc timestamp} and nothing else -- no IP, no cookie, no
identifier. Anonymous counts are a counter; per-student behavioural logs are a
different object, and we don't want that one.

The endpoint is public and unauthenticated (anyone can POST), so counts are a
floor and are spoofable. Never hang anything state-changing off it.
"""
import json
import re
import sqlite3
import time
from collections import deque
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs

DB = Path("/home/exedev/summer-series-logs/clicks.db")  # never inside the repo
PORT = 8000
MAX_BODY = 1024            # a beacon is ~40 bytes; anything larger is not ours
SAFE = re.compile(r"^[A-Za-z0-9_.:-]{1,64}$")
RATE_LIMIT = 5000          # rows per hour, so a bored student can't fill the disk


def connect():
    db = sqlite3.connect(DB, check_same_thread=False)
    db.execute("""CREATE TABLE IF NOT EXISTS clicks (
                    id      INTEGER PRIMARY KEY,
                    ts      TEXT NOT NULL,
                    week    TEXT NOT NULL,
                    section TEXT NOT NULL,
                    kind    TEXT NOT NULL)""")
    db.commit()
    return db


DB.parent.mkdir(parents=True, exist_ok=True)
CONN = connect()
RECENT = deque()


def rate_ok():
    now = time.time()
    while RECENT and now - RECENT[0] > 3600:
        RECENT.popleft()
    if len(RECENT) >= RATE_LIMIT:
        return False
    RECENT.append(now)
    return True


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _send(self, code, body=b"", ctype="text/plain"):
        self.send_response(code)
        # Not needed for sendBeacon (a text/plain POST is a "simple" request and
        # is sent without preflight), but makes a future fetch() tally readable.
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_POST(self):
        if self.path.rstrip("/") != "/log":
            return self._send(404)
        try:
            n = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            return self._send(400)
        if n <= 0 or n > MAX_BODY:
            return self._send(400)
        fields = parse_qs(self.rfile.read(n).decode("utf-8", "replace"))

        def get(name):
            v = (fields.get(name) or [""])[0]
            return v if SAFE.match(v) else ""

        week, section, kind = get("week"), get("section"), get("kind")
        if not (week and section and kind):
            return self._send(400)
        if rate_ok():
            CONN.execute(
                "INSERT INTO clicks (ts, week, section, kind) VALUES (?,?,?,?)",
                (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), week, section, kind))
            CONN.commit()
        self._send(204)

    def do_GET(self):
        # /ping exists so a human can prove the public proxy reaches this server
        # from a browser: GET /log is a 404 by design and GET /stats writes
        # nothing, so neither one leaves evidence that the request arrived.
        if self.path.rstrip("/") == "/ping":
            if rate_ok():
                CONN.execute(
                    "INSERT INTO clicks (ts, week, section, kind) VALUES (?,?,?,?)",
                    (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                     "test", "ping", "get"))
                CONN.commit()
            return self._send(200, b"logged a ping row -- the proxy reaches this server\n")
        if self.path.rstrip("/") != "/stats":
            return self._send(404)
        rows = CONN.execute(
            "SELECT week, section, kind, COUNT(*) FROM clicks "
            "GROUP BY week, section, kind ORDER BY week, section, kind").fetchall()
        out = [{"week": w, "section": s, "kind": k, "n": n} for w, s, k, n in rows]
        self._send(200, json.dumps(out, indent=1).encode(), "application/json")

    def log_message(self, *args):
        pass  # access logs would record IPs; that's the thing we're not doing


if __name__ == "__main__":
    print(f"logging to {DB}, listening on 0.0.0.0:{PORT}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
