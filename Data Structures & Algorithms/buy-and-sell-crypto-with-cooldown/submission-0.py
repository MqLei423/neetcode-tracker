class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #max profit of action after that day
        hold = -prices[0] #buy on first day
        sell = 0
        cool = 0

        for p in prices:
            prevHold,prevSell,prevCool = hold,sell,cool

            hold = max(prevHold,prevCool-p)
            sell = prevHold+p
            cool = max(prevCool,prevSell)
        
        return max(sell,cool)