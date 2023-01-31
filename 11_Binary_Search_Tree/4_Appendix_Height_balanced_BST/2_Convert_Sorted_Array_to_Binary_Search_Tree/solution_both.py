from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        return TreeNode(
            val=nums[len(nums) // 2],
            left=self.sortedArrayToBST(nums[:len(nums) // 2]),
            right=self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
        )

dummy = Solution()
bst = dummy.sortedArrayToBST([-10,-3,0,5,9])
bst = dummy.sortedArrayToBST([1,3])