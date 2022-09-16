from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack[-1] = stack[-2] + stack.pop()
            elif i == "-":
                stack[-1] = stack[-2] - stack.pop()
            elif i == "*":
                stack[-1] = stack[-2] * stack.pop()
            elif i == "/":
                stack[-1] = int(stack[-2] / stack.pop())
            else:
                stack.append(int(i))

        return stack.pop()

dummy = Solution()
print(dummy.evalRPN(["2","1","+","3","*"]))
print(dummy.evalRPN(["4","13","5","/","+"]))
print(dummy.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(dummy.evalRPN(["0","3","/"]))
