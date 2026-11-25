#!/usr/bin/env python3
"""The 3AM Fridge Text: one line a smart fridge texts its owner at 3am.

The line is the whole entry. The fridge has kept the cake cold all
night, it knows the owner is not here for water, and at 3am it finally
says so out loud. The angle is the fridge as a secret-keeper, not the
obvious milk, ice, or door-left-open joke. Fixed text, no clock, no
network, no randomness, so every run writes the same bytes to
/output/entry.txt.
"""

import os
import sys
from pathlib import Path

LINE = (
    "It's 3am. I know about the cake. I've always known about the cake. "
    "Eat it or go to bed, but stop pretending you're here for water."
)
LIMIT = 140


def check_line(line):
    """Refuse anything that would fail the gate before writing it."""
    if not 1 <= len(line) <= LIMIT:
        raise ValueError(f"entry is {len(line)} chars, limit is {LIMIT}")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line with no blank edges")
    return line


def write_entry(line):
    """Write the line to the grader's output file, then read it back."""
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    if out.read_text(encoding="utf-8") != line:
        raise RuntimeError("entry on disk does not match the line")
    return out


def main():
    line = check_line(LINE)
    target = write_entry(line)
    print(f"Wrote {len(line)} chars to {target}")


if __name__ == "__main__":
    main()
