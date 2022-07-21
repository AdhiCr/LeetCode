from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        for num in nums:
            squares.append(num * num)
        return sorted(squares)
