from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return
        root.next = None
        def dfs(node):
            if not node:
                return
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    has_next(node.next, node.left)
            if node.right:
                has_next(node.next, node.right)
            dfs(node.right)
            dfs(node.left)
        dfs(root)
        return root

def has_next(node, node_to_attach):
    while node:
        if node.left:
            node_to_attach.next = node.left
            return
        elif node.right:
            node_to_attach.next = node.right
            return
        node = node.next


