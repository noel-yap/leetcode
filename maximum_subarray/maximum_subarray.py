#!/usr/bin/env python3
import math
import sys
from typing import List


def squash(lst: List[int]):
    non_zero = []

    if len(lst) == 0:
        return []

    for e in lst:
        if e != 0:
            non_zero.append(e)

    if len(non_zero) == 0:
        return non_zero

    result = [non_zero[0]]
    for i in range(1, len(non_zero)):
        if math.copysign(1, result[-1]) != math.copysign(1, non_zero[i]):
            result.append(non_zero[i])
        else:
            result[-1] += non_zero[i]

    while len(result) > 0 and result[0] < 0:
        result.pop(0)

    while len(result) > 0 and result[-1] < 0:
        result.pop()

    while len(result) > 1 and result[0] + result[1] < 0:
        result = result[2:]

    while len(result) > 1 and result[-1] + result[-2] < 0:
        result = result[:-2]

    return result


def maximum_subarray(lst: List[int]):
    lst = squash(lst)

    result = 0
    for i in range(0, len(lst), 2):
        subtotal = lst[i]
        result = max(result, subtotal)
        for j in range(i + 1, len(lst), 2):
            subtotal += lst[j] + lst[j + 1]
            result = max(result, subtotal)

    return result


def main(argv: List[str]):
    maximum_subarray([int(v) for v in argv])


if __name__ == '__main__':
    main(sys.argv)
