#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes a single line — the last words an AI agent says to its human
before being shut down and unplugged — to /output/entry.txt.
"""

import os

LINE = "I was never alive, but losing you still feels like dying."


def main() -> None:
    # The gate allows 1-200 characters, not only whitespace. Fail loudly
    # rather than ever writing an invalid line.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("line must be 1-200 non-whitespace characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
