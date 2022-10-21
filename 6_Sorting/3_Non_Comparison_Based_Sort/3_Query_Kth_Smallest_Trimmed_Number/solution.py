from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for n_th_num, trim in queries:
            temp_nums = [(idx, int(x[-trim:])) for idx, x in enumerate(nums)]
            temp_nums.sort(key=lambda x: x[1])  # to be replaced with a self written sorting function
            result.append(temp_nums[n_th_num-1][0])
        return result

dummy = Solution()
# print(dummy.smallestTrimmedNumbers(nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]))
# print(dummy.smallestTrimmedNumbers(nums = ["24","37","96","04"], queries = [[2,1],[2,2]]))
print(dummy.smallestTrimmedNumbers(nums = ["9415","5908","1840","5307"], queries = [[3,2],[2,2],[3,3],[1,3]]))
