#!/usr/bin/env python3

import sys
from typing import List


def binary_search(nums: List[int], target: int):
    prev_i_mp = None
    i_mp = None

    i_lb = 0
    i_ub = len(nums)
    first_iteration = True
    while first_iteration or nums[i_mp] != target:
        first_iteration = False

        i_mp = int((i_lb + i_ub) / 2)
        if i_mp == prev_i_mp:
            break

        if nums[i_mp] < target:
            i_lb = i_mp
        else:
            i_ub = i_mp

        prev_i_mp = i_mp
    else:
        return i_mp

    return -1


def main(argv: List[str]):
    binary_search([int(v) for v in argv])


if __name__ == '__main__':
    main(sys.argv)