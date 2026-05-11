class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,cur = [],[]

        def backtrack(i,curSum):
            if i>= len(nums) or curSum > target:
                return
            if curSum == target:
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i,curSum+nums[i])
            cur.pop()
            backtrack(i+1,curSum)

        backtrack(0,0)
        return res
