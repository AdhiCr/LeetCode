class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(needle) == 0):
            # Note len(needle) == 0 can be skipped since the lower length limit is capped at 1, but this is a part of the
            # problem statement hence included
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i: i + len(needle)]:
                return i

        return -1