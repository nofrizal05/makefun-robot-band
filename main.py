#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry.

Writes one funny robot band name plus its hit song to /output/entry.txt.
Standard library only. The band is three robots who only know one
troubleshooting step — and it made them famous.
"""

import os

ENTRY = (
    "Ctrl+Alt+Delete \u2014 their chart-topper "
    "'Have You Tried Turning Me Off and On Again' "
    "went platinum in IT departments."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
