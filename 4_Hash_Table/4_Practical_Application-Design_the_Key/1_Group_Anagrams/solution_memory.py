from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = dict()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_group:
                anagram_group[sorted_word].append(word)
            else:
                anagram_group[sorted_word] = [word]

        return list(anagram_group.values())

dummy = Solution()
print(dummy.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(dummy.groupAnagrams([""]))
print(dummy.groupAnagrams(["a"]))



