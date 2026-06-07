class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[-1] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            ans = 1  # path consisting of only this cell

            for dx, dy in dirs:
                ni, nj = i + dx, j + dy

                if (0 <= ni < m and 0 <= nj < n and
                        grid[ni][nj] > grid[i][j]):
                    ans = (ans + dfs(ni, nj)) % MOD

            dp[i][j] = ans
            return ans

        result = 0

        for i in range(m):
            for j in range(n):
                result = (result + dfs(i, j)) % MOD

        return result
        