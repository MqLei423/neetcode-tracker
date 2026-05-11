class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u,v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False

            parent[root_u] = root_v
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]
        return []