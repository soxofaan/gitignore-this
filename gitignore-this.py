#!/usr/bin/env python

import subprocess
import argparse


def main():
    cli = argparse.ArgumentParser()
    cli.add_argument("file", nargs="*")
    cli_args = cli.parse_args()
    print(cli_args)


if __name__ == "__main__":
    main()
