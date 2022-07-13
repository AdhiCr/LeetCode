from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sizes = []
        count = 0
        for i in nums:
            if i == 0:
                sizes.append(count)
                count = 0
            else:
                count += 1
        sizes.append(count)
        return max(sizes)
