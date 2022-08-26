class Solution:

    def calculatedDigitSum(self, number: int) -> int:
        total = 0
        while number != 0:
            total += (number % 10) ** 2
            number //= 10
        return total

    def isHappy(self, n: int) -> bool:
        while True:
            n = self.calculatedDigitSum(n)
            #https://en.wikipedia.org/wiki/Happy_number The numbers converge to either 1 or 4
            if n == 1:
                return True
            elif n == 4:
                return False