from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))

    def rob1(self, arr):
        prev2 = 0
        prev1 = 0
        
        for num in arr:
            curr = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = curr
        
        return prev1