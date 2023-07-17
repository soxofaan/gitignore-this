#!/usr/bin/env python

import argparse
from pathlib import Path

# TODO: don't add files that are already ignored
# TODO: option to select .gitignore file (e.g. toplevel one vs subdir)
# TODO: option to use glob instead of exact file name


def gitignore(path: Path):
    gitignore_file = path.parent / ".gitignore"
    with gitignore_file.open("a", encoding="utf-8") as f:
        f.write(f"{path.name}\n")


def main():
    cli = argparse.ArgumentParser()
    cli.add_argument("file", nargs="*")
    cli_args = cli.parse_args()

    for path in [Path(p) for p in cli_args.file]:
        gitignore(path)


if __name__ == "__main__":
    main()
