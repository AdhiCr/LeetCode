from typing import List
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            check_dict = Counter(row)
            check_dict.pop(".", None)
            if len(check_dict) > 0 and max(check_dict.values()) > 1:
                return False
        # check columns
        for col_idx in range(9):
            col = list(zip(*board))[col_idx]
            check_dict = Counter(col)
            check_dict.pop(".", None)
            if len(check_dict) > 0 and max(check_dict.values()) > 1:
                return False
        # check 3x3 grid
        row_idx = col_idx = 0
        while row_idx <= 6:
            while col_idx <= 6:
                grid = board[row_idx][col_idx: col_idx + 3] + \
                       board[row_idx + 1][col_idx: col_idx + 3] + \
                       board[row_idx + 2][col_idx: col_idx + 3]
                check_dict = Counter(grid)
                check_dict.pop(".", None)
                if len(check_dict) > 0 and max(check_dict.values()) > 1:
                    return False
                col_idx += 3
            col_idx = 0
            row_idx += 3
        return True



dummy = Solution()
# print(dummy.isValidSudoku(
#     board =
#     [["5","3",".",".","7",".",".",".","."],
#      ["6",".",".","1","9","5",".",".","."],
#      [".","9","8",".",".",".",".","6","."],
#      ["8",".",".",".","6",".",".",".","3"],
#      ["4",".",".","8",".","3",".",".","1"],
#      ["7",".",".",".","2",".",".",".","6"],
#      [".","6",".",".",".",".","2","8","."],
#      [".",".",".","4","1","9",".",".","5"],
#      [".",".",".",".","8",".",".","7","9"]]
# ))
# print(dummy.isValidSudoku(
#     board =
#     [["8","3",".",".","7",".",".",".","."],
#      ["6",".",".","1","9","5",".",".","."],
#      [".","9","8",".",".",".",".","6","."],
#      ["8",".",".",".","6",".",".",".","3"],
#      ["4",".",".","8",".","3",".",".","1"],
#      ["7",".",".",".","2",".",".",".","6"],
#      [".","6",".",".",".",".","2","8","."],
#      [".",".",".","4","1","9",".",".","5"],
#      [".",".",".",".","8",".",".","7","9"]]
# ))
print(dummy.isValidSudoku(
    board =
    [["7",".",".",".","4",".",".",".","."],
     [".",".",".","8","6","5",".",".","."],
     [".","1",".","2",".",".",".",".","."],
     [".",".",".",".",".","9",".",".","."],
     [".",".",".",".","5",".","5",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."]]
))

