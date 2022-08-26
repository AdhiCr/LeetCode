class Solution:
    def calculatedDigitSum(self, number: int) -> int:
        total = 0
        while number != 0:
            total += (number % 10) ** 2
            number //= 10
        return total

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.calculatedDigitSum(n)

        return n == 1
