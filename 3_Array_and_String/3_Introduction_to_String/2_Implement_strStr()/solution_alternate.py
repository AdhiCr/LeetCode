class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle:
            return haystack.find(needle)
        else:
            # Note this can be skipped since the lower length limit is capped at 1, but this is a part of the problem statement hence included
            return 0