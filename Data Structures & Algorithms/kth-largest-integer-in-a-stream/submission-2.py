class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.length = k
        for n in nums:
            heapq.heappush(self.minHeap, n)
            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
            if len(self.minHeap) < self.length or val > self.minHeap[0]:
                heapq.heappush(self.minHeap, val) 
            if len(self.minHeap) > self.length:
                heapq.heappop(self.minHeap)
            return self.minHeap[0]

        
