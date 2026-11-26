#!/usr/bin/env python3
"""Deadpan forecast for the invented city of Varnmouth.

Writes one line (<=160 chars) to /output/entry.txt.
Stdlib only -- the grader image has no Pillow.
"""

import os

ENTRY = (
    "In Varnmouth, expect light rain of small coins through the afternoon, "
    "clearing by evening as the pigeons collect the takings. High 14, low 9."
)


def validate(text):
    """Mirror the sealed gate: UTF-8 text of 1 to 160 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 160):
        raise ValueError(f"entry is {len(text)} chars, gate needs 1-160")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
