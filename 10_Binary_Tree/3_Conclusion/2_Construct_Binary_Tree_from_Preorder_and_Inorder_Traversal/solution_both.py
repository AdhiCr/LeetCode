from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(stop):
            if preorder:
                if inorder and inorder[0] != stop:
                    root = TreeNode(preorder.pop(0))
                    root.left = build(root.val)
                    inorder.pop(0)
                    root.right = build(stop)
                    return root

        return build(None)

dummy = Solution()
print(dummy.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))
print(dummy.buildTree(preorder = [-1], inorder = [-1]))
