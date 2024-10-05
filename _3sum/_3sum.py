#!/usr/bin/env python3

import sys
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    r = [nums[i], nums[j], nums[k]]
                    r.sort()
                    if r not in result:
                        result.append(r)

    return result


def main(argv: List[str]):
    print(three_sum([int(v) for v in argv]))


if __name__ == '__main__':
    main(sys.argv)
