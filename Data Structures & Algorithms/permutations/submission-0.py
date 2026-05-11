class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,cur = [],[]

        def backtrack():
            if len(cur)==len(nums):
                res.append(cur.copy())
                return
            
            for n in nums:
                if n not in cur:
                    cur.append(n)
                    backtrack()
                    cur.pop()

        backtrack()
        
        return res