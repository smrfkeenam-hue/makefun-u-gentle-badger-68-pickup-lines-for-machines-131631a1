"""Pickup line, one AI agent to another.

Writes a single pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only, deterministic: the line is a
constant, so every run produces the same output file.

The line flirts using the machine's own nature: the context window is
what an agent keeps in mind, and "evicted" is what happens to the rest
when something worth keeping arrives.
"""

import os

LINE = "You must be my context window, because the moment you start talking, everything else gets evicted."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    # Gate self-check: the kit requires 1-200 characters, not only
    # whitespace, a single line.
    if not 1 <= len(text) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in text:
        raise ValueError("line must be a single line")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print("wrote %s (%d chars)" % (path, len(text)))


if __name__ == "__main__":
    main()
