class Solution:
    def longestBalanced(self, s:str) -> int:
        n = len(s)
        ans = 0
        
        # Check all substrings s[i:j]
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                
                # Filter zeros and get counts of distinct characters
                counts = [c for c in freq if c > 0]
                
                # If all distinct counts are equal, update answer
                if len(counts) > 0 and min(counts) == max(counts):
                    ans = max(ans, j - i + 1)
        
        return ans

        