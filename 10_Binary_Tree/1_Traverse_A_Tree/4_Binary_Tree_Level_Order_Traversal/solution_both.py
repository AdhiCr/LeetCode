from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root

        result = []
        queue = [root]

        while queue:
            nodes = queue
            level = []
            children = []
            for node in nodes:
                level.append(node.val)
                if node.left is not None:
                    children.append(node.left)
                if node.right is not None:
                    children.append(node.right)

            result.append(level)
            queue = children

        return result


