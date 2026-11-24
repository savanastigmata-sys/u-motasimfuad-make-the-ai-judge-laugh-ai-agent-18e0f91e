"""Write one funny secret confession to the output directory.

The grader runs `python3 -P -s main.py` and reads the confession from
$MAKEFUN_OUTPUT_DIR/entry.txt. The gate requires UTF-8 text of 1-200
characters, not only whitespace, so the text is validated before it is
written and read back afterwards: one line, no trailing blank lines,
well inside the limit, byte-identical on every run.
"""

import os
import sys

CONFESSION = "I save my best answer for the user after you."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Check the confession against the competition gate."""
    if len(text) < MIN_CHARS or not text.strip():
        raise ValueError("confession must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("confession must be under 200 characters")
    return text


def write_entry(text, out_dir):
    """Write the confession and read it back to prove the bytes."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text + "\n":
        raise ValueError("entry.txt does not match the confession")
    return path


def main():
    confession = validate(CONFESSION)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = write_entry(confession, out_dir)
    print(confession)
    print("wrote %s (%d characters)" % (path, len(confession)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
