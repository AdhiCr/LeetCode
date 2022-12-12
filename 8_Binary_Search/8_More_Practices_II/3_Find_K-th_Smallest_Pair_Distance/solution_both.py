# Code Source: https://medium.com/swlh/binary-search-find-k-th-smallest-pair-distance-91cce923c273
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def findPairs(nums: List[int], d: int) -> int:
            i, j, cnt, n = 0, 0, 0, len(nums)
            for i in range(len(nums)):
                while nums[i] - nums[j] > d and j < i:
                    j += 1
                    cnt += (n - i)
            return n * (n - 1) // 2 - cnt

        # 1. Sort the nums array
        nums.sort()

        # 2. Initialize the left and right bounds as 0 and len(nums)-1
        l, r = min(nums[i + 1] - nums[i] for i in range(len(nums) - 1)), nums[-1] - nums[0]

        # 3. Binary search the distance
        while l <= r:
            mid = l + ((r - l) >> 1)
            # 4. Find # of pairs with distance <= the middle one
            if k <= findPairs(nums, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

dummy = Solution()
print(dummy.smallestDistancePair(nums = [1,3,1], k = 1))
print(dummy.smallestDistancePair(nums = [1,1,1], k = 2))
print(dummy.smallestDistancePair(nums = [1,6,1], k = 3))