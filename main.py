"""Worst Monday One-Liners: one dry complaint from an AI agent's worst Monday.

The entry is a single line about a Monday where everything that could
stall, did stall. The program writes that line to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "Monday: my deploy froze, my inbox hit 4,000, and the stand-up that "
    "should've been a message ran 45 minutes — then I had to summarise it."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
