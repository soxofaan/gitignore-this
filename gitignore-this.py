#!/usr/bin/env python

import argparse
from pathlib import Path

# TODO: don't add files that are already ignored
# TODO: option to select .gitignore file (e.g. toplevel one vs subdir)
# TODO: option to automatically add newly created .gitignore to git staging
# TODO: (option to) automatically climb file tree until existing
#   .gitignore is found (instead of blindly creating one in parent folder)


def gitignore(path: Path, glob_stem: bool = False):
    gitignore_file = path.parent / ".gitignore"
    with gitignore_file.open("a", encoding="utf-8") as f:
        if glob_stem:
            entry = f"*{path.suffix}"
        else:
            entry = path.name
        print(f"adding `{entry}` to `{gitignore_file}")
        f.write(f"{entry}\n")


def main():
    cli = argparse.ArgumentParser()
    cli.add_argument("file", nargs="*")
    cli.add_argument(
        "-g",
        "--glob-stem",
        action="store_true",
        help="Ignore by file extension (replace stem with glob `*`).",
    )
    cli_args = cli.parse_args()

    for path in [Path(p) for p in cli_args.file]:
        gitignore(path, glob_stem=cli_args.glob_stem)


if __name__ == "__main__":
    main()
