class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        unique_chars = dict()
        max_len = start = 0
        for present_idx in range(len(s)):
            if s[present_idx] in unique_chars and start <= unique_chars[s[present_idx]]:
                start = unique_chars[s[present_idx]] + 1
            else:
                max_len = max(max_len, present_idx-start+1)
            unique_chars[s[present_idx]] = present_idx
        return max_len
        # return max_len

dummy = Solution()
print(dummy.lengthOfLongestSubstring(" "))  # 1
print(dummy.lengthOfLongestSubstring("abcabcbb"))  # 3
print(dummy.lengthOfLongestSubstring("bbbbb"))  # 1
print(dummy.lengthOfLongestSubstring("pwwkew"))  # 3
print(dummy.lengthOfLongestSubstring("au"))  # 2
print(dummy.lengthOfLongestSubstring("dvdf"))  # 3
