from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_idx = 0
        for right_idx in range(len(nums)):
            if (nums[right_idx] != 0):
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
                left_idx += 1


dummy = Solution()
# dummy.moveZeroes([0,1,0,3,12])
dummy.moveZeroes([1])