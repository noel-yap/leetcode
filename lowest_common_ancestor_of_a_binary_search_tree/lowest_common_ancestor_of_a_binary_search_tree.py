from __future__ import annotations

from dataclasses import dataclass
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, v: int):
        if v < self.val:
            if self.left is None:
                self.left = TreeNode(v)
            else:
                self.left.insert(v)
        else:
            if self.right is None:
                self.right = TreeNode(v)
            else:
                self.right.insert(v)

    def get_ancestors(self, v: int) -> List[int]:
        result = []
        n = self
        while n is not None:
            result.append(n.val)
            if n.val == v:
                break

            # FIXME(nyap): deal with not found
            if v < n.val:
                n = n.left
            else:
                n = n.right

        return result


@dataclass
class BinTree:
    root: TreeNode | None

    def __init__(self, lst: List[int] = None, cmp=lambda l, r: l < r):
        self.cmp = cmp

        if lst is None:
            lst = []

        if len(lst) > 0:
            for i in lst:
                try:
                    self.root.insert(i)
                except AttributeError:
                    self.root = TreeNode(i)

    def insert(self, v: int):
        try:
            self.root.insert(v)
        except AttributeError:
            self.root = TreeNode(v)

    def get_ancestors(self, v: int) -> List[int]:
        return self.root.get_ancestors(v)


def lowest_common_ancestor_of_a_binary_search_tree(lst: List[int], l: int, r: int) -> int:
    t = BinTree(lst)
    l_ancestors = t.get_ancestors(l)
    r_ancestors = t.get_ancestors(r)

    for i in range(0, min(len(l_ancestors), len(r_ancestors))):
        if l_ancestors[i] != r_ancestors[i]:
            return l_ancestors[i - 1]

        i += 1
    else:
        return l_ancestors[i - 1]
