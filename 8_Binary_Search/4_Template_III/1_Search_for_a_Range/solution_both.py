from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        else:
            start, end = -1, -1
            idx_1, idx_2 = 0, len(nums) - 1
            while idx_1 <= idx_2:
                mid = (idx_1 + idx_2)//2
                if nums[mid] == target:
                    idx_2 = mid - 1
                    start = mid
                elif nums[mid] > target:
                    idx_2 = mid - 1
                elif nums[mid] < target:
                    idx_1 = mid + 1
            if start == -1:
                return [-1, -1]

            idx_1, idx_2 = start, len(nums) - 1
            while idx_1 <= idx_2:
                mid = (idx_1 + idx_2)//2
                if nums[mid] == target:
                    idx_1 = mid + 1
                    end = mid
                elif nums[mid] > target:
                    idx_2 = mid - 1
                elif nums[mid] < target:
                    idx_1 = mid + 1

            return [start, end]



dummy = Solution()
print(dummy.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(dummy.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(dummy.searchRange(nums = [0], target = 0))
print(dummy.searchRange(nums = [1, 4], target = 4))
print(dummy.searchRange(nums = [], target = 0))