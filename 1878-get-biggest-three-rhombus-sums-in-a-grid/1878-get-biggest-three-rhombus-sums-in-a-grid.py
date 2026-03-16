class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])  # size 0 rhombus

                k = 1
                while True:
                    if i-k < 0 or i+k >= m or j-k < 0 or j+k >= n:
                        break

                    s = 0

                    for d in range(k):
                        s += grid[i-k+d][j+d]
                        s += grid[i+d][j+k-d]
                        s += grid[i+k-d][j-d]
                        s += grid[i-d][j-k+d]

                    sums.add(s)
                    k += 1

        return sorted(sums, reverse=True)[:3]
        