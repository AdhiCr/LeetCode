from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def flip_char(s, left_pointer, right_pointer):
            if left_pointer < right_pointer:
                s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
                flip_char(s, left_pointer + 1, right_pointer - 1)
            else:
                return

        flip_char(s, 0, len(s) - 1)