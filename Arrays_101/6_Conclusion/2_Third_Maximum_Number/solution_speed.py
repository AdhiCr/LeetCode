from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = nums[0]
        second = None
        third = None
        for num in nums[1:]:
            if num in [first, second, third]:
                continue
            elif first < num:
                third, second, first = second, first, num
            elif second is None:
                second = num
            elif (second < num):
                third, second = second, num
            elif third is None:
                third = num
            elif third < num:
                third = num
        return third if not (third is None) else first


dummy = Solution()
# print(dummy.thirdMax([3,2,1]))
# print(dummy.thirdMax([1,2]))
# print(dummy.thirdMax([2,2,3,1]))
# print(dummy.thirdMax([1,2,-2147483648]))
print(dummy.thirdMax([5,2,4,1,3,6,0]))