class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        
        # Result matrix
        res = [[0] * n for _ in range(m)]
        
        # Step 1: suffix pass (right → left, bottom → top)
        suffix = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                res[i][j] = suffix
                suffix = (suffix * grid[i][j]) % MOD
        
        # Step 2: prefix pass (left → right, top → bottom)
        prefix = 1
        for i in range(m):
            for j in range(n):
                res[i][j] = (res[i][j] * prefix) % MOD
                prefix = (prefix * grid[i][j]) % MOD
        
        return res
        