class Solution:
    def longestPalindrome(self, s: str) -> str:
        resI, resLen = 0,0

        for i in range(len(s)):
            #odd len
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resLen:
                    resI = l
                    resLen = r-l+1
                l-=1
                r+=1
            
            #even len
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resLen:
                    resI = l
                    resLen = r-l+1
                l-=1
                r+=1
        return s[resI:resI+resLen]