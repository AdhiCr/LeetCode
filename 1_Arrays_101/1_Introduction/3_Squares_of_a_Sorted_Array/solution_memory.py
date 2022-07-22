from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Since the input is already in non-decreasing order, one can compare the absolute values of the left most element and right most element and save the square of the larger number. Once this is done move to the next idx (or previous idx if the right side was larger), and continue.
        Repeate this until all numbers have been traversed through.
        """
        squared_list = []
        left_idx, right_idx = 0, len(nums) - 1
        while left_idx <= right_idx:
            left, right = abs(nums[left_idx]), abs(nums[right_idx])
            if left >= right:
                squared_list.insert(0, left**2)
                left_idx += 1
            else:
                squared_list.insert(0, right**2)
                right_idx -= 1
        return squared_list