class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total//2

        dp = [False] * (target+1)
        dp[0] = True

        for n in nums:
            # can only use n once, so going in reverse
            for i in range(target,n-1,-1):
                dp[i] = dp[i-n] or dp[i] #or dp[i] so True isn't set back to F
            # early stop
            if dp[target]:
                return True
        return dp[target]