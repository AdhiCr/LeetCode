from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        targetColor = image[sr][sc]
        if targetColor == color:
            return image

        def dfs(r: int, c: int):
            if image[r][c] == targetColor:
                image[r][c] = color
                if r + 1 < len(image): dfs(r + 1, c)
                if r - 1 >= 0: dfs(r - 1, c)
                if c + 1 < len(image[0]): dfs(r, c + 1)
                if c - 1 >= 0: dfs(r, c - 1)

        dfs(sr, sc)
        return image