class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        # Move the smallest of the larger half to the smaller half (maxHeap)
        val = heapq.heappop(self.minHeap)
        heapq.heappush(self.maxHeap, -val)
        
        # Rebalance if maxHeap gets too large
        if len(self.maxHeap) > len(self.minHeap):
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
    def findMedian(self) -> float:
        lenMin = len(self.minHeap)
        lenMax = len(self.maxHeap)
        if lenMin == lenMax :
            return (self.minHeap[0] + -self.maxHeap[0]) / 2.0
        return self.minHeap[0] if lenMin > lenMax else -self.maxHeap[0]

    