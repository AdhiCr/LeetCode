from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        climb_left = 0
        climb_right = len(arr) - 1
        for idx in range(1, len(arr)):
            if arr[idx] > arr[climb_left]:
                climb_left = idx
            elif arr[idx] == arr[climb_left]:
                return False
            else:
                break
        if climb_left == 0:
            return False

        for idx in range(len(arr)-2, 0, -1):
            if arr[idx] > arr[climb_right]:
                climb_right = idx
            elif arr[idx] == arr[climb_right]:
                return False
            else:
                break
        return (climb_left == climb_right) and (climb_right != len(arr) - 1)

dummy = Solution()
# print(dummy.validMountainArray([2,1]))
# print(dummy.validMountainArray([0, 2, 3, 4, 5, 2, 1, 0]))
# print(dummy.validMountainArray([0, 2, 3, 3, 5, 2, 1, 0]))
# print(dummy.validMountainArray([0, 2, 3, 3, 5, 2, 1, 0]))
print(dummy.validMountainArray([0,3,2,1]))

