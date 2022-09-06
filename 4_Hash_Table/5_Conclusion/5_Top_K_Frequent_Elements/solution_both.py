from typing import List
from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = Counter(nums)
        if len(num2freq.keys()) == k:
            return list(num2freq.keys())
        freq2num = defaultdict(lambda: list())

        for number, frequency in num2freq.items():
            freq2num[frequency].append(number)

        answer = []
        max_freq = max(freq2num.keys())
        for freq in range(max_freq, 0, -1):
            if k == 0:
                return answer
            else:
                answer.extend(freq2num[freq])
                k -= len(freq2num[freq])


dummy = Solution()
# print(dummy.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
# print(dummy.topKFrequent(nums = [1], k = 1))
print(dummy.topKFrequent(nums = [4,1,-1,2,-1,2,3], k = 2))
print(dummy.topKFrequent(nums =
[3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], k = 10))