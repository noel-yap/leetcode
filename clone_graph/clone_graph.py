from typing import Dict, List, Optional


class Node:
    val: int
    neighbors: List['Node']

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __eq__(self, other: 'Node') -> bool:
        result = self.val == other.val

        sn = [n.val for n in self.neighbors]
        on = [n.val for n in other.neighbors]
        result = result and sn == on

        return result


class NodeCloner:
    map: Dict[int, Node]

    def __init__(self):
        self.map = {}

    def clone_graph(self, node: Optional['Node']) -> Optional['Node']:
        return self.clone_node(node)

    def clone_node(self, node: Node) -> Node:
        if node is None:
            return None

        try:
            return self.map[node.val]
        except KeyError:
            result = Node(node.val)
            self.map[node.val] = result

            for n in node.neighbors:
                result.neighbors.append(self.clone_node(n))

            return result