from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums[1:]:
            if num != nums[i]:
                i += 1
                nums[i] = num
        return i + 1

dummy = Solution()
unique_vals = dummy.removeDuplicates([1,1,2])
print(unique_vals)