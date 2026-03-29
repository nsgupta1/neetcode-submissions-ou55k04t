class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            diff = abs(x-y)
            if diff > 0:
                heapq.heappush(maxheap, -diff)
        return 0 if len(maxheap) == 0 else -maxheap[0]

        