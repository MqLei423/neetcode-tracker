class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r

        while l<=r:
            timeToEat = 0
            eatSpd = (l+r)//2
            for p in piles:
                timeToEat += math.ceil(float(p)/eatSpd)
            if timeToEat <= h:
                r = eatSpd -1
                res = eatSpd
            else:
                l = eatSpd + 1
        return res
