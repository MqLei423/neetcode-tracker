class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur,res = [],[]

        def backtrack(openN,closeN):
            if openN==closeN==n:
                res.append(''.join(cur))
                return
            
            if openN<n:
                cur.append('(')
                backtrack(openN+1,closeN)
                cur.pop()
            if closeN<openN:
                cur.append(')')
                backtrack(openN,closeN+1)
                cur.pop()

        backtrack(0,0)
        return res