class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use max heap of size k to keep k closest points.
        # Keep a tuple of distance and point because we have to return points
        # TC: O(nlogk), SC: O(k)

        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = (x*x + y*y)
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for (dist, point) in heap:
            res.append(point)
        return res
            


        