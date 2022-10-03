from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        row, col = len(image), len(image[0])

        self.dfs(old_color, image, sr, sc, row, col, color)
        return image

    def dfs(self, old_color: int, image: List[List[int]], r: int, c: int, row: int, col: int, color: int):
        if r < 0 or r >= row or c < 0 or c >= col:
            return

        if image[r][c] == color or image[r][c] != old_color:
            return

        image[r][c] = color
        self.dfs(old_color, image, r + 1, c, row, col, color)
        self.dfs(old_color, image, r - 1, c, row, col, color)
        self.dfs(old_color, image, r, c - 1, row, col, color)
        self.dfs(old_color, image, r, c + 1, row, col, color)
