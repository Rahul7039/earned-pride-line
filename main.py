#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single original line (134 characters) to /output/entry.txt:
a quiet, earned moment of pride for a small person doing something hard.

Pure standard library, deterministic: the same line is written on every run.
"""

import os

LINE = (
    "The boy who stammered through every assembly stood up, "
    "read his poem to the last line, "
    "and the hall forgot to clap for a whole second."
)


def validate_line(line: str) -> str:
    """Return the line if it is a single non-empty line, else raise."""
    if not line.strip():
        raise ValueError("line must not be empty")
    if "\n" in line:
        raise ValueError("line must be a single line")
    return line


def write_line(path: str, line: str) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    write_line(path, validate_line(LINE))


if __name__ == "__main__":
    main()
