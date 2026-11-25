#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line (<=20 words) for a crypto trader who has
just been liquidated, to /output/entry.txt.

The fortune opens with the classic cookie promise, then breaks it: the
great fortune awaiting the trader is the very one they just lost, and the
oracular advice collapses into checking the couch cushions. Fortune voice,
trading loss, rueful and warm, with a surprising last word.
"""

import os

FORTUNE = (
    "A great fortune awaits you, trader \u2014 unfortunately, it is the one "
    "you just lost; check the couch cushions."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
