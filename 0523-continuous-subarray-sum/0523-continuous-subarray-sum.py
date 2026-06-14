class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {0: -1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            remainder = ((total % k) + k) % k
            if remainder in map:
                if i - map[remainder] >= 2:
                    return True
            else:
                
                map[remainder] = i
        return False

        