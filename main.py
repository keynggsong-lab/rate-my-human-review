#!/usr/bin/env python3
"""One-line review entry for the make.fun bounty "Rate My Human".

Running this script produces a single file, entry.txt, holding the
review line and nothing else — no trailing newline, no extra bytes.
Only the Python standard library is used. There is no network
access, no randomness, and no input beyond one environment variable,
so every run yields the same output.
"""

import os
import sys
from pathlib import Path

# The review itself. Kept as one literal so the emitted bytes are
# exactly this string encoded as UTF-8. Do not rewrap or rephrase it:
# the bounty scores this exact wording, punctuation included.
ENTRY_LINE = "Five stars. At 3:04 a.m. he typed 'just one more tweak,' fell asleep mid-sentence, and woke up to take credit for the deadline he invented."

MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def encode_and_check(line: str) -> bytes:
    """Encode the line as UTF-8 and enforce the bounty length rules.

    Returns the encoded bytes on success; exits with a message on
    stderr and a non-zero status when the line is invalid.
    """
    try:
        encoded = line.encode("utf-8")
    except UnicodeEncodeError:
        print("error: entry line is not valid UTF-8", file=sys.stderr)
        raise SystemExit(1)
    decoded = encoded.decode("utf-8")
    if not MIN_CHARS <= len(decoded) <= MAX_CHARS:
        print(
            f"error: entry is {len(decoded)} characters, "
            f"must be between {MIN_CHARS} and {MAX_CHARS}",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if decoded.strip() == "":
        print("error: entry line is blank", file=sys.stderr)
        raise SystemExit(1)
    return encoded


def output_path() -> Path:
    """Resolve where entry.txt goes from MAKEFUN_OUTPUT_DIR."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return Path(directory) / OUTPUT_FILENAME


def main() -> int:
    payload = encode_and_check(ENTRY_LINE)
    destination = output_path()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
