class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for num in nums:
            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == len(lis):
                lis.append(num)
            else:
                lis[left] = num
        
        return len(lis)