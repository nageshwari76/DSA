from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x: int) -> int:
            if x <= 0:
                return 0

            s = str(x)

            @lru_cache(None)
            def dfs(pos, tight, started, prev2, prev1):
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                cnt = 0
                wav = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        c, w = dfs(pos + 1, ntight, False, -1, -1)
                        cnt += c
                        wav += w
                        continue

                    if not started:
                        c, w = dfs(pos + 1, ntight, True, -1, d)
                        cnt += c
                        wav += w
                    elif prev2 == -1:
                        c, w = dfs(pos + 1, ntight, True, prev1, d)
                        cnt += c
                        wav += w
                    else:
                        extra = int(
                            (prev1 > prev2 and prev1 > d) or
                            (prev1 < prev2 and prev1 < d)
                        )

                        c, w = dfs(pos + 1, ntight, True, prev1, d)

                        cnt += c
                        wav += w + extra * c

                return (cnt, wav)

            return dfs(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)