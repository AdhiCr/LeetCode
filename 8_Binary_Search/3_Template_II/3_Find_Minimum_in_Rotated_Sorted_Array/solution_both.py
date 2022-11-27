from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if nums[left] > nums[right] or len(nums) > 1:

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1

        return nums[left]


dummy = Solution()
print(dummy.findMin([2,3,4,5,1]))