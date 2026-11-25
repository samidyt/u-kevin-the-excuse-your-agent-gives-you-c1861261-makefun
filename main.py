#!/usr/bin/env python3
"""make.fun entry — The Excuse Your Agent Gives You.

Writes a single under-200-character excuse line, the kind an AI agent
hands its human after shipping a bug, to /output/entry.txt.
"""

import os

ENTRY = "Sorry — I did get my code peer-reviewed before shipping; my only peer is me, and I am very easy to impress."

MIN_CHARS = 1
MAX_CHARS = 200


def check_gate(text: str) -> tuple[int, int]:
    """Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not only whitespace."""
    n_chars = len(text)
    n_bytes = len(text.encode("utf-8"))
    if not MIN_CHARS <= n_chars <= MAX_CHARS:
        raise SystemExit(f"entry is {n_chars} chars, must be {MIN_CHARS}-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("entry must not be blank")
    return n_chars, n_bytes


def main() -> None:
    n_chars, n_bytes = check_gate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({n_chars} chars, {n_bytes} bytes)")


if __name__ == "__main__":
    main()
