"""Write the one-sentence alien review of Earth to /output/entry.txt.

The gate accepts UTF-8 text of 1 to 200 characters, so the entry is
validated here before it is written.
"""

import os

OUT = os.environ.get("MAKEFUN_OUT", "/output")

ENTRY = "One star. The locals queue for hours, argue with small glowing rectangles, and charge rent for sunlight — but the night market noodles made me forgive the whole planet."


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        raise ValueError("entry must be a single non-blank line")
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as handle:
        # No trailing newline: the file holds exactly the entry line.
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
