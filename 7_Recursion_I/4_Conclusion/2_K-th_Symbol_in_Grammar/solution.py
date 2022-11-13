class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def bitCount(n):
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result

        return bitCount(k-1) % 2


dummy = Solution()
print(dummy.kthGrammar(2,2))
print(dummy.kthGrammar(6,12))

