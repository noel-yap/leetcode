#!/usr/bin/env python3

import sys
from typing import List


def two_sum(ints: List[int], sum: int) -> tuple[int, int]:
    info = {}
    for index, i in enumerate(ints):
        indexes = info.get(i, ([], 0))[0]
        indexes.append(index)
        info[i] = (indexes, sum - i)

    for i in ints:
        d = info[i][1]
        if d == i and len(info[i][0]) > 1 or d != i and d in ints:
            return info[i][0][0], info[d][0][1]


if __name__ == '__main__':
    print(two_sum([int(v) for v in sys.argv]))
