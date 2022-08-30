from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = Counter(s)
        for idx in range(len(s)):
            if char_dict[s[idx]] == 1:
                return idx
        return -1