class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        lastEnd = intervals[0][1]
        res = 0

        for itv in intervals[1:]:
            if itv[0]<lastEnd:
                res+=1
                lastEnd = min(itv[1],lastEnd)
            else:
                lastEnd = itv[1]
        return res
                