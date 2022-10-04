from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        init_val = rows + cols - 2
        
        # scan from left-top
        for i, row in enumerate(mat):
            for j, ele in enumerate(row):
                if ele:
                    top = mat[i - 1][j] + 1 if i > 0 else init_val
                    left = mat[i][j - 1] + 1 if j > 0 else init_val
                    mat[i][j] = min(top, left)

        # scan from right-bottom
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                ele = mat[i][j]
                if ele:
                    bottom = mat[i + 1][j] + 1 if i < rows - 1 else init_val
                    right = mat[i][j + 1] + 1 if j < cols - 1 else init_val
                    mat[i][j] = min(ele, bottom, right)
        return mat

dummy = Solution()
print(dummy.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(dummy.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))