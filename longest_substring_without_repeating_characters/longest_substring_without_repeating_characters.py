#!/usr/bin/env python3

import sys
from typing import List


def length_of_longest_substring(s: str):
    result = 0

    for i in range(len(s)):
        seen = ""
        for c in s[i:]:
            if c not in seen:
                seen += c
            else:
                result = max(result, len(seen))
                break

    return result


def main(argv: List[str]):
    for v in argv:
        print(length_of_longest_substring(v))


if __name__ == '__main__':
    main(sys.argv)
