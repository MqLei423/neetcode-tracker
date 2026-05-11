class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = nums[0]
        for n in nums:
            curSum+=n
            res = max(curSum,res)
            if curSum<0:
                curSum=0
        return res