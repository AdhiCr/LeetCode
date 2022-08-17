from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        This solution exploits that fact that the triangle is symmetric on the line bisecting the triangle from the top
            /|\
           / | \
        also uses the idea that the first element of each row is 1, there by for row N, one has to only calculate
        ceil(N/2)-1 values of the triangle in total. after which the values can be mirrored on the last element.
         (replicate last element if even row else replicate only values before the last element)
        :param numRows: number of rows of Pascal's triangle to return
        :return: pascal triangle in list of lists form
        """
        P_tri = []
        for row in range(1, numRows+1):
            row_val = [1] + [(P_tri[row - 2][idx-1] + P_tri[row - 2][idx]) for idx in range(1, (row + 1)//2)]
            P_tri.append(row_val + row_val[:(row//2)][::-1])
        return P_tri

dummy = Solution()
print(dummy.generate(5))
print(dummy.generate(1))