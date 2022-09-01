from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)

        for string in strs:
            sorted_str = ''.join(sorted(string))
            ana_map[sorted_str].append(string)

        return list(ana_map.values())

dummy = Solution()
print(dummy.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(dummy.groupAnagrams([""]))
print(dummy.groupAnagrams(["a"]))



