from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        str_len = len(strs[0])
        for len_to_rem in range(str_len):
            end_len = str_len-len_to_rem
            if all([word.startswith(strs[0][:end_len]) for word in strs[1:]]):
                return strs[0][:end_len]
        return ""

dummy = Solution()
print(dummy.longestCommonPrefix(["flower","flow","flight"]))
print(dummy.longestCommonPrefix(["dog","racecar","car"]))
print(dummy.longestCommonPrefix(["ab", "a"]))


