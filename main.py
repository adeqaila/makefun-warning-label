#!/usr/bin/env python3
"""Warning Label for Humans — one-line safety label, max 160 chars."""

import os

LINE = "WARNING: This human apologizes to furniture it walks into, then glares at it for not apologizing back."

def build_entry() -> str:
    return LINE

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_entry())

if __name__ == "__main__":
    main()
