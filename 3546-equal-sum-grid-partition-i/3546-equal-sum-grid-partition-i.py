class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        if total % 2 != 0:
            return False

        half = total // 2

        curr = 0
        for i in range(m):
            curr += sum(grid[i])
            if curr == half:
                return True
        
        curr = 0
        col_sums = [0] * n
        for j in range(n):
            for i in range(m):
                col_sums[j] += grid[i][j]
        
        for j in range(n):
            curr += col_sums[j]
            if curr == half:
                return True

        return False