# Last updated: 7/3/2026, 12:48:09 PM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        first_row_has_zeroes = any(matrix[0][j]==0 for j in range(col))
        first_col_has_zeroes = any(matrix[i][0]==0 for i in range(row))
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,row):
            if matrix[i][0]==0:
                for j in range(1,col):
                    matrix[i][j]=0
        for j in range(1,col):
            if matrix[0][j]==0:
                for i in range(1,row):
                    matrix[i][j]=0
        if first_row_has_zeroes:
            for j in range(col):
                matrix[0][j]=0
        if first_col_has_zeroes:
            for i in range(row):
                matrix[i][0]=0
                    
                
        