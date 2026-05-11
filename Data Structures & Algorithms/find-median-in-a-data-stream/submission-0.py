class MedianFinder:

    def __init__(self):
        self.big,self.small = [],[]

    def addNum(self, num: int) -> None:
        if self.big and num >self.big[0]:
            heapq.heappush(self.big,num)
        else:
            heapq.heappush(self.small,-num)

        if len(self.big)-len(self.small) >= 2:
            n = -heapq.heappop(self.big)
            heapq.heappush(self.small,n)
        elif len(self.small)-len(self.big) >= 2:
            n = -heapq.heappop(self.small)
            heapq.heappush(self.big,n)


    def findMedian(self) -> float:
        if len(self.big)>len(self.small):
            return self.big[0]
        elif len(self.big)<len(self.small):
            return -self.small[0]
        else:
            return (self.big[0]-self.small[0])/2.0
        