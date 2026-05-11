class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        cur = intervals[0]
        for i in range(1,len(intervals)):
            itv = intervals[i]
            if itv[0]>cur[1]:
                res.append(cur)
                cur = itv
            else:
                cur[1] = max(cur[1],itv[1])
        res.append(cur)
        return res