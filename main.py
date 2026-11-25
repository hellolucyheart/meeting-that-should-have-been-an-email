#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — one funny line.

The line is a single sentence of at most 200 characters: one joke about
a meeting that should have been an email. The punch is the meeting's own
paperwork turning on itself — after an hour in the room, the only thing
anyone has to do is send the email the meeting replaced.

The entry is written to /output/entry.txt and printed to stdout.
"""

from __future__ import annotations

import os
import sys

LINE = (
    "The meeting ended with one action item: "
    "send the email we should have sent instead of the meeting."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check_line(line: str) -> str:
    """Return the line when it meets the contest gate, else fail loudly.

    The gate is the brief itself: one line of plain text, 1 to 200
    characters, one joke, no second line, nothing but the joke.
    """
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> int:
    text = check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
