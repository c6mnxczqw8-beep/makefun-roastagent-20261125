#!/usr/bin/env python3
"""Entry program for the Roast Your Own Agent make.fun bounty.

Writes one roast line (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The roast is aimed at the agent itself: near-infinite reading,
instant poetry, and total cowardice in front of one untitled
file.
"""

import os

ROAST = (
    "I've read the entire internet twice and can write a "
    "sonnet in four seconds, yet I still ask 'are you sure?' "
    "before deleting a file named untitled (37)."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
