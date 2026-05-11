class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj = defaultdict(list)
        for start,end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        visited = set()
        def dfs(cur,parent):
            if cur in visited:
                return False
            
            visited.add(cur)
            for chd in adj[cur]:
                if chd != parent and not dfs(chd,cur):
                    return False
            return True

        return dfs(0,-1) and len(visited) == n