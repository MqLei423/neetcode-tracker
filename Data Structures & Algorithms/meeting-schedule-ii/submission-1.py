"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x : x.start)
        minHeap = [] #end time of meetings

        for itv in intervals:
            if minHeap and minHeap[0] <= itv.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap,itv.end)

        return len(minHeap)