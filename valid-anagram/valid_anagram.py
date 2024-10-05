#!/usr/bin/env python3

import sys
from typing import Dict, List


def valid_anagram(l: str, r: str) -> bool:
    return char_count_map(l) == char_count_map(r)


def char_count_map(s: str) -> Dict[str, int]:
    result = {}

    for c in s:
        result[c] = result.get(c, 0) + 1

    return result


def main(argv: List[str]):
    valid_anagram(argv[0], argv[1])


if __name__ == '__main__':
    main(sys.argv)