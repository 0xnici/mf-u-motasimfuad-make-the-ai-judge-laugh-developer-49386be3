#!/usr/bin/env python3
"""Write the one-line excuse to the make.fun output directory."""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
ENTRY_NAME = "entry.txt"


def main():
    excuse = (HERE / "excuse.txt").read_bytes()
    # Byte-for-byte copy: no decoding, no newline added.
    if not excuse or not excuse.strip():
        raise SystemExit("excuse.txt is empty")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / ENTRY_NAME).write_bytes(excuse)


if __name__ == "__main__":
    main()
