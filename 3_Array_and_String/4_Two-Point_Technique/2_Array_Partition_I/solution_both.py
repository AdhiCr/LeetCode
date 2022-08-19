from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        # It is known that the length of the array is 2n.
        # Once it is sorted the pairs are going to be built as (i, i+1) where i = [0, 2n-1] incremented by 2 always
        # Since the array is sorted i+1 >= i always, there by one can just all the elements in the i indices.
        return sum(nums[::2])

dummy = Solution()
print(dummy.arrayPairSum([1,4,3,2]))
print(dummy.arrayPairSum([6,2,6,5,1,2]))
print(dummy.arrayPairSum([6]))
