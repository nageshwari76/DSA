class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        height = [0] * n
        max_area = 0

        for i in range(m):
        # Build height
            for j in range(n):
                if matrix[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0
        
        # Sort heights in descending order
            sorted_heights = sorted(height, reverse=True)
        
        # Calculate max area
            for k in range(n):
                max_area = max(max_area, sorted_heights[k] * (k + 1))
    
        return max_area