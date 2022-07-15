from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Fastest solution
        """
        return sorted([num*num for num in nums])