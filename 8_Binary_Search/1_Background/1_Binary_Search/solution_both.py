from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = left + ((right - left)// 2)
        while mid not in [left, right]:
            if nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid

            mid = left + ((right - left) // 2)

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1

# Equivalent and more elegant solution
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left+right)//2
#             if target == nums[mid]:
#                 return mid
#             elif target < nums[mid]:
#                 right = mid - 1
#             elif target > nums[mid]:
#                 left = mid + 1
#         return -1

dummy = Solution()
print(dummy.search(nums = [-1,0,3,5,9,12], target = 9))
print(dummy.search([-1,0,3,5,9,12], target = 2))
print(dummy.search([-1,0,5], target = 5))
print(dummy.search([-1,0,5], target = -1))
print(dummy.search([-1,5], target = 5))