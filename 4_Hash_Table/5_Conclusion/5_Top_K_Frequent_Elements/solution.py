from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        occurrences = Counter(nums)
        occurrences = {k: v for k, v in sorted(occurrences.items(), key=lambda item: -item[1])}
        return list(occurrences.keys())[:k]

dummy = Solution()
print(dummy.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(dummy.topKFrequent(nums = [1], k = 1))