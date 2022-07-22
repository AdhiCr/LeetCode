from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        inverse_index_array_map = {}
        for num in arr:
            if (num * 2) in inverse_index_array_map or (num / 2) in inverse_index_array_map:
                return True
            else:
                inverse_index_array_map[num] = ""

        return False


dummy = Solution()
print(dummy.checkIfExist([10,2,5,3]))