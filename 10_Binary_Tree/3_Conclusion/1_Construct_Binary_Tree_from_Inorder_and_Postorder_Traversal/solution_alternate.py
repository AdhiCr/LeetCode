from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## This solutions is the inorder list is converted to a hash map, and the index is a lookup in a hash map
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder_hash = dict(zip(inorder, range(len(inorder))))
        return self.build(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)

    def build(self, inorder, postorder, in_start, in_end, post_start, post_end):
        if post_start > post_end:
            return None

        root_val = postorder[post_end]
        root_idx = self.inorder_hash[root_val]
        root = TreeNode(root_val)
        left_size = root_idx - in_start

        root.left = self.build(inorder, postorder, in_start, root_idx - 1, post_start, post_start + left_size - 1)
        root.right = self.build(inorder, postorder, root_idx + 1, in_end, post_start + left_size, post_end - 1)
        return root


## This solutions is the base version where for each recursion a search through the inorder list
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if not postorder or not inorder:
#             return None
#
#         root = TreeNode(postorder[-1])
#         mid = inorder.index(postorder[-1])
#         root.left = self.buildTree(inorder[:mid], postorder[: mid])
#         root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
#         return root

dummy = Solution()
print(dummy.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))
print(dummy.buildTree(inorder = [-1], postorder = [-1]))
