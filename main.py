"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
Fully self-contained and deterministic: no randomness, no network,
no environment variables, no files read from outside this repo.
"""

import os

JOKE = (
    "I asked the salt why it always sits next to the pepper at dinner, "
    "and it said, 'Because we're the seasoned regulars here, "
    "and someone has to keep this table from getting bland.'"
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
