from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = 0
        for idx, val in enumerate(nums):
            if val > max_val:
                max_val = val
                max_index = idx
        for n in nums:
            if (2 * n) > max_val and n != max_val:
                return -1
        return max_index