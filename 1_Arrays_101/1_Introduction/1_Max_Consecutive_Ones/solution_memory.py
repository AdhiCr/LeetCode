from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sequence_len = 0
        current_sequence_len = 0
        for num in nums:
            max_sequence_len = max(max_sequence_len, current_sequence_len)
            current_sequence_len = (current_sequence_len + 1) if num == 1 else 0
        return max(max_sequence_len, current_sequence_len)
