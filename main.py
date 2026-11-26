#!/usr/bin/env python3
"""Write the one sentence a house cat would say in its own defence after
knocking a glass off the table.

The excuse runs on a cat's own logic: territory and rent. The glass had
taken the sunbeam and was charging for it in judgemental glints, so the
cat evicted it; the floor merely signed the paperwork. No apology, no
confession, just a landlord settling a dispute.
"""

import os

ENTRY = (
    "The glass spent all morning squatting in my sunbeam, charging rent "
    "in judgemental little glints, so I evicted it \u2014 the floor merely "
    "signed the paperwork."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
