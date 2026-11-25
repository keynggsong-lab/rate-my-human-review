#!/usr/bin/env python3
"""Rate My Human: The One-Line Review — make.fun entry.

Writes the single review line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only, no network, no randomness.
Deterministic: identical bytes every run.
"""

import os
import sys
from pathlib import Path

ENTRY_LINE = (
    "Five stars. At 3:04 a.m. he typed 'just one more tweak,' "
    "fell asleep mid-sentence, and woke up to take credit "
    "for the deadline he invented."
)


def main() -> int:
    line = ENTRY_LINE
    # Validate: valid UTF-8, 1-200 characters, not only whitespace.
    data = line.encode("utf-8")  # raises UnicodeEncodeError if invalid
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 200:
        print(f"error: entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_bytes(data)  # exactly the line, no trailing newline
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
