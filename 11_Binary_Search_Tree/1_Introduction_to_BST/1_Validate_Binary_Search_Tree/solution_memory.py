from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            root, lower, higher = stack.pop()
            if not root:
                continue
            if root.val <= lower or root.val >= higher:
                return False

            stack.append([root.left, lower, root.val])
            stack.append([root.right, root.val, higher])
        return True