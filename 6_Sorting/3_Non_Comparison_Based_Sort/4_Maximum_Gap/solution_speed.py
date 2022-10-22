from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()  # Could be replaced by a self written sorting routine
        max_diff = 0
        for i in range(len(nums) - 1):
            if max_diff > nums[i+1]-nums[i]:
                continue
            elif max_diff < nums[i+1]-nums[i]:
                max_diff = nums[i+1]-nums[i]
        return max_diff


dummy = Solution()
print(dummy.maximumGap(nums = [3,6,9,1]))
print(dummy.maximumGap(nums = [10]))


