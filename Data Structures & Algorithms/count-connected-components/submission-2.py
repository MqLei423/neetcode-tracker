class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        res = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u,v):
            root_u = find(u)
            root_v = find(v)

            nonlocal res
            if root_u != root_v:
                res-=1
                parent[root_u] = root_v

        for u,v in edges:
            union(u,v)
        return res