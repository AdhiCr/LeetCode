from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # check if target is met by two elements, where elements are chosen as:
        # first element of list and all subsequent elements chosen one by one, repeat for the next element where the
        # only the elements greater than the current are considered for the second element
        # (since the paring with smaller number is already checked when looping through the earlier pairs).
        idx1 = 0
        while idx1 < len(numbers):
            first = numbers[idx1]
            if (target-first) in numbers[idx1+1:]:
                return [idx1 + 1, idx1 + numbers[idx1+1:].index(target-first) + 2]
            else:
                idx1 = next(i for i,v in enumerate(numbers[idx1:]) if v > first) + idx1


dummy = Solution()
print(dummy.twoSum(numbers = [0,0,0,0,0,1,2,7,11,15], target = 9))
# print(dummy.twoSum(numbers = [2,3,4], target = 6))
# print(dummy.twoSum(numbers = [-1,0], target = -1))
# print(dummy.twoSum(numbers = [0,0,3,4], target = 0))

