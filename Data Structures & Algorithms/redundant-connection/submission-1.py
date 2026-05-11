class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u,v):
            uroot = find(u)
            vroot = find(v)

            if uroot==vroot:
                return False
            else:
                parent[uroot] = vroot
            return True

        res = []
        for u,v in edges:
            if not union(u,v):
                res = [u,v]
        return res