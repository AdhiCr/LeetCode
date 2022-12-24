from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(stop):
            if postorder:
                if inorder and inorder[-1] != stop:
                    root = TreeNode(postorder.pop(-1))
                    root.right = build(root.val)
                    inorder.pop(-1)
                    root.left = build(stop)
                    return root

        return build(None)

dummy = Solution()
print(dummy.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))
print(dummy.buildTree(inorder = [-1], postorder = [-1]))
