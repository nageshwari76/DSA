class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q = [0]
        far = 0

        for i in q:
            start = max(i + minJump, far + 1)
            end = min(i + maxJump + 1, n)
            for j in range(start, end):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    q.append(j)
            far = i + maxJump
        return n == 1
        