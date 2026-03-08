class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # palindrome table
        pal = [[False]*n for _ in range(n)]

        for end in range(n):
            for start in range(end+1):
                if s[start] == s[end] and (end-start <= 2 or pal[start+1][end-1]):
                    pal[start][end] = True

        dp = [0]*n

        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')
                for j in range(i):
                    if pal[j+1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1] 