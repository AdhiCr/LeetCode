from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        init_val = rows + cols - 2
        
        # scan from left-top
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]:
                    top = mat[i - 1][j] + 1 if i > 0 else init_val
                    left = mat[i][j - 1] + 1 if j > 0 else init_val
                    mat[i][j] = min(top, left)

        # scan from right-bottom
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if mat[i][j]:
                    bottom = mat[i + 1][j] + 1 if i < rows - 1 else init_val
                    right = mat[i][j + 1] + 1 if j < cols - 1 else init_val
                    mat[i][j] = min(mat[i][j], bottom, right)
        return mat

dummy = Solution()
print(dummy.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(dummy.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))