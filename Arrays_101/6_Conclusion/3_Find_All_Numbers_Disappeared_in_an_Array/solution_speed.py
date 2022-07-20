from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        missing = []
        for i in range(1, n + 1):
            if i not in nums:
                missing.append(i)

        return missing


dummy = Solution()
print(dummy.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(dummy.findDisappearedNumbers([1,1]))
print(dummy.findDisappearedNumbers([2,2]))
