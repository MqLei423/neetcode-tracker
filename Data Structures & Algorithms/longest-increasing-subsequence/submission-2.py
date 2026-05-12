class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[0] = 1

        for i in range(1,len(nums)):
            longestPrev = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    longestPrev = max(longestPrev,dp[j])
            dp[i] = 1+longestPrev
        return max(dp)