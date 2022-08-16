from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_start = col_start = 0
        row_end, col_end = len(matrix), len(matrix[0])
        spiral_mat = []
        while (row_start < row_end and col_start < col_end):
            if col_start < col_end:
                spiral_mat.extend(matrix[row_start][col_start: col_end])
            row_start += 1
            if row_start < row_end and col_start < col_end:
                spiral_mat.extend([rows[col_end - 1] for rows in matrix[row_start:row_end]])
            col_end -= 1
            if row_start < row_end and col_start < col_end:
                spiral_mat.extend(matrix[row_end - 1][col_start: col_end][::-1])
            row_end -= 1
            if row_start < row_end and col_start < col_end:
                spiral_mat.extend([rows[col_start] for rows in matrix[row_start:row_end]][::-1])
            col_start += 1

        return spiral_mat


dummy = Solution()
print(dummy.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(dummy.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
