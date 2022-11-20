# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    """
    Predefined as api, hence here the logic is not really provided
    """
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        lower, higher = 1, n
        while lower <= higher:
            guessed_no = (lower + higher)//2
            guess_return = guess(guessed_no)
            if guess_return == -1:
                higher = guessed_no - 1
            elif guess_return == 1:
                lower = guessed_no + 1
            else:
                return guessed_no
        return higher