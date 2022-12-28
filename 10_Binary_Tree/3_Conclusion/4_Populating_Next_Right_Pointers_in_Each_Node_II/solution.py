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
        curr = root
        nxt = self.set_nxt(curr)

        while curr and nxt:
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = self.set_nxt(curr.next)
            else:
                self.set_nxt(curr).next = self.set_nxt(curr.next)

            curr = curr.next
            if not curr:
                curr = nxt
                nxt = self.set_nxt(curr)

        return root

    @staticmethod
    def set_nxt(node):
        if node.left:
            return node.left
        elif node.right:
            return node.right
        else:
            return None


