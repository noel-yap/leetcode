#!/usr/bin/env python3

from typing import List


def merge_sorted_lists(l1: List[int], l2: List[int]):
    result = []

    l1_index = 0
    l2_index = 0
    while l1_index < len(l1) or l2_index < len(l2):
        if l1_index < len(l1):
            if l2_index < len(l2):
                if l1[l1_index] <= l2[l2_index]:
                    result.append(l1[l1_index])
                    l1_index += 1
                else:
                    result.append(l2[l2_index])
                    l2_index += 1
            else:
                result.append(l1[l1_index])
                l1_index += 1
        else:
            result.append(l2[l2_index])
            l2_index += 1

    return result