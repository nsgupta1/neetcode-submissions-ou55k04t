class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        store = defaultdict(int)
        heap = []

        for task in tasks:
            store[task] += 1
        
        for key, val in store.items():
            heapq.heappush(heap, (-val, key))
        
        maxfreq = -heapq.heappop(heap)[0]
        initialIdleSlots = (maxfreq-1)*n

        while heap:
            freq = -heapq.heappop(heap)[0]
            initialIdleSlots -= min(freq, maxfreq-1)
        return len(tasks) + max(0, initialIdleSlots)



        

        
        

        

