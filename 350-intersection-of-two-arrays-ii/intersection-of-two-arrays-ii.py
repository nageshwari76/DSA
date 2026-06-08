from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        freq = Counter(nums1)
        ans = []

        for num in nums2:
            if freq[num] > 0:
                ans.append(num)
                freq[num] -= 1

        return ans
        