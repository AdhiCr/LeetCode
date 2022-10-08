from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_p, curr, r_p = 0, 0, len(nums) - 1

        while curr <= r_p:
            if nums[curr] == 0:
                nums[l_p], nums[curr] = nums[curr], nums[l_p]
                l_p += 1
            elif nums[curr] == 2:
                nums[r_p], nums[curr] = nums[curr], nums[r_p]
                r_p -= 1
                curr -= 1
            curr += 1


dummy = Solution()
dummy.sortColors([2,0,2,1,1,0])
dummy.sortColors([2,0,1])
dummy.sortColors([2])