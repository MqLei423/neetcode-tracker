class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()
        ROW,COL = len(grid),len(grid[0])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==0:
                    q.append((r,c))

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nr,nc = r+dr,c+dc
                    if not 0<=nr<ROW or not 0<=nc<COL or grid[nr][nc]!=INF:
                        continue
                    grid[nr][nc] = grid[r][c]+1
                    q.append((nr,nc))