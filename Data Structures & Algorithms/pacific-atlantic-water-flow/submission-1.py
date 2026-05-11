class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW,COL = len(heights),len(heights[0])
        pac,atl = set(),set()

        def dfs(r,c,lastH,ocean):
            if r<0 or r>=ROW or c<0 or c>=COL or heights[r][c]<lastH or (r,c) in ocean:
                return
            
            ocean.add((r,c))
            dfs(r+1,c,heights[r][c],ocean)
            dfs(r-1,c,heights[r][c],ocean)
            dfs(r,c+1,heights[r][c],ocean)
            dfs(r,c-1,heights[r][c],ocean)

        for r in range(ROW):
            dfs(r,0,0,pac)
            dfs(r,COL-1,0,atl)
        for c in range(COL):
            dfs(0,c,0,pac)
            dfs(ROW-1,c,0,atl)

        res = []
        for r,c in pac:
            if (r,c) in atl:
                res.append([r,c])
        return res