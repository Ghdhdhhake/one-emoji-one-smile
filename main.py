#!/usr/bin/env python3
"""Entry program for the make.fun contest "One Emoji, One Smile".

Writes one melting-face emoji — melting, but politely — to entry.txt
in the output directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

ENTRY_TEXT = "\U0001FAE0"  # melting face, a single codepoint


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
