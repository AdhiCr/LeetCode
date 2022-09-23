from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def recursive_traversal(root_node):
            if not root_node:
                return None

            recursive_traversal(root_node.left)
            result.append(root_node.val)
            recursive_traversal(root_node.right)

        recursive_traversal(root)
        return result