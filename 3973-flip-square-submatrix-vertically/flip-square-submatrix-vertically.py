from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # Flip the k x k submatrix vertically
        for i in range(k // 2):
            for j in range(k):
                grid[x + i][y + j], grid[x + k - 1 - i][y + j] = \
                grid[x + k - 1 - i][y + j], grid[x + i][y + j]
        
        return grid