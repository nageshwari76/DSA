class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n):
            idx = i % n

            while stack and nums[stack[-1]] < nums[idx]:
                ans[stack.pop()] = nums[idx]

            if i < n:
                stack.append(idx)

        return ans