from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(31, -1, -1):
            res <<= 1
            pre = {n >> i for n in nums}
            res += any(res ^ 1 ^ p in pre for p in pre)
        return res


dummy = Solution()
print(dummy.findMaximumXOR([3,10,5,25,2,8]))

dummy = Solution()
print(dummy.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))
