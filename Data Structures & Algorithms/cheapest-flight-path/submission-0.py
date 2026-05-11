class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for orig,to,price in flights:
            adj[orig].append((to,price))

        minCosts = [float('inf')] * n
        minCosts[src] = 0
        
        q = deque()
        q.append((0,src)) #(cost to node,node)
        stops = 0

        while q and stops<=k:
            for _ in range(len(q)):
                cost,node = q.popleft()
                for nei,price in adj[node]:
                    new_price = cost+price
                    if new_price < minCosts[nei]:
                        minCosts[nei] = new_price
                        q.append((new_price,nei))
            stops+=1
        
        return minCosts[dst] if minCosts[dst]!=float('inf') else -1