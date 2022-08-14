from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        row, col = 0, 0
        rasterised_matrix = []
        up_down = "up"

        while (0 <= row < m and 0<= col < n):
            if up_down == "up":
                while (0 < row and col < n - 1):
                    rasterised_matrix.append(mat[row][col])
                    row, col = row - 1, col + 1
                rasterised_matrix.append(mat[row][col])
                if col < n - 1:
                    col += 1
                else:
                    row += 1
                up_down = "down"

            elif up_down == "down":
                while (row < m - 1 and 0 < col):
                    rasterised_matrix.append(mat[row][col])
                    row, col = row + 1, col - 1
                rasterised_matrix.append(mat[row][col])
                if row < m - 1:
                    row += 1
                else:
                    col += 1
                up_down = "up"

        return rasterised_matrix



dummy = Solution()
print(dummy.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(dummy.findDiagonalOrder([[1,2],[3,4]]))
