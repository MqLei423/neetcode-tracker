class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDia = set()
        negDia = set()

        board = [['.']*n for _ in range(n)]
        res = []

        def backtrack(r):
            if r>=n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or r+c in posDia or r-c in negDia:
                    continue
                col.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                board[r][c] = '.'
                col.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
        backtrack(0)
        return res