from string import ascii_lowercase

class Solution:
    def firstUniqChar(self, s: str) -> int:
        first_occurrence = -1
        for char in ascii_lowercase:
            find_index = s.find(char)
            if find_index == -1 or s.find(char, find_index + 1) != -1:
                continue
            if first_occurrence == -1 or find_index < first_occurrence:
                first_occurrence = find_index
        return first_occurrence


dummy =Solution()
print(dummy.firstUniqChar("leetcode"))