class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in s:
            cur = 1
            while n+1 in s:
                n+=1
                cur += 1
            res = max(res,cur)
        return res