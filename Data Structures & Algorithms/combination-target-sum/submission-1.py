class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(i,curSum):
            if curSum == target:
                res.append(cur.copy())
                return
            if curSum > target or i>=len(nums):
                return

            cur.append(nums[i])
            backtrack(i,curSum+nums[i])
            cur.pop()
            backtrack(i+1,curSum)

        backtrack(0,0)
        return res