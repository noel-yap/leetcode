#!/usr/bin/env python3

import sys
from typing import List


def valid_palindrome(s: str):
    midpoint_index = int(len(s) / 2) - 1
    for i, c in enumerate(s[0:midpoint_index]):
        if c != s[len(s) - i - 1]:
            return False

    return True


def main(argv: List[str]):
    for v in argv:
        print(valid_palindrome(v))


if __name__ == '__main__':
    main(sys.argv)
