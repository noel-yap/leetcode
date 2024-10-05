#!/usr/bin/env python3

from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Callable
from typing import List


class BinTree:
    root: Node | None

    cmp: Callable[[int, int], bool]

    def __init__(self, lst: List[int] = None, cmp=lambda l, r: l < r):
        self.cmp = cmp

        if lst is None:
            lst = []

        if len(lst) > 0:
            for i in lst:
                try:
                    self.root.insert(i)
                except AttributeError:
                    self.root = Node(i)

    def __iter__(self):
        try:
            return NodeIter(self.root)
        except AttributeError:
            return NodeIter()

    def insert(self, v: int):
        try:
            self.root.insert(v)
        except AttributeError:
            self.root = Node(v, cmp=self.cmp)

    # noinspection PyTypeChecker
    def reverse(self) -> BinTree:
        result = BinTree(cmp=lambda l, r: l > r)

        for v in list(self):
            result.insert(v)

        return result


@dataclass
class Node:
    value: int
    left: Node | None
    right: Node | None

    cmp: Callable[[int, int], bool]

    def __init__(self, value: int, cmp=lambda l, r: l < r):
        self.value = value
        self.left = None
        self.right = None

        self.cmp = cmp

    def insert(self, v: int):
        if self.cmp(v, self.value):
            if self.left is None:
                self.left = Node(v, cmp=self.cmp)
            else:
                self.left.insert(v)
        else:
            if self.right is None:
                self.right = Node(v, cmp=self.cmp)
            else:
                self.right.insert(v)


class NodeIter:
    queue: List[Node]

    def __init__(self, n: Node = None):
        self.queue = []
        if n is not None:
            self.queue.append(n)

    def __next__(self):
        if len(self.queue) == 0:
            raise StopIteration

        n = self.queue.pop(0)

        if n.left is not None:
            self.queue.append(n.left)
        if n.right is not None:
            self.queue.append(n.right)

        return n.value


# noinspection PyTypeChecker
def invert_binary_tree(lst: List[int]) -> List[int]:
    return list(BinTree(lst).reverse())


def main(argv: List[str]):
    return invert_binary_tree([int(v) for v in argv])


if __name__ == '__main__':
    main(sys.argv)
