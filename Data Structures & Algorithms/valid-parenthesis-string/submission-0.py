class Solution:
    def checkValidString(self, s: str) -> bool:
        max_open,min_open = 0,0 #max/min possible amt of open paren

        for c in s:
            if c=='(':
                max_open+=1
                min_open+=1
            elif c==')':
                max_open-=1
                min_open-=1
            else:
                max_open+=1
                min_open-=1
            
            if max_open<0:
                return False
            if min_open<0:
                min_open=0
        return min_open == 0