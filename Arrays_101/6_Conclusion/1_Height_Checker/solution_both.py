from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        mis_match = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                mis_match += 1
        return mis_match