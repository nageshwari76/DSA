class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
           return False

        count1 = [0] * 26
        count2 = [0] * 26

    # Frequency of s1
        for c in s1:
            count1[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            count2[ord(s2[r]) - ord('a')] += 1

        # Maintain window size
            if r - l + 1 > len(s1):
               count2[ord(s2[l]) - ord('a')] -= 1
               l += 1

        # Compare
            if count1 == count2:
               return True

        return False