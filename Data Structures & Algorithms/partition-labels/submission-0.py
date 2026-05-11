class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastPos = {}
        for i,c in enumerate(s):
            lastPos[c] = i

        res = []
        l,r = 0,0
        for i,c in enumerate(s):
            r = max(r,lastPos[c])
            if i == r:
                res.append(r-l+1)
                l = i+1
        return res