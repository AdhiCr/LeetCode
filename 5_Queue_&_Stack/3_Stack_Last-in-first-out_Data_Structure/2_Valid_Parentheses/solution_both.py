class Solution:
    def isValid(self, s: str) -> bool:
        str_len = len(s)
        if str_len % 2 or s[0] not in ["(", "[", "{"]:
            return False

        bracket_pairs = {")": "(", "]": "[", "}": "{"}
        bracket_stack = []

        for idx in range(str_len):
            if s[idx] in ["(", "[", "{"]:
                bracket_stack.append(s[idx])
            elif not bracket_stack:
                return False
            elif bracket_stack[-1] == bracket_pairs[s[idx]]:
                bracket_stack.pop()
            else:
                return False

        return not bracket_stack

dummy = Solution()
print(dummy.isValid("()"))
print(dummy.isValid("()[]{}"))
print(dummy.isValid("(]"))
print(dummy.isValid("{[]}"))
print(dummy.isValid("){"))