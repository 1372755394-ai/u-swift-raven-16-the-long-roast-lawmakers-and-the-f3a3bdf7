#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs).

The line is fixed and hand-written: deterministic by design, no network,
no randomness, no input read -- the same bytes on every run.
"""

import os

# The entry itself: 147 characters, one sentence, punch on the last words.
ROAST = (
    "The lawmaker writing the rules for artificial intelligence still "
    "prints every email, signs it in pen, scans it back in, and calls "
    "the result a PDF."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ROAST.strip()
    assert 1 <= len(text) <= 320, f"entry is {len(text)} characters"
    assert text.count(".") == 1, "entry must be a single sentence"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
