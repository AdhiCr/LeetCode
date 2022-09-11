from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        # This solution uses optimisations based on number theory: Lagrange's four-square theorem
        # Reference:
        # 1. https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
        # 2. https://en.wikipedia.org/wiki/Jacobi%27s_four-square_theorem
        # 3. Will Jagy's answer at https://math.stackexchange.com/questions/3740395/solution-to-lagranges-four-square-theorem-with-fewest-terms

        #  keep dividing number (n) by 4 until it is not divisible by 8, then just check the remainder when dividing that
        #  number by 8. If the remainder is not 7, the original n is the sum of three squares.
        #  Once it is deduced that the number can be represented as sum of three squares, one must check the values
        #  since, upto 2 of those values can be zeros. So, if square of any two numbers can sum to n, then atleast one value is zero
        while n%4 == 0:  # The algorithm indicates checking reminder on division by 8, but it fails for example at 28, division check by 4 yields proper results
            n //= 4

        if n%8 == 7:
            return 4
        else:
            for x in range(n):
                if x*x > n:
                    break
                y = int(sqrt(n-x*x))
                if x*x + y*y == n:
                    return 1 if (x == 0 or y == 0) else 2

            return 3



dummy = Solution()
print(dummy.numSquares(12))
print(dummy.numSquares(16))
print(dummy.numSquares(25))
print(dummy.numSquares(28))
print(dummy.numSquares(13))