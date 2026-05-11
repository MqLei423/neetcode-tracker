class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = n
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u,v):
            nonlocal count
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                count -= 1
                parent[root_u] = root_v

        for i in range(n):
            for j in range(i,n):
                if isConnected[i][j] == 1:
                    union(i,j)
        return count