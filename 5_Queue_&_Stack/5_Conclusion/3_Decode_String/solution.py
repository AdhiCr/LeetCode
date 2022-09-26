class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                sub_decoder = multiplier = ""
                while stack[-1] != "[":
                    sub_decoder = stack.pop() + sub_decoder
                stack.pop()
                while len(stack) > 0 and stack[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    multiplier = stack.pop() + multiplier
                stack.append(sub_decoder * int(multiplier))

        return "".join(stack)

dummy = Solution()
# print(dummy.decodeString(s="3[a]2[bc]"))
# print(dummy.decodeString(s="3[a2[c]]"))
# print(dummy.decodeString(s="2[abc]3[cd]ef"))
print(dummy.decodeString(s="10[lc]"))

