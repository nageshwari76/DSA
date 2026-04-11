from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_dist = float('inf')
        num2indices = defaultdict(list)
        for k, num in enumerate(nums):
            indices = num2indices[num]
            if len(indices) == 2:
                i, j = indices
                # i < j < k, the following is cleaner
                # (k - j) + (j - i) + (k - i) = 2*k - 2*i
                dist = 2 * k - 2 * i
                min_dist = min(min_dist, dist)
                indices[0], indices[1] = j, k
            else:
                indices.append(k)
        return min_dist if min_dist < float('inf') else -1