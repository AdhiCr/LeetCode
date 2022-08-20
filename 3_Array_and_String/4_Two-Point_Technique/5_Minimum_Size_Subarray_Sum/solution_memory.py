from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        start = total = 0
        len_idx = len(nums) + 1

        for end in range(len(nums)):
            total += nums[end]
            while total >= target:
                len_idx = min(len_idx, end - start + 1)
                total -= nums[start]
                start += 1

        return len_idx

dummy = Solution()
print(dummy.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(dummy.minSubArrayLen(target = 4, nums = [1,4,4]))
print(dummy.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))




