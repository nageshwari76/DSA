class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                vals = []
                
                # collect k x k submatrix
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])
                
                vals.sort()
                
                # compute minimum absolute difference
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    if vals[t] != vals[t-1]:
                        min_diff = min(min_diff, vals[t] - vals[t-1])
                
                # if all elements same
                if min_diff == float('inf'):
                    min_diff = 0
                
                row.append(min_diff)
            
            result.append(row)
        
        return result 
        