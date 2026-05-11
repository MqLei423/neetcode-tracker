class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,curMin = nums[0],nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            n = nums[i]
            if n<0:
                curMax,curMin = curMin,curMax

            curMax = max(n,curMax*n)
            curMin = min(n,curMin*n)
            res = max(res,curMax)
        return res