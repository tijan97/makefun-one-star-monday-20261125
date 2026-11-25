#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday, as though Monday
were a restaurant. Writes the single review line to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (or OUTPUT_DIR, or /output).
"""

import os

ENTRY = (
    "One star. The waiter was Monday, the special was a 9 a.m. meeting, "
    "and the bill cost me my whole weekend."
)


def validate(entry: str) -> None:
    """Enforce the competition gate: one line, 1-180 chars, at most 25 words."""
    if not 1 <= len(entry) <= 180:
        raise ValueError(f"entry must be 1-180 chars, got {len(entry)}")
    if len(entry.split()) > 25:
        raise ValueError(f"entry must be at most 25 words, got {len(entry.split())}")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
