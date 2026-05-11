class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq1 = [0]*26
        window = [0]*26
        for c in s1:
            freq1[ord(c)-ord('a')] += 1
        l,r = 0,len(s1)

        for i in range(l,r):
            c = s2[i]
            window[ord(c)-ord('a')] += 1
        if freq1 == window:
            return True

        while r < len(s2):
            window[ord(s2[r])-ord('a')] += 1
            window[ord(s2[l])-ord('a')] -= 1

            if freq1 == window:
                return True
            
            l+=1
            r+=1
        return False

            
