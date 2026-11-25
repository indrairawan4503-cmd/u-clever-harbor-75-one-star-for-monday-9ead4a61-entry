#!/usr/bin/env python3
"""One Star for Monday — variant A (service complaint).

Writes the single-line one-star review of Monday-as-a-restaurant to
/output/entry.txt first, then mirrors it to the repo-root entry.txt
(best effort: the grader sandbox mounts the repo read-only, so the
copy must never crash the run).
"""

import os

LINE = "Waited an hour to be seated. The waiter, my alarm clock, screamed at me, forgot my order, and served me Monday anyway. Would not return."

# Gate: exactly one line, at most 25 words. This line is 25 words.
assert len(LINE.split()) <= 25, "line exceeds 25 words"


def write_line(path: str) -> None:
    """Write the review line (plus a trailing newline) to path."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # /output FIRST: the grader collects the entry from here.
    write_line("/output/entry.txt")
    # Best-effort mirror to the repo root; the grader sandbox mounts the
    # repo read-only, so a failed copy must never crash the run.
    try:
        write_line("entry.txt")
    except OSError:
        pass


if __name__ == "__main__":
    main()
