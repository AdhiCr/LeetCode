from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while len(nums) > 1:
            temp = nums.pop()
            if temp not in nums:
                return temp
            else:
                nums.remove(temp)
        return nums[0]