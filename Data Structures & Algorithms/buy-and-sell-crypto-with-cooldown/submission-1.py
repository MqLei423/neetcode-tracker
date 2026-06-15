class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #profit after the action that day
        hold = -prices[0] #buy on first day
        sell = 0
        cooldown = 0

        for p in prices:
            prevHold,prevSell,prevCool = hold,sell,cooldown

            hold = max(prevHold,prevCool - p) # keep holding or buy
            sell = prevHold + p # sell
            cooldown = max(prevCool,prevSell) #keep cooling or start cooldown

        return max(sell,cooldown)