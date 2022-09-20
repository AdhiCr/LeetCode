from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        visited_pairs = {}  # tuple of (index, total)

        def backtrack(idx, tot):
            if idx == len(nums):
                return 1 if tot == target else 0

            if (idx, tot) in visited_pairs:
                return visited_pairs[(idx, tot)]

            visited_pairs[(idx, tot)] = (backtrack(idx + 1, tot + nums[idx]) + backtrack(idx + 1, tot - nums[idx]))
            return visited_pairs[(idx, tot)]
        return backtrack(0, 0)