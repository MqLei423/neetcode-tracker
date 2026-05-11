class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [(-cnt,n) for n,cnt in Counter(nums).items()]
        res = []

        heapq.heapify(heap)
        for _ in range(k):
            _, n = heapq.heappop(heap)
            res.append(n)
        return res