from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def subSplit(largest_sum):
            sub_array = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > largest_sum:
                    sub_array += 1
                    curr_sum = num
            return sub_array <= k

        left, right = max(nums), sum(nums)
        curr_max = right
        while left <= right:
            mid = left + ((right - left) >> 1)
            if subSplit(mid):
                curr_max = mid
                right = mid - 1
            else:
                left = mid + 1

        return curr_max


