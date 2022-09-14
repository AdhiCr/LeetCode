from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                index, value = stack.pop()
                res[index] = i - index
            stack.append([i, v])
        return res



dummy = Solution()
print(dummy.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dummy.dailyTemperatures([30,40,50,60]))
print(dummy.dailyTemperatures([30,60,90]))