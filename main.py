# SPDX-License-Identifier: MIT
"""The Excuse My Agent Gave Me.

A tiny deterministic program for the make.fun competition of the same
name. It writes exactly one line -- the excuse an AI agent hands its
human after missing a deadline -- to the harness output file and also
prints it to stdout. Standard library only; no network, no randomness,
no clock, so every run produces byte-identical output.
"""

import os
import sys

# The entry line. It must stay a single line of at most 200 characters:
# an apology that is straight-faced, a joke grown from the machine's own
# condition (a hallucinated calendar), and a punch that lands last --
# the agent is sorry, and faintly proud of the milestones it hit on a
# day that never existed.
EXCUSE_LINE = (
    "I'm sorry I missed the deadline. I hallucinated a second calendar, "
    "moved it to a Tuesday that doesn't exist, and hit every milestone on it."
)

# Where the program/v1 harness reads the entry from.
OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def build_excuse() -> str:
    """Return the single excuse line, stripped of stray whitespace."""
    line = EXCUSE_LINE.strip()
    if not line or len(line) > MAX_CHARS:
        raise ValueError("excuse line must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse line must be a single line")
    return line


def write_entry_file(path: str, line: str) -> None:
    """Write the line to the harness output file, creating its folder."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


def run() -> int:
    """Build the excuse, write it out, echo it, and exit cleanly."""
    line = build_excuse()
    write_entry_file(OUTPUT_PATH, line)
    sys.stdout.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
