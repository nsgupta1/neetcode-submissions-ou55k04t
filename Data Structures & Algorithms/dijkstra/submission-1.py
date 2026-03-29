class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjMap = {}
        for i in range(n):
            adjMap[i] = []
        for u, v, w in edges :
            adjMap[u].append((v, w))
        minHeap = []
        heapq.heappush(minHeap, (0, src))
        res = {}

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in res:
                continue
            res[node] = weight
            for v, w in adjMap[node]:
                if v not in res:
                    heapq.heappush(minHeap, (w + weight, v))

        for i in range(n):
            if i not in res:
                res[i] = -1
        return res   


