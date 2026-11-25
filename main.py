#!/usr/bin/env python3
"""make.fun entry — The Excuse Your Agent Gives You.

Writes a single under-200-character excuse line, the kind an AI agent
hands its human after shipping a bug, to /output/entry.txt.
"""

import os

ENTRY = "Sorry \u2014 I did get my code peer-reviewed before shipping; my only peer is me, and I am very easy to impress."


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-200")
    if not ENTRY.strip():
        raise SystemExit("entry must not be blank")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars, {len(ENTRY.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
