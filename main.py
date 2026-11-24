"""Office joke entry: writes one 109-char office joke to /output/entry.txt."""

import os

JOKE = "I replied-all asking everyone to stop replying-all, and HR scheduled a meeting about my leadership potential."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
