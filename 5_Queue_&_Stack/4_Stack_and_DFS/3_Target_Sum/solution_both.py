from typing import List


class Solution:
    """
    The complete decision tree type approach can be optimised by modifying the requirement such that it only has to find a subset sum
    assume that for reaching the target, all the numbers that are to be kept positive is in the set P, and the numbers to be kept negative is N,
    sum(P) - sum(N) = target
    adding (sum(P) + sum(N)) on both sides,
    (sum(P) + sum(N)) + sum(P) - sum(N) = target + (sum(P) + sum(N))
    2 * sum(P) = target + sum(nums), where nums is set of all the numbers from P and N
    sum(P) = (target + sum(nums))/2

    this also adds a benefit that if (target + sum(nums)) is not even, no solution exists (since all numbers were ints).
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        if (target > sum_nums) or (target + sum_nums)%2 == 1:
            return 0

        bag_size = (target + sum_nums)//2
        dp = [0] * (-bag_size + 1) if bag_size < 0 else [0] * (bag_size + 1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(bag_size, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bag_size]


dummy = Solution()
print(dummy.findTargetSumWays(nums = [1,1,1,1,1], target = 3))
print(dummy.findTargetSumWays(nums = [1], target = 1))