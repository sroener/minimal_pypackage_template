#!/usr/bin/env python

import sys

from {{cookiecutter.project_slug}} import cli

def main():
    """
    Main module calling the command line interface
    """
    sys.exit(cli.cli())

if __name__ == "__main__":
    main()