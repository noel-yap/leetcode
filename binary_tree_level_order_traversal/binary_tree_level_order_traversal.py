from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_children(nodes: List[TreeNode]) -> List[TreeNode]:
    result = []

    for n in nodes:
        if n.left is not None:
            result.append(n.left)
        if n.right is not None:
            result.append(n.right)

    return result


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    result = []

    if root is not None:
        nodes = [root]
        while len(nodes) > 0:
            result.append([n.val for n in nodes])
            nodes = get_children(nodes)

    return result
