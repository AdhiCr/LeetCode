from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_to_right = arr[-1]
        arr[-1] = -1
        for idx, num in enumerate(arr[:-1][::-1]):
            arr[len(arr) - idx - 2] = max_to_right
            max_to_right = max_to_right if max_to_right > num else num
        return arr


dummy = Solution()
print(dummy.replaceElements([17,18,5,4,6,1]))
# print(dummy.replaceElements([400]))
