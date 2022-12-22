from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def getPathSum(node, node_val):
            if node.left:
                val_new = node_val + node.left.val
                if getPathSum(node.left, val_new) is True:
                    return True
            elif node_val == targetSum and node.right is None:
                return True
            if node.right:
                val_new = node_val + node.right.val
                if getPathSum(node.right, val_new) is True:
                    return True
            elif node_val == targetSum and node.left is None:
                return True

        return getPathSum(root, root.val) is True

    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if not root:
    #         return False
    #
    #     if (not root.left) and (not root.right) and root.val == targetSum:
    #         return True
    #
    #     return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)