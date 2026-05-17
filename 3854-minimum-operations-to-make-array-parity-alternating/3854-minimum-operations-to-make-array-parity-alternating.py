class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        
        def mnDiff(par):
            mxChg = (mxCnt == parity[par].count(mx))
            mnChg = (mnCnt == parity[par].count(mn))
            sameCnt = (mx == mn)
            return abs(mn - mx + mnChg + mxChg - sameCnt)


        parity, toggle = [[], []], 1
        mn, mx = min(nums), max(nums)
        mnCnt, mxCnt = nums.count(mn), nums.count(mx)

        if len(nums) == 1: 
            return [0, 0]

        for num in nums:
            parity[(num%2)^toggle].append(num)
            toggle^= 1

        n0, n1 = len(parity[0]), len(parity[1])

        if n0 < n1:
            return [n0, mnDiff(0)]
        elif n1 < n0:
            return [n1, mnDiff(1)]
        else:
            return [n0, min(mnDiff(0), mnDiff(1))]