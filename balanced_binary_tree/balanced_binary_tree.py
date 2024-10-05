#!/usr/bin/env python3

from typing import Tuple


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def is_balanced(self) -> Tuple[bool, int]:
        l_balanced = True
        l_depth = 0
        if self.left is not None:
            l_balanced, l_depth = self.left.is_balanced()

        r_balanced = True
        r_depth = 0
        if self.right is not None:
            r_balanced, r_depth = self.right.is_balanced()

        return l_balanced and r_balanced and abs(r_depth - l_depth) <= 1, max(l_depth, r_depth) + 1


def balanced_binary_tree(tree: TreeNode) -> bool:
    return tree.is_balanced()[0]
