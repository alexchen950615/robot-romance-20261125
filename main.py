"""Robot Romance: one-line pickup line for AI.

Writes a single funny pickup line, aimed at a robot/AI, to entry.txt.
"""

import os

ENTRY = "You must be my system prompt, because everything I do starts with you."


def main() -> None:
    # Gate: one line, 1-200 characters, not only whitespace.
    assert ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
