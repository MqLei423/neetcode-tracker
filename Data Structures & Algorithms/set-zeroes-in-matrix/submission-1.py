class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW,COL = len(matrix),len(matrix[0])
        rowZero = False

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r>=1:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1,ROW):
            for c in range(1,COL):
                if matrix[r][0] == 0 or matrix[0][c]==0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROW):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(COL):
                matrix[0][c] = 0
        