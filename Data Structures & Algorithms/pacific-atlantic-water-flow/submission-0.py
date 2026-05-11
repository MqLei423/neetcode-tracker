class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW,COL = len(heights),len(heights[0])
        pac,atl = set(),set()

        def dfs(r,c,lastH,isPac):
            if r<0 or r>=ROW or c<0 or c>=COL or heights[r][c]<lastH:
                return
            if (isPac and (r,c) in pac) or (not isPac and (r,c) in atl):
                return
            
            if isPac:
                pac.add((r,c))
            else:
                atl.add((r,c))
            dfs(r+1,c,heights[r][c],isPac)
            dfs(r-1,c,heights[r][c],isPac)
            dfs(r,c+1,heights[r][c],isPac)
            dfs(r,c-1,heights[r][c],isPac)

        for r in range(ROW):
            dfs(r,0,0,True)
            dfs(r,COL-1,0,False)
        for c in range(COL):
            dfs(0,c,0,True)
            dfs(ROW-1,c,0,False)

        res = []
        for r,c in pac:
            if (r,c) in atl:
                res.append([r,c])
        return res