from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        no_rows, no_cols = len(mat), len(mat[0])
        rasterised_matrix = []
        # Number of diagonals in a matrix = no_rows + no_cols - 1
        # Note: here the diagonals run orthogonal to the traditional matrix diagonal
        for diag_i in range(no_rows + no_cols - 1):
            # The result is expected in the order where first diagonal goes down to up (d->u), followed by (u->d) and so on.
            if diag_i % 2 == 0:
                # even diags go (d->u) - since diag_i starts at 0
                row_idx = min(no_rows - 1, diag_i)
                col_idx = diag_i - row_idx
                while 0 <= row_idx < no_rows and 0 <= col_idx < no_cols:
                    rasterised_matrix.append(mat[row_idx][col_idx])
                    row_idx = row_idx - 1
                    col_idx = col_idx + 1
            else:
                # odd diags go (d->u)
                col_idx = min(no_cols - 1, diag_i)
                row_idx = diag_i - col_idx
                while 0 <= row_idx < no_rows and 0 <= col_idx < no_cols:
                    rasterised_matrix.append(mat[row_idx][col_idx])
                    row_idx = row_idx + 1
                    col_idx = col_idx - 1
        return rasterised_matrix



dummy = Solution()
print(dummy.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(dummy.findDiagonalOrder([[1,2],[3,4]]))
