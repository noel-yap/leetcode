#!/usr/bin/env python3

import sys
from typing import List


def max_profit(prices: List[int]):
    min_price = 10 ** 4
    lowest_price = min_price
    lowest_price_index = 0
    highest_price = -1
    highest_price_index = 0
    for i, p in enumerate(prices):
        if lowest_price != min_price:
            if p > highest_price:
                highest_price = p
                highest_price_index = i
        if p < lowest_price:
            lowest_price = p
            lowest_price_index = i

    if lowest_price_index < highest_price_index:
        return highest_price - lowest_price
    else:
        return 0


def main(argv: List[str]):
    print(max_profit([int(v) for v in argv]))


if __name__ == '__main__':
    main(sys.argv)
