from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Since the given numbers are integers, converting them to strings and checking the length
        to be even is sufficient.
        """
        return len([num for num in nums if not len(str(num))%2])