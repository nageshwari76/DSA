class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [''] * n
        curr_char = ord('a')

        for i in range(n):
            if res[i] == '':
                if curr_char > ord('z'):
                    return ""
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = chr(curr_char)
                curr_char += 1

        # Validate by recomputing LCP
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if res[i] == res[j]:
                    if i == n - 1 or j == n - 1:
                        expected = 1
                    else:
                        expected = 1 + lcp[i + 1][j + 1]
                else:
                    expected = 0

                if lcp[i][j] != expected:
                    return ""

        return "".join(res) 