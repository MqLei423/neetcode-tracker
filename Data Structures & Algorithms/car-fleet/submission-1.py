class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos,(target-pos)/spd) for pos,spd in zip(position,speed)]
        cars.sort(reverse=True)

        slowest = 0
        res = 0

        for pos,time in cars:
            if time > slowest:
                slowest = time
                res +=1
        return res
