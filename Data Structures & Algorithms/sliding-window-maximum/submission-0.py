class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(nlogn) solution using Heap not most optimal
        res = []
        for i in range(len(nums)-k+1):
            store = []
            for j in range(i, i+k):
                heapq.heappush(store, -nums[j])
            res.append(-heapq.heappop(store))
        return res
