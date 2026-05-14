class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False

        return nums[-1] == n - 1
        