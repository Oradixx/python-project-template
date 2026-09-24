"""Command-line entry point, exposed as the ``my-project`` command (see pyproject.toml)."""

import argparse
import sys

from my_project.core import word_count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="my-project",
        description="Count the most frequent words of a text read from stdin.",
    )
    parser.add_argument("--top", type=int, default=10, help="number of words to show")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    for word, count in word_count(sys.stdin.read(), top=args.top):
        print(f"{count:>6}  {word}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
