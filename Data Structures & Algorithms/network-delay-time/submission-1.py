class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        visited = set()
        heap = []
        heap.append([0,k]) #[time needed to get to node, node]
        res = 0

        while heap:
            time,node = heapq.heappop(heap)

            if node in visited:
                continue
            visited.add(node)
            res = max(res,time)
            if len(visited) == n:
                return res

            for nei,cost in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap,[time+cost,nei])
        return res if len(visited) == n else -1