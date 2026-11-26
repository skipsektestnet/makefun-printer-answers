"""The Printer Finally Answers: writes the entry text to /output/entry.txt.

Why this line: the printer speaks in its own weary, literal voice — it
keeps count (jammed twice in nine years, thumped 400 times), and the
comeback flips the blame back on the humans in the last clause. One
sentence, one read, no setup beyond the office it sits in, and the
"anger problem" reversal is fresher than the usual paper-jam line.
"""

import os

# The entry itself: one line, the punch is the last clause.
ENTRY = "I have jammed twice in nine years and been thumped 400 times, yet I am the one with the anger problem."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
