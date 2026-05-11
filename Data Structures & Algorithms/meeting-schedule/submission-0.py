"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n<=1:
            return True
        intervals.sort(key=lambda x: x.start)
        prevEnd = intervals[0].end
        for itv in intervals[1:]:
            if itv.start < prevEnd:
                return False
            prevEnd = itv.end
        return True
