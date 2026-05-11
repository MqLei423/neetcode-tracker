class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL = len(grid),len(grid[0])

        def dfs(r,c):
            if r<0 or r>=ROW or c<0 or c>=COL or grid[r][c] != '1':
                return 
            
            grid[r][c] = '0'
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r,c)
        return res
        