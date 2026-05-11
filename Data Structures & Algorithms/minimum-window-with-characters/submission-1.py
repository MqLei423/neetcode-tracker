class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing = len(t)
        need = Counter(t)
        l = 0
        resPos,resLen = 0,float('inf')

        for r in range(len(s)):
            c = s[r]
            if need[c]>0:
                missing-=1
            need[c]-=1

            while missing==0:
                if r-l+1 < resLen:
                    resPos = l
                    resLen = r-l+1
                
                toDel = s[l]
                need[toDel]+=1
                if need[toDel]>0:
                    missing+=1
                l+=1
        return '' if resLen==float('inf') else s[resPos:resPos+resLen]