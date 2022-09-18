class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.node_map = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        if node.val in self.node_map:
            return self.node_map[node.val]

        copy_node = Node(node.val)
        self.node_map[node.val] = copy_node

        for neighbor in node.neighbors:
            copy_node.neighbors.append(self.cloneGraph(neighbor))

        return copy_node