#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes the funniest honest error message an appliance could show
(one line, at most 200 characters) to /output/entry.txt,
deterministically.

Craft note: the humour comes out of the truth of the fault — a lint
filter genuinely 98% full — told in the dryer's own flat, put-upon
voice. "Breathing through a straw since March" is the specific,
plausible detail; "Clean me or bury me" lands the twist without
explaining the joke.
"""

import os

ENTRY = (
    "ERROR: Lint filter 98% full. I have been breathing through a "
    "straw since March. Clean me or bury me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
