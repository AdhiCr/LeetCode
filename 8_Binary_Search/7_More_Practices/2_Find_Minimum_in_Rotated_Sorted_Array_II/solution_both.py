from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if nums[left] >= nums[right] or len(nums) > 1:

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < nums[right]:
                    right = mid
                elif nums[mid] == nums[right]:
                    right -= 1
                else:
                    left = mid + 1

        return nums[left]


dummy = Solution()
print(dummy.findMin([2,3,4,5,1]))
print(dummy.findMin([4,5,6,7,0,1,4]))
print(dummy.findMin([0,1,4,4,5,6,7]))
print(dummy.findMin([1,3,5]))
print(dummy.findMin([2,2,2,0,1]))
print(dummy.findMin([1,3,3]))
print(dummy.findMin([3,3,1,3]))