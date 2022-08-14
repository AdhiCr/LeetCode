from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(sum([(digit * (10 ** idx)) for idx, digit in enumerate(digits[::-1])]) + 1))



dummy = Solution()
print(dummy.plusOne([1,2,3]))
print(dummy.plusOne([4,3,2,1]))
print(dummy.plusOne([9]))