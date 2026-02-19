class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevGroup = 0
        currGroup = 1
        count = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                currGroup += 1
            else:
                count += min(prevGroup, currGroup)
                prevGroup = currGroup
                currGroup = 1
        count += min(prevGroup, currGroup)
        return count
        