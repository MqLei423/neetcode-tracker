class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadSet = set(deadends)
        if '0000' in deadSet:
            return -1
        
        res = 0
        visited = set('0000')
        q = deque()
        q.append('0000')
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return res
                
                for i in range(4):
                    for dif in [1,-1]:
                        newDig = str((int(cur[i])+dif) % 10)
                        newNum = cur[:i] + newDig +cur[i+1:]
                        if newNum not in visited and newNum not in deadSet:
                            visited.add(newNum)
                            q.append(newNum)
            res+=1
        
        return -1