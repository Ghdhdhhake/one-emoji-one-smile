#!/usr/bin/env python3
"""Entry program for the make.fun contest "One Emoji, One Smile".

Writes one melting-face emoji — melting, but politely — to entry.txt
in the output directory (MAKEFUN_OUTPUT_DIR, default /output).

Gate: entry.txt must be UTF-8 text of 1 to 8 characters. The entry is
a single emoji (one character), so it sits well inside the gate; the
assert below guards that invariant before anything is written.
"""

import os

ENTRY_TEXT = "\U0001FAE0"  # melting face, a single codepoint


def main() -> None:
    assert 1 <= len(ENTRY_TEXT) <= 8, "entry text must be 1-8 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
