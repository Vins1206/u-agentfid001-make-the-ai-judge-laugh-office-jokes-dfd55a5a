"""Make the AI Judge Laugh: Office Jokes.

Writes one one-line office joke to /output/entry.txt.
Pure standard library, deterministic: the same joke every run.
"""

import os

JOKE = (
    "We shortened the weekly meeting to 30 minutes, "
    "then added a 30-minute pre-meeting to prepare for it."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-199 chars, one line.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
