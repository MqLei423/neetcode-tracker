class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        l,r = intervals[0][0],intervals[0][1]
        for itv in intervals[1:]:
            if itv[0]<=r:
                l = min(itv[0],l)
                r = max(itv[1],r)
            else:
                res.append([l,r])
                l,r = itv
        res.append([l,r])
        return res