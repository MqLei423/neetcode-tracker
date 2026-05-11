class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        maxLen = max(len(w) for w in wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(1,len(s)+1):
            for j in range(max(0,i-maxLen),i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]