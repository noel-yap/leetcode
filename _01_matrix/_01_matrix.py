#!/usr/bin/env python3

import sys
from typing import List


def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    result = []

    to_be_processed = []
    for i, r in enumerate(mat):
        row = []
        for j, c in enumerate(r):
            if c == 0:
                row.append(0)
            else:
                row.append(sys.maxsize)
                to_be_processed.append((i, j))
        result.append(row)

    while len(to_be_processed) > 0:
        coord = to_be_processed.pop(0)
        push_back = True
        for offset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            try:
                row = coord[0] + offset[0]
                col = coord[1] + offset[1]

                if result[row][col] != sys.maxsize:
                    result[coord[0]][coord[1]] = min(result[coord[0]][coord[1]], result[row][col]+1)
                    push_back = False
            except IndexError:
                pass

        if push_back:
            to_be_processed.append(coord)

    return result
