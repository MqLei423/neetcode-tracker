class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        ROW,COL = len(grid),len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append([r,c])

        time = 0
        while fresh>0 and q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nr,nc = r+dr,c+dc
                    if nr>=0 and nr<ROW and nc>=0 and nc<COL and grid[nr][nc] == 1:
                        fresh-=1
                        grid[nr][nc] = 2
                        q.append([nr,nc])
            time+=1
        return time if fresh == 0 else -1