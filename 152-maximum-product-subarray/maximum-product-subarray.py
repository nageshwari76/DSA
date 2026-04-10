from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            temp = max(x, max_prod * x, min_prod * x)
            min_prod = min(x, max_prod * x, min_prod * x)
            max_prod = temp
            result = max(result, max_prod)

        return result