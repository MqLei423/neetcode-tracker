class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(heap)
        cooldown = deque()
        time = 0

        while heap or cooldown:
            if not heap:
                time = cooldown[0][0]
            else:
                cnt = 1+heapq.heappop(heap)
                if cnt <0:
                    cooldown.append([time+n,cnt])
            
            if cooldown and time == cooldown[0][0]:
                heapq.heappush(heap,(cooldown.popleft()[1]))
            time+=1

        return time
