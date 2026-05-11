class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l,res = 0,0

        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1
                
            while d[s[r]] > 1:
                d[s[l]]-=1
                l+=1

            res = max(res,r-l+1)
        return res