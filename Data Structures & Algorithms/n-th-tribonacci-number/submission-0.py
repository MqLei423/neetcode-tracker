class Solution:
    def tribonacci(self, n: int) -> int:
        if n<2:
            return n
        prev1,prev2,prev3 = 1,1,0
        for _ in range(2,n):
            cur = prev1+prev2+prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = cur
        return prev1