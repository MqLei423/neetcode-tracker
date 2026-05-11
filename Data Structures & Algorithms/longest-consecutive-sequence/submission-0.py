class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in s:
            cur = 1
            if n-1 not in s:
                cur = 1
            while n+1 in s:
                cur += 1
                n+=1
            res = max(cur,res)
        return res