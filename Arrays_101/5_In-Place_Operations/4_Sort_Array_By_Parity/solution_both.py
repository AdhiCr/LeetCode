from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        odd, even = [], []
        for num in nums:
            if num%2:
                even.append(num)
            else:
                odd.append(num)
        odd.extend(even)
        return odd

dummy = Solution()
print(dummy.sortArrayByParity([3,1,2,4]))
print(dummy.sortArrayByParity([1]))