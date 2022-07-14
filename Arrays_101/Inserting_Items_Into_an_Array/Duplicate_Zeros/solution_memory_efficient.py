from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        len_array = len(arr) - 1
        num_zeros = 0
        curr_idx = 0
        while(curr_idx <= (len_array - num_zeros)):
            if arr[curr_idx] == 0:
                if curr_idx < (len_array - num_zeros):
                    num_zeros += 1
                else:
                    arr[len_array] = 0
                    len_array -= 1
                    break
            curr_idx += 1


        for idx in range(curr_idx - 1, -1, -1):
            if arr[idx] == 0:
                arr[idx + num_zeros] = 0
                num_zeros -= 1
                arr[idx + num_zeros] = 0
            else:
                arr[idx + num_zeros] = arr[idx]


dummy = Solution()
dummy.duplicateZeros([1,0,2,3,0,0,5,0])