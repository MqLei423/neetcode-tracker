class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def rob_line(houses):
            prev1,prev2 = 0,0
            for h in houses:
                cur = max(prev1,prev2+h)
                prev2 = prev1
                prev1 = cur
            return prev1
        return max(rob_line(nums[:-1]),rob_line(nums[1:]))