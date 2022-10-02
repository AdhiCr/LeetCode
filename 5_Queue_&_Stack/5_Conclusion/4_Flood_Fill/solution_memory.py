from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        targetColor = image[sr][sc]
        row, col = len(image), len(image[0])

        def dfs(r: int, c: int):
            if r < 0 or r >= row or c < 0 or c >= col:
                return

            if image[r][c] == color or image[r][c] != targetColor:
                return

            image[r][c] = color
            dfs(sr + 1, sc)
            dfs(sr - 1, sc)
            dfs(sr, sc + 1)
            dfs(sr, sc - 1)

        dfs(sr, sc)
        return image