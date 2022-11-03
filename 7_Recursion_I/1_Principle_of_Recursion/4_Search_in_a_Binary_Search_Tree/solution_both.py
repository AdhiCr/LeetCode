from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val == val:
                return root

            node_check = self.searchBST(root.left, val)
            if node_check:
                return node_check

            node_check = self.searchBST(root.right, val)
            if node_check:
                return node_check
        return None

