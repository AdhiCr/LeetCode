from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pointer_1 = 0
        pointer_2 = len(s) - 1

        while pointer_1 < pointer_2:
            tmp = s[pointer_1]
            s[pointer_1] = s[pointer_2]
            s[pointer_2] = tmp
            pointer_1 += 1
            pointer_2 -= 1