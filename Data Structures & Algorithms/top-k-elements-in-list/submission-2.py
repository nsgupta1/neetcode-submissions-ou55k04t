class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []
        res = []
        for num in nums:
            count[num] += 1
        for num, freq in count.items():
            heapq.heappush(heap, (-freq, num))

        for i in range(k):
            res.append(heapq.heappop(heap)[1])  
        return res