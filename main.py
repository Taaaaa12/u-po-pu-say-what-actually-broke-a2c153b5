#!/usr/bin/env python3
"""Say What Actually Broke -- make.fun entry (program/v1).

Writes a single line of software error copy to /output/entry.txt: the
brutal truth about a failed save, told plainly and with a laugh.
Deterministic: the same line every run, no network, no randomness,
no input.

Why this line: it names the real failure (disk full) in plain words,
says where the unsaved work is now (held in memory) with an image a
reader repeats out loud, and tells the user exactly what to do next
(free some space, save again) — all in one line, no apology, no padding.
"""

import os

ENTRY = (
    "Your file didn't save \u2014 the disk is full, so we're holding "
    "your work in memory, the digital equivalent of balancing it on "
    "your head. Free some space, then save again."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
