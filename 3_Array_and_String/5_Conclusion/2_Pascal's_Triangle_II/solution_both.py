from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # https://en.wikipedia.org/wiki/Pascal%27s_triangle#Calculating_a_row_or_diagonal_by_itself
        # value at (row,row_idx+1) = (row,row_idx) * (row-row_idx) / (row_idx+1), where row_index starts at 0, whose value is 1
        pascals_row = [1]
        for idx in range(rowIndex):
            pascals_row.append(pascals_row[idx] * (rowIndex - idx) // (idx + 1))

        return pascals_row