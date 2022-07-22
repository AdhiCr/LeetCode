from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_to_right = arr[-1]
        arr[-1] = -1
        for idx in range(len(arr)-2, -1, -1):
            val = arr[idx]
            arr[idx] = max_to_right
            if max_to_right < val:
                max_to_right = val
        return arr


dummy = Solution()
print(dummy.replaceElements([17,18,5,4,6,1]))
# print(dummy.replaceElements([400]))
