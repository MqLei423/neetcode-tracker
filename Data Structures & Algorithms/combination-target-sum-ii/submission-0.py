class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res,cur = [],[]

        def backtrack(i,curSum):
            if curSum == target:
                res.append(cur.copy())
                return

            for j in range(i,len(candidates)):
                if curSum+candidates[j]>target:
                    break
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                cur.append(candidates[j])
                backtrack(j+1,curSum+candidates[j])
                cur.pop()

        backtrack(0,0)
        return res