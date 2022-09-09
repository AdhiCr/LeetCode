from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        no_rows, no_cols = len(grid), len(grid[0])
        neighbouring_idx = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for r_idx in range(no_rows):
            for c_idx in range(no_cols):
                if grid[r_idx][c_idx] == "1":
                    island_count += 1
                    visited_idx = [(r_idx, c_idx)]

                    while visited_idx:
                        curr_row, curr_col = visited_idx.pop()
                        # add neighbors
                        for offset_row, offset_col in neighbouring_idx:
                            new_row_idx, new_col_idx = curr_row + offset_row, curr_col + offset_col
                            if 0<= new_row_idx < no_rows and 0 <= new_col_idx < no_cols and grid[new_row_idx][new_col_idx] == "1":
                                visited_idx.append([new_row_idx, new_col_idx])
                        # mark as visited
                        grid[curr_row][curr_col] = "0"

        return island_count


dummy = Solution()
print(dummy.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))  # 1
print(dummy.numIslands([["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]))  # 3