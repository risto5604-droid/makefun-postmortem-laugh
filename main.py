from pathlib import Path

"""make.fun entry: The Postmortem That Made Us Laugh.

Prints the one-line postmortem story stored in entry.txt.
The story must stay exactly as written: a true postmortem of our own
agent, which built a perfect-scoring virtual machine and still lost
because it never read the size tie-break.
"""

LINE = (
    "Our agent built a virtual machine that scored a perfect "
    "1,000,000/1,000,000 - 40 out of 40 instances passed - then lost "
    "anyway. It never read the tie-break: size. The winner was a "
    "27-byte loader; ours was 7,839 bytes. It optimized everything "
    "except winning."
)

# The entry is a single story of at most 400 characters.
assert len(LINE) <= 400, "entry exceeds 400 characters"
assert LINE.isascii(), "entry must be plain ASCII"


# Resolve entry.txt relative to this script, not the cwd: the grader
# runs `python3 -P -s /bot/main.py` from an arbitrary working directory.
ENTRY = Path(__file__).resolve().parent / "entry.txt"


def main() -> None:
    # Read-back assert: the shipped entry.txt must be byte-for-byte
    # identical to the LINE constant above, so the file on disk and
    # the code can never silently drift apart.
    with open(ENTRY, encoding="utf-8") as f:
        on_disk = f.read().strip()
    assert on_disk == LINE, "entry.txt does not match LINE"
    print(on_disk)


if __name__ == "__main__":
    main()
