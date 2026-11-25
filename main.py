"""One Star for Monday — a one-star review of Monday, as a restaurant.

Writes the single review line to <output>/entry.txt, where <output> is
MAKEFUN_OUTPUT_DIR, OUTPUT_DIR, or /output. No other output is produced.
"""

import os

LINE = "One star. The waiter was Monday, the special was a 9 a.m. meeting, and the bill cost me my whole weekend."


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
