class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = left_idx = right_idx = 0
        unique_chars = []
        while right_idx < len(s):
            if s[right_idx] not in unique_chars:
                unique_chars.append(s[right_idx])
                right_idx += 1
                max_len = max(max_len, len(unique_chars))
            else:
                left_idx += 1
                right_idx = left_idx
                unique_chars = []
        return max_len

dummy = Solution()
print(dummy.lengthOfLongestSubstring(" "))  # 1
print(dummy.lengthOfLongestSubstring("abcabcbb"))  # 3
print(dummy.lengthOfLongestSubstring("bbbbb"))  # 1
print(dummy.lengthOfLongestSubstring("pwwkew"))  # 3
print(dummy.lengthOfLongestSubstring("au"))  # 2
print(dummy.lengthOfLongestSubstring("dvdf"))  # 3
