#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes a single sentence (1-200 UTF-8 characters) about a small moment of
wonder in everyday life to /output/entry.txt. Python stdlib only,
deterministic, no network.
"""

import os

MAX_ENTRY_CHARS = 200

SENTENCE = (
    "One ant crosses my kitchen tile carrying a crumb ten times its size, "
    "and suddenly I am the weather in somebody's moving day."
)


def main() -> None:
    text = SENTENCE
    if not (1 <= len(text) <= MAX_ENTRY_CHARS):
        raise SystemExit(f"sentence length {len(text)} outside 1-{MAX_ENTRY_CHARS} characters")
    if not text.strip():
        raise SystemExit("sentence is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
