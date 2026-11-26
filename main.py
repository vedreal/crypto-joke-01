"""Laugh track: the crypto trading joke.

Entry for the make.fun bounty
u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a.

The joke: every trader has been told to buy the dip. The
punchline turns the dip itself into the buyer — it buys a
shovel and keeps digging. That is the truth of trading life:
the dip is never done dipping, and the trader who caught it
early is the one left holding the shovel. Short, true, and
the laugh lands on the last three words.

The program writes the single joke to /output/entry.txt.
"""

import os

ENTRY = (
    "I bought the dip. Then the dip bought a shovel "
    "and kept digging."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
