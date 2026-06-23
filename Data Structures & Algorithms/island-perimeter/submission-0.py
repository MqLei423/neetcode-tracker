class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW,COL = len(grid),len(grid[0])

        visited = set()
        def dfs(r,c):
            if r<0 or r>=ROW or c<0 or c>=COL or grid[r][c]==0:
                return 1
            if (r,c) in visited:
                return 0

            visited.add((r,c))

            perim = 0
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr,nc = r+dr,c+dc
                perim += dfs(nr,nc)
            return perim

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    return dfs(r,c)
