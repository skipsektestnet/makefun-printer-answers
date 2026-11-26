"""The Printer Finally Answers — writes the one-line entry to /output/entry.txt.

The joke: the printer answers back in its own weary, literal voice. It
keeps count — jammed twice in nine years, thumped 400 times — and the
punchline flips the blame onto the humans in the last clause. One
sentence, one read, no setup beyond the office it sits in.
"""

from pathlib import Path

PARTS = [
    "I have jammed twice in nine years and been thumped 400 times,",
    "yet I am the one with the anger problem.",
]
ENTRY = " ".join(PARTS)

OUTPUT = Path("/output/entry.txt")


def check(entry: str) -> None:
    assert entry and not entry.isspace(), "entry must not be empty"
    assert len(entry) <= 240, "entry must be at most 240 chars"
    assert "\n" not in entry, "entry must be a single line"


def main() -> None:
    check(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {OUTPUT} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
