from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()  # Could be replaced by a self written sorting routine
        min_diff = arr[-1] - arr[0]
        return_list = []
        for i in range(len(arr) - 1):
            if min_diff == arr[i+1]-arr[i]:
                return_list.append([arr[i], arr[i + 1]])
            elif min_diff > arr[i+1]-arr[i]:
                min_diff = arr[i+1]-arr[i]
                return_list = [[arr[i], arr[i + 1]]]

        return return_list


dummy = Solution()
print(dummy.minimumAbsDifference(arr = [4,2,1,3]))
print(dummy.minimumAbsDifference(arr = [1,3,6,10,15]))
print(dummy.minimumAbsDifference(arr = [3,8,-10,23,19,-4,-14,27]))


