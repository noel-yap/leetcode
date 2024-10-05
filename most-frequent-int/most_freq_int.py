import sys
from typing import List


def most_frequent_int(ints: List[int]):
    d = {}
    for i in ints:
        d[i] = d.get(i, 0) + 1

    inverted = {value: key for key, value in d.items()}

    return inverted[max(list(inverted.keys()))]


if __name__ == '__main__':
    print(most_frequent_int([int(v) for v in sys.argv]))
