class Solution:
    def numSquares(self, n: int) -> int:
        # solution using dynamic_programming
        dp = [n] * (n+1)
        dp[0] = 0

        for target in range(1, n+1):
            for sq_val in range(1, target+1):
                diff = target - sq_val*sq_val
                if diff < 0:
                    break
                else:
                    dp[target] = min(dp[target], 1 + dp[diff])
        return dp[n]


dummy = Solution()
print(dummy.numSquares(12))
print(dummy.numSquares(16))
print(dummy.numSquares(25))
print(dummy.numSquares(28))
print(dummy.numSquares(13))