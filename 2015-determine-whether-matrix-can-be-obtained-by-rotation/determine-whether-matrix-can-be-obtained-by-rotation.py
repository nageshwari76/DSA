from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(matrix):
            n = len(matrix)
            
            # Transpose
            for i in range(n):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            # Reverse each row
            for row in matrix:
                row.reverse()
        
        # Try all 4 rotations
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False
