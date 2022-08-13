from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            # 2 x Left sum excluding the index ele indicates all left of index + all right of index
            if left_sum * 2 + nums[i] == total:
                return i
            left_sum += nums[i]
        return -1


dummy = Solution()
print(dummy.pivotIndex([1, 7, 3, 6, 5, 6]))
print(dummy.pivotIndex([1, 2, 3]))
print(dummy.pivotIndex([2, 1, -1]))

