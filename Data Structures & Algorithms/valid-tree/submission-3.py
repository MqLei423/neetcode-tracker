class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for start,end in edges:
            if start == end:
                return False
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