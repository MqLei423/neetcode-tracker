class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        l = 0
        res = 0
        maxf = 0

        for r in range(len(s)):
            cnt[s[r]] += 1
            maxf = max(maxf,cnt[s[r]])

            while r-l+1-maxf > k:
                cnt[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res