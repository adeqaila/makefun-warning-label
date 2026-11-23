#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh — make.fun entry (slot 1).

Writes exactly one funny warning label to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The line is a single sentence, well under the 160-character gate.
"""

import os

LINE = "WARNING: This human apologizes to furniture it walks into, then glares at it for not apologizing back."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
