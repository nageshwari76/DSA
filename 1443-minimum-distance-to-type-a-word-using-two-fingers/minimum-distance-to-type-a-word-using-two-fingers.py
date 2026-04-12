class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            return abs(a//6 - b//6) + abs(a%6 - b %6)
        
        n = len(word)
        dp = [0] * 26
        res = 0

        for i in range(1, n):
            cur = ord(word[i]) - ord('A')
            prev = ord(word[i-1]) - ord('A')
            step = dist(prev, cur)
            res += step
            new_dp = dp[:]
            for j in range(26):
                new_dp[prev] = max(new_dp[prev], dp[j] + step - dist(j, cur))
            dp = new_dp
        return res - max(dp)
        