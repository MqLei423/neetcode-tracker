class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROW,COL = len(grid),len(grid[0])
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r,c = q.popleft()
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr,nc = r+dr,c+dc

                if nr<0 or nr>=ROW or nc<0 or nc>=COL or grid[nr][nc]!=INF:
                    continue

                grid[nr][nc] = grid[r][c]+1
                q.append((nr,nc))
        