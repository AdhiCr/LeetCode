from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(r, c, color, pixel_color):
            if r < 0 or len(image)-1 < r or c < 0 or len(image[0])-1 < c or (image[r][c] != pixel_color):
                return

            image[r][c] = color
            for d in directions:
                dfs(r+d[0], c+d[1], color, pixel_color)

        pixel_color = image[sr][sc]
        if pixel_color == color:
            return image
        else:
            dfs(sr, sc, color, pixel_color)
        return image