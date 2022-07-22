from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for idx in range(1, len(nums)):
            if nums[idx] != nums[i]:
                i += 1
                nums[i] = nums[idx]
        return i + 1

dummy = Solution()
unique_vals = dummy.removeDuplicates([1,1,2])
print(unique_vals)