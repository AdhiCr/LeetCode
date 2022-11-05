class Solution:
    def __init__(self):
        self.fibonacci_sums = {
            0: 0,
            1: 1,
            2: 1,
        }

    def fib(self, n: int) -> int:
        if n < 0:
            return 0
        elif n in self.fibonacci_sums:
            return self.fibonacci_sums.get(n)
        else:
            self.fibonacci_sums[n] = self.fib(n-1) + self.fib(n-2)
            return self.fibonacci_sums[n]


dummy = Solution()
print(dummy.fib(19))


