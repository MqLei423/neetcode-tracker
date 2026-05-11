"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        res = 0
        j = 0
        for i in range(len(starts)):
            if starts[i]<ends[j]:
                res+=1
            else:
                j+=1
        return res