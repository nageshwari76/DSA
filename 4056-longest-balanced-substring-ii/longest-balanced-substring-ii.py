class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # CASE 1: only one character
        count = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        ans = max(ans, count)
        
        # CASE 2: two distinct characters
        def two_char(x, y):
            res = 0
            i = 0
            while i < n:
                while i < n and s[i] not in (x, y):
                    i += 1
                diff = {0: i - 1}
                d = 0
                while i < n and (s[i] == x or s[i] == y):
                    if s[i] == x:
                        d += 1
                    else:
                        d -= 1
                    if d in diff:
                        res = max(res, i - diff[d])
                    else:
                        diff[d] = i
                    i += 1
            return res
        
        ans = max(ans, two_char('a', 'b'))
        ans = max(ans, two_char('b', 'c'))
        ans = max(ans, two_char('a', 'c'))
        
        # CASE 3: all three characters
        prefix = {(0, 0): -1}
        cnt = [0, 0, 0]
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            cnt[idx] += 1
            key = (cnt[0] - cnt[1], cnt[1] - cnt[2])
            if key in prefix:
                ans = max(ans, i - prefix[key])
            else:
                prefix[key] = i
        
        return ans
