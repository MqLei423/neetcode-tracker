class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        #no. of ways to use first i coins to achieve j amount
        dp = [[0]* (amount+1) for _ in range(n+1)]

        #base case, only 1 way to reach 0
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):
            curCoin = coins[i-1]
            for j in range(1,amount+1):
                #don't use curCoin
                dp[i][j] = dp[i-1][j]
                #use curCoin
                if j>=curCoin:
                    dp[i][j] += dp[i][j-curCoin]
        return dp[n][amount]