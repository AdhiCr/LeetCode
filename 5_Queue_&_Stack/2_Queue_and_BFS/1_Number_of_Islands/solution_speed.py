from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        no_rows, no_cols = len(grid), len(grid[0])
        neighbouring_idx = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def collate_islands(row_idx: int, col_idx: int) -> None:
            grid[row_idx][col_idx] = '0'
            for dx, dy in neighbouring_idx:
                new_r_idx, new_c_idx = row_idx + dx, col_idx + dy
                if 0 <= new_r_idx < no_rows and 0 <= new_c_idx < no_cols and grid[new_r_idx][new_c_idx] == "1":
                    collate_islands(new_r_idx, new_c_idx)  # Recursively collate all the adjoining island elements

        for r_idx in range(no_rows):
            for c_idx in range(no_cols):
                if grid[r_idx][c_idx] == "1":
                    island_count += 1
                    ## Breadth first search in the grid for the islands
                    collate_islands(r_idx, c_idx)

        return island_count


dummy = Solution()
print(dummy.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))  # 1
print(dummy.numIslands([["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]))  # 3