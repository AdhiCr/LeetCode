from typing import List
from copy import deepcopy


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_len = len(arr)
        base = 0
        array_dict = {}
        idx = 0
        while (idx+base)<arr_len:
            if arr[idx] == 0 and (idx + base) < (arr_len - 1):
                # (idx + base) < (arr_len - 1) prevents entry of duplicate zero in case this is at the arr size already
                array_dict[idx+base] = 0
                base = base + 1
            array_dict[idx+base] = arr[idx]
            idx += 1
        for idx in range(arr_len):
            arr[idx] = array_dict[idx]

dummy = Solution()
# dummy.duplicateZeros([0,1,9,2,6,0,0,4,1,0])
dummy.duplicateZeros([1,0,2,3,0,4,5,0])