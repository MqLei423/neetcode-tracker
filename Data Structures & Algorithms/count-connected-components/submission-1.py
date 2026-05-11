class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        self.cnt = n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u,v):
            uroot = find(u)
            vroot = find(v)

            if uroot!=vroot:
                self.cnt-=1
                parent[uroot] = vroot

        for u,v in edges:
            union(u,v)
        return self.cnt